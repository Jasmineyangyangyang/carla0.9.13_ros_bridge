// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice
#include "kvaser_msg_interfaces/msg/detail/control_cmd__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
kvaser_msg_interfaces__msg__ControlCmd__init(kvaser_msg_interfaces__msg__ControlCmd * msg)
{
  if (!msg) {
    return false;
  }
  // time
  // stangle
  // vehiclevx
  return true;
}

void
kvaser_msg_interfaces__msg__ControlCmd__fini(kvaser_msg_interfaces__msg__ControlCmd * msg)
{
  if (!msg) {
    return;
  }
  // time
  // stangle
  // vehiclevx
}

bool
kvaser_msg_interfaces__msg__ControlCmd__are_equal(const kvaser_msg_interfaces__msg__ControlCmd * lhs, const kvaser_msg_interfaces__msg__ControlCmd * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // time
  if (lhs->time != rhs->time) {
    return false;
  }
  // stangle
  if (lhs->stangle != rhs->stangle) {
    return false;
  }
  // vehiclevx
  if (lhs->vehiclevx != rhs->vehiclevx) {
    return false;
  }
  return true;
}

bool
kvaser_msg_interfaces__msg__ControlCmd__copy(
  const kvaser_msg_interfaces__msg__ControlCmd * input,
  kvaser_msg_interfaces__msg__ControlCmd * output)
{
  if (!input || !output) {
    return false;
  }
  // time
  output->time = input->time;
  // stangle
  output->stangle = input->stangle;
  // vehiclevx
  output->vehiclevx = input->vehiclevx;
  return true;
}

kvaser_msg_interfaces__msg__ControlCmd *
kvaser_msg_interfaces__msg__ControlCmd__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  kvaser_msg_interfaces__msg__ControlCmd * msg = (kvaser_msg_interfaces__msg__ControlCmd *)allocator.allocate(sizeof(kvaser_msg_interfaces__msg__ControlCmd), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(kvaser_msg_interfaces__msg__ControlCmd));
  bool success = kvaser_msg_interfaces__msg__ControlCmd__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
kvaser_msg_interfaces__msg__ControlCmd__destroy(kvaser_msg_interfaces__msg__ControlCmd * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    kvaser_msg_interfaces__msg__ControlCmd__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
kvaser_msg_interfaces__msg__ControlCmd__Sequence__init(kvaser_msg_interfaces__msg__ControlCmd__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  kvaser_msg_interfaces__msg__ControlCmd * data = NULL;

  if (size) {
    data = (kvaser_msg_interfaces__msg__ControlCmd *)allocator.zero_allocate(size, sizeof(kvaser_msg_interfaces__msg__ControlCmd), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = kvaser_msg_interfaces__msg__ControlCmd__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        kvaser_msg_interfaces__msg__ControlCmd__fini(&data[i - 1]);
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
kvaser_msg_interfaces__msg__ControlCmd__Sequence__fini(kvaser_msg_interfaces__msg__ControlCmd__Sequence * array)
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
      kvaser_msg_interfaces__msg__ControlCmd__fini(&array->data[i]);
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

kvaser_msg_interfaces__msg__ControlCmd__Sequence *
kvaser_msg_interfaces__msg__ControlCmd__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  kvaser_msg_interfaces__msg__ControlCmd__Sequence * array = (kvaser_msg_interfaces__msg__ControlCmd__Sequence *)allocator.allocate(sizeof(kvaser_msg_interfaces__msg__ControlCmd__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = kvaser_msg_interfaces__msg__ControlCmd__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
kvaser_msg_interfaces__msg__ControlCmd__Sequence__destroy(kvaser_msg_interfaces__msg__ControlCmd__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    kvaser_msg_interfaces__msg__ControlCmd__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
kvaser_msg_interfaces__msg__ControlCmd__Sequence__are_equal(const kvaser_msg_interfaces__msg__ControlCmd__Sequence * lhs, const kvaser_msg_interfaces__msg__ControlCmd__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!kvaser_msg_interfaces__msg__ControlCmd__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
kvaser_msg_interfaces__msg__ControlCmd__Sequence__copy(
  const kvaser_msg_interfaces__msg__ControlCmd__Sequence * input,
  kvaser_msg_interfaces__msg__ControlCmd__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(kvaser_msg_interfaces__msg__ControlCmd);
    kvaser_msg_interfaces__msg__ControlCmd * data =
      (kvaser_msg_interfaces__msg__ControlCmd *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!kvaser_msg_interfaces__msg__ControlCmd__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          kvaser_msg_interfaces__msg__ControlCmd__fini(&data[i]);
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
    if (!kvaser_msg_interfaces__msg__ControlCmd__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
