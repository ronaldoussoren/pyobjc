
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAConstraintLayoutManager (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kCAConstraintMinX, 0)
        self.failUnlessEqual(kCAConstraintMidX, 1)
        self.failUnlessEqual(kCAConstraintMaxX, 2)
        self.failUnlessEqual(kCAConstraintWidth, 3)
        self.failUnlessEqual(kCAConstraintMinY, 4)
        self.failUnlessEqual(kCAConstraintMidY, 5)
        self.failUnlessEqual(kCAConstraintMaxY, 6)
        self.failUnlessEqual(kCAConstraintHeight, 7)

if __name__ == "__main__":
    main()
