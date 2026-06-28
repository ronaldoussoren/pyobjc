import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSOpenGLLayer(TestCase):
    def test_methods(self):
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
