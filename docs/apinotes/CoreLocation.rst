.. module:: CoreLocation
   :platform: macOS
   :synopsis: Bindings for the CoreLocation framework

API Notes: CoreLocation framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/corelocation/?preferredLanguage=occ

These bindings are accessed through the ``CoreLocation`` package (that is, ``import CoreLocation``).


API Notes
---------

Code only gets access to location information when the binary is signed
properly (not using an ad-hoc signature). This is a security feature in macOS.
