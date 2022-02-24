import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestNSAccessibilityCustomRotor(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSAccessibilityCustomRotorSearchDirection)
        self.assertIsEnumType(AppKit.NSAccessibilityCustomRotorType)

    def testConstants(self):
        self.assertEqual(AppKit.NSAccessibilityCustomRotorSearchDirectionPrevious, 0)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorSearchDirectionNext, 1)

        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeCustom, 0)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeAny, 1)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeAnnotation, 2)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeBoldText, 3)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeading, 4)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeadingLevel1, 5)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeadingLevel2, 6)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeadingLevel3, 7)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeadingLevel4, 8)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeadingLevel5, 9)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeHeadingLevel6, 10)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeImage, 11)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeItalicText, 12)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeLandmark, 13)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeLink, 14)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeList, 15)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeMisspelledWord, 16)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeTable, 17)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeTextField, 18)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeUnderlinedText, 19)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeVisitedLink, 20)
        self.assertEqual(AppKit.NSAccessibilityCustomRotorTypeAudiograph, 21)

    @min_sdk_level("10.13")
    def testProtocols(self):
        objc.protocolNamed("NSAccessibilityCustomRotorItemSearchDelegate")
