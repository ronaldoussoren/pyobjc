import unittest
import gc

from objc import *
from Foundation import *

class PythonClass (object):
    def __init__(self):
        self.fireCount = 0

    def fire_(self, timer):
        self.fireCount += 1


class TestNSTimer(unittest.TestCase):

    def _testHelp(self):
        obj = PythonClass()
        pool = NSAutoreleasePool.new()
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

if __name__ == '__main__':
    unittest.main( )
