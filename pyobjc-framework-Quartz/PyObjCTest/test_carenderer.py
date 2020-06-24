from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCARenderer(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertArgHasType(
            Quartz.CARenderer.rendererWithCGLContext_options_,
            0,
            b"^{_CGLContextObject=}",
        )
        self.assertArgIsIn(Quartz.CARenderer.beginFrameAtTime_timeStamp_, 1)

    @min_os_level("10.6")
    def testConstants(self):
        self.assertIsInstance(Quartz.kCARendererColorSpace, str)

    @min_os_level("10.14")
    def testConstants10_14(self):
        self.assertIsInstance(Quartz.kCARendererMetalCommandQueue, str)
