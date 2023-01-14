API Notes: IOBluetooth framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/iobluetooth/?preferredLanguage=occ

These bindings are accessed through the ``IOBluetooth`` package (that is, ``import IOBluetooth``).


API Notes
---------

The API is mostly available from Python, except for a number of APIs that require
manual bindings (most of which are deprecated and shouldn't be used for new development
anyway).

* ``IOBluetoothPackData``, ``IOBluetoothUnpackData``: These functions are not yet
  available to Python, they are variadic functions that require custom code.

* ``IOBluetoothPackDataList``, ``IOBluetoothUnpackDataList``:  Not available from Python

* ``OBEXSessionEvent``: This struct is not available from Python, likewise for all
   APIs that use this type.

* ``IOBluetoothL2CAPChannelEventType``: Not available from Python

* ``IOBluetoothL2CAPChannelDataBlock``: Not available from Python

* ``IOBluetoothL2CAPChannelEvent``: Not available from Python
