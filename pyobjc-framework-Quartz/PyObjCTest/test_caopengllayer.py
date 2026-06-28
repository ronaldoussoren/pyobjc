from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAOpenGLLayer(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CAOpenGLLayer.isAsynchronous)
        self.assertArgIsBOOL(Quartz.CAOpenGLLayer.setAsynchronous_, 0)

        self.assertResultIsBOOL(
            Quartz.CAOpenGLLayer.canDrawInCGLContext_pixelFormat_forLayerTime_displayTime_
        )
        self.assertArgIsIn(
            Quartz.CAOpenGLLayer.canDrawInCGLContext_pixelFormat_forLayerTime_displayTime_,
            3,
        )

        self.assertArgIsIn(
            Quartz.CAOpenGLLayer.drawInCGLContext_pixelFormat_forLayerTime_displayTime_,
            3,
        )

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(Quartz.CAOpenGLLayer.wantsExtendedDynamicRangeContent)
        self.assertArgIsBOOL(
            Quartz.CAOpenGLLayer.setWantsExtendedDynamicRangeContent_, 0
        )
