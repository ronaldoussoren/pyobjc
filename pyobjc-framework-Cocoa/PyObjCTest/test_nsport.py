from PyObjCTools.TestSupport import *

from Foundation import *

try:
    unicode
except NameError:
    unicode = str

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

if __name__ == "__main__":
    main()
