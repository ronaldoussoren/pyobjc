
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAMediaTimingFunction (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCAMediaTimingFunctionLinear, unicode)
        self.failUnlessIsInstance(kCAMediaTimingFunctionEaseIn, unicode)
        self.failUnlessIsInstance(kCAMediaTimingFunctionEaseOut, unicode)
        self.failUnlessIsInstance(kCAMediaTimingFunctionEaseInEaseOut, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(kCAMediaTimingFunctionDefault, unicode)

if __name__ == "__main__":
    main()
