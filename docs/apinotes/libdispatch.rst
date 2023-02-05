API Notes: dispatch library
===========================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__.

.. __: https://developer.apple.com/documentation/dispatch?language=objc

These bindings are accessed through the ``dispatch`` package (that is, ``import dispatch``).

For backward compatibility ``import libdispatch`` works as well.


API Notes
---------

.. note::

   These bindings are only available on macOS 10.8 or later. The dispatch library is
   available on earlier releases of macOS, but in a way that is not compatible with these
   bindings.

The libraries exposes a number APIs in two variants: one that has a block as an argument,
and one that has a function as an argument. Both can be used from Python, but in general
the block version is more convenient to use.

This is a fairly low-level API and programming errors can result in hard crashes instead
of exceptions or error returns.


```dispatch_retain```, ```dispatch_release```
.............................................

These functions are not available.

```dispatch_debug```, ```dispatch_debugv```
.............................................

These functions are not available.

```dispatch_wait```, ```dispatch_notify```, ```dispatch_cancel```, ```dispatch_testcancel```
............................................................................................

This functions are not available, use the specific variant for the type of object
you are working with instead.


```dispatch_once```, ```dispatch_once_f```
..........................................

These functions can be used from Python, but must be called with
an ```array.array``` instance as their first arguments:

::

   pred = array.array('l', [0])
   dispatch_one(pred, callable)


```dispatch_assert_queue_debug```, ```dispatch_assert_queue_barrier_debug```, ```dispatch_assert_queue_not_debug```
...................................................................................................................

These functions are not available. Call the functions without the ```_debug``` suffix instead.


```dispatch_introspection_hook_queue_create```, ```dispatch_introspection_hook_queue_destroy```
...............................................................................................

These functions are not available.


```dispatch_introspection_hook_queue_item_enqueue```, ```dispatch_introspection_hook_queue_item_dequeue```
..........................................................................................................

These functions are not available.


```dispatch_introspection_hook_queue_item_complete```, ```dispatch_introspection_hook_queue_item_complete```
............................................................................................................

These functions are not available.


```dispatch_introspection_hook_queue_callout_begin```, ```dispatch_introspection_hook_queue_callout_end```
..........................................................................................................

These functions are not available.


```dispatch_data_create```
..........................

Use *DISPATCH_DATA_DESTRUCTOR_DEFAULT* as the destructor.

The workgroup API's
....................

The various workgroup APIs (introduced in macOS 11) are not supported.
