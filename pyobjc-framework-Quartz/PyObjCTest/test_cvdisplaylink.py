from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz
import objc


class TestCVDisplayLink(TestCase):
    def testTypes(self):
        self.assertIsCFType(Quartz.CVDisplayLinkRef)

    @min_os_level("10.11")
    def testFunctions10_11(self):
        # XXX: headers claim this is generally available ??
        self.assertArgIsBlock(
            Quartz.CVDisplayLinkSetOutputHandler,
            1,
            b"i^{__CVDisplayLink=}n^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}n^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}Qo^Q",  # noqa: B950
        )

    def testFunctions(self):
        self.assertIsInstance(Quartz.CVDisplayLinkGetTypeID(), int)

        mainID = Quartz.CGMainDisplayID()

        self.assertArgIsIn(Quartz.CVDisplayLinkCreateWithCGDisplays, 0)
        self.assertArgSizeInArg(Quartz.CVDisplayLinkCreateWithCGDisplays, 0, 1)
        self.assertArgIsOut(Quartz.CVDisplayLinkCreateWithCGDisplays, 2)
        self.assertArgIsCFRetained(Quartz.CVDisplayLinkCreateWithCGDisplays, 2)

        rv, link = Quartz.CVDisplayLinkCreateWithCGDisplays([mainID], 1, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link, Quartz.CVDisplayLinkRef)

        self.assertArgIsOut(Quartz.CVDisplayLinkCreateWithOpenGLDisplayMask, 1)
        self.assertArgIsCFRetained(Quartz.CVDisplayLinkCreateWithOpenGLDisplayMask, 1)
        rv, link2 = Quartz.CVDisplayLinkCreateWithOpenGLDisplayMask(
            Quartz.CGDisplayIDToOpenGLDisplayMask(mainID), None
        )
        self.assertEqual(rv, 0)
        self.assertIsInstance(link2, Quartz.CVDisplayLinkRef)

        self.assertArgIsOut(Quartz.CVDisplayLinkCreateWithCGDisplay, 1)
        self.assertArgIsCFRetained(Quartz.CVDisplayLinkCreateWithCGDisplay, 1)
        rv, link3 = Quartz.CVDisplayLinkCreateWithCGDisplay(mainID, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link3, Quartz.CVDisplayLinkRef)

        self.assertArgIsOut(Quartz.CVDisplayLinkCreateWithActiveCGDisplays, 0)
        self.assertArgIsCFRetained(Quartz.CVDisplayLinkCreateWithActiveCGDisplays, 0)
        rv, link4 = Quartz.CVDisplayLinkCreateWithActiveCGDisplays(None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link4, Quartz.CVDisplayLinkRef)

        rv = Quartz.CVDisplayLinkSetCurrentCGDisplay(link, mainID)
        self.assertEqual(rv, 0)

        Quartz.CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext

        v = Quartz.CVDisplayLinkGetCurrentCGDisplay(link)
        self.assertEqual(v, mainID)

        self.assertArgIsFunction(
            Quartz.CVDisplayLinkSetOutputCallback,
            1,
            b"i^{__CVDisplayLink=}n^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}N^{CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}Qo^Q^v",  # noqa: B950
            True,
        )
        self.assertArgHasType(Quartz.CVDisplayLinkSetOutputCallback, 2, b"^v")

        @objc.callbackFor(Quartz.CVDisplayLinkSetOutputCallback)
        def callback(dl, now, time, flags, oflags, ctx):
            pass

        Quartz.CVDisplayLinkSetOutputCallback(link2, callback, None)

        rv = Quartz.CVDisplayLinkStart(link4)
        self.assertIsInstance(rv, int)
        rv = Quartz.CVDisplayLinkStop(link4)
        self.assertIsInstance(rv, int)

        self.assertResultHasType(
            Quartz.CVDisplayLinkGetNominalOutputVideoRefreshPeriod,
            Quartz.CVTime.__typestr__,
        )
        v = Quartz.CVDisplayLinkGetNominalOutputVideoRefreshPeriod(link)
        self.assertIsInstance(v, Quartz.CVTime)

        self.assertResultHasType(
            Quartz.CVDisplayLinkGetOutputVideoLatency, Quartz.CVTime.__typestr__
        )
        v = Quartz.CVDisplayLinkGetOutputVideoLatency(link)
        self.assertIsInstance(v, Quartz.CVTime)

        self.assertResultHasType(
            Quartz.CVDisplayLinkGetActualOutputVideoRefreshPeriod, objc._C_DBL
        )
        v = Quartz.CVDisplayLinkGetActualOutputVideoRefreshPeriod(link)
        self.assertIsInstance(v, float)

        self.assertResultIsBOOL(Quartz.CVDisplayLinkIsRunning)
        v = Quartz.CVDisplayLinkIsRunning(link)
        self.assertIsInstance(v, bool)

        self.assertArgHasType(
            Quartz.CVDisplayLinkGetCurrentTime,
            1,
            b"o^" + Quartz.CVTimeStamp.__typestr__,
        )
        rv, v = Quartz.CVDisplayLinkGetCurrentTime(link, None)
        self.assertIsInstance(rv, int)
        self.assertIsInstance(v, Quartz.CVTimeStamp)
        ts = v

        self.assertArgHasType(
            Quartz.CVDisplayLinkTranslateTime, 1, b"n^" + Quartz.CVTimeStamp.__typestr__
        )
        self.assertArgHasType(
            Quartz.CVDisplayLinkTranslateTime, 2, b"o^" + Quartz.CVTimeStamp.__typestr__
        )
        rv, v = Quartz.CVDisplayLinkTranslateTime(link, ts, None)
        self.assertIsInstance(rv, int)
        self.assertIsInstance(v, Quartz.CVTimeStamp)

        v = Quartz.CVDisplayLinkRetain(link)
        self.assertTrue(v is link)
        Quartz.CVDisplayLinkRelease(v)
