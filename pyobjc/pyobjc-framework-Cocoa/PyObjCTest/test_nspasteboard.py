
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

if __name__ == "__main__":
    main()
