import Security
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    expectedFailureIf,
)
import objc


class TestSecAccess(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecUseOnlyUID, 1)
        self.assertEqual(Security.kSecUseOnlyGID, 2)
        self.assertEqual(Security.kSecHonorRoot, 0x100)
        self.assertEqual(
            Security.kSecMatchBits, Security.kSecUseOnlyUID | Security.kSecUseOnlyGID
        )

    @min_os_level("10.7")
    def test_constants_10_7(self):
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
        self.assertArgHasType(Security.SecAccessCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCreate, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecAccessCreate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecAccessCreate, 2)

        self.assertFalse(hasattr(Security, "SecAccessCreateFromOwnerAndACL"))

        self.assertResultHasType(Security.SecAccessCreateWithOwnerAndACL, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecAccessCreateWithOwnerAndACL)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 2, objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 3, objc._C_ID)
        self.assertArgHasType(
            Security.SecAccessCreateWithOwnerAndACL,
            4,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )

        self.assertFalse(hasattr(Security, "SecAccessGetOwnerAndACL"))

        self.assertResultHasType(Security.SecAccessCopyOwnerAndACL, objc._C_INT)
        self.assertArgHasType(Security.SecAccessCopyOwnerAndACL, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecAccessCopyOwnerAndACL,
            1,
            objc._C_OUT + objc._C_PTR + objc._C_UINT,
        )
        self.assertArgHasType(
            Security.SecAccessCopyOwnerAndACL,
            2,
            objc._C_OUT + objc._C_PTR + objc._C_UINT,
        )
        self.assertArgHasType(
            Security.SecAccessCopyOwnerAndACL,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_UINT,
        )
        self.assertArgHasType(
            Security.SecAccessCopyOwnerAndACL, 4, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecAccessCopyOwnerAndACL, 4)

        self.assertResultHasType(Security.SecAccessCopyACLList, objc._C_INT)
        self.assertArgHasType(Security.SecAccessCopyACLList, 0, objc._C_ID)
        self.assertArgHasType(
            Security.SecAccessCopyACLList, 1, objc._C_OUT + objc._C_PTR + objc._C_ID
        )
        self.assertArgIsCFRetained(Security.SecAccessCopyACLList, 1)

        self.assertResultHasType(Security.SecAccessCopyMatchingACLList, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecAccessCopyMatchingACLList)
        self.assertArgHasType(Security.SecAccessCopyMatchingACLList, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCopyMatchingACLList, 1, objc._C_ID)
