from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCIContext (TestCase):
    def testConstants(self):
        self.assertIsInstance(kCIContextOutputColorSpace, unicode)
        self.assertIsInstance(kCIContextWorkingColorSpace, unicode)
        self.assertIsInstance(kCIContextUseSoftwareRenderer, unicode)


    def testMethods(self):
        self.assertArgIsOut(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)
        self.assertArgIsVariableSize(CIContext.render_toBitmap_rowBytes_bounds_format_colorSpace_, 1)

if __name__ == "__main__":
    main()
