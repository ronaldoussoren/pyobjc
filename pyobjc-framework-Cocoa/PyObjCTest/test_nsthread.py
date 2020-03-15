import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSThread(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(Foundation.NSThread.isMultiThreaded)
        self.assertArgIsSEL(
            Foundation.NSThread.detachNewThreadSelector_toTarget_withObject_, 0, b"v@:@"
        )
        self.assertResultIsBOOL(Foundation.NSThread.setThreadPriority_)

        self.assertArgIsSEL(
            Foundation.NSThread.performSelectorOnMainThread_withObject_waitUntilDone_modes_,
            0,
            b"v@:@",
        )
        self.assertArgIsBOOL(
            Foundation.NSThread.performSelectorOnMainThread_withObject_waitUntilDone_modes_,
            2,
        )
        self.assertArgIsSEL(
            Foundation.NSThread.performSelectorOnMainThread_withObject_waitUntilDone_,
            0,
            b"v@:@",
        )
        self.assertArgIsBOOL(
            Foundation.NSThread.performSelectorOnMainThread_withObject_waitUntilDone_, 2
        )

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsSEL(
            Foundation.NSThread.initWithTarget_selector_object_, 1, b"v@:@"
        )
        self.assertResultIsBOOL(Foundation.NSThread.isExecuting)
        self.assertResultIsBOOL(Foundation.NSThread.isFinished)
        self.assertResultIsBOOL(Foundation.NSThread.isCancelled)
        self.assertResultIsBOOL(Foundation.NSThread.isMainThread)
        self.assertResultIsBOOL(Foundation.NSThread.mainThread().isMainThread)
        self.assertArgIsSEL(
            Foundation.NSThread.performSelector_onThread_withObject_waitUntilDone_modes_,
            0,
            b"v@:@",
        )
        self.assertArgIsBOOL(
            Foundation.NSThread.performSelector_onThread_withObject_waitUntilDone_modes_,
            3,
        )
        self.assertArgIsSEL(
            Foundation.NSThread.performSelector_onThread_withObject_waitUntilDone_,
            0,
            b"v@:@",
        )
        self.assertArgIsBOOL(
            Foundation.NSThread.performSelector_onThread_withObject_waitUntilDone_, 3
        )
        self.assertArgIsSEL(
            Foundation.NSThread.performSelectorInBackground_withObject_, 0, b"v@:@"
        )

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBlock(Foundation.NSThread.detachNewThreadWithBlock_, 0, b"v")
        self.assertArgIsBlock(Foundation.NSThread.initWithBlock_, 0, b"v")

    def testConstants(self):
        self.assertIsInstance(Foundation.NSWillBecomeMultiThreadedNotification, str)
        self.assertIsInstance(Foundation.NSDidBecomeSingleThreadedNotification, str)
        self.assertIsInstance(Foundation.NSThreadWillExitNotification, str)
