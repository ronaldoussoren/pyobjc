from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSPort (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSPortDidBecomeInvalidNotification, unicode))


        self.assertEquals(NSMachPortDeallocateNone, 0)
        self.assertEquals(NSMachPortDeallocateSendRight, (1 << 0))
        self.assertEquals(NSMachPortDeallocateReceiveRight, (1 << 1))



if __name__ == "__main__":
    main()
