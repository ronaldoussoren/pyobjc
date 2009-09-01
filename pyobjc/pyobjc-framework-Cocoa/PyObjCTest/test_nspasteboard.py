
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSPasteboard (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSStringPboardType, unicode)
        self.failUnlessIsInstance(NSFilenamesPboardType, unicode)
        self.failUnlessIsInstance(NSPostScriptPboardType, unicode)
        self.failUnlessIsInstance(NSTIFFPboardType, unicode)
        self.failUnlessIsInstance(NSRTFPboardType, unicode)
        self.failUnlessIsInstance(NSTabularTextPboardType, unicode)
        self.failUnlessIsInstance(NSFontPboardType, unicode)
        self.failUnlessIsInstance(NSRulerPboardType, unicode)
        self.failUnlessIsInstance(NSFileContentsPboardType, unicode)
        self.failUnlessIsInstance(NSColorPboardType, unicode)
        self.failUnlessIsInstance(NSRTFDPboardType, unicode)
        self.failUnlessIsInstance(NSHTMLPboardType, unicode)
        self.failUnlessIsInstance(NSPICTPboardType, unicode)
        self.failUnlessIsInstance(NSURLPboardType, unicode)
        self.failUnlessIsInstance(NSPDFPboardType, unicode)
        self.failUnlessIsInstance(NSVCardPboardType, unicode)
        self.failUnlessIsInstance(NSFilesPromisePboardType, unicode)
        self.failUnlessIsInstance(NSInkTextPboardType, unicode)
        self.failUnlessIsInstance(NSGeneralPboard, unicode)
        self.failUnlessIsInstance(NSFontPboard, unicode)
        self.failUnlessIsInstance(NSRulerPboard, unicode)
        self.failUnlessIsInstance(NSFindPboard, unicode)
        self.failUnlessIsInstance(NSDragPboard, unicode)

    @min_os_level('10.5')
    def testConstants10_5(self):
        self.failUnlessIsInstance(NSMultipleTextSelectionPboardType, unicode)

    def testFunctions(self):
        tp = v = NSCreateFilenamePboardType("test/jpeg")
        self.failUnlessIsInstance(v, unicode)

        v = NSCreateFileContentsPboardType("test/jpeg")
        self.failUnlessIsInstance(v, unicode)

        v = NSGetFileType(tp)
        self.failUnlessIsInstance(v, unicode)

        v = NSGetFileTypes([tp])
        self.failUnlessIsInstance(v, NSArray)
    
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSPasteboard.setData_forType_)
        self.failUnlessResultIsBOOL(NSPasteboard.setPropertyList_forType_)
        self.failUnlessResultIsBOOL(NSPasteboard.setString_forType_)
        self.failUnlessResultIsBOOL(NSPasteboard.writeFileContents_)
        self.failUnlessResultIsBOOL(NSPasteboard.writeFileWrapper_)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.failUnlessIsInstance(NSPasteboardTypeString, unicode)
        self.failUnlessIsInstance(NSPasteboardTypePDF, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeTIFF, unicode)
        self.failUnlessIsInstance(NSPasteboardTypePNG, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeRTF, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeRTFD, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeHTML, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeTabularText, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeFont, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeRuler, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeColor, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeSound, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeMultipleTextSelection, unicode)
        self.failUnlessIsInstance(NSPasteboardTypeFindPanelSearchOptions, unicode)

        self.failUnlessIsInstance(NSPasteboardURLReadingFileURLsOnlyKey, unicode)
        self.failUnlessIsInstance(NSPasteboardURLReadingContentsConformToTypesKey, unicode)

        self.failUnlessEqual(NSPasteboardWritingPromised, 1<<9)

        self.failUnlessEqual(NSPasteboardReadingAsData, 0)
        self.failUnlessEqual(NSPasteboardReadingAsString, 1<<0)
        self.failUnlessEqual(NSPasteboardReadingAsPropertyList, 1<<1)
        self.failUnlessEqual(NSPasteboardReadingAsKeyedArchive, 1<<2)


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.failUnlessResultIsBOOL(NSPasteboard.writeObjects_)
        self.failUnlessResultIsBOOL(NSPasteboard.canReadItemWithDataConformingToTypes_)
        self.failUnlessResultIsBOOL(NSPasteboard.canReadObjectForClasses_options_)

        self.failUnlessResultIsBOOL(NSPasteboard.setPropertyList_forType_)
        self.failUnlessResultIsBOOL(NSPasteboard.setString_forType_)

if __name__ == "__main__":
    main()
