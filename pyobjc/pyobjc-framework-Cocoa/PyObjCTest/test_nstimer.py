from PyObjCTools.TestSupport import *
import gc

from objc import *
from Foundation import *

class PythonClass (object):
    def __init__(self):
        self.fireCount = 0

    def fire_(self, timer):
        self.fireCount += 1


class TestNSTimer(TestCase):

    def _testHelp(self):
        obj = PythonClass()
        pool = NSAutoreleasePool.new()
        self.failUnlessArgIsBOOL(NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_, 4)
        timer = NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_(
                0.1, obj, 'fire:', None, False)
        NSRunLoop.currentRunLoop().addTimer_forMode_(
                timer, NSDefaultRunLoopMode)
        NSRunLoop.currentRunLoop().runUntilDate_(
                NSDate.dateWithTimeIntervalSinceNow_(0.5))
        timer.invalidate()
        self.assertEquals(obj.fireCount, 1)

        del timer
        del pool

    def testPythonLeakage(self):

        # Ignore first run, this has some side-effects that would
        # taint the result.
        self._testHelp()

        # Now run the test again in a loop to detect leakage
        gc.collect()
        before = len(gc.get_objects())

        for i in range(10):
            self._testHelp()

        gc.collect()
        after = len(gc.get_objects())

        self.assertEquals(after, before)

    def testMethods(self):
        self.failUnlessArgIsBOOL(NSTimer.timerWithTimeInterval_invocation_repeats_, 2)
        self.failUnlessArgIsBOOL(NSTimer.scheduledTimerWithTimeInterval_invocation_repeats_, 2)
        self.failUnlessArgIsBOOL(NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_, 4)
        self.failUnlessArgIsSEL(NSTimer.timerWithTimeInterval_target_selector_userInfo_repeats_, 2, 'v@:@')
        self.failUnlessArgIsBOOL(NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_, 4)
        self.failUnlessArgIsSEL(NSTimer.scheduledTimerWithTimeInterval_target_selector_userInfo_repeats_, 2, 'v@:@')

        self.failUnlessArgIsBOOL(NSTimer.initWithFireDate_interval_target_selector_userInfo_repeats_, 5)
        self.failUnlessArgIsSEL(NSTimer.initWithFireDate_interval_target_selector_userInfo_repeats_, 3, 'v@:@')

        self.failUnlessResultIsBOOL(NSTimer.isValid)

if __name__ == '__main__':
    main( )
