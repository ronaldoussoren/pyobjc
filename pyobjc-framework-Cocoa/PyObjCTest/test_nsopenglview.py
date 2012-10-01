from PyObjCTools.TestSupport import *

import AppKit

class TestNSOpenGLView (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSOpenGLView.wantsBestResolutionOpenGLSurface)
        self.assertArgIsBOOL(AppKit.NSOpenGLView.setWantsBestResolutionOpenGLSurface_, 0)

if __name__ == "__main__":
    main()
