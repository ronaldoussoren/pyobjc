import AppKit
from PyObjCTools.TestSupport import TestCase


class TestAppKitErrors(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSTextReadInapplicableDocumentTypeError, 65806)
        self.assertEqual(AppKit.NSTextWriteInapplicableDocumentTypeError, 66062)
        self.assertEqual(AppKit.NSTextReadWriteErrorMinimum, 65792)
        self.assertEqual(AppKit.NSTextReadWriteErrorMaximum, 66303)
        self.assertEqual(AppKit.NSServiceApplicationNotFoundError, 66560)
        self.assertEqual(AppKit.NSServiceApplicationLaunchFailedError, 66561)
        self.assertEqual(AppKit.NSServiceRequestTimedOutError, 66562)
        self.assertEqual(AppKit.NSServiceInvalidPasteboardDataError, 66563)
        self.assertEqual(AppKit.NSServiceMalformedServiceDictionaryError, 66564)
        self.assertEqual(AppKit.NSServiceMiscellaneousError, 66800)
        self.assertEqual(AppKit.NSServiceErrorMinimum, 66560)
        self.assertEqual(AppKit.NSServiceErrorMaximum, 66817)
        self.assertEqual(AppKit.NSSharingServiceNotConfiguredError, 67072)
        self.assertEqual(AppKit.NSSharingServiceErrorMinimum, 67072)
        self.assertEqual(AppKit.NSSharingServiceErrorMaximum, 67327)
        self.assertEqual(AppKit.NSFontAssetDownloadError, 66304)
        self.assertEqual(AppKit.NSFontErrorMinimum, 66304)
        self.assertEqual(AppKit.NSFontErrorMaximum, 66335)
        self.assertEqual(AppKit.NSFontAssetDownloadError, 66304)
        self.assertEqual(AppKit.NSFontErrorMinimum, 66304)
        self.assertEqual(AppKit.NSFontErrorMaximum, 66335)
        self.assertEqual(AppKit.NSWorkspaceAuthorizationInvalidError, 67328)
        self.assertEqual(AppKit.NSWorkspaceErrorMinimum, 67328)
        self.assertEqual(AppKit.NSWorkspaceErrorMaximum, 67455)

        self.assertEqual(AppKit.NSWindowSharingRequestAlreadyRequested, 67456)
        self.assertEqual(AppKit.NSWindowSharingRequestNoEligibleSession, 67457)
        self.assertEqual(AppKit.NSWindowSharingRequestUnspecifiedError, 67458)
        self.assertEqual(AppKit.NSWindowSharingErrorMinimum, 67456)
        self.assertEqual(AppKit.NSWindowSharingErrorMaximum, 67466)
