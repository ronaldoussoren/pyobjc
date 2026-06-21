import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestNSAppearance(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(AppKit.NSAppearanceName, str)

    @min_os_level("10.9")
    def test_constants10_9(self):
        self.assertIsInstance(AppKit.NSAppearanceNameAqua, str)
        self.assertIsInstance(AppKit.NSAppearanceNameLightContent, str)

    @min_os_level("10.10")
    def test_constants10_10(self):
        self.assertIsInstance(AppKit.NSAppearanceNameVibrantDark, str)
        self.assertIsInstance(AppKit.NSAppearanceNameVibrantLight, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(AppKit.NSAppearanceNameDarkAqua, str)

        self.assertIsInstance(AppKit.NSAppearanceNameAccessibilityHighContrastAqua, str)
        self.assertIsInstance(
            AppKit.NSAppearanceNameAccessibilityHighContrastDarkAqua, str
        )
        self.assertIsInstance(
            AppKit.NSAppearanceNameAccessibilityHighContrastVibrantLight, str
        )
        self.assertIsInstance(
            AppKit.NSAppearanceNameAccessibilityHighContrastVibrantDark, str
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(AppKit.NSAppearance.allowsVibrancy)

    @min_os_level("11.0")
    def test_methods11_0(self):
        self.assertArgIsBlock(
            AppKit.NSAppearance.performAsCurrentDrawingAppearance_, 0, b"v"
        )

    @min_os_level("10.9")
    def test_protocols(self):
        self.assertProtocolExists("NSAppearanceCustomization", AppKit)
