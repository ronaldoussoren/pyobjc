API Notes: CoreMedia framework
===============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coremedia/?preferredLanguage=occ

These bindings are accessed through the ``CoreMedia`` package (that is, ``import CoreMedia``).

.. note::

   This framework was introduced in macOS 10.7


API Notes
---------

``CMBlockBufferCustomBlockSource``
..................................

This structure is not exposed to Python.

``CMBlockBufferCreateWithMemoryBlock``
......................................

The argument *customBlockSource* must be ``None``.  Please file an issue if you a usecase
for a custom block source.

``CMBlockBufferCreateContiguous``
.................................

The argument *customBlockSource* must be ``None``.  Please file an issue if you a usecase
for a custom block source.

``CMBlockBufferAppendMemoryBlock``
..................................

The argument *customBlockSource* must be ``None``.  Please file an issue if you a usecase
for a custom block source.

``CMBlockBufferAccessDataBytes``
................................

This function cannot be used from Python at this time. Please file an issue if you have
a usecase for this, in general you should use ``CMBlockBufferCopyDataBytes`` instead.

``CMBlockBufferGetDataPointer``
...............................

This function cannot be used from Python at this time. Please file an issue if you have
a usecase for this.

``CMTIME_COMPARE_INLINE``
.........................

This API is not available in Python.

``CMSampleBufferGetAudioStreamPacketDescriptionsPtr``
.....................................................

This API is not available in Python.

``CMVideoFormatDescriptionGetH264ParameterSetAtIndex``, ``CMVideoFormatDescriptionGetHEVCParameterSetAtIndex``
..............................................................................................................

These functions are not supported from Python at this time

CMBufferQueueGetCallbacksForUnsortedSampleBuffers, CMBufferQueueGetCallbacksForSampleBuffersSortedByOutputPTS, CMBufferQueueCreate
..................................................................................................................................

These functions are not supported from Python at this time

CMBlockBufferCreateWithMemoryBlock, CMBlockBufferCreateContiguous, CMBlockBufferAppendMemoryBlock, CMBlockBufferAccessDataBytes, CMBlockBufferGetDataPointer
............................................................................................................................................................

These functions are not supported from Python at this time

CMBufferQueueCreateWithHandlers
...............................

This function is not yet exposed to python.
