API Notes: CoreData framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coredata/?preferredLanguage=occ

These bindings are accessed through the ``CoreData`` package (that is, ``import CoreData``).


Compatibility information
-------------------------

When you're running on macOS 10.4 PyObjC will automatically translate
Python attribute access in KVO access to the underlying ``NSManagedObject``.
This functionality no longer works on MacOSX 10.5, you have to use proper
KVO methods to access properties to be compatible with both OSX 10.4 and 10.5.


API Notes
---------

* class ``NSManagedObject``

  The methods ``setObservationInfo:`` and ``observationInfo`` cannot be
  used from Python.
