API Notes: CoreServices/CarbonCore framework
============================================

Apple documentation
-------------------

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/coreservices?preferredLanguage=occ


API Notes
---------

The CarbonCore framework is a subframework of OSServices, use
``import CoreServices`` to access the definitions in this framework.

PyObjC provides only limited access to definitions in the framework,
primarily funcionility that cannot be accessed in a better (modern)
way.

In particular only the following functionality is available from Python:

* BackupCore

* DiskspaceRecovery
