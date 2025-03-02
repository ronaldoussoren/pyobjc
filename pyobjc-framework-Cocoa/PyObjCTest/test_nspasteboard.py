import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSPasteboardHelper(AppKit.NSObject):
    def writingOptionsForType_pasteboard_(self, t, p):
        return 1

    def readingOptionsForType_pasteboard_(self, t, p):
        return 1


class TestNSPasteboard(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(AppKit.NSPasteboardName, str)
        self.assertIsTypedEnum(AppKit.NSPasteboardReadingOptionKey, str)
        self.assertIsTypedEnum(AppKit.NSPasteboardType, str)
        self.assertIsTypedEnum(AppKit.NSPasteboardDetectionPattern, str)
        self.assertIsTypedEnum(AppKit.NSPasteboardMetadataType, str)

    def test_enum_types(self):
        self.assertIsEnumType(AppKit.NSPasteboardContentsOptions)
        self.assertIsEnumType(AppKit.NSPasteboardReadingOptions)
        self.assertIsEnumType(AppKit.NSPasteboardWritingOptions)
        self.assertIsEnumType(AppKit.NSPasteboardAccessBehavior)

    def testConstants(self):
        self.assertIsInstance(AppKit.NSStringPboardType, str)
        self.assertIsInstance(AppKit.NSFilenamesPboardType, str)
        self.assertIsInstance(AppKit.NSPostScriptPboardType, str)
        self.assertIsInstance(AppKit.NSTIFFPboardType, str)
        self.assertIsInstance(AppKit.NSRTFPboardType, str)
        self.assertIsInstance(AppKit.NSTabularTextPboardType, str)
        self.assertIsInstance(AppKit.NSFontPboardType, str)
        self.assertIsInstance(AppKit.NSRulerPboardType, str)
        self.assertIsInstance(AppKit.NSFileContentsPboardType, str)
        self.assertIsInstance(AppKit.NSColorPboardType, str)
        self.assertIsInstance(AppKit.NSRTFDPboardType, str)
        self.assertIsInstance(AppKit.NSHTMLPboardType, str)
        self.assertIsInstance(AppKit.NSPICTPboardType, str)
        self.assertIsInstance(AppKit.NSURLPboardType, str)
        self.assertIsInstance(AppKit.NSPDFPboardType, str)
        self.assertIsInstance(AppKit.NSVCardPboardType, str)
        self.assertIsInstance(AppKit.NSFilesPromisePboardType, str)
        self.assertIsInstance(AppKit.NSInkTextPboardType, str)
        self.assertIsInstance(AppKit.NSGeneralPboard, str)
        self.assertIsInstance(AppKit.NSFontPboard, str)
        self.assertIsInstance(AppKit.NSRulerPboard, str)
        self.assertIsInstance(AppKit.NSFindPboard, str)
        self.assertIsInstance(AppKit.NSDragPboard, str)

        self.assertEqual(AppKit.NSPasteboardAccessBehaviorDefault, 0)
        self.assertEqual(AppKit.NSPasteboardAccessBehaviorAsk, 1)
        self.assertEqual(AppKit.NSPasteboardAccessBehaviorAlwaysAllow, 2)
        self.assertEqual(AppKit.NSPasteboardAccessBehaviorAlwaysDeny, 3)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSMultipleTextSelectionPboardType, str)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertIsInstance(AppKit.NSPasteboardTypeTextFinderOptions, str)

    @min_os_level("15.4")
    def testConstants15_4(self):
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternProbableWebURL, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternProbableWebSearch, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternNumber, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternLink, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternPhoneNumber, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternEmailAddress, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternPostalAddress, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternCalendarEvent, str)
        self.assertIsInstance(
            AppKit.NSPasteboardDetectionPatternShipmentTrackingNumber, str
        )
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternFlightNumber, str)
        self.assertIsInstance(AppKit.NSPasteboardDetectionPatternMoneyAmount, str)
        self.assertIsInstance(AppKit.NSPasteboardMetadataTypeContentType, str)
        self.assertIsInstance(AppKit.NSPasteboardMetadataTypeImageProperties, str)

    def testFunctions(self):
        tp = v = AppKit.NSCreateFilenamePboardType("test/jpeg")
        self.assertIsInstance(v, str)

        v = AppKit.NSCreateFileContentsPboardType("test/jpeg")
        self.assertIsInstance(v, str)

        v = AppKit.NSGetFileType(tp)
        self.assertIsInstance(v, str)

        v = AppKit.NSGetFileTypes([tp])
        self.assertIsInstance(v, AppKit.NSArray)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSPasteboard.setData_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboard.setPropertyList_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboard.setString_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboard.writeFileContents_)
        self.assertResultIsBOOL(AppKit.NSPasteboard.writeFileWrapper_)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSPasteboardTypeString, str)
        self.assertIsInstance(AppKit.NSPasteboardTypePDF, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeTIFF, str)
        self.assertIsInstance(AppKit.NSPasteboardTypePNG, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeRTF, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeRTFD, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeHTML, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeTabularText, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeFont, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeRuler, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeColor, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeSound, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeMultipleTextSelection, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeFindPanelSearchOptions, str)

        self.assertIsInstance(AppKit.NSPasteboardURLReadingFileURLsOnlyKey, str)
        self.assertIsInstance(
            AppKit.NSPasteboardURLReadingContentsConformToTypesKey, str
        )

        self.assertEqual(AppKit.NSPasteboardWritingPromised, 1 << 9)

        self.assertEqual(AppKit.NSPasteboardReadingAsData, 0)
        self.assertEqual(AppKit.NSPasteboardReadingAsString, 1 << 0)
        self.assertEqual(AppKit.NSPasteboardReadingAsPropertyList, 1 << 1)
        self.assertEqual(AppKit.NSPasteboardReadingAsKeyedArchive, 1 << 2)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertEqual(AppKit.NSPasteboardContentsCurrentHostOnly, 1 << 0)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSPasteboardNameGeneral, str)
        self.assertIsInstance(AppKit.NSPasteboardNameFont, str)
        self.assertIsInstance(AppKit.NSPasteboardNameRuler, str)
        self.assertIsInstance(AppKit.NSPasteboardNameFind, str)
        self.assertIsInstance(AppKit.NSPasteboardNameDrag, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeURL, str)
        self.assertIsInstance(AppKit.NSPasteboardTypeFileURL, str)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AppKit.NSPasteboard.writeObjects_)
        self.assertResultIsBOOL(
            AppKit.NSPasteboard.canReadItemWithDataConformingToTypes_
        )
        self.assertResultIsBOOL(AppKit.NSPasteboard.canReadObjectForClasses_options_)

        self.assertResultIsBOOL(AppKit.NSPasteboard.setPropertyList_forType_)
        self.assertResultIsBOOL(AppKit.NSPasteboard.setString_forType_)

    @min_os_level("15.4")
    def testMethods15_4(self):
        self.assertResultIsBOOL(AppKit.NSPasteboardImageProperties.hasAlpha)

        self.assertArgIsBlock(
            AppKit.NSPasteboard.detectPatternsForPatterns_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AppKit.NSPasteboard.detectValuesForPatterns_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsBlock(
            AppKit.NSPasteboard.detectMetadataForTypes_completionHandler_, 1, b"v@@"
        )

    @min_sdk_level("10.6")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSPasteboardWriting")
        self.assertProtocolExists("NSPasteboardReading")

    @min_sdk_level("10.14")
    def testProtocolObjects10_14(self):
        self.assertProtocolExists("NSPasteboardTypeOwner")

    def testProtocols(self):
        self.assertResultHasType(
            TestNSPasteboardHelper.writingOptionsForType_pasteboard_, objc._C_NSUInteger
        )

        self.assertResultHasType(
            TestNSPasteboardHelper.readingOptionsForType_pasteboard_, objc._C_NSUInteger
        )
