// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "waypoints_types/srv/detail/get_waypoints_list__rosidl_typesupport_introspection_c.h"
#include "waypoints_types/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "waypoints_types/srv/detail/get_waypoints_list__functions.h"
#include "waypoints_types/srv/detail/get_waypoints_list__struct.h"


// Include directives for member types
// Member `vehiclename`
#include "std_msgs/msg/string.h"
// Member `vehiclename`
#include "std_msgs/msg/detail/string__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  waypoints_types__srv__GetWaypointsList_Request__init(message_memory);
}

void GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_fini_function(void * message_memory)
{
  waypoints_types__srv__GetWaypointsList_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_member_array[1] = {
  {
    "vehiclename",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(waypoints_types__srv__GetWaypointsList_Request, vehiclename),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_members = {
  "waypoints_types__srv",  // message namespace
  "GetWaypointsList_Request",  // message name
  1,  // number of fields
  sizeof(waypoints_types__srv__GetWaypointsList_Request),
  GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_member_array,  // message members
  GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_type_support_handle = {
  0,
  &GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_waypoints_types
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList_Request)() {
  GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, String)();
  if (!GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_type_support_handle.typesupport_identifier) {
    GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &GetWaypointsList_Request__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "waypoints_types/srv/detail/get_waypoints_list__rosidl_typesupport_introspection_c.h"
// already included above
// #include "waypoints_types/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "waypoints_types/srv/detail/get_waypoints_list__functions.h"
// already included above
// #include "waypoints_types/srv/detail/get_waypoints_list__struct.h"


// Include directives for member types
// Member `vehiclepose`
#include "geometry_msgs/msg/pose_stamped.h"
// Member `vehiclepose`
#include "geometry_msgs/msg/detail/pose_stamped__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  waypoints_types__srv__GetWaypointsList_Response__init(message_memory);
}

void GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_fini_function(void * message_memory)
{
  waypoints_types__srv__GetWaypointsList_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_member_array[1] = {
  {
    "vehiclepose",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(waypoints_types__srv__GetWaypointsList_Response, vehiclepose),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_members = {
  "waypoints_types__srv",  // message namespace
  "GetWaypointsList_Response",  // message name
  1,  // number of fields
  sizeof(waypoints_types__srv__GetWaypointsList_Response),
  GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_member_array,  // message members
  GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_type_support_handle = {
  0,
  &GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_waypoints_types
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList_Response)() {
  GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, geometry_msgs, msg, PoseStamped)();
  if (!GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_type_support_handle.typesupport_identifier) {
    GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &GetWaypointsList_Response__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "waypoints_types/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "waypoints_types/srv/detail/get_waypoints_list__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_members = {
  "waypoints_types__srv",  // service namespace
  "GetWaypointsList",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_Request_message_type_support_handle,
  NULL  // response message
  // waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_Response_message_type_support_handle
};

static rosidl_service_type_support_t waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_type_support_handle = {
  0,
  &waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_waypoints_types
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList)() {
  if (!waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_type_support_handle.typesupport_identifier) {
    waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, waypoints_types, srv, GetWaypointsList_Response)()->data;
  }

  return &waypoints_types__srv__detail__get_waypoints_list__rosidl_typesupport_introspection_c__GetWaypointsList_service_type_support_handle;
}
