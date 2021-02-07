API Notes: Metal framework
==========================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/metal/?language=objc

These bindings are accessed through the ``Metal`` package (that is, ``import Metal``).


API Notes
---------

.. note::

   This framework is only available on macOS 10.11 and later.

The full API is available from Python.

``-[MTLRasterizationRateLayerDescriptor horizontalSampleStorage]``
..................................................................

It is generally safer to use ``MTLRasterizationRateLayerDescriptor.horizontal`` instead


``-[MTLRasterizationRateLayerDescriptor verticalSampleStorage]``
................................................................

It is generally safer to use ``MTLRasterizationRateLayerDescriptor.vertical`` instead

``MTLPackedFloat3``, ``MTLPackedFloat4x3``, ``MTLAccelerationStructureInstanceDescriptor``
..........................................................................................

These structures contain vector types and are not exposed at the moment.


``MTLMapIndirectBufferFormat``
..............................

This structure is currently not available from python and needs a manual wrapper.
