from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCARenderer(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.kCARendererColorSpace, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(Quartz.kCARendererMetalCommandQueue, str)

    def test_methods(self):
        self.assertArgHasType(
            Quartz.CARenderer.rendererWithCGLContext_options_,
            0,
            b"^{_CGLContextObject=}",
        )
        self.assertArgIsIn(Quartz.CARenderer.beginFrameAtTime_timeStamp_, 1)
