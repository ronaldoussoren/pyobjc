from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAConstraintLayoutManager(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertEqual(Quartz.kCAConstraintMinX, 0)
        self.assertEqual(Quartz.kCAConstraintMidX, 1)
        self.assertEqual(Quartz.kCAConstraintMaxX, 2)
        self.assertEqual(Quartz.kCAConstraintWidth, 3)
        self.assertEqual(Quartz.kCAConstraintMinY, 4)
        self.assertEqual(Quartz.kCAConstraintMidY, 5)
        self.assertEqual(Quartz.kCAConstraintMaxY, 6)
        self.assertEqual(Quartz.kCAConstraintHeight, 7)
