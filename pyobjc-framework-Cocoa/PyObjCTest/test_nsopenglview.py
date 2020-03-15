import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSOpenGLView(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSOpenGLView.wantsBestResolutionOpenGLSurface)
        self.assertArgIsBOOL(
            AppKit.NSOpenGLView.setWantsBestResolutionOpenGLSurface_, 0
        )
