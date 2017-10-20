from PyObjCTools.TestSupport import *

from Foundation import *
from AppKit import *

class TestNSErrorHelper (NSObject):
    def attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_(self, a, b, c, d, e): pass
    def attemptRecoveryFromError_optionIndex_(self, a, b): return 1


class TestNSError (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSCocoaErrorDomain, unicode)

        self.assertIsInstance(NSPOSIXErrorDomain, unicode)
        self.assertIsInstance(NSOSStatusErrorDomain, unicode)

        self.assertIsInstance(NSUnderlyingErrorKey, unicode)

        self.assertIsInstance(NSFilePathErrorKey, unicode)
        self.assertIsInstance(NSHelpAnchorErrorKey, unicode)
        self.assertIsInstance(NSLocalizedDescriptionKey, unicode)
        self.assertIsInstance(NSLocalizedFailureReasonErrorKey, unicode)
        self.assertIsInstance(NSLocalizedRecoveryOptionsErrorKey, unicode)
        self.assertIsInstance(NSLocalizedRecoverySuggestionErrorKey, unicode)
        self.assertIsInstance(NSMachErrorDomain, unicode)
        self.assertIsInstance(NSRecoveryAttempterErrorKey, unicode)
        self.assertIsInstance(NSStringEncodingErrorKey, unicode)
        self.assertIsInstance(NSURLErrorKey, unicode)
        self.assertIsInstance(NSAbortModalException, unicode)
        self.assertIsInstance(NSAbortPrintingException, unicode)
        self.assertIsInstance(NSAccessibilityException, unicode)
        self.assertIsInstance(NSAppKitIgnoredException, unicode)
        self.assertIsInstance(NSAppKitVirtualMemoryException, unicode)
        self.assertIsInstance(NSBadBitmapParametersException, unicode)
        self.assertIsInstance(NSBadComparisonException, unicode)
        self.assertIsInstance(NSBadRTFColorTableException, unicode)
        self.assertIsInstance(NSBadRTFDirectiveException, unicode)
        self.assertIsInstance(NSBadRTFFontTableException, unicode)
        self.assertIsInstance(NSBadRTFStyleSheetException, unicode)
        self.assertIsInstance(NSBrowserIllegalDelegateException, unicode)
        self.assertIsInstance(NSColorListIOException, unicode)
        self.assertIsInstance(NSColorListNotEditableException, unicode)
        self.assertIsInstance(NSDraggingException, unicode)
        self.assertIsInstance(NSFontUnavailableException, unicode)
        self.assertIsInstance(NSIllegalSelectorException, unicode)
        self.assertIsInstance(NSImageCacheException, unicode)
        self.assertIsInstance(NSNibLoadingException, unicode)
        self.assertIsInstance(NSPPDIncludeNotFoundException, unicode)
        self.assertIsInstance(NSPPDIncludeStackOverflowException, unicode)
        self.assertIsInstance(NSPPDIncludeStackUnderflowException, unicode)
        self.assertIsInstance(NSPPDParseException, unicode)
        self.assertIsInstance(NSPasteboardCommunicationException, unicode)
        self.assertIsInstance(NSPrintPackageException, unicode)
        self.assertIsInstance(NSPrintingCommunicationException, unicode)
        self.assertIsInstance(NSRTFPropertyStackOverflowException, unicode)
        self.assertIsInstance(NSTIFFException, unicode)
        self.assertIsInstance(NSTextLineTooLongException, unicode)
        self.assertIsInstance(NSTextNoSelectionException, unicode)
        self.assertIsInstance(NSTextReadException, unicode)
        self.assertIsInstance(NSTextWriteException, unicode)
        self.assertIsInstance(NSTypedStreamVersionException, unicode)
        self.assertIsInstance(NSWindowServerCommunicationException, unicode)
        self.assertIsInstance(NSWordTablesReadException, unicode)
        self.assertIsInstance(NSWordTablesWriteException, unicode)

    @min_os_level('10.13')
    def testConstants10_13(self):
        self.assertIsInstance(NSLocalizedFailureErrorKey, unicode)

    def testAttemptRecovery(self):
        self.assertArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 1, objc._C_NSUInteger)
        self.assertArgIsSEL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 3, b'v@:' + objc._C_NSBOOL + b'^v')
        self.assertArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_, 4, b'^v')

        self.assertResultIsBOOL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_)
        self.assertArgHasType(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_, 1, objc._C_NSUInteger)

    @min_os_level('10.11')
    def testMethods10_11(self):
        self.assertArgIsBlock(NSError.setUserInfoValueProviderForDomain_provider_, 1, b'@@@')
        self.assertResultIsBlock(NSError.userInfoValueProviderForDomain_, b'@@@')


if __name__ == "__main__":
    main()
