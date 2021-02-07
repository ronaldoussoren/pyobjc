import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCVPixelBufferIOSurface(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey, str
        )
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey, str
        )
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey, str
        )

    @min_os_level("10.6")
    def testFunctions10_6(self):
        Quartz.CVPixelBufferGetIOSurface

        self.assertArgIsCFRetained(Quartz.CVPixelBufferCreateWithIOSurface, 3)
        self.assertArgIsOut(Quartz.CVPixelBufferCreateWithIOSurface, 3)
