.. module:: CompositorServices
   :platform: macOS 26+
   :synopsis: Bindings for the CompositorServices framework

API Notes: CompositorServices framework
========================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/compositorservices/?preferredLanguage=occ

These bindings are accessed through the ``CompositorServices`` package (that is, ``import CompositorServices``).

.. macosadded:: 26

API Notes
---------

Functions with SIMD types as arguments or return values are not supported at the moment.
