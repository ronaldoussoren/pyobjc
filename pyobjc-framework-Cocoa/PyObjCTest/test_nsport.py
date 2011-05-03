from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSPort (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSPortDidBecomeInvalidNotification, unicode)
        self.assertEqual(NSMachPortDeallocateNone, 0)
        self.assertEqual(NSMachPortDeallocateSendRight, (1 << 0))
        self.assertEqual(NSMachPortDeallocateReceiveRight, (1 << 1))

    def testMethods(self):
        self.assertResultIsBOOL(NSPort.isValid)

if __name__ == "__main__":
    main()
