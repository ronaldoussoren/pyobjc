from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


import MetalKit
import Quartz


class TestMTKViewHelper(MetalKit.NSObject):
    def mtkView_drawableSizeWillChange_(self, a, b):
        pass


class TestMTKView(TestCase):
    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(MetalKit.MTKView.framebufferOnly)
        self.assertArgIsBOOL(MetalKit.MTKView.setFramebufferOnly_, 0)

        self.assertResultIsBOOL(MetalKit.MTKView.presentsWithTransaction)
        self.assertArgIsBOOL(MetalKit.MTKView.setPresentsWithTransaction_, 0)

        self.assertResultIsBOOL(MetalKit.MTKView.enableSetNeedsDisplay)
        self.assertArgIsBOOL(MetalKit.MTKView.setEnableSetNeedsDisplay_, 0)

        self.assertResultIsBOOL(MetalKit.MTKView.autoResizeDrawable)
        self.assertArgIsBOOL(MetalKit.MTKView.setAutoResizeDrawable_, 0)

        self.assertResultIsBOOL(MetalKit.MTKView.isPaused)
        self.assertArgIsBOOL(MetalKit.MTKView.setPaused_, 0)

    @min_sdk_level("10.15")
    def test_protocols(self):
        objc.protocolNamed("MTKViewDelegate")

    def test_methods(self):
        self.assertArgHasType(
            TestMTKViewHelper.mtkView_drawableSizeWillChange_,
            1,
            Quartz.CGSize.__typestr__,
        )
