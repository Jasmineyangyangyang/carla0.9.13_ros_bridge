// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice

#ifndef WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__TRAITS_HPP_
#define WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__TRAITS_HPP_

#include "waypoints_types/srv/detail/get_waypoints_list__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

// Include directives for member types
// Member 'vehiclename'
#include "std_msgs/msg/detail/string__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<waypoints_types::srv::GetWaypointsList_Request>()
{
  return "waypoints_types::srv::GetWaypointsList_Request";
}

template<>
inline const char * name<waypoints_types::srv::GetWaypointsList_Request>()
{
  return "waypoints_types/srv/GetWaypointsList_Request";
}

template<>
struct has_fixed_size<waypoints_types::srv::GetWaypointsList_Request>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::String>::value> {};

template<>
struct has_bounded_size<waypoints_types::srv::GetWaypointsList_Request>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::String>::value> {};

template<>
struct is_message<waypoints_types::srv::GetWaypointsList_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'vehiclepose'
#include "geometry_msgs/msg/detail/pose_stamped__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<waypoints_types::srv::GetWaypointsList_Response>()
{
  return "waypoints_types::srv::GetWaypointsList_Response";
}

template<>
inline const char * name<waypoints_types::srv::GetWaypointsList_Response>()
{
  return "waypoints_types/srv/GetWaypointsList_Response";
}

template<>
struct has_fixed_size<waypoints_types::srv::GetWaypointsList_Response>
  : std::integral_constant<bool, has_fixed_size<geometry_msgs::msg::PoseStamped>::value> {};

template<>
struct has_bounded_size<waypoints_types::srv::GetWaypointsList_Response>
  : std::integral_constant<bool, has_bounded_size<geometry_msgs::msg::PoseStamped>::value> {};

template<>
struct is_message<waypoints_types::srv::GetWaypointsList_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<waypoints_types::srv::GetWaypointsList>()
{
  return "waypoints_types::srv::GetWaypointsList";
}

template<>
inline const char * name<waypoints_types::srv::GetWaypointsList>()
{
  return "waypoints_types/srv/GetWaypointsList";
}

template<>
struct has_fixed_size<waypoints_types::srv::GetWaypointsList>
  : std::integral_constant<
    bool,
    has_fixed_size<waypoints_types::srv::GetWaypointsList_Request>::value &&
    has_fixed_size<waypoints_types::srv::GetWaypointsList_Response>::value
  >
{
};

template<>
struct has_bounded_size<waypoints_types::srv::GetWaypointsList>
  : std::integral_constant<
    bool,
    has_bounded_size<waypoints_types::srv::GetWaypointsList_Request>::value &&
    has_bounded_size<waypoints_types::srv::GetWaypointsList_Response>::value
  >
{
};

template<>
struct is_service<waypoints_types::srv::GetWaypointsList>
  : std::true_type
{
};

template<>
struct is_service_request<waypoints_types::srv::GetWaypointsList_Request>
  : std::true_type
{
};

template<>
struct is_service_response<waypoints_types::srv::GetWaypointsList_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // WAYPOINTS_TYPES__SRV__DETAIL__GET_WAYPOINTS_LIST__TRAITS_HPP_
