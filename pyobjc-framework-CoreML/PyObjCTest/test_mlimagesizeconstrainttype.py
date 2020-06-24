from PyObjCTools.TestSupport import TestCase
import CoreML


class TestMLImageSizeConstraintType(TestCase):
    def test_constants(self):
        self.assertEqual(CoreML.MLImageSizeConstraintTypeUnspecified, 0)
        self.assertEqual(CoreML.MLImageSizeConstraintTypeEnumerated, 2)
        self.assertEqual(CoreML.MLImageSizeConstraintTypeRange, 3)
