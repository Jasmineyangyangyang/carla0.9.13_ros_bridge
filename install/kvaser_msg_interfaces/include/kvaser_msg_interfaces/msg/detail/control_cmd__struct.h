// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#ifndef KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__STRUCT_H_
#define KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Struct defined in msg/ControlCmd in the package kvaser_msg_interfaces.
typedef struct kvaser_msg_interfaces__msg__ControlCmd
{
  float time;
  float stangle;
  float vehiclevx;
} kvaser_msg_interfaces__msg__ControlCmd;

// Struct for a sequence of kvaser_msg_interfaces__msg__ControlCmd.
typedef struct kvaser_msg_interfaces__msg__ControlCmd__Sequence
{
  kvaser_msg_interfaces__msg__ControlCmd * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} kvaser_msg_interfaces__msg__ControlCmd__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__STRUCT_H_
