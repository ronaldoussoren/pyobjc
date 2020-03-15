import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level
import objc


class TestNSErrorHelper(AppKit.NSObject):
    def attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_(
        self, a, b, c, d, e
    ):
        pass

    def attemptRecoveryFromError_optionIndex_(self, a, b):
        return 1


class TestNSError(TestCase):
    def testConstants(self):
        self.assertIsInstance(AppKit.NSCocoaErrorDomain, str)

        self.assertIsInstance(AppKit.NSPOSIXErrorDomain, str)
        self.assertIsInstance(AppKit.NSOSStatusErrorDomain, str)

        self.assertIsInstance(AppKit.NSUnderlyingErrorKey, str)

        self.assertIsInstance(AppKit.NSFilePathErrorKey, str)
        self.assertIsInstance(AppKit.NSHelpAnchorErrorKey, str)
        self.assertIsInstance(AppKit.NSLocalizedDescriptionKey, str)
        self.assertIsInstance(AppKit.NSLocalizedFailureReasonErrorKey, str)
        self.assertIsInstance(AppKit.NSLocalizedRecoveryOptionsErrorKey, str)
        self.assertIsInstance(AppKit.NSLocalizedRecoverySuggestionErrorKey, str)
        self.assertIsInstance(AppKit.NSMachErrorDomain, str)
        self.assertIsInstance(AppKit.NSRecoveryAttempterErrorKey, str)
        self.assertIsInstance(AppKit.NSStringEncodingErrorKey, str)
        self.assertIsInstance(AppKit.NSURLErrorKey, str)
        self.assertIsInstance(AppKit.NSAbortModalException, str)
        self.assertIsInstance(AppKit.NSAbortPrintingException, str)
        self.assertIsInstance(AppKit.NSAccessibilityException, str)
        self.assertIsInstance(AppKit.NSAppKitIgnoredException, str)
        self.assertIsInstance(AppKit.NSAppKitVirtualMemoryException, str)
        self.assertIsInstance(AppKit.NSBadBitmapParametersException, str)
        self.assertIsInstance(AppKit.NSBadComparisonException, str)
        self.assertIsInstance(AppKit.NSBadRTFColorTableException, str)
        self.assertIsInstance(AppKit.NSBadRTFDirectiveException, str)
        self.assertIsInstance(AppKit.NSBadRTFFontTableException, str)
        self.assertIsInstance(AppKit.NSBadRTFStyleSheetException, str)
        self.assertIsInstance(AppKit.NSBrowserIllegalDelegateException, str)
        self.assertIsInstance(AppKit.NSColorListIOException, str)
        self.assertIsInstance(AppKit.NSColorListNotEditableException, str)
        self.assertIsInstance(AppKit.NSDraggingException, str)
        self.assertIsInstance(AppKit.NSFontUnavailableException, str)
        self.assertIsInstance(AppKit.NSIllegalSelectorException, str)
        self.assertIsInstance(AppKit.NSImageCacheException, str)
        self.assertIsInstance(AppKit.NSNibLoadingException, str)
        self.assertIsInstance(AppKit.NSPPDIncludeNotFoundException, str)
        self.assertIsInstance(AppKit.NSPPDIncludeStackOverflowException, str)
        self.assertIsInstance(AppKit.NSPPDIncludeStackUnderflowException, str)
        self.assertIsInstance(AppKit.NSPPDParseException, str)
        self.assertIsInstance(AppKit.NSPasteboardCommunicationException, str)
        self.assertIsInstance(AppKit.NSPrintPackageException, str)
        self.assertIsInstance(AppKit.NSPrintingCommunicationException, str)
        self.assertIsInstance(AppKit.NSRTFPropertyStackOverflowException, str)
        self.assertIsInstance(AppKit.NSTIFFException, str)
        self.assertIsInstance(AppKit.NSTextLineTooLongException, str)
        self.assertIsInstance(AppKit.NSTextNoSelectionException, str)
        self.assertIsInstance(AppKit.NSTextReadException, str)
        self.assertIsInstance(AppKit.NSTextWriteException, str)
        self.assertIsInstance(AppKit.NSTypedStreamVersionException, str)
        self.assertIsInstance(AppKit.NSWindowServerCommunicationException, str)
        self.assertIsInstance(AppKit.NSWordTablesReadException, str)
        self.assertIsInstance(AppKit.NSWordTablesWriteException, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSLocalizedFailureErrorKey, str)

    def testAttemptRecovery(self):
        self.assertArgHasType(
            TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_,  # noqa: B950
            1,
            objc._C_NSUInteger,
        )
        self.assertArgIsSEL(
            TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_,  # noqa: B950
            3,
            b"v@:" + objc._C_NSBOOL + b"^v",
        )
        self.assertArgHasType(
            TestNSErrorHelper.attemptRecoveryFromError_optionIndex_delegate_didRecoverSelector_contextInfo_,  # noqa: B950
            4,
            b"^v",
        )

        self.assertResultIsBOOL(TestNSErrorHelper.attemptRecoveryFromError_optionIndex_)
        self.assertArgHasType(
            TestNSErrorHelper.attemptRecoveryFromError_optionIndex_,
            1,
            objc._C_NSUInteger,
        )

    @min_os_level("10.11")
    def testMethods10_11(self):
        self.assertArgIsBlock(
            AppKit.NSError.setUserInfoValueProviderForDomain_provider_, 1, b"@@@"
        )
        self.assertResultIsBlock(AppKit.NSError.userInfoValueProviderForDomain_, b"@@@")
