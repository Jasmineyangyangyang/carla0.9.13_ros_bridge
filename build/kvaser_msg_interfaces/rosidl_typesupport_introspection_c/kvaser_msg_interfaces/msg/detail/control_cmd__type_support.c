// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "kvaser_msg_interfaces/msg/detail/control_cmd__rosidl_typesupport_introspection_c.h"
#include "kvaser_msg_interfaces/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "kvaser_msg_interfaces/msg/detail/control_cmd__functions.h"
#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  kvaser_msg_interfaces__msg__ControlCmd__init(message_memory);
}

void ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_fini_function(void * message_memory)
{
  kvaser_msg_interfaces__msg__ControlCmd__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_member_array[3] = {
  {
    "time",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(kvaser_msg_interfaces__msg__ControlCmd, time),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "stangle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(kvaser_msg_interfaces__msg__ControlCmd, stangle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "vehiclevx",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(kvaser_msg_interfaces__msg__ControlCmd, vehiclevx),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_members = {
  "kvaser_msg_interfaces__msg",  // message namespace
  "ControlCmd",  // message name
  3,  // number of fields
  sizeof(kvaser_msg_interfaces__msg__ControlCmd),
  ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_member_array,  // message members
  ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_init_function,  // function to initialize message memory (memory has to be allocated)
  ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_type_support_handle = {
  0,
  &ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_kvaser_msg_interfaces
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, kvaser_msg_interfaces, msg, ControlCmd)() {
  if (!ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_type_support_handle.typesupport_identifier) {
    ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &ControlCmd__rosidl_typesupport_introspection_c__ControlCmd_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
