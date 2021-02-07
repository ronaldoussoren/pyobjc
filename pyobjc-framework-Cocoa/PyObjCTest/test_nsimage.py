import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSImageHelper(AppKit.NSObject):
    def image_didLoadRepresentation_withStatus_(self, i, r, s):
        pass

    def image_didLoadPartOfRepresentation_withValidRows_(self, i, r, c):
        pass


class TestNSImage(TestCase):
    def test_compositePoint(self):
        # comes straight from ReSTedit.  Works on PPC, not on Intel (as of r1791)
        ws = AppKit.NSWorkspace.sharedWorkspace()
        txtIcon = ws.iconForFileType_("txt")
        txtIcon.setSize_((16, 16))
        htmlIcon = ws.iconForFileType_("html")
        htmlIcon.setSize_((16, 16))

        comboIcon = AppKit.NSImage.alloc().initWithSize_((100, 100))
        comboIcon.lockFocus()
        txtIcon.compositeToPoint_fromRect_operation_(
            (0, 0), ((0, 0), (16, 16)), AppKit.NSCompositeCopy
        )
        htmlIcon.compositeToPoint_fromRect_operation_(
            (8, 0), ((8, 0), (8, 16)), AppKit.NSCompositeCopy
        )
        comboIcon.unlockFocus()

    def testConstants(self):
        self.assertEqual(AppKit.NSImageLoadStatusCompleted, 0)
        self.assertEqual(AppKit.NSImageLoadStatusCancelled, 1)
        self.assertEqual(AppKit.NSImageLoadStatusInvalidData, 2)
        self.assertEqual(AppKit.NSImageLoadStatusUnexpectedEOF, 3)
        self.assertEqual(AppKit.NSImageLoadStatusReadError, 4)

        self.assertEqual(AppKit.NSImageCacheDefault, 0)
        self.assertEqual(AppKit.NSImageCacheAlways, 1)
        self.assertEqual(AppKit.NSImageCacheBySize, 2)
        self.assertEqual(AppKit.NSImageCacheNever, 3)

        if objc.arch == "x86_64":
            self.assertEqual(AppKit.NSImageResizingModeStretch, 0)
            self.assertEqual(AppKit.NSImageResizingModeTile, 1)
        else:
            self.assertEqual(AppKit.NSImageResizingModeTile, 0)
            self.assertEqual(AppKit.NSImageResizingModeStretch, 1)

        self.assertEqual(AppKit.NSImageSymbolScaleSmall, 1)
        self.assertEqual(AppKit.NSImageSymbolScaleMedium, 2)
        self.assertEqual(AppKit.NSImageSymbolScaleLarge, 3)

    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance(AppKit.NSImageNameQuickLookTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameBluetoothTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameIChatTheaterTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameSlideshowTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameActionTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameSmartBadgeTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameIconViewTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameListViewTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameColumnViewTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameFlowViewTemplate, str)
        self.assertIsInstance(AppKit.NSImageNamePathTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameInvalidDataFreestandingTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameLockLockedTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameLockUnlockedTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameGoRightTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameGoLeftTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameRightFacingTriangleTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameLeftFacingTriangleTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameAddTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameRemoveTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameRevealFreestandingTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameFollowLinkFreestandingTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameEnterFullScreenTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameExitFullScreenTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameStopProgressTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameStopProgressFreestandingTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameRefreshTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameRefreshFreestandingTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameBonjour, str)
        self.assertIsInstance(AppKit.NSImageNameDotMac, str)
        self.assertIsInstance(AppKit.NSImageNameComputer, str)
        self.assertIsInstance(AppKit.NSImageNameFolderBurnable, str)
        self.assertIsInstance(AppKit.NSImageNameFolderSmart, str)
        self.assertIsInstance(AppKit.NSImageNameNetwork, str)
        self.assertIsInstance(AppKit.NSImageNameMultipleDocuments, str)
        self.assertIsInstance(AppKit.NSImageNameUserAccounts, str)
        self.assertIsInstance(AppKit.NSImageNamePreferencesGeneral, str)
        self.assertIsInstance(AppKit.NSImageNameAdvanced, str)
        self.assertIsInstance(AppKit.NSImageNameInfo, str)
        self.assertIsInstance(AppKit.NSImageNameFontPanel, str)
        self.assertIsInstance(AppKit.NSImageNameColorPanel, str)
        self.assertIsInstance(AppKit.NSImageNameUser, str)
        self.assertIsInstance(AppKit.NSImageNameUserGroup, str)
        self.assertIsInstance(AppKit.NSImageNameEveryone, str)

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSImage.setName_)
        self.assertArgIsBOOL(AppKit.NSImage.setScalesWhenResized_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.scalesWhenResized)
        self.assertArgIsBOOL(AppKit.NSImage.setDataRetained_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.isDataRetained)
        self.assertArgIsBOOL(AppKit.NSImage.setCachedSeparately_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.isCachedSeparately)
        self.assertArgIsBOOL(AppKit.NSImage.setCacheDepthMatchesImageDepth_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.cacheDepthMatchesImageDepth)
        self.assertArgIsBOOL(AppKit.NSImage.setUsesEPSOnResolutionMismatch_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.usesEPSOnResolutionMismatch)
        self.assertArgIsBOOL(AppKit.NSImage.setPrefersColorMatch_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.prefersColorMatch)
        self.assertArgIsBOOL(AppKit.NSImage.setMatchesOnMultipleResolution_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.matchesOnMultipleResolution)
        self.assertResultIsBOOL(AppKit.NSImage.drawRepresentation_inRect_)
        self.assertResultIsBOOL(AppKit.NSImage.isValid)
        self.assertResultIsBOOL(AppKit.NSImage.canInitWithPasteboard_)
        self.assertResultIsBOOL(AppKit.NSImage.isFlipped)
        self.assertArgIsBOOL(AppKit.NSImage.setFlipped_, 0)
        self.assertResultIsBOOL(AppKit.NSImage.isTemplate)
        self.assertArgIsBOOL(AppKit.NSImage.setTemplate_, 0)

    def testProtocols(self):

        self.assertArgHasType(
            TestNSImageHelper.image_didLoadPartOfRepresentation_withValidRows_,
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSImageHelper.image_didLoadRepresentation_withStatus_,
            2,
            objc._C_NSUInteger,
        )

    @min_sdk_level("10.10")
    def testProtocolObjects(self):
        objc.protocolNamed("NSImageDelegate")

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertArgHasType(
            AppKit.NSImage.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgIsBOOL(
            AppKit.NSImage.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
            4,
        )
        self.assertArgIsBOOL(AppKit.NSImage.lockFocusFlipped_, 0)
        self.assertArgHasType(
            AppKit.NSImage.initWithCGImage_size_, 1, AppKit.NSSize.__typestr__
        )
        self.assertArgHasType(
            AppKit.NSImage.CGImageForProposedRect_context_hints_,
            0,
            b"o^" + AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSImage.bestRepresentationForRect_context_hints_,
            0,
            AppKit.NSRect.__typestr__,
        )

        self.assertResultIsBOOL(
            AppKit.NSImage.hitTestRect_withImageDestinationRect_context_hints_flipped_
        )
        self.assertArgHasType(
            AppKit.NSImage.hitTestRect_withImageDestinationRect_context_hints_flipped_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            AppKit.NSImage.hitTestRect_withImageDestinationRect_context_hints_flipped_,
            1,
            AppKit.NSRect.__typestr__,
        )

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(AppKit.NSImage.matchesOnlyOnBestFittingAxis)
        self.assertArgIsBOOL(AppKit.NSImage.setMatchesOnlyOnBestFittingAxis_, 0)

    @min_os_level("10.8")
    def testMethods10_8(self):
        self.assertArgIsBOOL(AppKit.NSImage.imageWithSize_flipped_drawingHandler_, 1)
        self.assertArgIsBlock(
            AppKit.NSImage.imageWithSize_flipped_drawingHandler_,
            2,
            objc._C_NSBOOL + AppKit.NSRect.__typestr__,
        )

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(AppKit.NSImageHintCTM, str)
        self.assertIsInstance(AppKit.NSImageHintInterpolation, str)
        self.assertIsInstance(AppKit.NSImageNameFolder, str)
        self.assertIsInstance(AppKit.NSImageNameMobileMe, str)
        self.assertIsInstance(AppKit.NSImageNameUserGuest, str)
        self.assertIsInstance(AppKit.NSImageNameMenuOnStateTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameMenuMixedStateTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameApplicationIcon, str)
        self.assertIsInstance(AppKit.NSImageNameTrashEmpty, str)
        self.assertIsInstance(AppKit.NSImageNameTrashFull, str)
        self.assertIsInstance(AppKit.NSImageNameHomeTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameBookmarksTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameCaution, str)
        self.assertIsInstance(AppKit.NSImageNameStatusAvailable, str)
        self.assertIsInstance(AppKit.NSImageNameStatusPartiallyAvailable, str)
        self.assertIsInstance(AppKit.NSImageNameStatusUnavailable, str)
        self.assertIsInstance(AppKit.NSImageNameStatusNone, str)

    @min_os_level("10.8")
    def testConstants10_8(self):
        self.assertIsInstance(AppKit.NSImageNameShareTemplate, str)

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSImageHintUserInterfaceLayoutDirection, str)
        self.assertIsInstance(AppKit.NSImageNameGoForwardTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameGoBackTemplate, str)

        self.assertIsInstance(AppKit.NSImageNameTouchBarAddDetailTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarAddTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarAlarmTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarAudioInputMuteTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarAudioInputTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarAudioOutputMuteTemplate, str)
        self.assertIsInstance(
            AppKit.NSImageNameTouchBarAudioOutputVolumeHighTemplate, str
        )
        self.assertIsInstance(
            AppKit.NSImageNameTouchBarAudioOutputVolumeLowTemplate, str
        )
        self.assertIsInstance(
            AppKit.NSImageNameTouchBarAudioOutputVolumeMediumTemplate, str
        )
        self.assertIsInstance(
            AppKit.NSImageNameTouchBarAudioOutputVolumeOffTemplate, str
        )
        self.assertIsInstance(AppKit.NSImageNameTouchBarBookmarksTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarColorPickerFill, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarColorPickerFont, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarColorPickerStroke, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarCommunicationAudioTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarCommunicationVideoTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarComposeTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarDeleteTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarDownloadTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarEnterFullScreenTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarExitFullScreenTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarFastForwardTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarFolderCopyToTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarFolderMoveToTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarFolderTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarGetInfoTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarGoBackTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarGoDownTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarGoForwardTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarGoUpTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarHistoryTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarIconViewTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarListViewTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarMailTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarNewFolderTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarNewMessageTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarOpenInBrowserTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarPauseTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarPlayheadTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarPlayPauseTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarPlayTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarQuickLookTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarRecordStartTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarRecordStopTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarRefreshTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarRewindTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarRotateLeftTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarRotateRightTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSearchTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarShareTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSidebarTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipAhead15SecondsTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipAhead30SecondsTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipAheadTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipBack15SecondsTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipBack30SecondsTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipBackTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipToEndTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSkipToStartTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarSlideshowTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTagIconTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextBoldTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextBoxTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextCenterAlignTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextItalicTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextJustifiedAlignTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextLeftAlignTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextListTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextRightAlignTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextStrikethroughTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarTextUnderlineTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarUserAddTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarUserGroupTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarUserTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarVolumeDownTemplate, str)
        self.assertIsInstance(AppKit.NSImageNameTouchBarVolumeUpTemplate, str)

    @min_os_level("10.13")
    def testConstants10_13(self):
        self.assertIsInstance(AppKit.NSImageNameTouchBarRemoveTemplate, str)
