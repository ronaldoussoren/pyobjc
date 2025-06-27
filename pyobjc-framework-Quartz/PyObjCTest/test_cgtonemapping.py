from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCGToneMapping(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Quartz.CGToneMapping)
        self.assertEqual(Quartz.kCGToneMappingDefault, 0)
        self.assertEqual(Quartz.kCGToneMappingImageSpecificLumaScaling, 1)
        self.assertEqual(Quartz.kCGToneMappingReferenceWhiteBased, 2)
        self.assertEqual(Quartz.kCGToneMappingITURecommended, 3)
        self.assertEqual(Quartz.kCGToneMappingEXRGamma, 4)
        self.assertEqual(Quartz.kCGToneMappingNone, 5)
