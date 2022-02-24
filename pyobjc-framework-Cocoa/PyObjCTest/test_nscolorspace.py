import AppKit
from PyObjCTools.TestSupport import TestCase


class TestNSColorSpace(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSColorSpaceModel)

    def testConstants(self):
        self.assertEqual(AppKit.NSUnknownColorSpaceModel, -1)
        self.assertEqual(AppKit.NSGrayColorSpaceModel, 0)
        self.assertEqual(AppKit.NSRGBColorSpaceModel, 1)
        self.assertEqual(AppKit.NSCMYKColorSpaceModel, 2)
        self.assertEqual(AppKit.NSLABColorSpaceModel, 3)
        self.assertEqual(AppKit.NSDeviceNColorSpaceModel, 4)
        self.assertEqual(AppKit.NSIndexedColorSpaceModel, 5)
        self.assertEqual(AppKit.NSPatternColorSpaceModel, 6)

        self.assertEqual(AppKit.NSColorSpaceModelUnknown, -1)
        self.assertEqual(AppKit.NSColorSpaceModelGray, 0)
        self.assertEqual(AppKit.NSColorSpaceModelRGB, 1)
        self.assertEqual(AppKit.NSColorSpaceModelCMYK, 2)
        self.assertEqual(AppKit.NSColorSpaceModelLAB, 3)
        self.assertEqual(AppKit.NSColorSpaceModelDeviceN, 4)
        self.assertEqual(AppKit.NSColorSpaceModelIndexed, 5)
        self.assertEqual(AppKit.NSColorSpaceModelPatterned, 6)

    def testMethods(self):
        self.assertArgHasType(
            AppKit.NSColorSpace.initWithColorSyncProfile_, 0, b"^{OpaqueCMProfileRef=}"
        )
        self.assertResultHasType(
            AppKit.NSColorSpace.colorSyncProfile, b"^{OpaqueCMProfileRef=}"
        )
