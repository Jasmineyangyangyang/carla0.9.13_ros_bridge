// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice
#include "kvaser_msg_interfaces/msg/detail/control_cmd__rosidl_typesupport_fastrtps_cpp.hpp"
#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.hpp"

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

namespace kvaser_msg_interfaces
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_kvaser_msg_interfaces
cdr_serialize(
  const kvaser_msg_interfaces::msg::ControlCmd & ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: time
  cdr << ros_message.time;
  // Member: stangle
  cdr << ros_message.stangle;
  // Member: vehiclevx
  cdr << ros_message.vehiclevx;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_kvaser_msg_interfaces
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  kvaser_msg_interfaces::msg::ControlCmd & ros_message)
{
  // Member: time
  cdr >> ros_message.time;

  // Member: stangle
  cdr >> ros_message.stangle;

  // Member: vehiclevx
  cdr >> ros_message.vehiclevx;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_kvaser_msg_interfaces
get_serialized_size(
  const kvaser_msg_interfaces::msg::ControlCmd & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: time
  {
    size_t item_size = sizeof(ros_message.time);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: stangle
  {
    size_t item_size = sizeof(ros_message.stangle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: vehiclevx
  {
    size_t item_size = sizeof(ros_message.vehiclevx);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_kvaser_msg_interfaces
max_serialized_size_ControlCmd(
  bool & full_bounded,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;
  (void)full_bounded;


  // Member: time
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: stangle
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: vehiclevx
  {
    size_t array_size = 1;

    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  return current_alignment - initial_alignment;
}

static bool _ControlCmd__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const kvaser_msg_interfaces::msg::ControlCmd *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ControlCmd__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<kvaser_msg_interfaces::msg::ControlCmd *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ControlCmd__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const kvaser_msg_interfaces::msg::ControlCmd *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ControlCmd__max_serialized_size(bool & full_bounded)
{
  return max_serialized_size_ControlCmd(full_bounded, 0);
}

static message_type_support_callbacks_t _ControlCmd__callbacks = {
  "kvaser_msg_interfaces::msg",
  "ControlCmd",
  _ControlCmd__cdr_serialize,
  _ControlCmd__cdr_deserialize,
  _ControlCmd__get_serialized_size,
  _ControlCmd__max_serialized_size
};

static rosidl_message_type_support_t _ControlCmd__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ControlCmd__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace kvaser_msg_interfaces

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_kvaser_msg_interfaces
const rosidl_message_type_support_t *
get_message_type_support_handle<kvaser_msg_interfaces::msg::ControlCmd>()
{
  return &kvaser_msg_interfaces::msg::typesupport_fastrtps_cpp::_ControlCmd__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, kvaser_msg_interfaces, msg, ControlCmd)() {
  return &kvaser_msg_interfaces::msg::typesupport_fastrtps_cpp::_ControlCmd__handle;
}

#ifdef __cplusplus
}
#endif
