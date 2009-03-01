
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGBase (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(CGFLOAT_MIN, float)
        self.failUnlessIsInstance(CGFLOAT_MAX, float)
        self.failUnlessIsInstance(CGFLOAT_IS_DOUBLE, (int, long))

if __name__ == "__main__":
    main()
