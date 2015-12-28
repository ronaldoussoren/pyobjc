from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCIContext (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIContextOutputColorSpace, unicode)
        self.assertIsInstance(kCIContextWorkingColorSpace, unicode)
        self.assertIsInstance(kCIContextUseSoftwareRenderer, unicode)

        self.assertIsInstance(kCIContextWorkingFormat, unicode)

    @min_os_level('10.11')
    def testConstants10_11(self):
        self.assertIsInstance(kCIContextHighQualityDownsample, unicode)


    def testMethods(self):
        self.assertArgIsOut(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)
        self.assertArgIsVariableSize(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)

if __name__ == "__main__":
    main()
