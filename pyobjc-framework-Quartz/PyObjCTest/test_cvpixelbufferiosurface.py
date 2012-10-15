from PyObjCTools.TestSupport import *

import Quartz

try:
    unicode
except NameError:
    unicode = str

class TestCVPixelBufferIOSurface (TestCase):

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCVPixelBufferIOSurfaceOpenGLTextureCompatibilityKey, unicode)
        self.assertIsInstance(Quartz.kCVPixelBufferIOSurfaceOpenGLFBOCompatibilityKey, unicode)
        self.assertIsInstance(Quartz.kCVPixelBufferIOSurfaceCoreAnimationCompatibilityKey, unicode)

    @min_os_level('10.6')
    def testFunctions10_6(self):
        Quartz.CVPixelBufferGetIOSurface

        self.assertArgIsCFRetained(Quartz.CVPixelBufferCreateWithIOSurface, 3)
        self.assertArgIsOut(Quartz.CVPixelBufferCreateWithIOSurface, 3)

if __name__ == "__main__":
    main()
