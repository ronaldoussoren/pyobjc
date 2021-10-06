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

``EISL_*``
..........

These lowlevel APIs are not available from Python.

``SecAsn1*``
............

This APIs are specialized and would require manual bindings. They are therefore not available from Python at this time.

Please file an issue at `PyObjC's issue tracker <https://github.com/ronaldoussoren/pyobjc/issues>`_ when you have a
usecase for these APIs.

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

``CMSEncoderSetEncapsulatedContentType``, ``CMSEncode``
.......................................................

These functions were deprecated in macOS and are not available from Python.

``SecACLCreateFromSimpleContents``, ``SecACLCopySimpleContents``, ``SecACLSetSimpleContents``, ``SecACLGetAuthorizations``, ``SecACLSetAuthorizations``
.......................................................................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecAccessCreateFromOwnerAndACL``, ``SecAccessGetOwnerAndACL``, ``SecAccessCopySelectedACLList``
..................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecCertificateCreateFromData``, ``SecCertificateGetData``, ``SecCertificateGetType``, ``SecCertificateGetSubject``, ``SecCertificateGetIssuer``
.................................................................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecCertificateGetCLHandle``, ``SecCertificateGetAlgorithmID``, ``SecCertificateCopyPreference``, ``SecCertificateSetPreference``
..................................................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecKeychainGetCSPHandle``, ``SecKeychainGetDLDBHandle``
.........................................................

These functions were deprecated in macOS and are not available from Python.

``SecTrustSetParameters``, ``SecTrustGetResult``, ``SecTrustGetCssmResultCode``, ``SecTrustGetCssmResult``, ``SecTrustGetTPHandle``
...................................................................................................................................

These functions were deprecated in macOS and are not available from Python.

``SecKeychainItemGetDLDBHandle``, ``SecKeychainItemGetUniqueRecordID``
......................................................................

These functions were deprecated in macOS and are not available from Python.

``SecKeychainFindInternetPassword``, ``SecKeychainFindGenericPassword``
.......................................................................

Don't call ``SecKeychainItemFreeContent`` to free the password data, PyObjC does this for you and returns a standard bytes object.

Legacy KeychainItem API
.......................

The following functions are not available from Python because they are legacy APIs (soft deprecated) that require manual wrapping:
``SecKeychainItemCopyAttributesAndData``, ``SecKeychainItemModifyAttributesAndData``, ``SecKeychainItemFreeAttributesAndData``,
``SecKeychainItemCopyContent``, ``SecKeychainItemModifyContent``, ``SecKeychainItemFreeContent``.

Please file an issue at `PyObjC's issue tracker <https://github.com/ronaldoussoren/pyobjc/issues>`_ when you have a
usecase for these APIs.

Legacy Keychain attribute API
.............................

The following functions are not available from Python because they are legacy APIs (soft deprecated) that require manual wrapping:
``SecKeychainAttributeInfoForItemID``, ``SecKeychainFreeAttributeInfo``.

``AuthorizationCreate``
.......................

The arguments *rights* and *environment* should be passed as tuples of *AuthorizationItem* values.

``AuthorizationCopyInfo``
.........................

The information is returned as a tuple of *AuthorizationItem* (instead of specific type wrapping an ``AuthorizationItemSet``),
and it is not necessary to call ``AuthorizationFreeItemSet``.

``AuthorizationFreeItemSet``
............................

This function is automatically called as needed by PyObjC and is not exposed to Python.

``AuthorizationExecuteWithPrivileges``
......................................

The argument *arguments* should be a sequence of byte strings. PyObjC automatically adds a *NULL* value to the end of the array.

The function cannot be used with Python 3 at the moment, because there is no Python type corresponding to a ``FILE*``. This
will be fixed in a later version.
