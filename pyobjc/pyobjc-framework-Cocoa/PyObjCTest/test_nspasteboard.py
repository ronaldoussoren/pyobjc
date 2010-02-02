
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPasteboard (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSStringPboardType, unicode)
        self.assertIsInstance(NSFilenamesPboardType, unicode)
        self.assertIsInstance(NSPostScriptPboardType, unicode)
        self.assertIsInstance(NSTIFFPboardType, unicode)
        self.assertIsInstance(NSRTFPboardType, unicode)
        self.assertIsInstance(NSTabularTextPboardType, unicode)
        self.assertIsInstance(NSFontPboardType, unicode)
        self.assertIsInstance(NSRulerPboardType, unicode)
        self.assertIsInstance(NSFileContentsPboardType, unicode)
        self.assertIsInstance(NSColorPboardType, unicode)
        self.assertIsInstance(NSRTFDPboardType, unicode)
        self.assertIsInstance(NSHTMLPboardType, unicode)
        self.assertIsInstance(NSPICTPboardType, unicode)
        self.assertIsInstance(NSURLPboardType, unicode)
        self.assertIsInstance(NSPDFPboardType, unicode)
        self.assertIsInstance(NSVCardPboardType, unicode)
        self.assertIsInstance(NSFilesPromisePboardType, unicode)
        self.assertIsInstance(NSInkTextPboardType, unicode)
        self.assertIsInstance(NSGeneralPboard, unicode)
        self.assertIsInstance(NSFontPboard, unicode)
        self.assertIsInstance(NSRulerPboard, unicode)
        self.assertIsInstance(NSFindPboard, unicode)
        self.assertIsInstance(NSDragPboard, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.assertIsInstance(NSMultipleTextSelectionPboardType, unicode)

    def testFunctions(self):
        tp = v = NSCreateFilenamePboardType("test/jpeg")
        self.assertIsInstance(v, unicode)

        v = NSCreateFileContentsPboardType("test/jpeg")
        self.assertIsInstance(v, unicode)

        v = NSGetFileType(tp)
        self.assertIsInstance(v, unicode)

        v = NSGetFileTypes([tp])
        self.assertIsInstance(v, NSArray)
    
    def testMethods(self):
        self.assertResultIsBOOL(NSPasteboard.setData_forType_)
        self.assertResultIsBOOL(NSPasteboard.setPropertyList_forType_)
        self.assertResultIsBOOL(NSPasteboard.setString_forType_)
        self.assertResultIsBOOL(NSPasteboard.writeFileContents_)
        self.assertResultIsBOOL(NSPasteboard.writeFileWrapper_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSPasteboardTypeString, unicode)
        self.assertIsInstance(NSPasteboardTypePDF, unicode)
        self.assertIsInstance(NSPasteboardTypeTIFF, unicode)
        self.assertIsInstance(NSPasteboardTypePNG, unicode)
        self.assertIsInstance(NSPasteboardTypeRTF, unicode)
        self.assertIsInstance(NSPasteboardTypeRTFD, unicode)
        self.assertIsInstance(NSPasteboardTypeHTML, unicode)
        self.assertIsInstance(NSPasteboardTypeTabularText, unicode)
        self.assertIsInstance(NSPasteboardTypeFont, unicode)
        self.assertIsInstance(NSPasteboardTypeRuler, unicode)
        self.assertIsInstance(NSPasteboardTypeColor, unicode)
        self.assertIsInstance(NSPasteboardTypeSound, unicode)
        self.assertIsInstance(NSPasteboardTypeMultipleTextSelection, unicode)
        self.assertIsInstance(NSPasteboardTypeFindPanelSearchOptions, unicode)

        self.assertIsInstance(NSPasteboardURLReadingFileURLsOnlyKey, unicode)
        self.assertIsInstance(NSPasteboardURLReadingContentsConformToTypesKey, unicode)

        self.assertEqual(NSPasteboardWritingPromised, 1<<9)

        self.assertEqual(NSPasteboardReadingAsData, 0)
        self.assertEqual(NSPasteboardReadingAsString, 1<<0)
        self.assertEqual(NSPasteboardReadingAsPropertyList, 1<<1)
        self.assertEqual(NSPasteboardReadingAsKeyedArchive, 1<<2)


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultIsBOOL(NSPasteboard.writeObjects_)
        self.assertResultIsBOOL(NSPasteboard.canReadItemWithDataConformingToTypes_)
        self.assertResultIsBOOL(NSPasteboard.canReadObjectForClasses_options_)

        self.assertResultIsBOOL(NSPasteboard.setPropertyList_forType_)
        self.assertResultIsBOOL(NSPasteboard.setString_forType_)

if __name__ == "__main__":
    main()
