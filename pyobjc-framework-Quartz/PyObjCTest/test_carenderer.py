
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCARenderer (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertArgHasType(CARenderer.rendererWithCGLContext_options_, 0, b'^{_CGLContextObject=}')
        self.assertArgIsIn(CARenderer.beginFrameAtTime_timeStamp_, 1)

    @min_os_level('10.6')
    def testConstants(self):
        self.assertIsInstance(kCARendererColorSpace, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(kCARendererMetalCommandQueue, unicode)

if __name__ == "__main__":
    main()
