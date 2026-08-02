from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCIVector(TestCase):
    def test_methods(self):
        self.assertArgIsIn(Quartz.CIVector.vectorWithValues_count_, 0)
        self.assertArgSizeInArg(Quartz.CIVector.vectorWithValues_count_, 0, 1)
        self.assertArgIsIn(Quartz.CIVector.initWithValues_count_, 0)
        self.assertArgSizeInArg(Quartz.CIVector.initWithValues_count_, 0, 1)

    def test_convenience(self):
        v = Quartz.CIVector.vectorWithValues_count_([1, 2, 3, 4], 4)
        self.assertEqual(v.valueAtIndex_(2), 3.0)
        self.assertEqual(v[2], 3.0)
        self.assertEqual(v[3], 4.0)
        self.assertEqual(v[-1], 4.0)
        self.assertEqual(v[1:3], (2.0, 3.0))
        self.assertEqual(v[3:1], ())
        self.assertEqual(v[1:4:2], (2.0, 4.0))
        with self.assertRaisesRegex(IndexError, "4"):
            print(v[4])
        with self.assertRaisesRegex(IndexError, "-8"):
            print(v[-8])
