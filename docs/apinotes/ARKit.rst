.. module:: ARKit
   :platform: macOS 26+
   :synopsis: Bindings for the ARKit framework

API Notes: ARKit framework
==========================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/arkit/?preferredLanguage=occ

These bindings are accessed through the ``ARKit`` package (that is, ``import ARKit``).

.. macosadded:: 26

API Notes
---------

Functions with SIMD types as arguments or return values are not supported at the moment.
