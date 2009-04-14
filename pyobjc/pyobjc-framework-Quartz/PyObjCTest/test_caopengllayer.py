
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAOpenGLLayer (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(CAOpenGLLayer.isAsynchronous)
        self.failUnlessArgIsBOOL(CAOpenGLLayer.setAsynchronous_, 0)

        self.failUnlessResultIsBOOL(CAOpenGLLayer.canDrawInCGLContext_pixelFormat_forLayerTime_displayTime_)
        self.failUnlessArgIsIn(CAOpenGLLayer.canDrawInCGLContext_pixelFormat_forLayerTime_displayTime_, 3)

        self.failUnlessArgIsIn(CAOpenGLLayer.drawInCGLContext_pixelFormat_forLayerTime_displayTime_, 3)

if __name__ == "__main__":
    main()
