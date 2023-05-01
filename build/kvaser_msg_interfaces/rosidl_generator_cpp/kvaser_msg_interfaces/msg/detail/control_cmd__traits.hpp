// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#ifndef KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__TRAITS_HPP_
#define KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__TRAITS_HPP_

#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<kvaser_msg_interfaces::msg::ControlCmd>()
{
  return "kvaser_msg_interfaces::msg::ControlCmd";
}

template<>
inline const char * name<kvaser_msg_interfaces::msg::ControlCmd>()
{
  return "kvaser_msg_interfaces/msg/ControlCmd";
}

template<>
struct has_fixed_size<kvaser_msg_interfaces::msg::ControlCmd>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<kvaser_msg_interfaces::msg::ControlCmd>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<kvaser_msg_interfaces::msg::ControlCmd>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__TRAITS_HPP_
