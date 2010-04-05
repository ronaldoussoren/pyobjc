
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAOpenGLLayer (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(CAOpenGLLayer.isAsynchronous)
        self.assertArgIsBOOL(CAOpenGLLayer.setAsynchronous_, 0)

        self.assertResultIsBOOL(CAOpenGLLayer.canDrawInCGLContext_pixelFormat_forLayerTime_displayTime_)
        self.assertArgIsIn(CAOpenGLLayer.canDrawInCGLContext_pixelFormat_forLayerTime_displayTime_, 3)

        self.assertArgIsIn(CAOpenGLLayer.drawInCGLContext_pixelFormat_forLayerTime_displayTime_, 3)

if __name__ == "__main__":
    main()
