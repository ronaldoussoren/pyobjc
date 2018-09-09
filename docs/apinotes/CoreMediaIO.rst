API Notes: CoreMediaIO framework
=================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coremedia/?preferredLanguage=occ

These bindings are accessed through the ``CoreMediaIO`` package (that is, ``import CoreMediaIO``).

.. note::

   This framework was introduced in macOS 10.7

API Notes
---------

``CMIOHardwarePlugIn.h``
........................

The APIs to create hardware plugins are not available from Python.

``CMIODeviceProcessAVCCommand``, ``CMIODeviceProcessRS422Command``
..................................................................

The buffers in the command buffer should be bytearray instances and
will be changed by the call.

.. warning::

   The current implementation of these wrappers does not validate
   that the buffers are actually mutable, which may lead to
   surprising results when code passes an immutable buffer.
