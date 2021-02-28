API Notes VideoToolbox framework
=================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/videotoolbox/?language=objc

These bindings are accessed through the ``VideoToolbox`` package (that is, ``import VideoToolbox``).


API Notes
---------

``VTDecompressionSessionCreate``
................................

The callback structure should be None, passing a callback function is
not supported at the moment.
