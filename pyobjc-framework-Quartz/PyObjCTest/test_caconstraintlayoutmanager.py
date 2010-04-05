
from PyObjCTools.TestSupport import *
from Quartz.QuartzCore import *

class TestCAConstraintLayoutManager (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(kCAConstraintMinX, 0)
        self.assertEqual(kCAConstraintMidX, 1)
        self.assertEqual(kCAConstraintMaxX, 2)
        self.assertEqual(kCAConstraintWidth, 3)
        self.assertEqual(kCAConstraintMinY, 4)
        self.assertEqual(kCAConstraintMidY, 5)
        self.assertEqual(kCAConstraintMaxY, 6)
        self.assertEqual(kCAConstraintHeight, 7)

if __name__ == "__main__":
    main()
