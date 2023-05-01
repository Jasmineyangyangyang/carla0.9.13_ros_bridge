// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from waypoints_types:srv/GetWaypointsList.idl
// generated code does not contain a copyright notice
#include "waypoints_types/srv/detail/get_waypoints_list__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

// Include directives for member types
// Member `vehiclename`
#include "std_msgs/msg/detail/string__functions.h"

bool
waypoints_types__srv__GetWaypointsList_Request__init(waypoints_types__srv__GetWaypointsList_Request * msg)
{
  if (!msg) {
    return false;
  }
  // vehiclename
  if (!std_msgs__msg__String__init(&msg->vehiclename)) {
    waypoints_types__srv__GetWaypointsList_Request__fini(msg);
    return false;
  }
  return true;
}

void
waypoints_types__srv__GetWaypointsList_Request__fini(waypoints_types__srv__GetWaypointsList_Request * msg)
{
  if (!msg) {
    return;
  }
  // vehiclename
  std_msgs__msg__String__fini(&msg->vehiclename);
}

bool
waypoints_types__srv__GetWaypointsList_Request__are_equal(const waypoints_types__srv__GetWaypointsList_Request * lhs, const waypoints_types__srv__GetWaypointsList_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // vehiclename
  if (!std_msgs__msg__String__are_equal(
      &(lhs->vehiclename), &(rhs->vehiclename)))
  {
    return false;
  }
  return true;
}

bool
waypoints_types__srv__GetWaypointsList_Request__copy(
  const waypoints_types__srv__GetWaypointsList_Request * input,
  waypoints_types__srv__GetWaypointsList_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // vehiclename
  if (!std_msgs__msg__String__copy(
      &(input->vehiclename), &(output->vehiclename)))
  {
    return false;
  }
  return true;
}

