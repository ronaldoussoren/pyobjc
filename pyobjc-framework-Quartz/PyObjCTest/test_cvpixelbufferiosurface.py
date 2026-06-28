import Quartz
from PyObjCTools.TestSupport import TestCase


class TestCVPixelBufferIOSurface(TestCase):
    def test_constants(self):
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey, str
        )
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey, str
        )
        self.assertIsInstance(
            Quartz.kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey, str
        )

    def test_functions(self):
        Quartz.CVPixelBufferGetIOSurface

        self.assertArgIsCFRetained(Quartz.CVPixelBufferCreateWithIOSurface, 3)
        self.assertArgIsOut(Quartz.CVPixelBufferCreateWithIOSurface, 3)
