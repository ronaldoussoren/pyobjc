import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSOpenGLLayer(TestCase):
    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(
            AppKit.NSOpenGLLayer.canDrawInOpenGLContext_pixelFormat_forLayerTime_displayTime_
        )
        self.assertArgIsIn(
            AppKit.NSOpenGLLayer.canDrawInOpenGLContext_pixelFormat_forLayerTime_displayTime_,
            3,
        )

        self.assertArgIsIn(
            AppKit.NSOpenGLLayer.drawInOpenGLContext_pixelFormat_forLayerTime_displayTime_,
            3,
        )
