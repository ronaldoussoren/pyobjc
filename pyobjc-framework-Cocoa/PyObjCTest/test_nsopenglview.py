import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSOpenGLView(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSOpenGLView.wantsBestResolutionOpenGLSurface)
        self.assertArgIsBOOL(
            AppKit.NSOpenGLView.setWantsBestResolutionOpenGLSurface_, 0
        )
