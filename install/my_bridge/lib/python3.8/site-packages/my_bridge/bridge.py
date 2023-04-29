"""
basic: spawn ego_vehicle and add camera and lidar 2023/04-27

"""
import rclpy
from rclpy.node import Node

import carla
import math

CARLA_FPS = 60.0
CARLA_SCENE_NAME = "Bend03"
CARLA_EGO_MODEL_FILTER = "model3"
CARLA_EGO_STATE_TOPIC_NAME = "cec_ego_state0"
CARLA_EGO_INIT_X = 417.495391845703
CARLA_EGO_INIT_Y = 252.950531005859
CARLA_EGO_INIT_Z = 0.1
CARLA_EGO_INIT_YAW = -12.729858/180.*math.pi
CARLA_SPECTATOR_DX = 0.10
CARLA_SPECTATOR_DY = -0.40
CARLA_SPECTATOR_DZ = 1.22

class CarlaRosBridge(Node):
    """
    Carla Ros bridge
    """
    def __init__(self, name):
        """
        Constructor

        :param carla_world: carla world object
        :type carla_world: carla.World
        :param params: dict of parameters, see settings.yaml
        :type params: dict
        """
        super().__init__(name)
        # while rclpy.ok():
        self.get_logger().info("-----Successfully create my bridge node!-----")

        self.declare_parameter("host", "localhost")
        self.declare_parameter("port", 2000)
        self.declare_parameter("timeout", 10)
        self.declare_parameter("synchronous_mode", True)
        self.declare_parameter("fixed_delta_seconds", 1.0/CARLA_FPS)
        self.declare_parameter("town", CARLA_SCENE_NAME)
        self.declare_parameter("ego_vehicle_role_name", CARLA_EGO_STATE_TOPIC_NAME)
    
    def initialize_bridge(self, carla_world):
        """
        Initialize the simulator
        """
        self.synchronous_mode = self.get_parameter("synchronous_mode").value
        self.fixed_delta_seconds = self.get_parameter("fixed_delta_seconds").value
        self.ego_vehicle_name = self.get_parameter("ego_vehicle_role_name").value

        self.carla_world = carla_world
        self.carla_settings = self.carla_world.get_settings()
        # self.get_logger().info(f"[not]Change simulate mode from {self.carla_settings.synchronous_mode}\
        #                        to {self.synchronous_mode}")
        if self.synchronous_mode:
            self.carla_settings.synchronous_mode = True
            self.carla_settings.fixed_delta_seconds = self.fixed_delta_seconds
        self.carla_world.apply_settings(self.carla_settings)

        self.weather = carla.WeatherParameters(
            cloudiness=20.0, precipitation=0.0, sun_altitude_angle=40.0)
        self.carla_world.set_weather(self.weather)

        # spawn the ego vehicle actor
        self.actor_list = []
        self.blueprint_library = self.carla_world.get_blueprint_library()
        self.ego_vehicle_bp = self.blueprint_library.filter(
            CARLA_EGO_MODEL_FILTER)[0]
        self.ego_vehicle_bp.set_attribute('color', '0, 0, 0')
        self.ego_sp = carla.Transform(carla.Location(
            x=CARLA_EGO_INIT_X, y=CARLA_EGO_INIT_Y, z=CARLA_EGO_INIT_Z),
            carla.Rotation(yaw=CARLA_EGO_INIT_YAW*180/math.pi))
        self.ego_transform0 = carla.Transform(carla.Location(
            x=CARLA_EGO_INIT_X, y=CARLA_EGO_INIT_Y, z=0),
            carla.Rotation(yaw=CARLA_EGO_INIT_YAW*180/math.pi))
        self.ego_vehicle = self.carla_world.spawn_actor(
            self.ego_vehicle_bp, self.ego_sp)
        self.ego_vehicle.set_simulate_physics(False)
        self.actor_list.append(self.ego_vehicle)

        self.spectator = self.carla_world.get_spectator()
        transform = self.ego_vehicle.get_transform()

        self.spectator.set_transform(carla.Transform(transform.location + carla.Location(z=20),
                                                carla.Rotation(pitch=-90))) 
        self.carla_world.tick()

def main(args=None):
    """
    main function for carla simulator ROS bridge
    maintaining the communication client and the CarlaBridge object
    """
    rclpy.init(args=args)
    carla_bridge = CarlaRosBridge("bridge")

    parameters = {}
    parameters['host']    = carla_bridge.get_parameter('host').value
    parameters['port']    = carla_bridge.get_parameter('port').value
    parameters['timeout'] = carla_bridge.get_parameter('timeout').value
    parameters['town']    = carla_bridge.get_parameter('town').value

    try:
        carla_client = carla.Client(
            host=parameters['host'],
            port=parameters['port']
        )
        print("Trying to connect to {host}:{port}".format(
            host=parameters['host'], port=parameters['port']))
        carla_client.set_timeout(parameters['timeout'])

        carla_world = carla_client.get_world()

        if "town" in parameters:
            if parameters["town"].endswith(".xodr"):
                print(
                    "Loading opendrive world from file '{}'".format(parameters["town"]))
                with open(parameters["town"]) as od_file:
                    data = od_file.read()
                carla_world = carla_client.generate_opendrive_world(str(data))
            else:
                if carla_world.get_map().name != parameters["town"]:
                    print("Loading town '{}' (previous: '{}').".format(
                        parameters["town"], carla_world.get_map().name))
                    carla_world = carla_client.load_world(parameters["town"])
            carla_world.tick()    # make sure to update the new town
        
        carla_bridge.initialize_bridge(carla_world)

        rclpy.spin(carla_bridge)

    except (IOError, RuntimeError) as e:
        print("Error: {}".format(e))
    except KeyboardInterrupt:
        print("-----Bye---Stop by user.----")
    finally:
        carla_bridge.destroy_node()
        rclpy.shutdown()
        del carla_world
        del carla_client



    rclpy.shutdown()

if __name__ == '__main__':
     main()