// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from kvaser_msg_interfaces:msg/ControlCmd.idl
// generated code does not contain a copyright notice

#ifndef KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__FUNCTIONS_H_
#define KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "kvaser_msg_interfaces/msg/rosidl_generator_c__visibility_control.h"

#include "kvaser_msg_interfaces/msg/detail/control_cmd__struct.h"

/// Initialize msg/ControlCmd message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * kvaser_msg_interfaces__msg__ControlCmd
 * )) before or use
 * kvaser_msg_interfaces__msg__ControlCmd__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
bool
kvaser_msg_interfaces__msg__ControlCmd__init(kvaser_msg_interfaces__msg__ControlCmd * msg);

/// Finalize msg/ControlCmd message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
void
kvaser_msg_interfaces__msg__ControlCmd__fini(kvaser_msg_interfaces__msg__ControlCmd * msg);

/// Create msg/ControlCmd message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * kvaser_msg_interfaces__msg__ControlCmd__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
kvaser_msg_interfaces__msg__ControlCmd *
kvaser_msg_interfaces__msg__ControlCmd__create();

/// Destroy msg/ControlCmd message.
/**
 * It calls
 * kvaser_msg_interfaces__msg__ControlCmd__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
void
kvaser_msg_interfaces__msg__ControlCmd__destroy(kvaser_msg_interfaces__msg__ControlCmd * msg);

/// Check for msg/ControlCmd message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
bool
kvaser_msg_interfaces__msg__ControlCmd__are_equal(const kvaser_msg_interfaces__msg__ControlCmd * lhs, const kvaser_msg_interfaces__msg__ControlCmd * rhs);

/// Copy a msg/ControlCmd message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
bool
kvaser_msg_interfaces__msg__ControlCmd__copy(
  const kvaser_msg_interfaces__msg__ControlCmd * input,
  kvaser_msg_interfaces__msg__ControlCmd * output);

/// Initialize array of msg/ControlCmd messages.
/**
 * It allocates the memory for the number of elements and calls
 * kvaser_msg_interfaces__msg__ControlCmd__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
bool
kvaser_msg_interfaces__msg__ControlCmd__Sequence__init(kvaser_msg_interfaces__msg__ControlCmd__Sequence * array, size_t size);

/// Finalize array of msg/ControlCmd messages.
/**
 * It calls
 * kvaser_msg_interfaces__msg__ControlCmd__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
void
kvaser_msg_interfaces__msg__ControlCmd__Sequence__fini(kvaser_msg_interfaces__msg__ControlCmd__Sequence * array);

/// Create array of msg/ControlCmd messages.
/**
 * It allocates the memory for the array and calls
 * kvaser_msg_interfaces__msg__ControlCmd__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
kvaser_msg_interfaces__msg__ControlCmd__Sequence *
kvaser_msg_interfaces__msg__ControlCmd__Sequence__create(size_t size);

/// Destroy array of msg/ControlCmd messages.
/**
 * It calls
 * kvaser_msg_interfaces__msg__ControlCmd__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
void
kvaser_msg_interfaces__msg__ControlCmd__Sequence__destroy(kvaser_msg_interfaces__msg__ControlCmd__Sequence * array);

/// Check for msg/ControlCmd message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
bool
kvaser_msg_interfaces__msg__ControlCmd__Sequence__are_equal(const kvaser_msg_interfaces__msg__ControlCmd__Sequence * lhs, const kvaser_msg_interfaces__msg__ControlCmd__Sequence * rhs);

/// Copy an array of msg/ControlCmd messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_kvaser_msg_interfaces
bool
kvaser_msg_interfaces__msg__ControlCmd__Sequence__copy(
  const kvaser_msg_interfaces__msg__ControlCmd__Sequence * input,
  kvaser_msg_interfaces__msg__ControlCmd__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // KVASER_MSG_INTERFACES__MSG__DETAIL__CONTROL_CMD__FUNCTIONS_H_
