API Notes: CoreServices/Metadata framework
==========================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices?preferredLanguage=occ


API Notes
---------

The Metadata framework is a subframework of CoreServices, use
``import CoreServices`` to access the definitions in this framework.

PyObjC provides only limited access to definitions in the framework,
primarily funcionility that cannot be accessed in a better (modern)
way.

The APIs to implement metadata importers is not available to
python at this time.

* MDQuerySetCreateResultFunction: The CFArrayCallbacks argument must be None

* MDQuerySetCreateValueFunction: The CFArrayCallbacks argument must be None
