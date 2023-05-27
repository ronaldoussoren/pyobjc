API Notes: CoreMIDI framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coremidi/?preferredLanguage=occ

These bindings are accessed through the ``CoreMIDI`` package (that is, ``import CoreMIDI``).

.. note::

   This is fairly low-level API mostly not based on CoreFoundation or Objective-C
   types. Because of this users will have to perform manual reference counting.

   I'm also not sure if these bindings are correct.


API Notes
---------

The driver implementation interface is not available from Python.

The following functions are not available from Python:

* ``MIDIEndpointSetRefCons``

* ``MIDIEndpointGetRefCons``

* ``MIDIDestinationCreateWithBlock``

* ``MIDI1UPSysExArray``

Type ``MIDIUniversalMessage`` is not available from Python at this time
because it contains a C union. Because of that ``MIDIUniversalMessage``
is not available either.

Manual bindings needed
----------------------

The APIs below require manual bindings and are not yet available:


* ``MIDIDeviceCreate``

* ``MIDIDriverEnableMonitoring``

* ``MIDIEventListAdd``

* ``MIDIEventListInit``

* ``MIDIPacketListAdd``

* ``MIDIPacketListInit``

* ``MIDIReceived``

* ``MIDIReceivedEventList``

* ``MIDISend``

* ``MIDISendEventList``

* ``MIDISendSysex``
