import Security
from PyObjCTools.TestSupport import TestCase, fourcc
import objc


class TestKeychainitem(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecInternetPasswordItemClass, fourcc(b"inet"))
        self.assertEqual(Security.kSecGenericPasswordItemClass, fourcc(b"genp"))
        self.assertEqual(Security.kSecAppleSharePasswordItemClass, fourcc(b"ashp"))
        self.assertEqual(Security.kSecCertificateItemClass, 0x80001000)
        self.assertEqual(Security.kSecPublicKeyItemClass, 0x0000000F)
        self.assertEqual(Security.kSecPrivateKeyItemClass, 0x00000010)
        self.assertEqual(Security.kSecSymmetricKeyItemClass, 0x00000011)

        self.assertEqual(Security.kSecCreationDateItemAttr, fourcc(b"cdat"))
        self.assertEqual(Security.kSecModDateItemAttr, fourcc(b"mdat"))
        self.assertEqual(Security.kSecDescriptionItemAttr, fourcc(b"desc"))
        self.assertEqual(Security.kSecCommentItemAttr, fourcc(b"icmt"))
        self.assertEqual(Security.kSecCreatorItemAttr, fourcc(b"crtr"))
        self.assertEqual(Security.kSecTypeItemAttr, fourcc(b"type"))
        self.assertEqual(Security.kSecScriptCodeItemAttr, fourcc(b"scrp"))
        self.assertEqual(Security.kSecLabelItemAttr, fourcc(b"labl"))
        self.assertEqual(Security.kSecInvisibleItemAttr, fourcc(b"invi"))
        self.assertEqual(Security.kSecNegativeItemAttr, fourcc(b"nega"))
        self.assertEqual(Security.kSecCustomIconItemAttr, fourcc(b"cusi"))
        self.assertEqual(Security.kSecAccountItemAttr, fourcc(b"acct"))
        self.assertEqual(Security.kSecServiceItemAttr, fourcc(b"svce"))
        self.assertEqual(Security.kSecGenericItemAttr, fourcc(b"gena"))
        self.assertEqual(Security.kSecSecurityDomainItemAttr, fourcc(b"sdmn"))
        self.assertEqual(Security.kSecServerItemAttr, fourcc(b"srvr"))
        self.assertEqual(Security.kSecAuthenticationTypeItemAttr, fourcc(b"atyp"))
        self.assertEqual(Security.kSecPortItemAttr, fourcc(b"port"))
        self.assertEqual(Security.kSecPathItemAttr, fourcc(b"path"))
        self.assertEqual(Security.kSecVolumeItemAttr, fourcc(b"vlme"))
        self.assertEqual(Security.kSecAddressItemAttr, fourcc(b"addr"))
        self.assertEqual(Security.kSecSignatureItemAttr, fourcc(b"ssig"))
        self.assertEqual(Security.kSecProtocolItemAttr, fourcc(b"ptcl"))
        self.assertEqual(Security.kSecCertificateType, fourcc(b"ctyp"))
        self.assertEqual(Security.kSecCertificateEncoding, fourcc(b"cenc"))
        self.assertEqual(Security.kSecCrlType, fourcc(b"crtp"))
        self.assertEqual(Security.kSecCrlEncoding, fourcc(b"crnc"))
        self.assertEqual(Security.kSecAlias, fourcc(b"alis"))

    def test_functions(self):
        self.assertIsInstance(Security.SecKeychainItemGetTypeID(), int)

        self.assertResultHasType(Security.SecKeychainItemDelete, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainItemDelete, 0, objc._C_ID)

        self.assertResultHasType(Security.SecKeychainItemCopyKeychain, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainItemCopyKeychain, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainItemCopyKeychain,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainItemCopyKeychain, 1)

        self.assertResultHasType(Security.SecKeychainItemCreateCopy, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainItemCreateCopy, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainItemCreateCopy, 1, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainItemCreateCopy, 2, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainItemCreateCopy,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainItemCreateCopy, 3)

        self.assertResultHasType(
            Security.SecKeychainItemCreatePersistentReference, objc._C_INT
        )
        self.assertArgHasType(
            Security.SecKeychainItemCreatePersistentReference, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.SecKeychainItemCreatePersistentReference,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainItemCreatePersistentReference, 1)

        self.assertResultHasType(
            Security.SecKeychainItemCopyFromPersistentReference, objc._C_INT
        )
        self.assertArgHasType(
            Security.SecKeychainItemCopyFromPersistentReference, 0, objc._C_ID
        )
        self.assertArgHasType(
            Security.SecKeychainItemCopyFromPersistentReference,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(
            Security.SecKeychainItemCopyFromPersistentReference, 1
        )

        self.assertFalse(hasattr(Security, "SecKeychainItemGetDLDBHandle"))
        self.assertFalse(hasattr(Security, "SecKeychainItemGetUniqueRecordID"))

        self.assertResultHasType(Security.SecKeychainItemCopyAccess, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainItemCopyAccess, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecKeychainItemCopyAccess,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
        self.assertArgIsCFRetained(Security.SecKeychainItemCopyAccess, 1)

        self.assertResultHasType(Security.SecKeychainItemSetAccess, objc._C_INT)
        self.assertArgHasType(Security.SecKeychainItemSetAccess, 0, objc._C_ID)
        self.assertArgHasType(Security.SecKeychainItemSetAccess, 1, objc._C_ID)

    def test_functions_manual(self):
        # Legacy API, not wrapped:
        self.assertFalse(hasattr(Security, "SecKeychainItemCopyAttributesAndData"))
        self.assertFalse(hasattr(Security, "SecKeychainItemModifyAttributesAndData"))
        self.assertFalse(hasattr(Security, "SecKeychainItemFreeAttributesAndData"))
        self.assertFalse(hasattr(Security, "SecKeychainItemCopyContent"))
        self.assertFalse(hasattr(Security, "SecKeychainItemModifyContent"))
        self.assertFalse(hasattr(Security, "SecKeychainItemFreeContent"))
