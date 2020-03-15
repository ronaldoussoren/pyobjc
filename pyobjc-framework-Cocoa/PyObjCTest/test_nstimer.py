import gc

import Foundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class PythonClass(object):
    def __init__(self):
        self.fireCount = 0

    def fire_(self, timer):
        self.fireCount += 1


class TestNSTimer(TestCase):
    def _testHelp(self):
        obj = PythonClass()
        pool = Foundation.NSAutoreleasePool.alloc().init()
        self.assertArgIsBOOL(
            Foundation.NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_,
            4,
        )
        timer = Foundation.NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_(
            0.1, obj, "fire:", None, False
        )
        Foundation.NSRunLoop.currentRunLoop().addTimer_forMode_(
            timer, Foundation.NSDefaultRunLoopMode
        )
        Foundation.NSRunLoop.currentRunLoop().runUntilDate_(
            Foundation.NSDate.dateWithTimeIntervalSinceNow_(0.5)
        )
        timer.invalidate()
        self.assertEqual(obj.fireCount, 1)

        del timer
        del pool

    def testPythonLeakage(self):

        # Ignore first run, this has some side-effects that would
        # taint the result.
        self._testHelp()

        # Now run the test again in a loop to detect leakage
        gc.collect()
        before = len(gc.get_objects())

        for _ in range(10):
            self._testHelp()

        gc.collect()
        after = len(gc.get_objects())

        for _ in range(10):
            self._testHelp()

        gc.collect()
        after2 = len(gc.get_objects())

        self.assertEqual(after, before, "%d - %d - %d" % (before, after, after2))

    def testMethods(self):
        self.assertArgIsBOOL(
            Foundation.NSTimer.timerWithTimeInterval_invocation_repeats_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSTimer.scheduledTimerWithTimeInterval_invocation_repeats_, 2
        )
        self.assertArgIsBOOL(
            Foundation.NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_,
            4,
        )
        self.assertArgIsSEL(
            Foundation.NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_,
            2,
            b"v@:@",
        )
        self.assertArgIsBOOL(
            Foundation.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_,
            4,
        )
        self.assertArgIsSEL(
            Foundation.NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_,
            2,
            b"v@:@",
        )

        self.assertArgIsBOOL(
            Foundation.NSTimer.initWithFireDate_interval_target_selector_userInfo_repeats_,
            5,
        )
        self.assertArgIsSEL(
            Foundation.NSTimer.initWithFireDate_interval_target_selector_userInfo_repeats_,
            3,
            b"v@:@",
        )

        self.assertResultIsBOOL(Foundation.NSTimer.isValid)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertArgIsBOOL(Foundation.NSTimer.timerWithTimeInterval_repeats_block_, 1)
        self.assertArgIsBlock(
            Foundation.NSTimer.timerWithTimeInterval_repeats_block_, 2, b"v@"
        )

        self.assertArgIsBOOL(
            Foundation.NSTimer.scheduledTimerWithTimeInterval_repeats_block_, 1
        )
        self.assertArgIsBlock(
            Foundation.NSTimer.scheduledTimerWithTimeInterval_repeats_block_, 2, b"v@"
        )

        self.assertArgIsBOOL(
            Foundation.NSTimer.initWithFireDate_interval_repeats_block_, 2
        )
        self.assertArgIsBlock(
            Foundation.NSTimer.initWithFireDate_interval_repeats_block_, 3, b"v@"
        )
