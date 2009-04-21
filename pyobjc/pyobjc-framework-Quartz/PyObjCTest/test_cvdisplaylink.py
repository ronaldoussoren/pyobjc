from PyObjCTools.TestSupport import *
from Quartz.CoreVideo import *
from Quartz import *

class TestCVDisplayLink (TestCase):
    def testTypes(self):
        self.failUnlessIsCFType(CVDisplayLinkRef)

    def testFunctions(self):
        self.failUnlessIsInstance(CVDisplayLinkGetTypeID(), (int, long))

        mainID = CGMainDisplayID()

        self.failUnlessArgIsIn(CVDisplayLinkCreateWithCGDisplays, 0)
        self.failUnlessArgSizeInArg(CVDisplayLinkCreateWithCGDisplays, 0, 1)
        self.failUnlessArgIsOut(CVDisplayLinkCreateWithCGDisplays, 2)
        self.failUnlessArgIsCFRetained(CVDisplayLinkCreateWithCGDisplays, 2)

        rv, link = CVDisplayLinkCreateWithCGDisplays([mainID], 1, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(link, CVDisplayLinkRef)

        self.failUnlessArgIsOut(CVDisplayLinkCreateWithOpenGLDisplayMask, 1)
        self.failUnlessArgIsCFRetained(CVDisplayLinkCreateWithOpenGLDisplayMask, 1)
        rv, link2 = CVDisplayLinkCreateWithOpenGLDisplayMask(CGDisplayIDToOpenGLDisplayMask(mainID), None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(link2, CVDisplayLinkRef)

        self.failUnlessArgIsOut(CVDisplayLinkCreateWithCGDisplay, 1)
        self.failUnlessArgIsCFRetained(CVDisplayLinkCreateWithCGDisplay, 1)
        rv, link3 = CVDisplayLinkCreateWithCGDisplay(mainID, None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(link3, CVDisplayLinkRef)

        self.failUnlessArgIsOut(CVDisplayLinkCreateWithActiveCGDisplays, 0)
        self.failUnlessArgIsCFRetained(CVDisplayLinkCreateWithActiveCGDisplays, 0)
        rv, link4 = CVDisplayLinkCreateWithActiveCGDisplays(None)
        self.failUnlessEqual(rv, 0)
        self.failUnlessIsInstance(link4, CVDisplayLinkRef)

        rv = CVDisplayLinkSetCurrentCGDisplay(link, mainID)
        self.failUnlessEqual(rv, 0)

        # FIXME
        CVDisplayLinkSetCurrentCGDisplayFromOpenGLContext

        v = CVDisplayLinkGetCurrentCGDisplay(link)
        self.failUnlessEqual(v, mainID)

        self.failUnlessArgIsFunction(CVDisplayLinkSetOutputCallback, 1, 'i@n^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}N^{_CVTimeStamp=IiqQdq{CVSMPTETime=ssIIIssss}QQ}Qo^Q^v', True)
        self.failUnlessArgHasType(CVDisplayLinkSetOutputCallback, 2, '^v')

        @objc.callbackFor(CVDisplayLinkSetOutputCallback)
        def callback(dl, now, time, flags, oflags, ctx):
            pass
        CVDisplayLinkSetOutputCallback(link2, callback, None)

        rv = CVDisplayLinkStart(link4)
        self.failUnlessIsInstance(rv, (int, long))
        rv = CVDisplayLinkStop(link4)
        self.failUnlessIsInstance(rv, (int, long))

        self.failUnlessResultHasType(CVDisplayLinkGetNominalOutputVideoRefreshPeriod, CVTime.__typestr__)
        v = CVDisplayLinkGetNominalOutputVideoRefreshPeriod(link)
        self.failUnlessIsInstance(v, CVTime)

        self.failUnlessResultHasType(CVDisplayLinkGetOutputVideoLatency, CVTime.__typestr__)
        v = CVDisplayLinkGetOutputVideoLatency(link)
        self.failUnlessIsInstance(v, CVTime)

        self.failUnlessResultHasType(CVDisplayLinkGetActualOutputVideoRefreshPeriod, objc._C_DBL)
        v = CVDisplayLinkGetActualOutputVideoRefreshPeriod(link)
        self.failUnlessIsInstance(v, float)

        self.failUnlessResultIsBOOL(CVDisplayLinkIsRunning)
        v = CVDisplayLinkIsRunning(link)
        self.failUnlessIsInstance(v, bool)

        self.failUnlessArgHasType(CVDisplayLinkGetCurrentTime, 1, 'o^' + CVTimeStamp.__typestr__)
        rv, v = CVDisplayLinkGetCurrentTime(link, None)
        self.failUnlessIsInstance(rv, (int, long))
        self.failUnlessIsInstance(v, CVTimeStamp)
        ts = v

        self.failUnlessArgHasType(CVDisplayLinkTranslateTime, 1, 'n^' + CVTimeStamp.__typestr__)
        self.failUnlessArgHasType(CVDisplayLinkTranslateTime, 2, 'o^' + CVTimeStamp.__typestr__)
        rv, v = CVDisplayLinkTranslateTime(link,  ts, None)
        self.failUnlessIsInstance(rv, (int, long))
        self.failUnlessIsInstance(v, CVTimeStamp)

        v = CVDisplayLinkRetain(link)
        self.failUnless(v is link)
        CVDisplayLinkRelease(v)
        

if __name__ == "__main__":
    main()
