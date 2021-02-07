API Notes: GameController framework
===================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/gamecontroller/?preferredLanguage=occ

These bindings are accessed through the ``GameController`` package (that is, ``import GameController``).


API Notes
---------

The full API for the GameController framework is available from Python

.. note::

   This framework is only available on macOS 10.9 and later.

GCRay
.....

This class is basically not usable from Python at the moment, because its public API uses
type "simd_float3d" which isn't supported by PyObjC.
