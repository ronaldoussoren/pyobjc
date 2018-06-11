from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSAppearance (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertResultIsBOOL(NSAppearance.allowsVibrancy)

    @min_os_level('10.9')
    def testConstants10_9(self):
        self.assertIsInstance(NSAppearanceNameAqua, unicode)
        self.assertIsInstance(NSAppearanceNameLightContent, unicode)

    @min_os_level('10.10')
    def testConstants10_10(self):
         self.assertIsInstance(NSAppearanceNameVibrantDark, unicode)
         self.assertIsInstance(NSAppearanceNameVibrantLight, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(NSAppearanceNameDarkAqua, unicode)

        self.assertIsInstance(NSAppearanceNameAccessibilityHighContrastAqua, unicode)
        self.assertIsInstance(NSAppearanceNameAccessibilityHighContrastDarkAqua, unicode)
        self.assertIsInstance(NSAppearanceNameAccessibilityHighContrastVibrantLight, unicode)
        self.assertIsInstance(NSAppearanceNameAccessibilityHighContrastVibrantDark, unicode)

    @min_os_level('10.9')
    def testProtocols(self):
        objc.protocolNamed('NSAppearanceCustomization')



if __name__ == "__main__":
    main()
