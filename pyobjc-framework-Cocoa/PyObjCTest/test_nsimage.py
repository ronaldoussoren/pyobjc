from PyObjCTools.TestSupport import *
import AppKit
from AppKit import *

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
        self.failUnlessEqual(NSImageLoadStatusCompleted, 0)
        self.failUnlessEqual(NSImageLoadStatusCancelled, 1)
        self.failUnlessEqual(NSImageLoadStatusInvalidData, 2)
        self.failUnlessEqual(NSImageLoadStatusUnexpectedEOF, 3)
        self.failUnlessEqual(NSImageLoadStatusReadError, 4)

        self.failUnlessEqual(NSImageCacheDefault, 0)
        self.failUnlessEqual(NSImageCacheAlways, 1)
        self.failUnlessEqual(NSImageCacheBySize, 2)
        self.failUnlessEqual(NSImageCacheNever, 3)

    
    @min_os_level("10.5")
    def testConstants10_5(self):
        self.failUnlessIsInstance( NSImageNameQuickLookTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameBluetoothTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameIChatTheaterTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameSlideshowTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameActionTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameSmartBadgeTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameIconViewTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameListViewTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameColumnViewTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameFlowViewTemplate, unicode)
        self.failUnlessIsInstance( NSImageNamePathTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameInvalidDataFreestandingTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameLockLockedTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameLockUnlockedTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameGoRightTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameGoLeftTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameRightFacingTriangleTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameLeftFacingTriangleTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameAddTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameRemoveTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameRevealFreestandingTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameFollowLinkFreestandingTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameEnterFullScreenTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameExitFullScreenTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameStopProgressTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameStopProgressFreestandingTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameRefreshTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameRefreshFreestandingTemplate, unicode)
        self.failUnlessIsInstance( NSImageNameBonjour, unicode)
        self.failUnlessIsInstance( NSImageNameDotMac, unicode)
        self.failUnlessIsInstance( NSImageNameComputer, unicode)
        self.failUnlessIsInstance( NSImageNameFolderBurnable, unicode)
        self.failUnlessIsInstance( NSImageNameFolderSmart, unicode)
        self.failUnlessIsInstance( NSImageNameNetwork, unicode)
        self.failUnlessIsInstance( NSImageNameMultipleDocuments, unicode)
        self.failUnlessIsInstance( NSImageNameUserAccounts, unicode)
        self.failUnlessIsInstance( NSImageNamePreferencesGeneral, unicode)
        self.failUnlessIsInstance( NSImageNameAdvanced, unicode)
        self.failUnlessIsInstance( NSImageNameInfo, unicode)
        self.failUnlessIsInstance( NSImageNameFontPanel, unicode)
        self.failUnlessIsInstance( NSImageNameColorPanel, unicode)
        self.failUnlessIsInstance( NSImageNameUser, unicode)
        self.failUnlessIsInstance( NSImageNameUserGroup, unicode)
        self.failUnlessIsInstance( NSImageNameEveryone, unicode)

    def testMethods(self):
        self.fail("- (id)initWithIconRef:(IconRef)iconRef;")


if __name__ == "__main__":
    main()
