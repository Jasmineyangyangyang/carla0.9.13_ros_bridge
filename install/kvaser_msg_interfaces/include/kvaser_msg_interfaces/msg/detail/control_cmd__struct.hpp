// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#ifndef KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__STRUCT_HPP_
#define KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


#ifndef _WIN32
# define DEPRECATED__kvaser_msg_interfaces__msg__ControlCmd __attribute__((deprecated))
#else
# define DEPRECATED__kvaser_msg_interfaces__msg__ControlCmd __declspec(deprecated)
#endif

namespace kvaser_msg_interfaces
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControlCmd_
{
  using Type = ControlCmd_<ContainerAllocator>;

  explicit ControlCmd_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0f;
      this->stangle = 0.0f;
      this->vehiclevx = 0.0f;
    }
  }

  explicit ControlCmd_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->time = 0.0f;
      this->stangle = 0.0f;
      this->vehiclevx = 0.0f;
    }
  }

  // field types and members
  using _time_type =
    float;
  _time_type time;
  using _stangle_type =
    float;
  _stangle_type stangle;
  using _vehiclevx_type =
    float;
  _vehiclevx_type vehiclevx;

  // setters for named parameter idiom
  Type & set__time(
    const float & _arg)
  {
    this->time = _arg;
    return *this;
  }
  Type & set__stangle(
    const float & _arg)
  {
    this->stangle = _arg;
    return *this;
  }
  Type & set__vehiclevx(
    const float & _arg)
  {
    this->vehiclevx = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator> *;
  using ConstRawPtr =
    const kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__kvaser_msg_interfaces__msg__ControlCmd
    std::shared_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__kvaser_msg_interfaces__msg__ControlCmd
    std::shared_ptr<kvaser_msg_interfaces::msg::ControlCmd_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlCmd_ & other) const
  {
    if (this->time != other.time) {
      return false;
    }
    if (this->stangle != other.stangle) {
      return false;
    }
    if (this->vehiclevx != other.vehiclevx) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlCmd_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlCmd_

// alias to use template instance with default allocator
using ControlCmd =
  kvaser_msg_interfaces::msg::ControlCmd_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace kvaser_msg_interfaces

#endif  // KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__STRUCT_HPP_
