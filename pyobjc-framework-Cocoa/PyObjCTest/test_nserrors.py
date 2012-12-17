
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSErrors (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSTextLineTooLongException, unicode)
        self.assertIsInstance(NSTextNoSelectionException, unicode)
        self.assertIsInstance(NSWordTablesWriteException, unicode)
        self.assertIsInstance(NSWordTablesReadException, unicode)
        self.assertIsInstance(NSTextReadException, unicode)
        self.assertIsInstance(NSTextWriteException, unicode)
        self.assertIsInstance(NSPasteboardCommunicationException, unicode)
        self.assertIsInstance(NSPrintingCommunicationException, unicode)
        self.assertIsInstance(NSAbortModalException, unicode)
        self.assertIsInstance(NSAbortPrintingException, unicode)
        self.assertIsInstance(NSIllegalSelectorException, unicode)
        self.assertIsInstance(NSAppKitVirtualMemoryException, unicode)
        self.assertIsInstance(NSBadRTFDirectiveException, unicode)
        self.assertIsInstance(NSBadRTFFontTableException, unicode)
        self.assertIsInstance(NSBadRTFStyleSheetException, unicode)
        self.assertIsInstance(NSTypedStreamVersionException, unicode)
        self.assertIsInstance(NSTIFFException, unicode)
        self.assertIsInstance(NSPrintPackageException, unicode)
        self.assertIsInstance(NSBadRTFColorTableException, unicode)
        self.assertIsInstance(NSDraggingException, unicode)
        self.assertIsInstance(NSColorListIOException, unicode)
        self.assertIsInstance(NSColorListNotEditableException, unicode)
        self.assertIsInstance(NSBadBitmapParametersException, unicode)
        self.assertIsInstance(NSWindowServerCommunicationException, unicode)
        self.assertIsInstance(NSFontUnavailableException, unicode)
        self.assertIsInstance(NSPPDIncludeNotFoundException, unicode)
        self.assertIsInstance(NSPPDParseException, unicode)
        self.assertIsInstance(NSPPDIncludeStackOverflowException, unicode)
        self.assertIsInstance(NSPPDIncludeStackUnderflowException, unicode)
        self.assertIsInstance(NSRTFPropertyStackOverflowException, unicode)
        self.assertIsInstance(NSAppKitIgnoredException, unicode)
        self.assertIsInstance(NSBadComparisonException, unicode)
        self.assertIsInstance(NSImageCacheException, unicode)
        self.assertIsInstance(NSNibLoadingException, unicode)
        self.assertIsInstance(NSBrowserIllegalDelegateException, unicode)
        self.assertIsInstance(NSAccessibilityException, unicode)


if __name__ == "__main__":
    main()
