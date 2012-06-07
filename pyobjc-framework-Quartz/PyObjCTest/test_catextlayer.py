
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

try:
    unicode
except NameError:
    unicode = str

class TestCATextLayer (TestCase):

    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(CATextLayer.isWrapped)
        self.assertArgIsBOOL(CATextLayer.setWrapped_, 0)

    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(kCATruncationNone, unicode)
        self.assertIsInstance(kCATruncationStart, unicode)
        self.assertIsInstance(kCATruncationEnd, unicode)
        self.assertIsInstance(kCATruncationMiddle, unicode)
        self.assertIsInstance(kCAAlignmentNatural, unicode)
        self.assertIsInstance(kCAAlignmentLeft, unicode)
        self.assertIsInstance(kCAAlignmentRight, unicode)
        self.assertIsInstance(kCAAlignmentCenter, unicode)
        self.assertIsInstance(kCAAlignmentJustified, unicode)


if __name__ == "__main__":
    main()
