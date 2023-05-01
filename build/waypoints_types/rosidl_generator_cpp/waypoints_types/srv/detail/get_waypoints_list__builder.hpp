// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice

#ifndef WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__BUILDER_HPP_
#define WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__BUILDER_HPP_

#include "waypoints_types/srv/detail/get_waypoints_list__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace waypoints_types
{

namespace srv
{

namespace builder
{

class Init_GetWaypointsList_Request_vehiclename
{
public:
  Init_GetWaypointsList_Request_vehiclename()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::waypoints_types::srv::GetWaypointsList_Request vehiclename(::waypoints_types::srv::GetWaypointsList_Request::_vehiclename_type arg)
  {
    msg_.vehiclename = std::move(arg);
    return std::move(msg_);
  }

private:
  ::waypoints_types::srv::GetWaypointsList_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::waypoints_types::srv::GetWaypointsList_Request>()
{
  return waypoints_types::srv::builder::Init_GetWaypointsList_Request_vehiclename();
}

}  // namespace waypoints_types


namespace waypoints_types
{

namespace srv
{

namespace builder
{

class Init_GetWaypointsList_Response_vehiclepose
{
public:
  Init_GetWaypointsList_Response_vehiclepose()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::waypoints_types::srv::GetWaypointsList_Response vehiclepose(::waypoints_types::srv::GetWaypointsList_Response::_vehiclepose_type arg)
  {
    msg_.vehiclepose = std::move(arg);
    return std::move(msg_);
  }

private:
  ::waypoints_types::srv::GetWaypointsList_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::waypoints_types::srv::GetWaypointsList_Response>()
{
  return waypoints_types::srv::builder::Init_GetWaypointsList_Response_vehiclepose();
}

}  // namespace waypoints_types

#endif  // WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__BUILDER_HPP_
