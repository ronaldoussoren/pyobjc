API Notes: dispatch library
===========================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__.

.. __: https://developer.apple.com/documentation/dispatch?language=objc

These bindings are accessed through the ``libdispatch`` package (that is, ``import libdispatch``).


API Notes
---------

.. note::

   These bindings are only available on macOS 10.10 or later. The dispatch library is
   available on earlier releases of OSX, but in a way that is not compatbile with these
   bindings.


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

