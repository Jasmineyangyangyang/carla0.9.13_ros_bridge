// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice
#include "waypoints_types/srv/detail/get_waypoints_list__rosidl_typesupport_fastrtps_cpp.hpp"
#include "waypoints_types/srv/detail/get_waypoints_list__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace std_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const std_msgs::msg::String &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  std_msgs::msg::String &);
size_t get_serialized_size(
  const std_msgs::msg::String &,
  size_t current_alignment);
size_t
max_serialized_size_String(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace std_msgs


namespace waypoints_types
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
cdr_serialize(
  const waypoints_types::srv::GetWaypointsList_Request & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: vehiclename
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.vehiclename,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  waypoints_types::srv::GetWaypointsList_Request & ros_message)
{
  // Member: vehiclename
  std_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.vehiclename);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
get_serialized_size(
  const waypoints_types::srv::GetWaypointsList_Request & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: vehiclename

  current_alignment +=
    std_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.vehiclename, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
max_serialized_size_GetWaypointsList_Request(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: vehiclename
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        std_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_String(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _GetWaypointsList_Request__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const waypoints_types::srv::GetWaypointsList_Request *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _GetWaypointsList_Request__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<waypoints_types::srv::GetWaypointsList_Request *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _GetWaypointsList_Request__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const waypoints_types::srv::GetWaypointsList_Request *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _GetWaypointsList_Request__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_GetWaypointsList_Request(full_bounded, 0);
}

static message_type_support_callbacks_t _GetWaypointsList_Request__callbacks = {
  "waypoints_types::srv",
  "GetWaypointsList_Request",
  _GetWaypointsList_Request__cdr_serialize,
  _GetWaypointsList_Request__cdr_deserialize,
  _GetWaypointsList_Request__get_serialized_size,
  _GetWaypointsList_Request__max_serialized_size
};

static rosidl_message_type_support_t _GetWaypointsList_Request__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_GetWaypointsList_Request__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace waypoints_types

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_waypoints_types
const rosidl_message_type_support_t *
get_message_type_support_handle<waypoints_types::srv::GetWaypointsList_Request>()
{
  return &waypoints_types::srv::typesupport_fastrtps_cpp::_GetWaypointsList_Request__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, waypoints_types, srv, GetWaypointsList_Request)() {
  return &waypoints_types::srv::typesupport_fastrtps_cpp::_GetWaypointsList_Request__handle;
}

#ifdef __cplusplus
}
#endif

// already included above
// #include <limits>
// already included above
// #include <stdexcept>
// already included above
// #include <string>
// already included above
// #include "rosidl_typesupport_cpp/message_type_support.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
// already included above
// #include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions
namespace geometry_msgs
{
namespace msg
{
namespace typesupport_fastrtps_cpp
{
bool cdr_serialize(
  const geometry_msgs::msg::PoseStamped &,
  eprosima::fastcdr::Cdr &);
bool cdr_deserialize(
  eprosima::fastcdr::Cdr &,
  geometry_msgs::msg::PoseStamped &);
size_t get_serialized_size(
  const geometry_msgs::msg::PoseStamped &,
  size_t current_alignment);
size_t
max_serialized_size_PoseStamped(
  bool & full_bounded,
  size_t current_alignment);
}  // namespace typesupport_fastrtps_cpp
}  // namespace msg
}  // namespace geometry_msgs


namespace waypoints_types
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
cdr_serialize(
  const waypoints_types::srv::GetWaypointsList_Response & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: vehiclepose
  geometry_msgs::msg::typesupport_fastrtps_cpp::cdr_serialize(
    ros_message.vehiclepose,
    cdr);
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  waypoints_types::srv::GetWaypointsList_Response & ros_message)
{
  // Member: vehiclepose
  geometry_msgs::msg::typesupport_fastrtps_cpp::cdr_deserialize(
    cdr, ros_message.vehiclepose);

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
get_serialized_size(
  const waypoints_types::srv::GetWaypointsList_Response & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: vehiclepose

  current_alignment +=
    geometry_msgs::msg::typesupport_fastrtps_cpp::get_serialized_size(
    ros_message.vehiclepose, current_alignment);

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_waypoints_types
max_serialized_size_GetWaypointsList_Response(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: vehiclepose
  {
    size_t array_size = 1;


    for (size_t index = 0; index < array_size; ++index) {
      current_alignment +=
        geometry_msgs::msg::typesupport_fastrtps_cpp::max_serialized_size_PoseStamped(
        full_bounded, current_alignment);
    }
  }

  return current_alignment - initial_alignment;
}

static bool _GetWaypointsList_Response__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const waypoints_types::srv::GetWaypointsList_Response *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _GetWaypointsList_Response__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<waypoints_types::srv::GetWaypointsList_Response *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _GetWaypointsList_Response__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const waypoints_types::srv::GetWaypointsList_Response *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _GetWaypointsList_Response__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_GetWaypointsList_Response(full_bounded, 0);
}

static message_type_support_callbacks_t _GetWaypointsList_Response__callbacks = {
  "waypoints_types::srv",
  "GetWaypointsList_Response",
  _GetWaypointsList_Response__cdr_serialize,
  _GetWaypointsList_Response__cdr_deserialize,
  _GetWaypointsList_Response__get_serialized_size,
  _GetWaypointsList_Response__max_serialized_size
};

static rosidl_message_type_support_t _GetWaypointsList_Response__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_GetWaypointsList_Response__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace waypoints_types

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_waypoints_types
const rosidl_message_type_support_t *
get_message_type_support_handle<waypoints_types::srv::GetWaypointsList_Response>()
{
  return &waypoints_types::srv::typesupport_fastrtps_cpp::_GetWaypointsList_Response__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, waypoints_types, srv, GetWaypointsList_Response)() {
  return &waypoints_types::srv::typesupport_fastrtps_cpp::_GetWaypointsList_Response__handle;
}

#ifdef __cplusplus
}
#endif

#include "rmw/error_handling.h"
// already included above
// #include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/service_type_support_decl.hpp"

namespace waypoints_types
{

namespace srv
{

namespace typesupport_fastrtps_cpp
{

static service_type_support_callbacks_t _GetWaypointsList__callbacks = {
  "waypoints_types::srv",
  "GetWaypointsList",
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, waypoints_types, srv, GetWaypointsList_Request)(),
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, waypoints_types, srv, GetWaypointsList_Response)(),
};

static rosidl_service_type_support_t _GetWaypointsList__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_GetWaypointsList__callbacks,
  get_service_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace srv

}  // namespace waypoints_types

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_waypoints_types
const rosidl_service_type_support_t *
get_service_type_support_handle<waypoints_types::srv::GetWaypointsList>()
{
  return &waypoints_types::srv::typesupport_fastrtps_cpp::_GetWaypointsList__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, waypoints_types, srv, GetWaypointsList)() {
  return &waypoints_types::srv::typesupport_fastrtps_cpp::_GetWaypointsList__handle;
}

#ifdef __cplusplus
}
#endif
