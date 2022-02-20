import Foundation
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class PortDelegate(Foundation.NSObject):
    def handleMachMessage_(self, m):
        pass


class NSPortHelper(Foundation.NSPort):
    def sendBeforeDate_components_from_reserved_(self, a, b, c, d):
        pass

    def sendBeforeDate_msgid_components_from_reserved_(self, a, b, c, d, e):
        pass


class TestNSPort(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Foundation.NSMachPortOptions)

    def testConstants(self):
        self.assertIsInstance(Foundation.NSPortDidBecomeInvalidNotification, str)
        self.assertEqual(Foundation.NSMachPortDeallocateNone, 0)
        self.assertEqual(Foundation.NSMachPortDeallocateSendRight, (1 << 0))
        self.assertEqual(Foundation.NSMachPortDeallocateReceiveRight, (1 << 1))

    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSPort.isValid)

        self.assertResultIsBOOL(
            Foundation.NSPortHelper.sendBeforeDate_components_from_reserved_
        )
        self.assertResultIsBOOL(
            Foundation.NSPortHelper.sendBeforeDate_msgid_components_from_reserved_
        )

        self.assertArgHasType(
            Foundation.NSPortHelper.sendBeforeDate_components_from_reserved_,
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            Foundation.NSPortHelper.sendBeforeDate_msgid_components_from_reserved_,
            4,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(PortDelegate.handleMachMessage_, 0, b"^v")

    @min_sdk_level("10.6")
    def testProtocols(self):
        objc.protocolNamed("NSPortDelegate")
        objc.protocolNamed("NSMachPortDelegate")
