from PyObjCTools.TestSupport import *
from CoreFoundation import *


class TestRunLoop (TestCase):

    def testTypes(self):
        self.failUnlessIsCFType(CFRunLoopRef)
        self.failUnlessIsCFType(CFRunLoopSourceRef)
        self.failUnlessIsCFType(CFRunLoopObserverRef)
        self.failUnlessIsCFType(CFRunLoopTimerRef)

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

        self.failUnlessResultIsCFRetained(CFRunLoopCopyAllModes)
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

        res = CFRunLoopRunInMode("mode", 2.0, True)
        self.failUnless(isinstance(res, (int, long)))
        self.assertEquals(res, kCFRunLoopRunFinished)

        # CFRunLoopRun is hard to test reliably
        self.failUnless(hasattr(CoreFoundation, 'CFRunLoopRun'))

    def testObserver(self):

        rl = CFRunLoopGetCurrent()

        data = {}
        state = []
        def callback(observer, activity, info):
            state.append((observer, activity, info))

        observer = CFRunLoopObserverCreate(None, kCFRunLoopEntry|kCFRunLoopExit,
                True, 4, callback, data)
        self.failUnless(isinstance(observer, CFRunLoopObserverRef))
        ctx = CFRunLoopObserverGetContext(observer)
        self.failUnless(ctx is data)

        self.assertEquals(CFRunLoopObserverGetActivities(observer), kCFRunLoopEntry|kCFRunLoopExit)
        self.failUnless(CFRunLoopObserverDoesRepeat(observer) is True)
        self.assertEquals(CFRunLoopObserverGetOrder(observer), 4)
        self.failUnless(CFRunLoopObserverIsValid(observer) is True)
        CFRunLoopObserverInvalidate(observer)
        self.failUnless(CFRunLoopObserverIsValid(observer) is False)
        ctx = CFRunLoopObserverGetContext(observer)
        self.failUnless(ctx is objc.NULL)


        observer = CFRunLoopObserverCreate(None, kCFRunLoopEntry|kCFRunLoopExit,
                True, 4, callback, data)
        self.failUnless(isinstance(observer, CFRunLoopObserverRef))

        self.failUnless (CFRunLoopContainsObserver(rl, observer, kCFRunLoopDefaultMode) is False)
        CFRunLoopAddObserver(rl, observer, kCFRunLoopDefaultMode)
        self.failUnless (CFRunLoopContainsObserver(rl, observer, kCFRunLoopDefaultMode) is True)

        # Use dummy stream to ensure that the runloop actually performs work
        strval = 'hello world'
        stream = CFReadStreamCreateWithBytesNoCopy(None,
                                strval, len(strval), kCFAllocatorNull)
        self.failUnless(isinstance(stream, CFReadStreamRef))

        CFReadStreamScheduleWithRunLoop(stream, rl, kCFRunLoopDefaultMode)
        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
        CFReadStreamUnscheduleFromRunLoop(stream, rl, kCFRunLoopDefaultMode)
        
        self.failIf( len(state) == 0 )
        for item in state:
            self.failUnless(item[0] is observer)
            self.failUnless(item[1] in (kCFRunLoopEntry, kCFRunLoopExit))
            self.failUnless(item[2] is data)


        CFRunLoopRemoveObserver(rl, observer, kCFRunLoopDefaultMode)
        self.failUnless (CFRunLoopContainsObserver(rl, observer, kCFRunLoopDefaultMode) is False)


    def testTimer(self):
        rl = CFRunLoopGetCurrent()

        state = []
        data = {}
        def callback(timer, info):
            state.append((timer, info))

        timer = CFRunLoopTimerCreate(None, 0, 0.5, 0, 0, callback, data)

        r = CFRunLoopTimerGetNextFireDate(timer)
        self.failUnless(isinstance(r, float))

        CFRunLoopTimerSetNextFireDate(timer, r + 2)
        r2 = CFRunLoopTimerGetNextFireDate(timer)
        self.assertEquals(int(r2), int(r + 2))

        r = CFRunLoopTimerGetInterval(timer)
        self.assertEquals(r, 0.5)

        self.failUnless(CFRunLoopTimerGetContext(timer) is data)
        self.failUnless(CFRunLoopTimerDoesRepeat(timer) is True)
        self.assertEquals(CFRunLoopTimerGetOrder(timer), 0)
        self.failUnless(CFRunLoopTimerIsValid(timer) is True)
        CFRunLoopTimerInvalidate(timer)
        self.failUnless(CFRunLoopTimerIsValid(timer) is False)
        self.failUnless(CFRunLoopTimerGetContext(timer) is objc.NULL)


        timer = CFRunLoopTimerCreate(None, 0, 0.5, 0, 0, callback, data)
        self.failUnless(CFRunLoopContainsTimer(rl, timer, kCFRunLoopDefaultMode) is False)
        CFRunLoopAddTimer(rl, timer, kCFRunLoopDefaultMode)
        self.failUnless(CFRunLoopContainsTimer(rl, timer, kCFRunLoopDefaultMode) is True)

        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 2.0, True)

        CFRunLoopRemoveTimer(rl, timer, kCFRunLoopDefaultMode)
        self.failUnless(CFRunLoopContainsTimer(rl, timer, kCFRunLoopDefaultMode) is False)

        self.failIf(len(state) < 3)
        for item in state:
            self.failUnless(item[0] is timer)
            self.failUnless(item[1] is data)

    def testSource(self):
        rl = CFRunLoopGetCurrent()
        
        state = []
        data = {}
        def schedule(info, rl, mode):
            state.append(['schedule', info, rl, mode])
        def cancel(info, rl, mode):
            state.append(['cancel', info, rl, mode])
        def perform(info):
            state.append(['perform', info])

        source = CFRunLoopSourceCreate(None, 55, 
                (0, schedule, cancel, perform, data))
        self.failUnless(isinstance(source, CFRunLoopSourceRef))

        ctx = CFRunLoopSourceGetContext(source, None)
        self.failUnless(isinstance(ctx, tuple))
        self.assertEquals(ctx[0], 0)
        self.assertEquals(ctx[1], schedule)
        self.assertEquals(ctx[2], cancel)
        self.assertEquals(ctx[3], perform)
        self.assertEquals(ctx[4], data)

        self.assertEquals(CFRunLoopSourceGetOrder(source), 55)
        self.failUnless(CFRunLoopSourceIsValid(source) is True)
        CFRunLoopSourceInvalidate(source)
        self.failUnless(CFRunLoopSourceIsValid(source) is False)

        source = CFRunLoopSourceCreate(None, 55, 
                (0, schedule, cancel, perform, data))
        self.failUnless(isinstance(source, CFRunLoopSourceRef))

        self.failUnless(CFRunLoopContainsSource(rl, source, kCFRunLoopDefaultMode) is False)
        CFRunLoopAddSource(rl, source, kCFRunLoopDefaultMode)
        self.failUnless(CFRunLoopContainsSource(rl, source, kCFRunLoopDefaultMode) is True)
        self.failUnless(len(state) == 1)
        self.failUnless(state[0][0] == 'schedule')
        self.failUnless(state[0][1] is data)
        self.failUnless(state[0][2] is rl)
        self.failUnless(state[0][3] == kCFRunLoopDefaultMode)


        del state[:]

        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.5, True)
        self.failUnless(isinstance(res, (int, long)))
        #self.assertEquals(res, kCFRunLoopRunTimedOut)

        self.assertEquals(len(state), 0)

        CFRunLoopSourceSignal(source)

        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.5, True)
        self.failUnless(isinstance(res, (int, long)))
        self.assertEquals(res, kCFRunLoopRunHandledSource)

        self.assertEquals(len(state), 1)
        self.failUnless(state[0][0] == 'perform')
        self.failUnless(state[0][1] is data)

        del state[:]

        CFRunLoopRemoveSource(rl, source, kCFRunLoopDefaultMode)
        self.failUnless(CFRunLoopContainsSource(rl, source, kCFRunLoopDefaultMode) is False)

        self.assertEquals(len(state), 1)
        self.failUnless(state[0][0] == 'cancel')
        self.failUnless(state[0][1] is data)
        self.failUnless(state[0][2] is rl)
        self.failUnless(state[0][3] == kCFRunLoopDefaultMode)

if __name__ == "__main__":
    main()
