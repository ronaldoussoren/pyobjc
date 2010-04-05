
from PyObjCTools.TestSupport import *
from Quartz.CoreGraphics import *

class TestCGBase (TestCase):
    def testConstants(self):
        self.assertIsInstance(CGFLOAT_MIN, float)
        self.assertIsInstance(CGFLOAT_MAX, float)
        self.assertIsInstance(CGFLOAT_IS_DOUBLE, (int, long))

if __name__ == "__main__":
    main()
