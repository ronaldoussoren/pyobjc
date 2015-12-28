from PyObjCTools.TestSupport import *

from Foundation import *

class PortDelegate (NSObject):
    def handleMachMessage_(self, m): pass

class NSPortHelper (NSPort):
    def sendBeforeDate_components_from_reserved_(self, a, b, c, d): pass
    def sendBeforeDate_msgid_components_from_reserved_(self, a, b, c, d, e): pass

class TestNSPort (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSPortDidBecomeInvalidNotification, unicode)
        self.assertEqual(NSMachPortDeallocateNone, 0)
        self.assertEqual(NSMachPortDeallocateSendRight, (1 << 0))
        self.assertEqual(NSMachPortDeallocateReceiveRight, (1 << 1))

    def testMethods(self):
        self.assertResultIsBOOL(NSPort.isValid)

        self.assertResultIsBOOL(NSPortHelper.sendBeforeDate_components_from_reserved_)
        self.assertResultIsBOOL(NSPortHelper.sendBeforeDate_msgid_components_from_reserved_)

        self.assertArgHasType(NSPortHelper.sendBeforeDate_components_from_reserved_, 3, objc._C_NSUInteger)
        self.assertArgHasType(NSPortHelper.sendBeforeDate_msgid_components_from_reserved_, 4, objc._C_NSUInteger)

        self.assertArgHasType(PortDelegate.handleMachMessage_, 0, b'^v')

    @min_sdk_level('10.6')
    def testProtocols(self):
        objc.protocolNamed('NSPortDelegate')
        objc.protocolNamed('NSMachPortDelegate')

if __name__ == "__main__":
    main()
