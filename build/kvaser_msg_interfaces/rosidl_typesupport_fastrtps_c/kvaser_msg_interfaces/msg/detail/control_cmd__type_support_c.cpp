// generated from rosidl_typesupport_fastrtps_c/resource/idl__type_support_c.cpp.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice
#include "kvaser_msg_interfaces/msg/detail/control_cmd__rosidl_typesupport_fastrtps_c.h"


#include <cassert>
#include <limits>
#include <string>
#include "rosidl_typesupport_fastrtps_c/identifier.h"
#include "rosidl_typesupport_fastrtps_c/wstring_conversion.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "kvaser_msg_interfaces/msg/rosidl_typesupport_fastrtps_c__visibility_control.h"
#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.h"
#include "kvaser_msg_interfaces/msg/detail/control_cmd__functions.h"
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


// forward declare type support functions


using _ControlCmd__ros_msg_type = kvaser_msg_interfaces__msg__ControlCmd;

static bool _ControlCmd__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  const _ControlCmd__ros_msg_type * ros_message = static_cast<const _ControlCmd__ros_msg_type *>(untyped_ros_message);
  // Field name: time
  {
    cdr << ros_message->time;
  }

  // Field name: stangle
  {
    cdr << ros_message->stangle;
  }

  // Field name: vehiclevx
  {
    cdr << ros_message->vehiclevx;
  }

  return true;
}

static bool _ControlCmd__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  if (!untyped_ros_message) {
    fprintf(stderr, "ros message handle is null\n");
    return false;
  }
  _ControlCmd__ros_msg_type * ros_message = static_cast<_ControlCmd__ros_msg_type *>(untyped_ros_message);
  // Field name: time
  {
    cdr >> ros_message->time;
  }

  // Field name: stangle
  {
    cdr >> ros_message->stangle;
  }

  // Field name: vehiclevx
  {
    cdr >> ros_message->vehiclevx;
  }

  return true;
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_kvaser_msg_interfaces
size_t get_serialized_size_kvaser_msg_interfaces__msg__ControlCmd(
  const void * untyped_ros_message,
  size_t current_alignment)
{
  const _ControlCmd__ros_msg_type * ros_message = static_cast<const _ControlCmd__ros_msg_type *>(untyped_ros_message);
  (void)ros_message;
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // field.name time
  {
    size_t item_size = sizeof(ros_message->time);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name stangle
  {
    size_t item_size = sizeof(ros_message->stangle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // field.name vehiclevx
  {
    size_t item_size = sizeof(ros_message->vehiclevx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

static uint32_t _ControlCmd__get_serialized_size(const void * untyped_ros_message)
{
  return static_cast<uint32_t>(
    get_serialized_size_kvaser_msg_interfaces__msg__ControlCmd(
      untyped_ros_message, 0));
}

ROSIDL_TYPESUPPORT_FASTRTPS_C_PUBLIC_kvaser_msg_interfaces
size_t max_serialized_size_kvaser_msg_interfaces__msg__ControlCmd(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;

  // member: time
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: stangle
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }
  // member: vehiclevx
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static size_t _ControlCmd__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_kvaser_msg_interfaces__msg__ControlCmd(
    full_bounded, 0);
}


static message_type_support_callbacks_t __callbacks_ControlCmd = {
  "kvaser_msg_interfaces::msg",
  "ControlCmd",
  _ControlCmd__cdr_serialize,
  _ControlCmd__cdr_deserialize,
  _ControlCmd__get_serialized_size,
  _ControlCmd__max_serialized_size
};

static rosidl_message_type_support_t _ControlCmd__type_support = {
  rosidl_typesupport_fastrtps_c__identifier,
  &__callbacks_ControlCmd,
  get_message_typesupport_handle_function,
};

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_c, kvaser_msg_interfaces, msg, ControlCmd)() {
  return &_ControlCmd__type_support;
}

#if defined(__cplusplus)
}
#endif
