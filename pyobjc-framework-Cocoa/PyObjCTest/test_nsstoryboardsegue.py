import AppKit
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSStoryboardSegueHelper(AppKit.NSObject):
    def shouldPerformSegueWithIdentifier_sender_(self, i, s):
        return 1


class TestNSStoryboardSegue(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgIsBlock(
            AppKit.NSStoryboardSegue.segueWithIdentifier_source_destination_performHandler_,
            3,
            b"v",
        )

        self.assertArgIsBlock(AppKit.NSStoryboardSegue.setPerformHandler_, 0, b"v")
        self.assertResultIsBlock(AppKit.NSStoryboardSegue.performHandler, b"v")

    @min_os_level("10.10")
    def testProtocols10_10(self):
        objc.protocolNamed("NSSeguePerforming")

        self.assertResultIsBOOL(
            TestNSStoryboardSegueHelper.shouldPerformSegueWithIdentifier_sender_
        )
