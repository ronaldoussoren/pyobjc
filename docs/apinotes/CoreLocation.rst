API Notes: CoreLocation framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/corelocation/?preferredLanguage=occ

These bindings are accessed through the ``CoreLocation`` package (that is, ``import CoreLocation``).


API Notes
---------

The entire CoreLocation framework is supported

* ``kCLErrorGeocodeFoundNoResult``, ``kCLErrorGeocodeCanceled``

   These constants have different values in the macOS 10.7
   and 10.8 SDKs. With PyObjC you get the value
   corresponding to the macOS release you are running
   on.
