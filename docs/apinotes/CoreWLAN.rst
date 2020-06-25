API notes: CoreWLAN framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/corewlan?preferredLanguage=occ

These bindings are accessed through the ``CoreWLAN`` package (that is, ``import CoreWLAN``).


API Notes
---------

.. note::

   The Accounts framework is only available in macOS 10.6 or later.


CWKeychainCopyEAPIdentity
.........................

This function returns a SecIdentityRef (by reference), the security
framework isn't wrapped by PyObjC at this time.

CWKeychainSetEAPIdentity
........................

This function has a SecIdentityRef argument, but because the
security framework isn't wrapped by PyObjC at this time it is
not yet possible to create values for this argument.
