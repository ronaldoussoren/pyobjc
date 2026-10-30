from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCAConstraintLayoutManager(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Quartz.CAConstraintAttribute)
        self.assertEqual(Quartz.kCAConstraintMinX, 0)
        self.assertEqual(Quartz.kCAConstraintMidX, 1)
        self.assertEqual(Quartz.kCAConstraintMaxX, 2)
        self.assertEqual(Quartz.kCAConstraintWidth, 3)
        self.assertEqual(Quartz.kCAConstraintMinY, 4)
        self.assertEqual(Quartz.kCAConstraintMidY, 5)
        self.assertEqual(Quartz.kCAConstraintMaxY, 6)
        self.assertEqual(Quartz.kCAConstraintHeight, 7)
