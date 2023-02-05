API Notes: xpc library
===========================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__.

.. __: https://developer.apple.com/documentation/xpc?language=objc

These bindings are accessed through the ``xpc`` package (that is, ``import xpc``).


API Notes
---------

The libraries exposes a number APIs in two variants: one that has a block as an argument,
and one that has a function as an argument. Both can be used from Python, but in general
the block version is more convenient to use.

This is a fairly low-level API and programming errors can result in hard crashes instead
of exceptions or error returns.

All "C" strings in the API are represented as bytes objects in Python, not as normal
(unicode) strings.


```xpc_retain```, ```xpc_release```
...................................

These functions are not available.


```xpc_string_create_with_format_and_arguments```
.................................................

Not available, use ``xpc_string_create_with_format`` instead.

SHMEM values
............

There is no clear mapping of "shmem" type objects to Python, although
the APIs are available.
