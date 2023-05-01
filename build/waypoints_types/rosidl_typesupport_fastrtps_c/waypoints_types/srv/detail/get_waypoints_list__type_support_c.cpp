// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice
#include "waypoints_types/srv/detail/get_waypoints_list__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "waypoints_types/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "waypoints_types/srv/detail/get_waypoints_list__struct.h"
#include "waypoints_types/srv/detail/get_waypoints_list__functions.h"
#include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "std_msgs/msg/detail/string__functions.h"  // vehiclename

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_waypoints_types
size_t get_serialized_size_std_msgs__msg__String(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_waypoints_types
size_t max_serialized_size_std_msgs__msg__String(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_waypoints_types
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, std_msgs, msg, String)();


using _GetWaypointsList_Request__ros_msg_type = waypoints_types__srv__GetWaypointsList_Request;

static bool _GetWaypointsList_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetWaypointsList_Request__ros_msg_type * ros_message = static_cast<const _GetWaypointsList_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: vehiclename
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->vehiclename, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _GetWaypointsList_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetWaypointsList_Request__ros_msg_type * ros_message = static_cast<_GetWaypointsList_Request__ros_msg_type *>(untyped_ros_message);
  // Field name: vehiclename
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, std_msgs, msg, String
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->vehiclename))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_waypoints_types
size_t get_serialized_size_waypoints_types__srv__GetWaypointsList_Request(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetWaypointsList_Request__ros_msg_type * ros_message = static_cast<const _GetWaypointsList_Request__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name vehiclename

  current_alignment += get_serialized_size_std_msgs__msg__String(
    &(ros_message->vehiclename), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _GetWaypointsList_Request__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_waypoints_types__srv__GetWaypointsList_Request(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_waypoints_types
size_t max_serialized_size_waypoints_types__srv__GetWaypointsList_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: vehiclename
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_std_msgs__msg__String(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _GetWaypointsList_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_waypoints_types__srv__GetWaypointsList_Request(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_GetWaypointsList_Request = {
  "waypoints_types::srv",
  "GetWaypointsList_Request",
  _GetWaypointsList_Request__cdr_serialize,
  _GetWaypointsList_Request__cdr_deserialize,
  _GetWaypointsList_Request__get_serialized_size,
  _GetWaypointsList_Request__max_serialized_size
};

static rosidl_message_type_support_t _GetWaypointsList_Request__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetWaypointsList_Request,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, waypoints_types, srv, GetWaypointsList_Request)() {
  return &_GetWaypointsList_Request__type_support;
}

#if defined(__cplusplus)
}
#endif

// already included above
// #include <cassert>
// already included above
// #include <limits>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "waypoints_types/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
// already included above
// #include "waypoints_types/srv/detail/get_waypoints_list__struct.h"
// already included above
// #include "waypoints_types/srv/detail/get_waypoints_list__functions.h"
// already included above
// #include "fastcdr/Cdr.h"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

// includes and forward declarations of message dependencies and their conversion functions

#if defined(__cplusplus)
extern "C"
{
#endif

#include "geometry_msgs/msg/detail/pose_stamped__functions.h"  // vehiclepose

// forward declare type support functions
ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_waypoints_types
size_t get_serialized_size_geometry_msgs__msg__PoseStamped(
  const void * untyped_ros_message,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_waypoints_types
size_t max_serialized_size_geometry_msgs__msg__PoseStamped(
  bool & full_bounded,
  size_t current_alignment);

ROSIDL_TYPESUPPORT_FASTRTPS_C_IMPORT_waypoints_types
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, geometry_msgs, msg, PoseStamped)();


using _GetWaypointsList_Response__ros_msg_type = waypoints_types__srv__GetWaypointsList_Response;

static bool _GetWaypointsList_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _GetWaypointsList_Response__ros_msg_type * ros_message = static_cast<const _GetWaypointsList_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: vehiclepose
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, geometry_msgs, msg, PoseStamped
      )()->data);
    if (!callbacks->cdr_serialize(
        &ros_message->vehiclepose, cdr))
    {
      return false;
    }
  }

  return true;
}

static bool _GetWaypointsList_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _GetWaypointsList_Response__ros_msg_type * ros_message = static_cast<_GetWaypointsList_Response__ros_msg_type *>(untyped_ros_message);
  // Field name: vehiclepose
  {
    const message_type_support_callbacks_t * callbacks =
      static_cast<const message_type_support_callbacks_t *>(
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(
        rosidl_typesupport_fastrtps_c, geometry_msgs, msg, PoseStamped
      )()->data);
    if (!callbacks->cdr_deserialize(
        cdr, &ros_message->vehiclepose))
    {
      return false;
    }
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_waypoints_types
size_t get_serialized_size_waypoints_types__srv__GetWaypointsList_Response(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _GetWaypointsList_Response__ros_msg_type * ros_message = static_cast<const _GetWaypointsList_Response__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name vehiclepose

  current_alignment += get_serialized_size_geometry_msgs__msg__PoseStamped(
    &(ros_message->vehiclepose), current_alignment);

  return current_alignment - initial_alignment;
}

static uint32_t _GetWaypointsList_Response__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_waypoints_types__srv__GetWaypointsList_Response(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_waypoints_types
size_t max_serialized_size_waypoints_types__srv__GetWaypointsList_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: vehiclepose
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        max_serialized_size_geometry_msgs__msg__PoseStamped(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static size_t _GetWaypointsList_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_waypoints_types__srv__GetWaypointsList_Response(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_GetWaypointsList_Response = {
  "waypoints_types::srv",
  "GetWaypointsList_Response",
  _GetWaypointsList_Response__cdr_serialize,
  _GetWaypointsList_Response__cdr_deserialize,
  _GetWaypointsList_Response__get_serialized_size,
  _GetWaypointsList_Response__max_serialized_size
};

static rosidl_message_type_support_t _GetWaypointsList_Response__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_GetWaypointsList_Response,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, waypoints_types, srv, GetWaypointsList_Response)() {
  return &_GetWaypointsList_Response__type_support;
}

#if defined(__cplusplus)
}
#endif

#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_cpp/service_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_c/identifier.h"
// already included above
// #include "waypoints_types/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "waypoints_types/srv/get_waypoints_list.h"

#if defined(__cplusplus)
extern "C"
{
#endif

static service_type_support_callbacks_t GetWaypointsList__callbacks = {
  "waypoints_types::srv",
  "GetWaypointsList",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, waypoints_types, srv, GetWaypointsList_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, waypoints_types, srv, GetWaypointsList_Response)(),
};

static rosidl_service_type_support_t GetWaypointsList__handle = {
  rosidl_typesupport_fastrtps_c__identifier,
  &GetWaypointsList__callbacks,
  get_service_typesupport_handle_function,
};

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, waypoints_types, srv, GetWaypointsList)() {
  return &GetWaypointsList__handle;
}

#if defined(__cplusplus)
}
#endif
