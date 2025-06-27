.. module:: Metal
   :platform: macOS 10.11+
   :synopsis: Bindings for the Metal framework

API Notes: Metal framework
==========================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/metal/?language=objc

These bindings are accessed through the ``Metal`` package (that is, ``import Metal``).

.. versionadded:: macOS 10.11

API Notes
---------

``-[MTLRasterizationRateLayerDescriptor horizontalSampleStorage]``
..................................................................

It is generally safer to use ``MTLRasterizationRateLayerDescriptor.horizontal`` instead


``-[MTLRasterizationRateLayerDescriptor verticalSampleStorage]``
................................................................

It is generally safer to use ``MTLRasterizationRateLayerDescriptor.vertical`` instead

``MTLPackedFloat3``
...................

The C type contains an anonymous union. In Python the only attribute is
``elements`` (list of 3 floats).

``MTLMapIndirectBufferFormat``
..............................

This structure is currently not available from python and needs a manual wrapper.
