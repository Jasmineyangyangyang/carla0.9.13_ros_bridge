
import rclpy
from rclpy.node import Node

import time
import carla
import collections
import threading
import math
import queue

from waypoints_types.srv import GetWaypointsList
from kvaser_msg_interfaces.msg import ControlCmd
import carla_common.transforms as trans

from std_msgs.msg import Bool
from nav_msgs.msg import Path
from geometry_msgs.msg import PoseStamped, Quaternion
from agents.navigation.global_route_planner import GlobalRoutePlanner


# for carla_waypoint publish
WAYPOINT_DISTANCE = 0.2
WAYPOINTDISTANCE = 150
WAYPOINTRESOLUTION = 0.1

# 为了寻找ego车所在的车道线id
CARLA_EGO_INIT_X = 417.495391845703
CARLA_EGO_INIT_Y = 252.950531005859
CARLA_EGO_INIT_Z = 0.0
EGO_IN_LEFT_LANE = True   # ego vehicle in left lane 

class VehiclePoseNode(Node):
    def __init__(self, name):
        super().__init__(name)

        self.lane_client = self.create_client(
            GetWaypointsList,
            "/carla/vehicle/posestamped"
            )
        while not self.lane_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.request = GetWaypointsList.Request()

        self.control_publisher = self.create_publisher(ControlCmd, "/ControlBottom", 10)
        # self.control_publisher_timer = self.create_timer(0.01, self.control_publishe_callback)

    def send_pose_request(self, name):
        self.request.vehiclename.data = name
        self.future = self.lane_client.call_async(self.request)  # 异步方式发送请求（通过其他线程发送请求）
        rclpy.spin_until_future_complete(self, self.future)
        if self.future.result() is not None:
            ego_pose = self.future.result().vehiclepose
            ego_transform = trans.ros_pose_to_carla_transform(ego_pose.pose)
            # self.get_logger().info(f"receive from service: {ego_transform}")
            return ego_transform
        else:
            self.get_logger().info("Service call failed")
        
    def control_publishe_callback(self, steer, vx):
        msg = ControlCmd()
        msg.time = float(1.23)
        # msg.stangle = float(-3.0)
        # msg.vehiclevx = float(40.0)
        msg.stangle = float(steer)  # rad???
        msg.vehiclevx = float(vx)  #km/h
        self.control_publisher.publish(msg)
        self.get_logger().info(f'Publishing : {msg.time} s, {msg.stangle} deg, {msg.vehiclevx} km/h')


