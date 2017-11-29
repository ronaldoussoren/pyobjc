from PyObjCTools.TestSupport import *

import Security

class TestSecAccess (TestCase):

    def test_constants(self):
        self.assertEqual(Security.kSecUseOnlyUID, 1)
        self.assertEqual(Security.kSecUseOnlyGID, 2)
        self.assertEqual(Security.kSecHonorRoot, 0x100)
        self.assertEqual(Security.kSecMatchBits, Security.kSecUseOnlyUID | Security.kSecUseOnlyGID)

    @min_os_level('10.7')
    def test_constants_10_7(self):
        self.assertIsInstance(Security.kSecACLAuthorizationAny, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationLogin, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationGenKey, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationDelete, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationExportWrapped, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationExportClear, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationImportWrapped, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationImportClear, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationSign, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationEncrypt, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationDecrypt, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationMAC, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationDerive, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainCreate, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainDelete, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemRead, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemInsert, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemModify, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationKeychainItemDelete, unicode)

    @expectedFailureIf(os_release().rsplit('.',1)[0] in ('10.9', '10.10', '10.11', '10.12'))
    @min_os_level('10.7')
    def test_constants_10_7_missing(self):
        self.assertIsInstance(Security.kSecACLAuthorizationChangeACL, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationChangeOwner, unicode)

    @min_os_level('10.11')
    def test_constants_10_11(self):
        self.assertIsInstance(Security.kSecACLAuthorizationPartitionID, unicode)
        self.assertIsInstance(Security.kSecACLAuthorizationIntegrity, unicode)

    def test_functions(self):
        self.assertIsInstance(Security.SecAccessGetTypeID(), (int, long))

        self.assertResultHasType(Security.SecAccessCreate, objc._C_INT)
        self.assertArgHasType(Security.SecAccessCreate, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCreate, 1, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCreate, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecAccessCreate, 2)

        self.assertFalse(hasattr(Security, 'SecAccessCreateFromOwnerAndACL'))

        self.assertResultHasType(Security.SecAccessCreateWithOwnerAndACL, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecAccessCreateWithOwnerAndACL)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 2, objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 3, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCreateWithOwnerAndACL, 4, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertFalse(hasattr(Security, 'SecAccessGetOwnerAndACL'))

        self.assertResultHasType(Security.SecAccessCopyOwnerAndACL, objc._C_INT)
        self.assertArgHasType(Security.SecAccessCopyOwnerAndACL, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCopyOwnerAndACL, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCopyOwnerAndACL, 2, objc._C_OUT + objc._C_PTR + objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCopyOwnerAndACL, 3, objc._C_OUT + objc._C_PTR + objc._C_UINT)
        self.assertArgHasType(Security.SecAccessCopyOwnerAndACL, 4, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecAccessCopyOwnerAndACL, 4)

        self.assertResultHasType(Security.SecAccessCopyACLList, objc._C_INT)
        self.assertArgHasType(Security.SecAccessCopyACLList, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCopyACLList, 1, objc._C_OUT + objc._C_PTR + objc._C_ID)
        self.assertArgIsCFRetained(Security.SecAccessCopyACLList, 1)

        self.assertResultHasType(Security.SecAccessCopyMatchingACLList, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecAccessCopyMatchingACLList)
        self.assertArgHasType(Security.SecAccessCopyMatchingACLList, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessCopyMatchingACLList, 1, objc._C_ID)

if __name__ == "__main__":
    main()
