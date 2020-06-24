import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSItemProviderHelper(AppKit.NSObject):
    def itemProviderVisibilityForRepresentationWithTypeIdentifier_(self, a):
        return 1

    def loadDataWithTypeIdentifier_forItemProviderCompletionHandler_(self, a, b):
        pass

    def objectWithItemProviderData_typeIdentifier_error_(self, a, b, c):
        return 1

    def initWithItemProviderData_typeIdentifier_error_(self, a, b, c):
        return 1


NSItemProviderCompletionHandler = b"v@@"
NSItemProviderLoadHandler = b"v@?#@"


class TestNSItemProvider(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSItemProviderRepresentationVisibilityAll, 0)
        self.assertEqual(AppKit.NSItemProviderRepresentationVisibilityGroup, 2)
        self.assertEqual(AppKit.NSItemProviderRepresentationVisibilityOwnProcess, 3)
        self.assertEqual(AppKit.NSItemProviderFileOptionOpenInPlace, 1)

    @min_os_level("10.10")
    def testConstants10_10(self):
        self.assertIsInstance(AppKit.NSTypeIdentifierDateText, str)
        self.assertIsInstance(AppKit.NSTypeIdentifierAddressText, str)
        self.assertIsInstance(AppKit.NSTypeIdentifierPhoneNumberText, str)
        self.assertIsInstance(AppKit.NSTypeIdentifierTransitInformationText, str)

        self.assertIsInstance(AppKit.NSItemProviderPreferredImageSizeKey, str)
        self.assertIsInstance(AppKit.NSExtensionJavaScriptPreprocessingResultsKey, str)
        self.assertIsInstance(AppKit.NSItemProviderErrorDomain, str)

        self.assertEqual(AppKit.NSItemProviderUnknownError, -1)
        self.assertEqual(AppKit.NSItemProviderItemUnavailableError, -1000)
        self.assertEqual(AppKit.NSItemProviderUnexpectedValueClassError, -1100)

    @min_os_level("10.11")
    def testConstants10_11(self):
        self.assertEqual(AppKit.NSItemProviderUnavailableCoercionError, -1200)

    def testMethods(self):
        self.assertResultHasType(
            TestNSItemProviderHelper.itemProviderVisibilityForRepresentationWithTypeIdentifier_,
            objc._C_NSInteger,
        )
        self.assertResultHasType(
            TestNSItemProviderHelper.itemProviderVisibilityForRepresentationWithTypeIdentifier_,
            objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            TestNSItemProviderHelper.loadDataWithTypeIdentifier_forItemProviderCompletionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsOut(
            TestNSItemProviderHelper.objectWithItemProviderData_typeIdentifier_error_, 2
        )
        self.assertArgIsOut(
            TestNSItemProviderHelper.initWithItemProviderData_typeIdentifier_error_, 2
        )

    @min_os_level("10.10")
    def testMethods10_10(self):

        self.assertResultIsBOOL(
            AppKit.NSItemProvider.hasItemConformingToTypeIdentifier_
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadItemForTypeIdentifier_options_completionHandler_,
            2,
            NSItemProviderCompletionHandler,
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.registerItemForTypeIdentifier_loadHandler_,
            1,
            NSItemProviderLoadHandler,
        )

        self.assertResultIsBlock(
            AppKit.NSItemProvider.previewImageHandler, NSItemProviderLoadHandler
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.setPreviewImageHandler_, 0, NSItemProviderLoadHandler
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadPreviewImageWithOptions_completionHandler_,
            1,
            NSItemProviderCompletionHandler,
        )

        # XXX:
        # self.fail("NSItemProviderLoadHandler metadata test")

    @min_os_level("10.13")
    def testMethods10_13(self):
        # XXX: Cannot properly test right now...
        self.assertArgIsBlock(
            AppKit.NSItemProvider.registerDataRepresentationForTypeIdentifier_visibility_loadHandler_,  # noqa: B950
            2,
            b"@@?",
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.registerFileRepresentationForTypeIdentifier_fileOptions_visibility_loadHandler_,  # noqa: B950
            3,
            b"@@?",
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.registerObjectOfClass_visibility_loadHandler_,
            2,
            b"@@?",
        )

        self.assertResultIsBOOL(
            AppKit.NSItemProvider.hasRepresentationConformingToTypeIdentifier_fileOptions_
        )

        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadDataRepresentationForTypeIdentifier_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadFileRepresentationForTypeIdentifier_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadInPlaceFileRepresentationForTypeIdentifier_completionHandler_,  # noqa: B950
            1,
            b"v@Z@",
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadObjectOfClass_completionHandler_, 1, b"v@@"
        )
        self.assertResultIsBOOL(AppKit.NSItemProvider.canLoadObjectOfClass_)

        # XXX: Cannot properly test right now...
        self.assertArgIsBlock(
            AppKit.NSItemProvider.registerItemForTypeIdentifier_loadHandler_,
            1,
            NSItemProviderLoadHandler,
        )
        self.assertArgIsBlock(
            AppKit.NSItemProvider.loadItemForTypeIdentifier_options_completionHandler_,
            2,
            NSItemProviderCompletionHandler,
        )

    @min_sdk_level("10.13")
    def testProtocols10_13(self):
        objc.protocolNamed("NSItemProviderWriting")
        objc.protocolNamed("NSItemProviderReading")
