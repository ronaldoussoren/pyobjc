API Notes: GameplayKit framework
================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/gameplaykit?language=objc

These bindings are accessed through the ``GameplayKit`` package (that is, ``import GameplayKit``).


API Notes
---------

.. note::

   This framework is only available on macOS 10.11 and later.


A number of APIs in this framework use SIMD types such as ``vector_float2``.
Those SIMD types are not yet supported in PyObjC and those APIs cannot be
used.


``GK_VERSION``
..............

This is a version number for the SDK is not available in Python.
