import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSLevelIndicator(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSLevelIndicatorPlaceholderVisibility)

    def test_constants(self):
        self.assertEqual(AppKit.NSLevelIndicatorPlaceholderVisibilityAutomatic, 0)
        self.assertEqual(AppKit.NSLevelIndicatorPlaceholderVisibilityAlways, 1)
        self.assertEqual(AppKit.NSLevelIndicatorPlaceholderVisibilityWhileEditing, 2)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertResultIsBOOL(AppKit.NSLevelIndicator.drawsTieredCapacityLevels)
        self.assertArgIsBOOL(AppKit.NSLevelIndicator.setDrawsTieredCapacityLevels_, 0)

        self.assertResultIsBOOL(AppKit.NSLevelIndicator.isEditable)
        self.assertArgIsBOOL(AppKit.NSLevelIndicator.setEditable_, 0)
