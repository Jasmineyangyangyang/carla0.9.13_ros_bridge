// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#ifndef KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__BUILDER_HPP_
#define KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__BUILDER_HPP_

#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace kvaser_msg_interfaces
{

namespace msg
{

namespace builder
{

class Init_ControlCmd_vehiclevx
{
public:
  explicit Init_ControlCmd_vehiclevx(::kvaser_msg_interfaces::msg::ControlCmd & msg)
  : msg_(msg)
  {}
  ::kvaser_msg_interfaces::msg::ControlCmd vehiclevx(::kvaser_msg_interfaces::msg::ControlCmd::_vehiclevx_type arg)
  {
    msg_.vehiclevx = std::move(arg);
    return std::move(msg_);
  }

private:
  ::kvaser_msg_interfaces::msg::ControlCmd msg_;
};

class Init_ControlCmd_stangle
{
public:
  explicit Init_ControlCmd_stangle(::kvaser_msg_interfaces::msg::ControlCmd & msg)
  : msg_(msg)
  {}
  Init_ControlCmd_vehiclevx stangle(::kvaser_msg_interfaces::msg::ControlCmd::_stangle_type arg)
  {
    msg_.stangle = std::move(arg);
    return Init_ControlCmd_vehiclevx(msg_);
  }

private:
  ::kvaser_msg_interfaces::msg::ControlCmd msg_;
};

class Init_ControlCmd_time
{
public:
  Init_ControlCmd_time()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlCmd_stangle time(::kvaser_msg_interfaces::msg::ControlCmd::_time_type arg)
  {
    msg_.time = std::move(arg);
    return Init_ControlCmd_stangle(msg_);
  }

private:
  ::kvaser_msg_interfaces::msg::ControlCmd msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::kvaser_msg_interfaces::msg::ControlCmd>()
{
  return kvaser_msg_interfaces::msg::builder::Init_ControlCmd_time();
}

}  // namespace kvaser_msg_interfaces

#endif  // KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__BUILDER_HPP_
