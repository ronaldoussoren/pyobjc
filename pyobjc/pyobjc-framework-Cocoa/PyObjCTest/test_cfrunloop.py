from PyObjCTools.TestSupport import *
from CoreFoundation import *
import CoreFoundation


class TestRunLoop (TestCase):

    def testTypes(self):
        self.assertIsCFType(CFRunLoopRef)
        self.assertIsCFType(CFRunLoopSourceRef)
        self.assertIsCFType(CFRunLoopObserverRef)
        self.assertIsCFType(CFRunLoopTimerRef)

    def testConstants(self):
        self.assertEqual(kCFRunLoopRunFinished , 1)
        self.assertEqual(kCFRunLoopRunStopped , 2)
        self.assertEqual(kCFRunLoopRunTimedOut , 3)
        self.assertEqual(kCFRunLoopRunHandledSource , 4)
        self.assertEqual(kCFRunLoopEntry , (1 << 0))
        self.assertEqual(kCFRunLoopBeforeTimers , (1 << 1))
        self.assertEqual(kCFRunLoopBeforeSources , (1 << 2))
        self.assertEqual(kCFRunLoopBeforeWaiting , (1 << 5))
        self.assertEqual(kCFRunLoopAfterWaiting , (1 << 6))
        self.assertEqual(kCFRunLoopExit , (1 << 7))
        self.assertEqual(kCFRunLoopAllActivities , 0x0FFFFFFF)
        self.assertIsInstance(kCFRunLoopDefaultMode, unicode)
        self.assertIsInstance(kCFRunLoopCommonModes, unicode)
    def testGetTypeID(self):
        self.assertIsInstance(CFRunLoopGetTypeID(), (int, long))
        self.assertIsInstance(CFRunLoopSourceGetTypeID(), (int, long))
        self.assertIsInstance(CFRunLoopObserverGetTypeID(), (int, long))
        self.assertIsInstance(CFRunLoopTimerGetTypeID(), (int, long))
    def testRunloop(self):
        loop = CFRunLoopGetCurrent()
        self.assertIsInstance(loop, CFRunLoopRef)
        loop = CFRunLoopGetMain()
        self.assertIsInstance(loop, CFRunLoopRef)
        mode = CFRunLoopCopyCurrentMode(loop)
        if mode is not None:
            self.assertIsInstance(mode, unicode)
        self.assertResultIsCFRetained(CFRunLoopCopyAllModes)
        allmodes = CFRunLoopCopyAllModes(loop)
        self.assertIsInstance(allmodes, CFArrayRef)
        self.assertNotEqual(len(allmodes) , 0)
        for mode in allmodes:
            self.assertIsInstance(mode, unicode)
        CFRunLoopAddCommonMode(loop, "pyobjctest")
        allmodes = CFRunLoopCopyAllModes(loop)

        tm = CFRunLoopGetNextTimerFireDate(loop, kCFRunLoopDefaultMode)
        self.assertIsInstance(tm, float)
        b = CFRunLoopIsWaiting(loop)
        self.assertIsInstance(b, bool)
        CFRunLoopWakeUp(loop)
        CFRunLoopStop(loop)

        res = CFRunLoopRunInMode("mode", 2.0, True)
        self.assertIsInstance(res, (int, long))
        self.assertEqual(res, kCFRunLoopRunFinished)

        # CFRunLoopRun is hard to test reliably
        self.assertHasAttr(CoreFoundation, 'CFRunLoopRun')
    def testObserver(self):

        rl = CFRunLoopGetCurrent()

        data = {}
        state = []
        def callback(observer, activity, info):
            state.append((observer, activity, info))

        observer = CFRunLoopObserverCreate(None, kCFRunLoopEntry|kCFRunLoopExit,
                True, 4, callback, data)
        self.assertIsInstance(observer, CFRunLoopObserverRef)
        ctx = CFRunLoopObserverGetContext(observer)
        self.assertIsObject(ctx, data)
        self.assertEqual(CFRunLoopObserverGetActivities(observer), kCFRunLoopEntry|kCFRunLoopExit)
        self.assertIsObject(CFRunLoopObserverDoesRepeat(observer), True)
        self.assertEqual(CFRunLoopObserverGetOrder(observer), 4)
        self.assertIsObject(CFRunLoopObserverIsValid(observer), True)
        CFRunLoopObserverInvalidate(observer)
        self.assertIsObject(CFRunLoopObserverIsValid(observer), False)
        ctx = CFRunLoopObserverGetContext(observer)
        self.assertIsObject(ctx, objc.NULL)
        observer = CFRunLoopObserverCreate(None, kCFRunLoopEntry|kCFRunLoopExit,
                True, 4, callback, data)
        self.assertIsInstance(observer, CFRunLoopObserverRef)
        self.failUnless (CFRunLoopContainsObserver(rl, observer, kCFRunLoopDefaultMode) is False)
        CFRunLoopAddObserver(rl, observer, kCFRunLoopDefaultMode)
        self.failUnless (CFRunLoopContainsObserver(rl, observer, kCFRunLoopDefaultMode) is True)

        # Use dummy stream to ensure that the runloop actually performs work
        strval = 'hello world'
        stream = CFReadStreamCreateWithBytesNoCopy(None,
                                strval, len(strval), kCFAllocatorNull)
        self.assertIsInstance(stream, CFReadStreamRef)
        CFReadStreamScheduleWithRunLoop(stream, rl, kCFRunLoopDefaultMode)
        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 1.0, True)
        CFReadStreamUnscheduleFromRunLoop(stream, rl, kCFRunLoopDefaultMode)
        
        self.assertNotEqual(len(state) , 0 )
        for item in state:
            self.assertIsObject(item[0], observer)
            self.assertIsIn(item[1], (kCFRunLoopEntry, kCFRunLoopExit))
            self.assertIsObject(item[2], data)
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
        self.assertIsInstance(r, float)
        CFRunLoopTimerSetNextFireDate(timer, r + 2)
        r2 = CFRunLoopTimerGetNextFireDate(timer)
        self.assertEqual(int(r2), int(r + 2))

        r = CFRunLoopTimerGetInterval(timer)
        self.assertEqual(r, 0.5)

        self.assertIsObject(CFRunLoopTimerGetContext(timer), data)
        self.assertIsObject(CFRunLoopTimerDoesRepeat(timer), True)
        self.assertEqual(CFRunLoopTimerGetOrder(timer), 0)
        self.assertIsObject(CFRunLoopTimerIsValid(timer), True)
        CFRunLoopTimerInvalidate(timer)
        self.assertIsObject(CFRunLoopTimerIsValid(timer), False)
        self.assertIsObject(CFRunLoopTimerGetContext(timer), objc.NULL)
        timer = CFRunLoopTimerCreate(None, 0, 0.5, 0, 0, callback, data)
        self.assertIsObject(CFRunLoopContainsTimer(rl, timer, kCFRunLoopDefaultMode), False)
        CFRunLoopAddTimer(rl, timer, kCFRunLoopDefaultMode)
        self.assertIsObject(CFRunLoopContainsTimer(rl, timer, kCFRunLoopDefaultMode), True)
        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 2.0, True)

        CFRunLoopRemoveTimer(rl, timer, kCFRunLoopDefaultMode)
        self.assertIsObject(CFRunLoopContainsTimer(rl, timer, kCFRunLoopDefaultMode), False)
        self.assertFalse(len(state) < 3)
        for item in state:
            self.assertIsObject(item[0], timer)
            self.assertIsObject(item[1], data)
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
        self.assertIsInstance(source, CFRunLoopSourceRef)
        ctx = CFRunLoopSourceGetContext(source, None)
        self.assertIsInstance(ctx, tuple)
        self.assertEqual(ctx[0], 0)
        self.assertEqual(ctx[1], schedule)
        self.assertEqual(ctx[2], cancel)
        self.assertEqual(ctx[3], perform)
        self.assertEqual(ctx[4], data)

        self.assertEqual(CFRunLoopSourceGetOrder(source), 55)
        self.assertIsObject(CFRunLoopSourceIsValid(source), True)
        CFRunLoopSourceInvalidate(source)
        self.assertIsObject(CFRunLoopSourceIsValid(source), False)
        source = CFRunLoopSourceCreate(None, 55, 
                (0, schedule, cancel, perform, data))
        self.assertIsInstance(source, CFRunLoopSourceRef)
        self.assertIsObject(CFRunLoopContainsSource(rl, source, kCFRunLoopDefaultMode), False)
        CFRunLoopAddSource(rl, source, kCFRunLoopDefaultMode)
        self.assertIsObject(CFRunLoopContainsSource(rl, source, kCFRunLoopDefaultMode), True)
        self.assertEqual(len(state) , 1)
        self.assertEqual(state[0][0] , 'schedule')
        self.assertIsObject(state[0][1], data)
        self.assertIsObject(state[0][2], rl)
        self.assertEqual(state[0][3] , kCFRunLoopDefaultMode)
        del state[:]

        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.5, True)
        self.assertIsInstance(res, (int, long))
        #self.assertEqual(res, kCFRunLoopRunTimedOut)

        self.assertEqual(len(state), 0)

        CFRunLoopSourceSignal(source)

        res = CFRunLoopRunInMode(kCFRunLoopDefaultMode, 0.5, True)
        self.assertIsInstance(res, (int, long))
        self.assertEqual(res, kCFRunLoopRunHandledSource)

        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0] , 'perform')
        self.assertIsObject(state[0][1], data)
        del state[:]

        CFRunLoopRemoveSource(rl, source, kCFRunLoopDefaultMode)
        self.assertIsObject(CFRunLoopContainsSource(rl, source, kCFRunLoopDefaultMode), False)
        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0] , 'cancel')
        self.assertIsObject(state[0][1], data)
        self.assertIsObject(state[0][2], rl)
        self.assertEqual(state[0][3] , kCFRunLoopDefaultMode)
    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertArgIsBlock(CFRunLoopPerformBlock, 2, 'v')

if __name__ == "__main__":
    main()
