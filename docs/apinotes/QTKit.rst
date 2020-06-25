API Notes: QTKit framework
==========================


The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/qtkit/?preferredLanguage=occ

These bindings are accessed through the ``QTKit`` package (that is, ``import QTKit``).

.. note::

   This framework was removed in macOS 10.15

API Notes
---------

* Functions ``QTMakeTimeWithTimeRecord`` and ``QTGetTimeRecord`` are not
  supported.

.. note::

   This framework is deprecated in macOS 10.9, use the AVKit and AVFoundation
   frameworks instead.
