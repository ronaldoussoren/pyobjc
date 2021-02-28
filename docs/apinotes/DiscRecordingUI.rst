API Notes: DiscRecordingUI framework
====================================

Apple documentation
-------------------

The full API is described in Apple's documentation, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

These bindings are accessed through the ``DiscRecordingUI`` package (that is, ``import DiscRecordingUI``).


API Notes
---------

This framework has an Objective-C API and a more limited C API. The
C API is mostly supported in Python, but using the Objective-C
API is advised.

``DRBurnSessionBeginProgressDialog``, ``DRBurnSessionSetupDialog``
..................................................................

The callback structure argument must be None, custom behavior is
not supported.

``DREraseSessionSetupDialog``, ``DREraseSessionBeginProgressDialog``
....................................................................

The callback structure argument must be None, custom behavior is
not supported.
