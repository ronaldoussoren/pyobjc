import CoreBluetooth
from PyObjCTools.TestSupport import TestCase


class TestCBManager(TestCase):
    def testConstants(self):
        self.assertEqual(CoreBluetooth.CBManagerStateUnknown, 0)
        self.assertEqual(CoreBluetooth.CBManagerStateResetting, 1)
        self.assertEqual(CoreBluetooth.CBManagerStateUnsupported, 2)
        self.assertEqual(CoreBluetooth.CBManagerStateUnauthorized, 3)
        self.assertEqual(CoreBluetooth.CBManagerStatePoweredOff, 4)
        self.assertEqual(CoreBluetooth.CBManagerStatePoweredOn, 5)

        self.assertEqual(CoreBluetooth.CBManagerAuthorizationNotDetermined, 0)
        self.assertEqual(CoreBluetooth.CBManagerAuthorizationRestricted, 1)
        self.assertEqual(CoreBluetooth.CBManagerAuthorizationDenied, 2)
        self.assertEqual(CoreBluetooth.CBManagerAuthorizationAllowedAlways, 3)
