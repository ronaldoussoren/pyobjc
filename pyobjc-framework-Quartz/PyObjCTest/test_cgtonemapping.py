from PyObjCTools.TestSupport import TestCase, min_os_level
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

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(Quartz.kCGPreferredDynamicRange, str)
        self.assertIsInstance(Quartz.kCGDynamicRangeHigh, str)
        self.assertIsInstance(Quartz.kCGDynamicRangeConstrained, str)
        self.assertIsInstance(Quartz.kCGDynamicRangeStandard, str)
        self.assertIsInstance(Quartz.kCGContentAverageLightLevel, str)
        self.assertIsInstance(Quartz.kCGContentAverageLightLevelNits, str)

    def test_structs(self):
        v = Quartz.CGContentToneMappingInfo()
        self.assertEqual(v.method, 0)
        self.assertIs(v.options, None)
