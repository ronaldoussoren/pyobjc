import unittest
from CoreFoundation import *


class TestRunLoop (unittest.TestCase):
    def testDummy(self):
        self.fail("CFRunLoop tests not implemented yet")


    def testConstants(self):
        self.failUnless(kCFRunLoopRunFinished == 1)
        self.failUnless(kCFRunLoopRunStopped == 2)
        self.failUnless(kCFRunLoopRunTimedOut == 3)
        self.failUnless(kCFRunLoopRunHandledSource == 4)

        self.failUnless(kCFRunLoopEntry == (1 << 0))
        self.failUnless(kCFRunLoopBeforeTimers == (1 << 1))
        self.failUnless(kCFRunLoopBeforeSources == (1 << 2))
        self.failUnless(kCFRunLoopBeforeWaiting == (1 << 5))
        self.failUnless(kCFRunLoopAfterWaiting == (1 << 6))
        self.failUnless(kCFRunLoopExit == (1 << 7))
        self.failUnless(kCFRunLoopAllActivities == 0x0FFFFFFF)

        self.failUnless(isinstance(kCFRunLoopDefaultMode, unicode))
        self.failUnless(isinstance(kCFRunLoopCommonModes, unicode))

    def testGetTypeID(self):
        self.failUnless(isinstance(CFRunLoopGetTypeID(), (int, long)))
        self.failUnless(isinstance(CFRunLoopSourceGetTypeID(), (int, long)))
        self.failUnless(isinstance(CFRunLoopObserverGetTypeID(), (int, long)))
        self.failUnless(isinstance(CFRunLoopTimerGetTypeID(), (int, long)))

    def testRunloop(self):
        loop = CFRunLoopGetCurrent()
        self.failUnless(isinstance(loop, CFRunLoopRef))

        loop = CFRunLoopGetMain()
        self.failUnless(isinstance(loop, CFRunLoopRef))

        mode = CFRunLoopCopyCurrentMode(loop)
        self.failUnless(mode is None or isinstance(mode, unicode))

        allmodes = CFRunLoopCopyAllModes(loop)
        self.failUnless(isinstance(allmodes, CFArrayRef))
        self.failIf(len(allmodes) == 0)
        for mode in allmodes:
            self.failUnless(isinstance(mode, unicode))

        CFRunLoopAddCommonMode(loop, "pyobjctest")
        allmodes = CFRunLoopCopyAllModes(loop)

        tm = CFRunLoopGetNextTimerFireDate(loop, kCFRunLoopDefaultMode)
        self.failUnless(isinstance(tm, float))

        b = CFRunLoopIsWaiting(loop)
        self.failUnless(isinstance(b, bool))
        CFRunLoopWakeUp(loop)
        CFRunLoopStop(loop)

        # CFRunLoopRun
        # CFRunLoopRunInMode

    def testObserver(self):
        #CF_EXPORT Boolean CFRunLoopContainsObserver(CFRunLoopRef rl, CFRunLoopObserverRef observer, CFStringRef mode);
        #CF_EXPORT void CFRunLoopAddObserver(CFRunLoopRef rl, CFRunLoopObserverRef observer, CFStringRef mode);
        #CF_EXPORT void CFRunLoopRemoveObserver(CFRunLoopRef rl, CFRunLoopObserverRef observer, CFStringRef mode);
        pass


    def testTimer(self):
        #CF_EXPORT Boolean CFRunLoopContainsTimer(CFRunLoopRef rl, CFRunLoopTimerRef timer, CFStringRef mode);
        #CF_EXPORT void CFRunLoopAddTimer(CFRunLoopRef rl, CFRunLoopTimerRef timer, CFStringRef mode);
        #CF_EXPORT void CFRunLoopRemoveTimer(CFRunLoopRef rl, CFRunLoopTimerRef timer, CFStringRef mode);
        pass

    def testSource(self):
        #CF_EXPORT Boolean CFRunLoopContainsSource(CFRunLoopRef rl, CFRunLoopSourceRef source, CFStringRef mode);
        #CF_EXPORT void CFRunLoopAddSource(CFRunLoopRef rl, CFRunLoopSourceRef source, CFStringRef mode);
        #CF_EXPORT void CFRunLoopRemoveSource(CFRunLoopRef rl, CFRunLoopSourceRef source, CFStringRef mode);

        pass







if __name__ == "__main__":
    unittest.main()
