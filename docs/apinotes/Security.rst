API notes: Security framework
=============================

The full API is described in `Apple's documentation`__, both
the C and Objective-C APIs are available (but see the `API Notes`_ below).

.. __: https://developer.apple.com/documentation/security?language=objc

These bindings are accessed through the ``Security`` package (that is, ``import Security``).


API Notes
---------

Plugin API
..........

The APIs related to authorization plugins are not exposed to python.

``SecCodeRef``, ``SecStaticCodeRef``, ``SecRequirementRef``
...........................................................

These CoreFoundation types are not available as named types in Python.

That is, it is possible to use instances of these types but there is
no Python object that represent the type itself.

``SecKeyCreatePair``, ``SecKeyGenerate``, ``SecKeyGetCSSMKey``, ``SecKeyGetCSPHandle``, ``SecKeyGetCredentials``
................................................................................................................

These functions were deprecated in macOS and are not available from Python.

``MDS_*``, ``CSSM_*``
.....................

These functions were deprecated in macOS and are not available from Python.

``SecPolicyCreateWithOID``, ``SecPolicyGetOID``, ``SecPolicyGetValue``, ``SecPolicySetValue``, ``SecPolicyGetTPHandle``, ``SecPolicySetProperties``
...................................................................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecIdentityCopyPreference``, ``SecIdentitySetPreference``
...........................................................

These functions were deprecated in macOS and are not available from Python.

``SecKeychainSearchGetTypeID``, ``SecKeychainSearchCreateFromAttributes``, ``SecKeychainSearchCopyNext``
........................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecPolicySearchGetTypeID``, ``SecPolicySearchCreate``, ``SecPolicySearchCopyNext``
....................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecIdentitySearchCreate``, ``SecIdentitySearchCopyNext``
..........................................................

These functions were deprecated in macOS and are not available from Python.

``SSLNewContext``, ``SSLDisposeContext``, ``SSLSetProtocolVersionEnabled``, ``SSLGetProtocolVersionEnabled``
............................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SSLSetProtocolVersion``, ``SSLGetProtocolVersion``
....................................................

These functions were deprecated in macOS and are not available from Python.

``SSLSetEnableCertVerify``, ``SSLGetEnableCertVerify``, ``SSLSetAllowsExpiredCerts``, ``SSLGetAllowsExpiredCerts``
..................................................................................................................

These functions were deprecated in macOS and are not available from Python.


``SSLSetAllowsExpiredRoots``, ``SSLGetAllowsExpiredRoots``, ``SSLSetAllowsAnyRoot``, ``SSLGetAllowsAnyRoot``
.............................................................................................................

These functions were deprecated in macOS and are not available from Python.


``SSLSetTrustedRoots``, ``SSLCopyTrustedRoots``, ``SSLCopyPeerCertificates``
............................................................................

These functions were deprecated in macOS and are not available from Python.

``SSLGetRsaBlinding``, ``SSLSetRsaBlinding``
............................................

These functions were deprecated in macOS and are not available from Python.

``SecKeychainItemExport``, ``SecKeychainItemImport``
....................................................

These functions were deprecated in macOS and are not available from Python.

