import CoreFoundation
import objc
from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_level_key,
    os_release,
    skipUnless,
)


class TestRunLoop(TestCase):
    def testTypes(self):
        self.assertIsCFType(CoreFoundation.CFRunLoopRef)
        self.assertIsCFType(CoreFoundation.CFRunLoopSourceRef)
        self.assertIsCFType(CoreFoundation.CFRunLoopObserverRef)

        try:
            if objc.lookUpClass("__NSCFTimer") is CoreFoundation.CFRunLoopTimerRef:
                return
        except objc.error:
            pass
        try:
            if objc.lookUpClass("NSCFTimer") is CoreFoundation.CFRunLoopTimerRef:
                return
        except objc.error:
            pass
        self.assertIsCFType(CoreFoundation.CFRunLoopTimerRef)

    def testConstants(self):
        self.assertEqual(CoreFoundation.kCFRunLoopRunFinished, 1)
        self.assertEqual(CoreFoundation.kCFRunLoopRunStopped, 2)
        self.assertEqual(CoreFoundation.kCFRunLoopRunTimedOut, 3)
        self.assertEqual(CoreFoundation.kCFRunLoopRunHandledSource, 4)
        self.assertEqual(CoreFoundation.kCFRunLoopEntry, (1 << 0))
        self.assertEqual(CoreFoundation.kCFRunLoopBeforeTimers, (1 << 1))
        self.assertEqual(CoreFoundation.kCFRunLoopBeforeSources, (1 << 2))
        self.assertEqual(CoreFoundation.kCFRunLoopBeforeWaiting, (1 << 5))
        self.assertEqual(CoreFoundation.kCFRunLoopAfterWaiting, (1 << 6))
        self.assertEqual(CoreFoundation.kCFRunLoopExit, (1 << 7))
        self.assertEqual(CoreFoundation.kCFRunLoopAllActivities, 0x0FFFFFFF)
        self.assertIsInstance(CoreFoundation.kCFRunLoopDefaultMode, str)
        self.assertIsInstance(CoreFoundation.kCFRunLoopCommonModes, str)

    def testGetTypeID(self):
        self.assertIsInstance(CoreFoundation.CFRunLoopGetTypeID(), int)
        self.assertIsInstance(CoreFoundation.CFRunLoopSourceGetTypeID(), int)
        self.assertIsInstance(CoreFoundation.CFRunLoopObserverGetTypeID(), int)
        self.assertIsInstance(CoreFoundation.CFRunLoopTimerGetTypeID(), int)

    def testRunloop(self):
        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"

        loop = CoreFoundation.CFRunLoopGetCurrent()
        self.assertIsInstance(loop, CoreFoundation.CFRunLoopRef)
        loop = CoreFoundation.CFRunLoopGetMain()
        self.assertIsInstance(loop, CoreFoundation.CFRunLoopRef)
        mode = CoreFoundation.CFRunLoopCopyCurrentMode(loop)
        if mode is not None:
            self.assertIsInstance(mode, str)
        self.assertResultIsCFRetained(CoreFoundation.CFRunLoopCopyAllModes)
        allmodes = CoreFoundation.CFRunLoopCopyAllModes(loop)
        self.assertIsInstance(allmodes, CoreFoundation.CFArrayRef)
        self.assertNotEqual(len(allmodes), 0)
        for mode in allmodes:
            self.assertIsInstance(mode, str)
        CoreFoundation.CFRunLoopAddCommonMode(loop, "pyobjctest")
        allmodes = CoreFoundation.CFRunLoopCopyAllModes(loop)

        tm = CoreFoundation.CFRunLoopGetNextTimerFireDate(loop, runloop_mode)
        self.assertIsInstance(tm, float)
        b = CoreFoundation.CFRunLoopIsWaiting(loop)
        self.assertIsInstance(b, bool)
        CoreFoundation.CFRunLoopWakeUp(loop)
        CoreFoundation.CFRunLoopStop(loop)

        res = CoreFoundation.CFRunLoopRunInMode("mode", 2.0, True)
        self.assertIsInstance(res, int)
        self.assertEqual(res, CoreFoundation.kCFRunLoopRunFinished)

        # CoreFoundation.CFRunLoopRun is hard to test reliably
        self.assertHasAttr(CoreFoundation, "CFRunLoopRun")

    def testObserver(self):
        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"

        rl = CoreFoundation.CFRunLoopGetCurrent()

        data = {}
        state = []

        def callback(observer, activity, info):
            state.append((observer, activity, info))

        observer = CoreFoundation.CFRunLoopObserverCreate(
            None,
            CoreFoundation.kCFRunLoopEntry | CoreFoundation.kCFRunLoopExit,
            True,
            4,
            callback,
            data,
        )
        self.assertIsInstance(observer, CoreFoundation.CFRunLoopObserverRef)
        ctx = CoreFoundation.CFRunLoopObserverGetContext(observer, None)
        self.assertIs(ctx, data)
        self.assertIs(CoreFoundation.CFRunLoopObserverDoesRepeat(observer), True)
        self.assertEqual(CoreFoundation.CFRunLoopObserverGetOrder(observer), 4)
        self.assertIs(CoreFoundation.CFRunLoopObserverIsValid(observer), True)
        self.assertEqual(
            CoreFoundation.CFRunLoopObserverGetActivities(observer),
            CoreFoundation.kCFRunLoopEntry | CoreFoundation.kCFRunLoopExit,
        )
        CoreFoundation.CFRunLoopObserverInvalidate(observer)
        self.assertIs(CoreFoundation.CFRunLoopObserverIsValid(observer), False)
        ctx = CoreFoundation.CFRunLoopObserverGetContext(observer, None)
        self.assertIs(ctx, objc.NULL)
        observer = CoreFoundation.CFRunLoopObserverCreate(
            None,
            CoreFoundation.kCFRunLoopEntry | CoreFoundation.kCFRunLoopExit,
            True,
            4,
            callback,
            data,
        )
        self.assertIsInstance(observer, CoreFoundation.CFRunLoopObserverRef)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsObserver(rl, observer, runloop_mode), False
        )
        CoreFoundation.CFRunLoopAddObserver(rl, observer, runloop_mode)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsObserver(rl, observer, runloop_mode), True
        )

        # Use dummy stream to ensure that the runloop actually performs work
        strval = b"hello world"
        stream = CoreFoundation.CFReadStreamCreateWithBytesNoCopy(
            None, strval, len(strval), CoreFoundation.kCFAllocatorNull
        )
        self.assertIsInstance(stream, CoreFoundation.CFReadStreamRef)
        CoreFoundation.CFReadStreamScheduleWithRunLoop(stream, rl, runloop_mode)
        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 1.0, True)
        self.assertIsInstance(res, int)
        CoreFoundation.CFReadStreamUnscheduleFromRunLoop(stream, rl, runloop_mode)

        self.assertNotEqual(len(state), 0)
        for item in state:
            self.assertIs(item[0], observer)
            self.assertIn(
                item[1], (CoreFoundation.kCFRunLoopEntry, CoreFoundation.kCFRunLoopExit)
            )
            self.assertIs(item[2], data)
        CoreFoundation.CFRunLoopRemoveObserver(rl, observer, runloop_mode)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsObserver(rl, observer, runloop_mode), False
        )

    def testTimer(self):
        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"
        rl = CoreFoundation.CFRunLoopGetCurrent()

        state = []
        data = {}

        def callback(timer, info):
            state.append((timer, info))

        timer = CoreFoundation.CFRunLoopTimerCreate(None, 0, 0.5, 0, 0, callback, data)

        r = CoreFoundation.CFRunLoopTimerGetNextFireDate(timer)
        self.assertIsInstance(r, float)
        CoreFoundation.CFRunLoopTimerSetNextFireDate(timer, r + 2)
        r2 = CoreFoundation.CFRunLoopTimerGetNextFireDate(timer)
        self.assertEqual(int(r2), int(r + 2))

        r = CoreFoundation.CFRunLoopTimerGetInterval(timer)
        self.assertEqual(r, 0.5)

        self.assertIs(CoreFoundation.CFRunLoopTimerGetContext(timer, None), data)
        self.assertIs(CoreFoundation.CFRunLoopTimerDoesRepeat(timer), True)
        self.assertEqual(CoreFoundation.CFRunLoopTimerGetOrder(timer), 0)
        self.assertIs(CoreFoundation.CFRunLoopTimerIsValid(timer), True)
        CoreFoundation.CFRunLoopTimerInvalidate(timer)
        self.assertIs(CoreFoundation.CFRunLoopTimerIsValid(timer), False)
        self.assertIs(CoreFoundation.CFRunLoopTimerGetContext(timer, None), objc.NULL)
        timer = CoreFoundation.CFRunLoopTimerCreate(None, 0, 0.5, 0, 0, callback, data)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsTimer(rl, timer, runloop_mode), False
        )
        CoreFoundation.CFRunLoopAddTimer(rl, timer, runloop_mode)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsTimer(rl, timer, runloop_mode), True
        )
        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 1.3, True)
        self.assertIsInstance(res, int)

        CoreFoundation.CFRunLoopTimerInvalidate(timer)
        CoreFoundation.CFRunLoopRemoveTimer(rl, timer, runloop_mode)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsTimer(rl, timer, runloop_mode), False
        )
        self.assertFalse(len(state) < 3)
        for item in state:
            self.assertIs(item[0], timer)
            self.assertIs(item[1], data)

    def testSource(self):
        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        runloop_mode = "pyobjctest.cfrunloop"

        rl = CoreFoundation.CFRunLoopGetCurrent()

        state = []
        data = {}

        def schedule(info, rl, mode):
            state.append(["schedule", info, rl, mode])

        def cancel(info, rl, mode):
            state.append(["cancel", info, rl, mode])

        def perform(info):
            state.append(["perform", info])

        source = CoreFoundation.CFRunLoopSourceCreate(
            None, 55, (0, schedule, cancel, perform, data)
        )
        self.assertIsInstance(source, CoreFoundation.CFRunLoopSourceRef)
        ctx = CoreFoundation.CFRunLoopSourceGetContext(source, None)
        self.assertIsInstance(ctx, tuple)
        self.assertEqual(ctx[0], 0)
        self.assertEqual(ctx[1], schedule)
        self.assertEqual(ctx[2], cancel)
        self.assertEqual(ctx[3], perform)
        self.assertEqual(ctx[4], data)

        self.assertEqual(CoreFoundation.CFRunLoopSourceGetOrder(source), 55)
        self.assertIs(CoreFoundation.CFRunLoopSourceIsValid(source), True)
        CoreFoundation.CFRunLoopSourceInvalidate(source)
        self.assertIs(CoreFoundation.CFRunLoopSourceIsValid(source), False)
        source = CoreFoundation.CFRunLoopSourceCreate(
            None, 55, (0, schedule, cancel, perform, data)
        )
        self.assertIsInstance(source, CoreFoundation.CFRunLoopSourceRef)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsSource(rl, source, runloop_mode), False
        )
        CoreFoundation.CFRunLoopAddSource(rl, source, runloop_mode)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsSource(rl, source, runloop_mode), True
        )
        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0], "schedule")
        self.assertIs(state[0][1], data)
        self.assertIs(state[0][2], rl)
        self.assertEqual(state[0][3], runloop_mode)
        del state[:]

        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 0.5, True)
        self.assertIsInstance(res, int)
        # self.assertEqual(res, CoreFoundation.kCFRunLoopRunTimedOut)

        self.assertEqual(len(state), 0)

        CoreFoundation.CFRunLoopSourceSignal(source)

        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 0.5, True)
        self.assertIsInstance(res, int)
        self.assertEqual(res, CoreFoundation.kCFRunLoopRunHandledSource)

        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0], "perform")
        self.assertIs(state[0][1], data)
        del state[:]

        CoreFoundation.CFRunLoopRemoveSource(rl, source, runloop_mode)
        self.assertIs(
            CoreFoundation.CFRunLoopContainsSource(rl, source, runloop_mode), False
        )
        self.assertEqual(len(state), 1)
        self.assertEqual(state[0][0], "cancel")
        self.assertIs(state[0][1], data)
        self.assertIs(state[0][2], rl)
        self.assertEqual(state[0][3], runloop_mode)

    @skipUnless(
        not (
            os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.15")
        ),
        "Crash on 10.13, 10.14??",
    )
    @skipUnless(
        not (os_level_key("15.0") <= os_level_key(os_release()) < os_level_key("16.0")),
        "Crash on macOS 15",
    )
    @min_os_level("10.6")
    def testFunctions10_6(self):
        self.assertArgIsBlock(CoreFoundation.CFRunLoopPerformBlock, 2, b"v")

        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        rl = CoreFoundation.CFRunLoopGetCurrent()

        lst = []

        def doit():
            lst.append(True)

        CoreFoundation.CFRunLoopPerformBlock(rl, runloop_mode, doit)
        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 0.5, True)
        self.assertIsInstance(res, int)

        self.assertEqual(lst, [True])

    @skipUnless(
        not (
            os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.15")
        ),
        "Crash on 10.13, 10.14??",
    )
    @skipUnless(
        not (os_level_key("15.0") <= os_level_key(os_release()) < os_level_key("16.0")),
        "Crash on macOS 15",
    )
    @min_os_level("10.7")
    def testFunctions10_7(self):
        self.assertArgIsBOOL(CoreFoundation.CFRunLoopObserverCreateWithHandler, 2)
        self.assertArgIsBlock(
            CoreFoundation.CFRunLoopObserverCreateWithHandler,
            4,
            b"v^{__CFRunLoopObserver=}" + objc._C_NSUInteger,
        )

        lst = []

        def record(observer, activity):
            lst.append((observer, activity))

        ref = CoreFoundation.CFRunLoopObserverCreateWithHandler(
            None, CoreFoundation.kCFRunLoopAllActivities, False, 0, record
        )
        self.assertIsInstance(ref, CoreFoundation.CFRunLoopObserverRef)

        runloop_mode = CoreFoundation.kCFRunLoopDefaultMode
        rl = CoreFoundation.CFRunLoopGetCurrent()

        CoreFoundation.CFRunLoopAddObserver(rl, ref, runloop_mode)
        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 0.5, True)
        CoreFoundation.CFRunLoopRemoveObserver(rl, ref, runloop_mode)

        self.assertNotEqual(lst, [])
        for a, b in lst:
            self.assertEqual(a, ref)
            self.assertIsInstance(b, int)

        self.assertArgIsBlock(
            CoreFoundation.CFRunLoopTimerCreateWithHandler, 5, b"v^{__CFRunLoopTimer=}"
        )
        lst = []
        ref = CoreFoundation.CFRunLoopTimerCreateWithHandler(
            None,
            CoreFoundation.CFAbsoluteTimeGetCurrent() + 2.9,
            0.0,
            0,
            0,
            lambda x: lst.append(x),
        )
        self.assertIsInstance(ref, CoreFoundation.CFRunLoopTimerRef)

        CoreFoundation.CFRunLoopAddTimer(rl, ref, runloop_mode)
        res = CoreFoundation.CFRunLoopRunInMode(runloop_mode, 6.0, True)
        self.assertIsInstance(res, int)
        CoreFoundation.CFRunLoopRemoveTimer(rl, ref, runloop_mode)

        import __main__

        # XXX: See issue #11 in the pyobjc tracker
        if "setup" in __main__.__file__:
            return

        self.assertNotEqual(lst, [])
        for a in lst:
            self.assertEqual(a, ref)

    @min_os_level("10.9")
    def testFunctions10_9(self):
        lst = []
        ref = CoreFoundation.CFRunLoopTimerCreateWithHandler(
            None,
            CoreFoundation.CFAbsoluteTimeGetCurrent() + 2.9,
            0.0,
            0,
            0,
            lambda x: lst.append(x),
        )
        self.assertIsInstance(ref, CoreFoundation.CFRunLoopTimerRef)
        CoreFoundation.CFRunLoopTimerSetTolerance(ref, 5.0)
        v = CoreFoundation.CFRunLoopTimerGetTolerance(ref)
        self.assertIsInstance(v, float)
