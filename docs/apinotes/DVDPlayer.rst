API Notes: DVDPlayer framework
==============================

Apple documentation
-------------------

The full API is described in Apple's documentation, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

These bindings are accessed through the ``DVDPlayer`` package (that is, ``import DVDPlayer``).


API Notes
---------

``DVDIsSupportedDevice``, ``DVDSwitchToDevice``, ``DVDSetVideoDevice``, ``DVDGetVideoDevice``
.............................................................................................

These 32-bit legacy APIs are not available from Python.

``DVDSetVideoPort``, ``DVDGetVideoPort``, ``DVDSetVideoBounds``, ``DVDGetVideoBounds``, ``DVDGetVideoKeyColor``
...............................................................................................................

These 32-bit legacy APIs are not available from Python.

``DVDDoMenuClick``, ``DVDDoMenuMouseOver``
..........................................

These 32-bit legacy APIs are not available from Python.

``DVDGetMediaVolumeName``
.........................

This API is not available from Python. Use ``DVDGetMediaVolumeCFName`` instead.