class TrajectPlan():
    def __init__(self):
        
        self.map = None
        self.carla_world = connect_to_carla()
        self.map = self.carla_world.get_map()

        self.ego_vehicle_init_location = carla.Location(x=CARLA_EGO_INIT_X, y=CARLA_EGO_INIT_Y, z=CARLA_EGO_INIT_Z)
        ego_init_waypoint = self.map.get_waypoint(self.ego_vehicle_init_location)
        lane_waypoints = self.map.generate_waypoints(WAYPOINTRESOLUTION)
        # 如果车辆的出生位置已经是固定在某条车道上的了，那get_left_lan就是车道边线了
        if EGO_IN_LEFT_LANE:
            # ego_lane_id = ego_init_waypoint.get_left_lane().lane_id
            ego_lane_id = ego_init_waypoint.lane_id
        else:
            # ego_lane_id = ego_init_waypoint.get_right_lane().lane_id
            ego_lane_id = ego_init_waypoint.lane_id
        self.all_waypoints = [wp for wp in lane_waypoints if wp.lane_id == ego_lane_id]

        # for wp in self.all_waypoints:
        #     # print(wp)
        #     self.carla_world.debug.draw_point(wp.transform.location, size=0.1, color=carla.Color(255,0,0), life_time=0)

    def plan_and_control(self, ego_transformation, adjacent_transformation, control_queue):
        # get vehicles transform
        ego_vehicle_transform = ego_transformation
        print(f"ego x = {ego_vehicle_transform.location.x}m, y = {ego_vehicle_transform.location.y}m")
        adjacent_vehicle_transform = adjacent_transformation
        print(f"adjacent x = {adjacent_vehicle_transform.location.x}m, y = {adjacent_vehicle_transform.location.y}m")

        # find waypointslist in self.map
        self.ego_vehicle_location = ego_vehicle_transform.location
        print(self.ego_vehicle_location)

        print("get waypoints list...")
        if self.map is None:
            self.current_route = None
            print("can't get carla_world's map...")
        else:
            self.current_route = self.calculate_route_distance()
        steer, vx = self.get_instruct_from_waypoints()
        control_queue.put((steer, vx))

    # def calculate_route_distance(self):
    #     """
    #     Calculate a route from the current location go WAYPOINTDISTANCE
    #     """
    #     print(f"Calculating route to {WAYPOINTDISTANCE} m")

    #     grp = GlobalRoutePlanner(self.map, sampling_resolution=0.2)
        
    #     goal = None
    #     for waypoint_ in self.all_waypoints:
    #         # get Location
    #         location = waypoint_.transform.location
    #         # rotation = waypoint_.transform.rotation
    #         if self.ego_vehicle_location:
    #             dx = self.ego_vehicle_location.x - location.x
    #             dy = self.ego_vehicle_location.y - location.y
    #             distance = math.sqrt(dx * dx + dy * dy)
    #             if distance > WAYPOINTDISTANCE:
    #                 print("calculate route.")
    #                 goal = waypoint_.transform
    #                 break
    #     if goal is not None:
    #         route = grp.trace_route(self.ego_vehicle_location,
    #                                 carla.Location(goal.location.x,
    #                                             goal.location.y,
    #                                             goal.location.z))   #(current_waypoint, road_option)
    #     else:
    #         print("goal is None")
    #         # route = None

    #     return route
    def calculate_route_distance(self):
        """
        Calculate a route from the current location go WAYPOINTDISTANCE
        """
        print(f"Calculating route to {WAYPOINTDISTANCE} m")

        far_index =-1
        near_index=-1
        mindistance = float('inf')
        for index, waypoint_ in enumerate(self.all_waypoints):
            location = waypoint_.transform.location  
            dx = self.ego_vehicle_location.x - location.x
            dy = self.ego_vehicle_location.y - location.y
            distance = math.sqrt(dx*dx + dy*dy)
            if distance < mindistance:
                mindistance = distance
                near_index = index

        temp_waypoints = self.all_waypoints[near_index:]
        temp_waypoints.extend(self.all_waypoints[0:near_index])
        for index, waypoint_ in enumerate(temp_waypoints):
            location = waypoint_.transform.location  
            dx = self.ego_vehicle_location.x - location.x
            dy = self.ego_vehicle_location.y - location.y
            distance = math.sqrt(dx*dx + dy*dy)
            if distance > 100.0:
                far_index = index
                break
    
        far_index += near_index 

        if far_index < near_index:
            self.current_route = self.all_waypoints[near_index:]
            self.current_route.extend(self.all_waypoints[0:far_index+1])
        else:
            self.current_route = self.all_waypoints[near_index:far_index+1]

        if self.current_route is not None:
            for wp in self.current_route:
                # print(wp)
                self.carla_world.debug.draw_point(wp.transform.location, size=0.1, color=carla.Color(255,0,0), life_time=0)
                # self.world.debug.draw_arrow(wp[0].transform.location, wp[0].transform.location + carla.Location(x=math.cos(math.radians(wp[0].transform.rotation.yaw)),\
                #                                                     y=math.sin(math.radians(wp[0].transform.rotation.yaw))), \
                #                                                         thickness=0.05, arrow_size=0.1, \
                #                                                             color=carla.Color(255,255,255), life_time=0)
        return self.current_route
    
    def get_instruct_from_waypoints(self):
        """
        get the waypoints
        """

        steer = -3
        vx = 40
        return steer, vx

def connect_to_carla():

    print("Waiting for CARLA world (topic: /carla/world_info)...")
    host =  "127.0.0.1"
    port = 2000
    timeout = 10
    print("CARLA world available. Trying to connect to {host}:{port}".format(
        host=host, port=port))

    carla_client = carla.Client(host=host, port=port)
    carla_client.set_timeout(timeout)

    try:
        carla_world = carla_client.get_world()
    except RuntimeError as e:
        print("Error while connecting to Carla: {}".format(e))
        raise e
    print("Connected to Carla.")
    return carla_world


def main(args=None):

    rclpy.init(args=args)
    pose_node = VehiclePoseNode("trajectory_control")

    control_queue = queue.Queue(maxsize=2)
    traject_plan = TrajectPlan()
    ego_vehicle_transform = pose_node.send_pose_request("ego_vehicle")
    print(f"receive from service: {ego_vehicle_transform}")

    adjacent_vehicle_transform = pose_node.send_pose_request("adjacent0_vehicle")
    print(f"receive from service: {adjacent_vehicle_transform}")

    control_thread = threading.Thread(
        target=traject_plan.plan_and_control, 
        args=(ego_vehicle_transform, adjacent_vehicle_transform, control_queue))
    control_thread.start()

    rclpy.spin(pose_node)
    control_thread.join()
    pose_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
