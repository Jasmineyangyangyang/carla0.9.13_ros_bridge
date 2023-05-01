// generated from rosidl_typesupport_introspection_cpp/resource/idl__type_support.cpp.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#include "array"
#include "cstddef"
#include "string"
#include "vector"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_interface/macros.h"
#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.hpp"
#include "rosidl_typesupport_introspection_cpp/field_types.hpp"
#include "rosidl_typesupport_introspection_cpp/identifier.hpp"
#include "rosidl_typesupport_introspection_cpp/message_introspection.hpp"
#include "rosidl_typesupport_introspection_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_introspection_cpp/visibility_control.h"

namespace kvaser_msg_interfaces
{

namespace msg
{

namespace rosidl_typesupport_introspection_cpp
{

void ControlCmd_init_function(
  void * message_memory, rosidl_runtime_cpp::MessageInitialization _init)
{
  new (message_memory) kvaser_msg_interfaces::msg::ControlCmd(_init);
}

void ControlCmd_fini_function(void * message_memory)
{
  auto typed_message = static_cast<kvaser_msg_interfaces::msg::ControlCmd *>(message_memory);
  typed_message->~ControlCmd();
}

static const ::rosidl_typesupport_introspection_cpp::MessageMember ControlCmd_message_member_array[3] = {
  {
    "time",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(kvaser_msg_interfaces::msg::ControlCmd, time),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "stangle",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(kvaser_msg_interfaces::msg::ControlCmd, stangle),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  },
  {
    "vehiclevx",  // name
    ::rosidl_typesupport_introspection_cpp::ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    nullptr,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(kvaser_msg_interfaces::msg::ControlCmd, vehiclevx),  // bytes offset in struct
    nullptr,  // default value
    nullptr,  // size() function pointer
    nullptr,  // get_const(index) function pointer
    nullptr,  // get(index) function pointer
    nullptr  // resize(index) function pointer
  }
};

static const ::rosidl_typesupport_introspection_cpp::MessageMembers ControlCmd_message_members = {
  "kvaser_msg_interfaces::msg",  // message namespace
  "ControlCmd",  // message name
  3,  // number of fields
  sizeof(kvaser_msg_interfaces::msg::ControlCmd),
  ControlCmd_message_member_array,  // message members
  ControlCmd_init_function,  // function to initialize message memory (memory has to be allocated)
  ControlCmd_fini_function  // function to terminate message instance (will not free memory)
};

static const rosidl_message_type_support_t ControlCmd_message_type_support_handle = {
  ::rosidl_typesupport_introspection_cpp::typesupport_identifier,
  &ControlCmd_message_members,
  get_message_typesupport_handle_function,
};

}  // namespace rosidl_typesupport_introspection_cpp

}  // namespace msg

}  // namespace kvaser_msg_interfaces


namespace rosidl_typesupport_introspection_cpp
{

template<>
ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
get_message_type_support_handle<kvaser_msg_interfaces::msg::ControlCmd>()
{
  return &::kvaser_msg_interfaces::msg::rosidl_typesupport_introspection_cpp::ControlCmd_message_type_support_handle;
}

}  // namespace rosidl_typesupport_introspection_cpp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_INTROSPECTION_CPP_PUBLIC
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_cpp, kvaser_msg_interfaces, msg, ControlCmd)() {
  return &::kvaser_msg_interfaces::msg::rosidl_typesupport_introspection_cpp::ControlCmd_message_type_support_handle;
}

#ifdef __cplusplus
}
#endif
