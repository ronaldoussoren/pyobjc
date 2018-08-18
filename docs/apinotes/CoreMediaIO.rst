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
