from PyObjCTools.TestSupport import *
from CoreFoundation import *
import CoreFoundation

try:
    unicode
except NameError:
    unicode = str


try:
    long
except NameError:
    long = int

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
        runloop_mode = kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"

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

        tm = CFRunLoopGetNextTimerFireDate(loop, runloop_mode)
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
        runloop_mode = kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"

        rl = CFRunLoopGetCurrent()

        data = {}
        state = []
        def callback(observer, activity, info):
            state.append((observer, activity, info))

        observer = CFRunLoopObserverCreate(None, kCFRunLoopEntry|kCFRunLoopExit,
                True, 4, callback, data)
        self.assertIsInstance(observer, CFRunLoopObserverRef)
        ctx = CFRunLoopObserverGetContext(observer, None)
        self.assertIs(ctx, data)
        self.assertEqual(CFRunLoopObserverGetActivities(observer), kCFRunLoopEntry|kCFRunLoopExit)
        self.assertIs(CFRunLoopObserverDoesRepeat(observer), True)
        self.assertEqual(CFRunLoopObserverGetOrder(observer), 4)
        self.assertIs(CFRunLoopObserverIsValid(observer), True)
        CFRunLoopObserverInvalidate(observer)
        self.assertIs(CFRunLoopObserverIsValid(observer), False)
        ctx = CFRunLoopObserverGetContext(observer, None)
        self.assertIs(ctx, objc.NULL)
        observer = CFRunLoopObserverCreate(None, kCFRunLoopEntry|kCFRunLoopExit,
                True, 4, callback, data)
        self.assertIsInstance(observer, CFRunLoopObserverRef)
        self.assertIs(CFRunLoopContainsObserver(rl, observer, runloop_mode), False)
        CFRunLoopAddObserver(rl, observer, runloop_mode)
        self.assertIs(CFRunLoopContainsObserver(rl, observer, runloop_mode), True)

        # Use dummy stream to ensure that the runloop actually performs work
        strval = b'hello world'
        stream = CFReadStreamCreateWithBytesNoCopy(None,
                                strval, len(strval), kCFAllocatorNull)
        self.assertIsInstance(stream, CFReadStreamRef)
        CFReadStreamScheduleWithRunLoop(stream, rl, runloop_mode)
        res = CFRunLoopRunInMode(runloop_mode, 1.0, True)
        CFReadStreamUnscheduleFromRunLoop(stream, rl, runloop_mode)

        self.assertNotEqual(len(state) , 0 )
        for item in state:
            self.assertIs(item[0], observer)
            self.assertIn(item[1], (kCFRunLoopEntry, kCFRunLoopExit))
            self.assertIs(item[2], data)
        CFRunLoopRemoveObserver(rl, observer, runloop_mode)
        self.assertIs(CFRunLoopContainsObserver(rl, observer, runloop_mode), False)

    def testTimer(self):
        runloop_mode = kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"
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

        self.assertIs(CFRunLoopTimerGetContext(timer, None), data)
        self.assertIs(CFRunLoopTimerDoesRepeat(timer), True)
        self.assertEqual(CFRunLoopTimerGetOrder(timer), 0)
        self.assertIs(CFRunLoopTimerIsValid(timer), True)
        CFRunLoopTimerInvalidate(timer)
        self.assertIs(CFRunLoopTimerIsValid(timer), False)
        self.assertIs(CFRunLoopTimerGetContext(timer, None), objc.NULL)
        timer = CFRunLoopTimerCreate(None, 0, 0.5, 0, 0, callback, data)
        self.assertIs(CFRunLoopContainsTimer(rl, timer, runloop_mode), False)
        CFRunLoopAddTimer(rl, timer, runloop_mode)
        self.assertIs(CFRunLoopContainsTimer(rl, timer, runloop_mode), True)
        res = CFRunLoopRunInMode(runloop_mode, 1.3, True)

        CFRunLoopTimerInvalidate(timer)
        CFRunLoopRemoveTimer(rl, timer, runloop_mode)
        self.assertIs(CFRunLoopContainsTimer(rl, timer, runloop_mode), False)
        self.assertFalse(len(state) < 3)
        for item in state:
            self.assertIs(item[0], timer)
            self.assertIs(item[1], data)

    def testSource(self):
        runloop_mode = kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"

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
        self.assertIs(CFRunLoopSourceIsValid(source), True)
        CFRunLoopSourceInvalidate(source)
        self.assertIs(CFRunLoopSourceIsValid(source), False)
        source = CFRunLoopSourceCreate(None, 55,
                (0, schedule, cancel, perform, data))
        self.assertIsInstance(source, CFRunLoopSourceRef)
        self.assertIs(CFRunLoopContainsSource(rl, source, runloop_mode), False)
        CFRunLoopAddSource(rl, source, runloop_mode)
        self.assertIs(CFRunLoopContainsSource(rl, source, runloop_mode), True)
        self.assertEqual(len(state) , 1)
        self.assertEqual(state[0][0] , 'schedule')
        self.assertIs(state[0][1], data)
        self.assertIs(state[0][2], rl)
        self.assertEqual(state[0][3] , runloop_mode)
        del state[:]

        res = CFRunLoopRunInMode(runloop_mode, 0.5, True)
        self.assertIsInstance(res, (int, long))
        #self.assertEqual(res, kCFRunLoopRunTimedOut)

        self.assertEqual(len(state), 0)

        CFRunLoopSourceSignal(source)

        res = CFRunLoopRunInMode(runloop_mode, 0.5, True)
        self.assertIsInstance(res, (int, long))
        self.assertEqual(res, kCFRunLoopRunHandledSource)

        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0] , 'perform')
        self.assertIs(state[0][1], data)
        del state[:]

        CFRunLoopRemoveSource(rl, source, runloop_mode)
        self.assertIs(CFRunLoopContainsSource(rl, source, runloop_mode), False)
        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0] , 'cancel')
        self.assertIs(state[0][1], data)
        self.assertIs(state[0][2], rl)
        self.assertEqual(state[0][3] , runloop_mode)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        self.assertArgIsBlock(CFRunLoopPerformBlock, 2, b'v')


        runloop_mode = kCFRunLoopDefaultMode
        rl = CFRunLoopGetCurrent()

        l = []
        def doit():
            l.append(True)
        CFRunLoopPerformBlock(rl, runloop_mode, doit)
        res = CFRunLoopRunInMode(runloop_mode, 0.5, True)

        self.assertEqual(l, [True])

    @min_os_level('10.7')
    def testFunctions10_7(self):
        self.assertArgIsBOOL(CFRunLoopObserverCreateWithHandler, 2)
        self.assertArgIsBlock(CFRunLoopObserverCreateWithHandler, 4, b"v^{__CFRunLoopObserver=}" + objc._C_NSUInteger)

        l = []
        def record(observer, activity):
            l.append((observer, activity))


        ref = CFRunLoopObserverCreateWithHandler(None, kCFRunLoopAllActivities, False, 0, record)
        self.assertIsInstance(ref, CFRunLoopObserverRef)

        runloop_mode = kCFRunLoopDefaultMode
        rl = CFRunLoopGetCurrent()

        CFRunLoopAddObserver(rl, ref, runloop_mode)
        res = CFRunLoopRunInMode(runloop_mode, 0.5, True)
        CFRunLoopRemoveObserver(rl, ref, runloop_mode)


        self.assertNotEqual(l, [])
        for a, b in l:
            self.assertEqual(a, ref)
            self.assertIsInstance(b, (int, long))


        self.assertArgIsBlock(CFRunLoopTimerCreateWithHandler, 5, b'v^{__CFRunLoopTimer=}')
        l = []
        ref = CFRunLoopTimerCreateWithHandler(None,
                CFAbsoluteTimeGetCurrent() + 2.9, 0.0, 0, 0, lambda x: l.append(x))
        self.assertIsInstance(ref, CFRunLoopTimerRef)

        CFRunLoopAddTimer(rl, ref, runloop_mode)
        res = CFRunLoopRunInMode(runloop_mode, 6.0, True)
        CFRunLoopRemoveTimer(rl, ref, runloop_mode)

        # XXX: For some reason the timer fails with a full testrun.
        # See also issue #11 in the pyobjc tracker
        import __main__
        if 'setup' in __main__.__file__:
            return

        self.assertNotEqual(l, [])
        for a in l:
            self.assertEqual(a, ref)




if __name__ == "__main__":
    main()
