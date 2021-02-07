import Security
from PyObjCTools.TestSupport import TestCase
import objc


class TestSecCodeHost(TestCase):
    def test_constants(self):
        self.assertEqual(Security.kSecCSDedicatedHost, 1 << 0)
        self.assertEqual(Security.kSecCSGenerateGuestHash, 1 << 1)

    def test_functions(self):
        self.assertResultHasType(Security.SecHostCreateGuest, objc._C_INT)
        self.assertArgHasType(Security.SecHostCreateGuest, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecHostCreateGuest, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecHostCreateGuest, 2, objc._C_ID)
        self.assertArgHasType(Security.SecHostCreateGuest, 3, objc._C_ID)
        self.assertArgHasType(Security.SecHostCreateGuest, 4, objc._C_UINT)
        self.assertArgHasType(
            Security.SecHostCreateGuest, 5, objc._C_OUT + objc._C_PTR + objc._C_UINT
        )

        self.assertResultHasType(Security.SecHostRemoveGuest, objc._C_INT)
        self.assertArgHasType(Security.SecHostRemoveGuest, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecHostRemoveGuest, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecHostRemoveGuest, 2, objc._C_UINT)

        self.assertResultHasType(Security.SecHostSelectGuest, objc._C_INT)
        self.assertArgHasType(Security.SecHostSelectGuest, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecHostSelectGuest, 1, objc._C_UINT)

        self.assertResultHasType(Security.SecHostSelectedGuest, objc._C_INT)
        self.assertArgHasType(Security.SecHostSelectedGuest, 0, objc._C_UINT)
        self.assertArgHasType(
            Security.SecHostSelectedGuest, 1, objc._C_OUT + objc._C_PTR + objc._C_UINT
        )

        self.assertResultHasType(Security.SecHostSetGuestStatus, objc._C_INT)
        self.assertArgHasType(Security.SecHostSetGuestStatus, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecHostSetGuestStatus, 1, objc._C_UINT)
        self.assertArgHasType(Security.SecHostSetGuestStatus, 2, objc._C_ID)
        self.assertArgHasType(Security.SecHostSetGuestStatus, 3, objc._C_UINT)

        self.assertResultHasType(Security.SecHostSetHostingPort, objc._C_INT)
        self.assertArgHasType(Security.SecHostSetHostingPort, 0, objc._C_UINT)
        self.assertArgHasType(Security.SecHostSetHostingPort, 1, objc._C_UINT)
