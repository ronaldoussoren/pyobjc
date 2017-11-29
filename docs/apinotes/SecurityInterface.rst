API notes: SecurityInterface framework
=======================================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/securityinterface?language=objc

These bindings are accessed through the ``SecurityInterface`` package (that is, ``import SecurityInterface``).


API Notes
---------

The entire "SecurityInterface" framework on macOS is available from Python.

``-[SFAuthorizationView authorizationRights]``
..............................................

The *authorizationRights* are returned as a tuple of AuthorizationItem instances.

``-[SFAuthorizationView setAauthorizationRights:]``
...................................................

Pass the *authorizationRights* argument as a tuple of AuthorizationItem instances.
