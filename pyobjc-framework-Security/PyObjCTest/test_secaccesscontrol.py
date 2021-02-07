import Security
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestSecAccessControl(TestCase):
    @min_os_level("10.10")
    def test_types(self):
        self.assertIsCFType(Security.SecAccessControlRef)

    def test_constants(self):
        self.assertEqual(Security.kSecAccessControlUserPresence, 1 << 0)
        self.assertEqual(Security.kSecAccessControlBiometryAny, 1 << 1)
        self.assertEqual(Security.kSecAccessControlTouchIDAny, 1 << 1)
        self.assertEqual(Security.kSecAccessControlBiometryCurrentSet, 1 << 3)
        self.assertEqual(Security.kSecAccessControlTouchIDCurrentSet, 1 << 3)
        self.assertEqual(Security.kSecAccessControlDevicePasscode, 1 << 4)
        self.assertEqual(Security.kSecAccessControlOr, 1 << 14)
        self.assertEqual(Security.kSecAccessControlAnd, 1 << 15)
        self.assertEqual(Security.kSecAccessControlPrivateKeyUsage, 1 << 30)
        self.assertEqual(Security.kSecAccessControlApplicationPassword, 1 << 31)
        self.assertEqual(Security.kSecAccessControlDevicePasscode, 1 << 4)
        self.assertEqual(Security.kSecAccessControlWatch, 1 << 5)

    @min_os_level("10.10")
    def test_functions(self):
        self.assertResultHasType(Security.SecAccessControlCreateWithFlags, objc._C_ID)
        self.assertResultIsCFRetained(Security.SecAccessControlCreateWithFlags)
        self.assertArgHasType(Security.SecAccessControlCreateWithFlags, 0, objc._C_ID)
        self.assertArgHasType(Security.SecAccessControlCreateWithFlags, 1, objc._C_ID)
        self.assertArgHasType(
            Security.SecAccessControlCreateWithFlags, 2, objc._C_NSUInteger
        )
        self.assertArgHasType(
            Security.SecAccessControlCreateWithFlags,
            3,
            objc._C_OUT + objc._C_PTR + objc._C_ID,
        )