waypoints_types__srv__GetWaypointsList_Request *
waypoints_types__srv__GetWaypointsList_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  waypoints_types__srv__GetWaypointsList_Request * msg = (waypoints_types__srv__GetWaypointsList_Request *)allocator.allocate(sizeof(waypoints_types__srv__GetWaypointsList_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(waypoints_types__srv__GetWaypointsList_Request));
  bool success = waypoints_types__srv__GetWaypointsList_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
waypoints_types__srv__GetWaypointsList_Request__destroy(waypoints_types__srv__GetWaypointsList_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    waypoints_types__srv__GetWaypointsList_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
waypoints_types__srv__GetWaypointsList_Request__Sequence__init(waypoints_types__srv__GetWaypointsList_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  waypoints_types__srv__GetWaypointsList_Request * data = NULL;

  if (size) {
    data = (waypoints_types__srv__GetWaypointsList_Request *)allocator.zero_allocate(size, sizeof(waypoints_types__srv__GetWaypointsList_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = waypoints_types__srv__GetWaypointsList_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        waypoints_types__srv__GetWaypointsList_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
waypoints_types__srv__GetWaypointsList_Request__Sequence__fini(waypoints_types__srv__GetWaypointsList_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      waypoints_types__srv__GetWaypointsList_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

waypoints_types__srv__GetWaypointsList_Request__Sequence *
waypoints_types__srv__GetWaypointsList_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  waypoints_types__srv__GetWaypointsList_Request__Sequence * array = (waypoints_types__srv__GetWaypointsList_Request__Sequence *)allocator.allocate(sizeof(waypoints_types__srv__GetWaypointsList_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = waypoints_types__srv__GetWaypointsList_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
waypoints_types__srv__GetWaypointsList_Request__Sequence__destroy(waypoints_types__srv__GetWaypointsList_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    waypoints_types__srv__GetWaypointsList_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
waypoints_types__srv__GetWaypointsList_Request__Sequence__are_equal(const waypoints_types__srv__GetWaypointsList_Request__Sequence * lhs, const waypoints_types__srv__GetWaypointsList_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!waypoints_types__srv__GetWaypointsList_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
waypoints_types__srv__GetWaypointsList_Request__Sequence__copy(
  const waypoints_types__srv__GetWaypointsList_Request__Sequence * input,
  waypoints_types__srv__GetWaypointsList_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(waypoints_types__srv__GetWaypointsList_Request);
    waypoints_types__srv__GetWaypointsList_Request * data =
      (waypoints_types__srv__GetWaypointsList_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!waypoints_types__srv__GetWaypointsList_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          waypoints_types__srv__GetWaypointsList_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!waypoints_types__srv__GetWaypointsList_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `vehiclepose`
#include "geometry_msgs/msg/detail/pose_stamped__functions.h"

bool
waypoints_types__srv__GetWaypointsList_Response__init(waypoints_types__srv__GetWaypointsList_Response * msg)
{
  if (!msg) {
    return false;
  }
  // vehiclepose
  if (!geometry_msgs__msg__PoseStamped__init(&msg->vehiclepose)) {
    waypoints_types__srv__GetWaypointsList_Response__fini(msg);
    return false;
  }
  return true;
}

void
waypoints_types__srv__GetWaypointsList_Response__fini(waypoints_types__srv__GetWaypointsList_Response * msg)
{
  if (!msg) {
    return;
  }
  // vehiclepose
  geometry_msgs__msg__PoseStamped__fini(&msg->vehiclepose);
}

bool
waypoints_types__srv__GetWaypointsList_Response__are_equal(const waypoints_types__srv__GetWaypointsList_Response * lhs, const waypoints_types__srv__GetWaypointsList_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // vehiclepose
  if (!geometry_msgs__msg__PoseStamped__are_equal(
      &(lhs->vehiclepose), &(rhs->vehiclepose)))
  {
    return false;
  }
  return true;
}

bool
waypoints_types__srv__GetWaypointsList_Response__copy(
  const waypoints_types__srv__GetWaypointsList_Response * input,
  waypoints_types__srv__GetWaypointsList_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // vehiclepose
  if (!geometry_msgs__msg__PoseStamped__copy(
      &(input->vehiclepose), &(output->vehiclepose)))
  {
    return false;
  }
  return true;
}

waypoints_types__srv__GetWaypointsList_Response *
waypoints_types__srv__GetWaypointsList_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  waypoints_types__srv__GetWaypointsList_Response * msg = (waypoints_types__srv__GetWaypointsList_Response *)allocator.allocate(sizeof(waypoints_types__srv__GetWaypointsList_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(waypoints_types__srv__GetWaypointsList_Response));
  bool success = waypoints_types__srv__GetWaypointsList_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
waypoints_types__srv__GetWaypointsList_Response__destroy(waypoints_types__srv__GetWaypointsList_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    waypoints_types__srv__GetWaypointsList_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
waypoints_types__srv__GetWaypointsList_Response__Sequence__init(waypoints_types__srv__GetWaypointsList_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  waypoints_types__srv__GetWaypointsList_Response * data = NULL;

  if (size) {
    data = (waypoints_types__srv__GetWaypointsList_Response *)allocator.zero_allocate(size, sizeof(waypoints_types__srv__GetWaypointsList_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = waypoints_types__srv__GetWaypointsList_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        waypoints_types__srv__GetWaypointsList_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
waypoints_types__srv__GetWaypointsList_Response__Sequence__fini(waypoints_types__srv__GetWaypointsList_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      waypoints_types__srv__GetWaypointsList_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

waypoints_types__srv__GetWaypointsList_Response__Sequence *
waypoints_types__srv__GetWaypointsList_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  waypoints_types__srv__GetWaypointsList_Response__Sequence * array = (waypoints_types__srv__GetWaypointsList_Response__Sequence *)allocator.allocate(sizeof(waypoints_types__srv__GetWaypointsList_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = waypoints_types__srv__GetWaypointsList_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
waypoints_types__srv__GetWaypointsList_Response__Sequence__destroy(waypoints_types__srv__GetWaypointsList_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    waypoints_types__srv__GetWaypointsList_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
waypoints_types__srv__GetWaypointsList_Response__Sequence__are_equal(const waypoints_types__srv__GetWaypointsList_Response__Sequence * lhs, const waypoints_types__srv__GetWaypointsList_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!waypoints_types__srv__GetWaypointsList_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
waypoints_types__srv__GetWaypointsList_Response__Sequence__copy(
  const waypoints_types__srv__GetWaypointsList_Response__Sequence * input,
  waypoints_types__srv__GetWaypointsList_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(waypoints_types__srv__GetWaypointsList_Response);
    waypoints_types__srv__GetWaypointsList_Response * data =
      (waypoints_types__srv__GetWaypointsList_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!waypoints_types__srv__GetWaypointsList_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          waypoints_types__srv__GetWaypointsList_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!waypoints_types__srv__GetWaypointsList_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
