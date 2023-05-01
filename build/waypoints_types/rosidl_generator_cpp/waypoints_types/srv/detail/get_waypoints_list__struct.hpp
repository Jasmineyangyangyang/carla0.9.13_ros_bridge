// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice

#ifndef WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__STRUCT_HPP_
#define WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__STRUCT_HPP_

#include <rosidl_runtime_cpp/bounded_vector.hpp>
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>


// Include directives for member types
// Member 'vehiclename'
#include "std_msgs/msg/detail/string__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__waypoints_types__srv__GetWaypointsList_Request __attribute__((deprecated))
#else
# define DEPRECATED__waypoints_types__srv__GetWaypointsList_Request __declspec(deprecated)
#endif

namespace waypoints_types
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetWaypointsList_Request_
{
  using Type = GetWaypointsList_Request_<ContainerAllocator>;

  explicit GetWaypointsList_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : vehiclename(_init)
  {
    (void)_init;
  }

  explicit GetWaypointsList_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : vehiclename(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _vehiclename_type =
    std_msgs::msg::String_<ContainerAllocator>;
  _vehiclename_type vehiclename;

  // setters for named parameter idiom
  Type & set__vehiclename(
    const std_msgs::msg::String_<ContainerAllocator> & _arg)
  {
    this->vehiclename = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__waypoints_types__srv__GetWaypointsList_Request
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__waypoints_types__srv__GetWaypointsList_Request
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetWaypointsList_Request_ & other) const
  {
    if (this->vehiclename != other.vehiclename) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetWaypointsList_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetWaypointsList_Request_

// alias to use template instance with default allocator
using GetWaypointsList_Request =
  waypoints_types::srv::GetWaypointsList_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace waypoints_types


// Include directives for member types
// Member 'vehiclepose'
#include "geometry_msgs/msg/detail/pose_stamped__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__waypoints_types__srv__GetWaypointsList_Response __attribute__((deprecated))
#else
# define DEPRECATED__waypoints_types__srv__GetWaypointsList_Response __declspec(deprecated)
#endif

namespace waypoints_types
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetWaypointsList_Response_
{
  using Type = GetWaypointsList_Response_<ContainerAllocator>;

  explicit GetWaypointsList_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : vehiclepose(_init)
  {
    (void)_init;
  }

  explicit GetWaypointsList_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : vehiclepose(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _vehiclepose_type =
    geometry_msgs::msg::PoseStamped_<ContainerAllocator>;
  _vehiclepose_type vehiclepose;

  // setters for named parameter idiom
  Type & set__vehiclepose(
    const geometry_msgs::msg::PoseStamped_<ContainerAllocator> & _arg)
  {
    this->vehiclepose = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__waypoints_types__srv__GetWaypointsList_Response
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__waypoints_types__srv__GetWaypointsList_Response
    std::shared_ptr<waypoints_types::srv::GetWaypointsList_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetWaypointsList_Response_ & other) const
  {
    if (this->vehiclepose != other.vehiclepose) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetWaypointsList_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetWaypointsList_Response_

// alias to use template instance with default allocator
using GetWaypointsList_Response =
  waypoints_types::srv::GetWaypointsList_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace waypoints_types

namespace waypoints_types
{

namespace srv
{

struct GetWaypointsList
{
  using Request = waypoints_types::srv::GetWaypointsList_Request;
  using Response = waypoints_types::srv::GetWaypointsList_Response;
};

}  // namespace srv

}  // namespace waypoints_types

#endif  // WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__STRUCT_HPP_
