API Notes: CoreML framework
===========================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreml?language=objc

These bindings are accessed through the ``ColorSync`` package (that is,
``import ColorSync``).


API Notes
---------

.. note::

   This framework is only available on macOS 10.13 and later.

.. warning::

   This frameworks make use of SIMD/vector types, and those are not yet
   supported by PyObjC.
