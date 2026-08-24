import Security
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)
import objc


class TestSecAccess(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Security.SecAccessOwnerType)
        self.assertEqual(Security.kSecUseOnlyUID, 1)
        self.assertEqual(Security.kSecUseOnlyGID, 2)
        self.assertEqual(Security.kSecHonorRoot, 0x100)
        self.assertEqual(
            Security.kSecMatchBits, Security.kSecUseOnlyUID | Security.kSecUseOnlyGID
        )

    def test_constants(self):
        self.assertIsInstance(Security.kSecACLAuthorizationAny, str)
        self.assertIsInstance(Security.kSecACLAuthorizationLogin, str)
        self.assertIsInstance(Security.kSecACLAuthorizationGenKey, str)
        self.assertIsInstance(Security.kSecACLAuthorizationDelete, str)
        self.assertIsInstance(Security.kSecACLAuthorizationExportWrapped, str)
        self.assertIsInstance(Security.kSecACLAuthorizationExportClear, str)
        self.assertIsInstance(Security.kSecACLAuthorizationImportWrapped, str)
        self.assertIsInstance(Security.kSecACLAuthorizationImportClear, str)
        self.assertIsInstance(Security.kSecACLAuthorizationSign, str)
        self.assertIsInstance(Security.kSecACLAuthorizationEncrypt, str)
        self.assertIsInstance(Security.kSecACLAuthorizationDecrypt, str)
        self.assertIsInstance(Security.kSecACLAuthorizationMAC, str)
        self.assertIsInstance(Security.kSecACLAuthorizationDerive, str)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainCreate, str)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainDelete, str)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemRead, str)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemInsert, str)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemModify, str)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemDelete, str)

    @expectedFailureIf(
        os_release().rsplit(".", 1)[0] in ("10.9", "10.10", "10.11", "10.12")
    )
    @min_os_level("10.13")
    def test_constants_10_13(self):
        self.assertIsInstance(Security.kSecACLAuthorizationChangeACL, str)
        self.assertIsInstance(Security.kSecACLAuthorizationChangeOwner, str)

    @min_os_level("10.11")
    def test_constants_10_11(self):
        self.assertIsInstance(Security.kSecACLAuthorizationPartitionID, str)
        self.assertIsInstance(Security.kSecACLAuthorizationIntegrity, str)

    def test_functions(self):
        self.assertIsInstance(Security.SecAccessGetTypeID(), int)

        self.assertResultHasType(Security.SecAccessCreate, objc._C_INT)
        self.assertArgIsOut(Security.SecAccessCreate, 2)
        self.assertArgIsCFRetained(Security.SecAccessCreate, 2)

        self.assertFalse(hasattr(Security, "SecAccessCreateFromOwnerAndACL"))

        self.assertResultIsCFRetained(Security.SecAccessCreateWithOwnerAndACL)
        self.assertArgIsOut(
            Security.SecAccessCreateWithOwnerAndACL,
            4,
        )
        self.assertArgIsCFRetained(
            Security.SecAccessCreateWithOwnerAndACL,
            4,
        )

        self.assertFalse(hasattr(Security, "SecAccessGetOwnerAndACL"))

        self.assertArgIsOut(
            Security.SecAccessCopyOwnerAndACL,
            1,
        )
        self.assertArgIsOut(
            Security.SecAccessCopyOwnerAndACL,
            2,
        )
        self.assertArgIsOut(
            Security.SecAccessCopyOwnerAndACL,
            3,
        )
        self.assertArgIsOut(Security.SecAccessCopyOwnerAndACL, 4)
        self.assertArgIsCFRetained(Security.SecAccessCopyOwnerAndACL, 4)

        self.assertArgIsOut(Security.SecAccessCopyACLList, 1)
        self.assertArgIsCFRetained(Security.SecAccessCopyACLList, 1)

        self.assertResultIsCFRetained(Security.SecAccessCopyMatchingACLList)
