// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice

#ifndef WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__STRUCT_H_
#define WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'vehiclename'
#include "std_msgs/msg/detail/string__struct.h"

// Struct defined in srv/GetWaypointsList in the package waypoints_types.
typedef struct waypoints_types__srv__GetWaypointsList_Request
{
  std_msgs__msg__String vehiclename;
} waypoints_types__srv__GetWaypointsList_Request;

// Struct for a sequence of waypoints_types__srv__GetWaypointsList_Request.
typedef struct waypoints_types__srv__GetWaypointsList_Request__Sequence
{
  waypoints_types__srv__GetWaypointsList_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} waypoints_types__srv__GetWaypointsList_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'vehiclepose'
#include "geometry_msgs/msg/detail/pose_stamped__struct.h"

// Struct defined in srv/GetWaypointsList in the package waypoints_types.
typedef struct waypoints_types__srv__GetWaypointsList_Response
{
  geometry_msgs__msg__PoseStamped vehiclepose;
} waypoints_types__srv__GetWaypointsList_Response;

// Struct for a sequence of waypoints_types__srv__GetWaypointsList_Response.
typedef struct waypoints_types__srv__GetWaypointsList_Response__Sequence
{
  waypoints_types__srv__GetWaypointsList_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} waypoints_types__srv__GetWaypointsList_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__STRUCT_H_
