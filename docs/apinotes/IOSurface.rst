API Notes: IOSurface framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/iosurface/?preferredLanguage=occ

These bindings are accessed through the ``IOSurface`` package (that is, ``import IOSurface``).


API Notes
---------

The entire framework is available from Python. But note that PyObjC does not have bindings
for mach ports and the C library for XPC.

.. note::

   This framework is only available on macOS 10.6.
