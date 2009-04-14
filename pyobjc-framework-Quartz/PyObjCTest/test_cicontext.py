from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIContext (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(kCIContextOutputColorSpace, unicode)
        self.failUnlessIsInstance(kCIContextWorkingColorSpace, unicode)
        self.failUnlessIsInstance(kCIContextUseSoftwareRenderer, unicode)


    def testMethods(self):
        self.failUnlessArgIsOut(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)
        self.failUnlessArgIsVariableSize(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)

if __name__ == "__main__":
    main()
