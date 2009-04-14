
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCATextLayer (TestCase):

    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(CATextLayer.isWrapped)
        self.failUnlessArgIsBOOL(CATextLayer.setWrapped_, 0)

    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCATruncationNone, unicode)
        self.failUnlessIsInstance(kCATruncationStart, unicode)
        self.failUnlessIsInstance(kCATruncationEnd, unicode)
        self.failUnlessIsInstance(kCATruncationMiddle, unicode)
        self.failUnlessIsInstance(kCAAlignmentNatural, unicode)
        self.failUnlessIsInstance(kCAAlignmentLeft, unicode)
        self.failUnlessIsInstance(kCAAlignmentRight, unicode)
        self.failUnlessIsInstance(kCAAlignmentCenter, unicode)
        self.failUnlessIsInstance(kCAAlignmentJustified, unicode)


if __name__ == "__main__":
    main()
