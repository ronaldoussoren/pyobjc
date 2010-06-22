from PyObjCTools.TestSupport import *
from Quartz import *

class TestCVDisplayLink (TestCase):
    def testTypes(self):
        self.assertIsCFType(CVDisplayLinkRef)

    def testFunctions(self):
        self.assertIsInstance(CVDisplayLinkGetTypeID(), (int, long))

        mainID = CGMainDisplayID()

        self.assertArgIsIn(CVDisplayLinkCreateWithCGDisplays, 0)
        self.assertArgSizeInArg(CVDisplayLinkCreateWithCGDisplays, 0, 1)
        self.assertArgIsOut(CVDisplayLinkCreateWithCGDisplays, 2)
        self.assertArgIsCFRetained(CVDisplayLinkCreateWithCGDisplays, 2)

        rv, link = CVDisplayLinkCreateWithCGDisplays([mainID], 1, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link, CVDisplayLinkRef)

        self.assertArgIsOut(CVDisplayLinkCreateWithOpenGLDisplayMask, 1)
        self.assertArgIsCFRetained(CVDisplayLinkCreateWithOpenGLDisplayMask, 1)
        rv, link2 = CVDisplayLinkCreateWithOpenGLDisplayMask(CGDisplayIDToOpenGLDisplayMask(mainID), None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link2, CVDisplayLinkRef)

        self.assertArgIsOut(CVDisplayLinkCreateWithCGDisplay, 1)
        self.assertArgIsCFRetained(CVDisplayLinkCreateWithCGDisplay, 1)
        rv, link3 = CVDisplayLinkCreateWithCGDisplay(mainID, None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link3, CVDisplayLinkRef)

        self.assertArgIsOut(CVDisplayLinkCreateWithActiveCGDisplays, 0)
        self.assertArgIsCFRetained(CVDisplayLinkCreateWithActiveCGDisplays, 0)
        rv, link4 = CVDisplayLinkCreateWithActiveCGDisplays(None)
        self.assertEqual(rv, 0)
        self.assertIsInstance(link4, CVDisplayLinkRef)

        rv = CVDisplayLinkSetCurrentCGDisplay(link, mainID)
        self.assertEqual(rv, 0)

        # FIXME
        CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext

        v = CVDisplayLinkGetCurrentCGDisplay(link)
        self.assertEqual(v, mainID)

        self.assertArgIsFunction(CVDisplayLinkSetOutputCallback, 1, b'i@n^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}N^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}Qo^Q^v', True)
        self.assertArgHasType(CVDisplayLinkSetOutputCallback, 2, b'^v')

        @objc.callbackFor(CVDisplayLinkSetOutputCallback)
        def callback(dl, now, time, flags, oflags, ctx):
            pass
        CVDisplayLinkSetOutputCallback(link2, callback, None)

        rv = CVDisplayLinkStart(link4)
        self.assertIsInstance(rv, (int, long))
        rv = CVDisplayLinkStop(link4)
        self.assertIsInstance(rv, (int, long))

        self.assertResultHasType(CVDisplayLinkGetNominalOutputVideoRefreshPeriod, CVTime.__typestr__)
        v = CVDisplayLinkGetNominalOutputVideoRefreshPeriod(link)
        self.assertIsInstance(v, CVTime)

        self.assertResultHasType(CVDisplayLinkGetOutputVideoLatency, CVTime.__typestr__)
        v = CVDisplayLinkGetOutputVideoLatency(link)
        self.assertIsInstance(v, CVTime)

        self.assertResultHasType(CVDisplayLinkGetActualOutputVideoRefreshPeriod, objc._C_DBL)
        v = CVDisplayLinkGetActualOutputVideoRefreshPeriod(link)
        self.assertIsInstance(v, float)

        self.assertResultIsBOOL(CVDisplayLinkIsRunning)
        v = CVDisplayLinkIsRunning(link)
        self.assertIsInstance(v, bool)

        self.assertArgHasType(CVDisplayLinkGetCurrentTime, 1, b'o^' + CVTimeStamp.__typestr__)
        rv, v = CVDisplayLinkGetCurrentTime(link, None)
        self.assertIsInstance(rv, (int, long))
        self.assertIsInstance(v, CVTimeStamp)
        ts = v

        self.assertArgHasType(CVDisplayLinkTranslateTime, 1, b'n^' + CVTimeStamp.__typestr__)
        self.assertArgHasType(CVDisplayLinkTranslateTime, 2, b'o^' + CVTimeStamp.__typestr__)
        rv, v = CVDisplayLinkTranslateTime(link,  ts, None)
        self.assertIsInstance(rv, (int, long))
        self.assertIsInstance(v, CVTimeStamp)

        v = CVDisplayLinkRetain(link)
        self.assertTrue(v is link)
        CVDisplayLinkRelease(v)
        

if __name__ == "__main__":
    main()
