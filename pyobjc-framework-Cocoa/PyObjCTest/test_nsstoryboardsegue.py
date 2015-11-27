from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSStoryboardSegueHelper (NSObject):
    def shouldPerformSegueWithIdentifier_sender_(self, i, s): return 1

class TestNSStoryboardSegue (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgIsBlock(NSStoryboardSegue.segueWithIdentifier_source_destination_performHandler_, 3, b'v')

        self.assertArgIsBlock(NSStoryboardSegue.setPerformHandler_, 0, b'v')
        self.assertResultIsBlock(NSStoryboardSegue.performHandler, b'v')

    @min_os_level('10.10')
    def testProtocols10_10(self):
        objc.protocolNamed('NSSeguePerforming')

        self.assertResultIsBOOL(TestNSStoryboardSegueHelper.shouldPerformSegueWithIdentifier_sender_)

if __name__ == "__main__":
    main()
