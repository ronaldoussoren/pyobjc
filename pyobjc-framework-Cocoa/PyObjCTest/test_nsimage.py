from PyObjCTools.TestSupport import *
import AppKit
from AppKit import *

class TestNSImageHelper (NSObject):
    def image_didLoadRepresentation_withStatus_(self, i, r, s): pass
    def image_didLoadPartOfRepresentation_withValidRows_(self, i, r, c): pass

class TestNSImage (TestCase):
    def test_compositePoint(self):
        # comes straight from ReSTedit.  Works on PPC, not on Intel (as of r1791)
        ws = AppKit.NSWorkspace.sharedWorkspace()
        txtIcon = ws.iconForFileType_("txt")
        txtIcon.setSize_( (16,16) )
        htmlIcon = ws.iconForFileType_("html")
        htmlIcon.setSize_( (16,16) )
        
        comboIcon = AppKit.NSImage.alloc().initWithSize_( (100,100) )
        comboIcon.lockFocus()
        txtIcon.compositeToPoint_fromRect_operation_((0,0), ((0,0),(16,16)), AppKit.NSCompositeCopy)
        htmlIcon.compositeToPoint_fromRect_operation_((8,0), ((8,0),(8,16)), AppKit.NSCompositeCopy)
        comboIcon.unlockFocus()

    def testConstants(self):
        self.assertEqual(NSImageLoadStatusCompleted, 0)
        self.assertEqual(NSImageLoadStatusCancelled, 1)
        self.assertEqual(NSImageLoadStatusInvalidData, 2)
        self.assertEqual(NSImageLoadStatusUnexpectedEOF, 3)
        self.assertEqual(NSImageLoadStatusReadError, 4)

        self.assertEqual(NSImageCacheDefault, 0)
        self.assertEqual(NSImageCacheAlways, 1)
        self.assertEqual(NSImageCacheBySize, 2)
        self.assertEqual(NSImageCacheNever, 3)

    
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.assertIsInstance( NSImageNameQuickLookTemplate, unicode)
        self.assertIsInstance( NSImageNameBluetoothTemplate, unicode)
        self.assertIsInstance( NSImageNameIChatTheaterTemplate, unicode)
        self.assertIsInstance( NSImageNameSlideshowTemplate, unicode)
        self.assertIsInstance( NSImageNameActionTemplate, unicode)
        self.assertIsInstance( NSImageNameSmartBadgeTemplate, unicode)
        self.assertIsInstance( NSImageNameIconViewTemplate, unicode)
        self.assertIsInstance( NSImageNameListViewTemplate, unicode)
        self.assertIsInstance( NSImageNameColumnViewTemplate, unicode)
        self.assertIsInstance( NSImageNameFlowViewTemplate, unicode)
        self.assertIsInstance( NSImageNamePathTemplate, unicode)
        self.assertIsInstance( NSImageNameInvalidDataFreestandingTemplate, unicode)
        self.assertIsInstance( NSImageNameLockLockedTemplate, unicode)
        self.assertIsInstance( NSImageNameLockUnlockedTemplate, unicode)
        self.assertIsInstance( NSImageNameGoRightTemplate, unicode)
        self.assertIsInstance( NSImageNameGoLeftTemplate, unicode)
        self.assertIsInstance( NSImageNameRightFacingTriangleTemplate, unicode)
        self.assertIsInstance( NSImageNameLeftFacingTriangleTemplate, unicode)
        self.assertIsInstance( NSImageNameAddTemplate, unicode)
        self.assertIsInstance( NSImageNameRemoveTemplate, unicode)
        self.assertIsInstance( NSImageNameRevealFreestandingTemplate, unicode)
        self.assertIsInstance( NSImageNameFollowLinkFreestandingTemplate, unicode)
        self.assertIsInstance( NSImageNameEnterFullScreenTemplate, unicode)
        self.assertIsInstance( NSImageNameExitFullScreenTemplate, unicode)
        self.assertIsInstance( NSImageNameStopProgressTemplate, unicode)
        self.assertIsInstance( NSImageNameStopProgressFreestandingTemplate, unicode)
        self.assertIsInstance( NSImageNameRefreshTemplate, unicode)
        self.assertIsInstance( NSImageNameRefreshFreestandingTemplate, unicode)
        self.assertIsInstance( NSImageNameBonjour, unicode)
        self.assertIsInstance( NSImageNameDotMac, unicode)
        self.assertIsInstance( NSImageNameComputer, unicode)
        self.assertIsInstance( NSImageNameFolderBurnable, unicode)
        self.assertIsInstance( NSImageNameFolderSmart, unicode)
        self.assertIsInstance( NSImageNameNetwork, unicode)
        self.assertIsInstance( NSImageNameMultipleDocuments, unicode)
        self.assertIsInstance( NSImageNameUserAccounts, unicode)
        self.assertIsInstance( NSImageNamePreferencesGeneral, unicode)
        self.assertIsInstance( NSImageNameAdvanced, unicode)
        self.assertIsInstance( NSImageNameInfo, unicode)
        self.assertIsInstance( NSImageNameFontPanel, unicode)
        self.assertIsInstance( NSImageNameColorPanel, unicode)
        self.assertIsInstance( NSImageNameUser, unicode)
        self.assertIsInstance( NSImageNameUserGroup, unicode)
        self.assertIsInstance( NSImageNameEveryone, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSImage.setName_)
        self.assertArgIsBOOL(NSImage.setScalesWhenResized_, 0)
        self.assertResultIsBOOL(NSImage.scalesWhenResized)
        self.assertArgIsBOOL(NSImage.setDataRetained_, 0)
        self.assertResultIsBOOL(NSImage.isDataRetained)
        self.assertArgIsBOOL(NSImage.setCachedSeparately_, 0)
        self.assertResultIsBOOL(NSImage.isCachedSeparately)
        self.assertArgIsBOOL(NSImage.setCacheDepthMatchesImageDepth_, 0)
        self.assertResultIsBOOL(NSImage.cacheDepthMatchesImageDepth)
        self.assertArgIsBOOL(NSImage.setUsesEPSOnResolutionMismatch_, 0)
        self.assertResultIsBOOL(NSImage.usesEPSOnResolutionMismatch)
        self.assertArgIsBOOL(NSImage.setPrefersColorMatch_, 0)
        self.assertResultIsBOOL(NSImage.prefersColorMatch)
        self.assertArgIsBOOL(NSImage.setMatchesOnMultipleResolution_, 0)
        self.assertResultIsBOOL(NSImage.matchesOnMultipleResolution)
        self.assertResultIsBOOL(NSImage.drawRepresentation_inRect_)
        self.assertResultIsBOOL(NSImage.isValid)
        self.assertResultIsBOOL(NSImage.canInitWithPasteboard_)
        self.assertResultIsBOOL(NSImage.isFlipped)
        self.assertArgIsBOOL(NSImage.setFlipped_, 0)
        self.assertResultIsBOOL(NSImage.isTemplate)
        self.assertArgIsBOOL(NSImage.setTemplate_, 0)

    def testProtocols(self):
        self.assertArgHasType(TestNSImageHelper.image_didLoadPartOfRepresentation_withValidRows_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSImageHelper.image_didLoadRepresentation_withStatus_, 2, objc._C_NSUInteger)


    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgHasType(NSImage.drawInRect_fromRect_operation_fraction_respectFlipped_hints_,
                0, NSRect.__typestr__)
        self.assertArgIsBOOL(NSImage.drawInRect_fromRect_operation_fraction_respectFlipped_hints_, 4)
        self.assertArgIsBOOL(NSImage.lockFocusFlipped_, 0)
        self.assertArgHasType(NSImage.initWithCGImage_size_, 1, NSSize.__typestr__)
        self.assertArgHasType(NSImage.CGImageForProposedRect_context_hints_, 0, b'o^' + NSRect.__typestr__)
        self.assertArgHasType(NSImage.bestRepresentationForRect_context_hints_, 0, NSRect.__typestr__)

        self.assertResultIsBOOL(NSImage.hitTestRect_withImageDestinationRect_context_hints_flipped_)
        self.assertArgHasType(NSImage.hitTestRect_withImageDestinationRect_context_hints_flipped_, 0, NSRect.__typestr__)
        self.assertArgHasType(NSImage.hitTestRect_withImageDestinationRect_context_hints_flipped_, 1, NSRect.__typestr__)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSImageHintCTM, unicode)
        self.assertIsInstance(NSImageHintInterpolation, unicode)
        self.assertIsInstance(NSImageNameFolder, unicode)
        self.assertIsInstance(NSImageNameMobileMe, unicode)
        self.assertIsInstance(NSImageNameUserGuest, unicode)
        self.assertIsInstance(NSImageNameMenuOnStateTemplate, unicode)
        self.assertIsInstance(NSImageNameMenuMixedStateTemplate, unicode)
        self.assertIsInstance(NSImageNameApplicationIcon, unicode)
        self.assertIsInstance(NSImageNameTrashEmpty, unicode)
        self.assertIsInstance(NSImageNameTrashFull, unicode)
        self.assertIsInstance(NSImageNameHomeTemplate, unicode)
        self.assertIsInstance(NSImageNameBookmarksTemplate, unicode)
        self.assertIsInstance(NSImageNameCaution, unicode)
        self.assertIsInstance(NSImageNameStatusAvailable, unicode)
        self.assertIsInstance(NSImageNameStatusPartiallyAvailable, unicode)
        self.assertIsInstance(NSImageNameStatusUnavailable, unicode)
        self.assertIsInstance(NSImageNameStatusNone, unicode)

if __name__ == "__main__":
    main()
