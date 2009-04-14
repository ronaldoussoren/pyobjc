
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAScrollLayer (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(kCAScrollNone, unicode)
        self.failUnlessIsInstance(kCAScrollVertically, unicode)
        self.failUnlessIsInstance(kCAScrollHorizontally, unicode)
        self.failUnlessIsInstance(kCAScrollBoth, unicode)


if __name__ == "__main__":
    main()
