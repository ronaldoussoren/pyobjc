import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSRunLoop(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Foundation.NSRunLoop.runMode_beforeDate_)

        self.assertArgIsSEL(
            Foundation.NSRunLoop.performSelector_withObject_afterDelay_inModes_,
            0,
            b"v@:@",
        )
        self.assertArgIsSEL(
            Foundation.NSRunLoop.performSelector_withObject_afterDelay_, 0, b"v@:@"
        )
        self.assertArgIsSEL(
            Foundation.NSRunLoop.performSelector_target_argument_order_modes_,
            0,
            b"v@:@",
        )

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertArgIsBlock(Foundation.NSRunLoop.performInModes_block_, 1, b"v")
        self.assertArgIsBlock(Foundation.NSRunLoop.performBlock_, 0, b"v")

    def test_constants(self):
        self.assertIsInstance(Foundation.NSDefaultRunLoopMode, str)
        self.assertIsInstance(Foundation.NSRunLoopCommonModes, str)
