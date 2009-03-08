
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSErrors (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(NSTextLineTooLongException, unicode)
        self.failUnlessIsInstance(NSTextNoSelectionException, unicode)
        self.failUnlessIsInstance(NSWordTablesWriteException, unicode)
        self.failUnlessIsInstance(NSWordTablesReadException, unicode)
        self.failUnlessIsInstance(NSTextReadException, unicode)
        self.failUnlessIsInstance(NSTextWriteException, unicode)   
        self.failUnlessIsInstance(NSPasteboardCommunicationException, unicode)
        self.failUnlessIsInstance(NSPrintingCommunicationException, unicode)
        self.failUnlessIsInstance(NSAbortModalException, unicode)
        self.failUnlessIsInstance(NSAbortPrintingException, unicode)
        self.failUnlessIsInstance(NSIllegalSelectorException, unicode)
        self.failUnlessIsInstance(NSAppKitVirtualMemoryException, unicode)
        self.failUnlessIsInstance(NSBadRTFDirectiveException, unicode)
        self.failUnlessIsInstance(NSBadRTFFontTableException, unicode)
        self.failUnlessIsInstance(NSBadRTFStyleSheetException, unicode)
        self.failUnlessIsInstance(NSTypedStreamVersionException, unicode)
        self.failUnlessIsInstance(NSTIFFException, unicode)
        self.failUnlessIsInstance(NSPrintPackageException, unicode)
        self.failUnlessIsInstance(NSBadRTFColorTableException, unicode)
        self.failUnlessIsInstance(NSDraggingException, unicode)
        self.failUnlessIsInstance(NSColorListIOException, unicode)
        self.failUnlessIsInstance(NSColorListNotEditableException, unicode)
        self.failUnlessIsInstance(NSBadBitmapParametersException, unicode)
        self.failUnlessIsInstance(NSWindowServerCommunicationException, unicode)
        self.failUnlessIsInstance(NSFontUnavailableException, unicode)
        self.failUnlessIsInstance(NSPPDIncludeNotFoundException, unicode)
        self.failUnlessIsInstance(NSPPDParseException, unicode)
        self.failUnlessIsInstance(NSPPDIncludeStackOverflowException, unicode)
        self.failUnlessIsInstance(NSPPDIncludeStackUnderflowException, unicode)
        self.failUnlessIsInstance(NSRTFPropertyStackOverflowException, unicode)
        self.failUnlessIsInstance(NSAppKitIgnoredException, unicode)
        self.failUnlessIsInstance(NSBadComparisonException, unicode)
        self.failUnlessIsInstance(NSImageCacheException, unicode)
        self.failUnlessIsInstance(NSNibLoadingException, unicode)
        self.failUnlessIsInstance(NSBrowserIllegalDelegateException, unicode)
        self.failUnlessIsInstance(NSAccessibilityException, unicode)


if __name__ == "__main__":
    main()
