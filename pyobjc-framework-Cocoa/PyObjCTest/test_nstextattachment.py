import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level, min_os_level
import objc


class TestNSTextAttachmentHelper(AppKit.NSObject):
    def drawWithFrame_inView_(self, fr, vi):
        pass

    def wantsToTrackMouse(self):
        return 1

    def highlight_withFrame_inView_(self, fl, fr, vi):
        pass

    def trackMouse_inRect_ofView_untilMouseUp_(self, ev, fr, vi, fl):
        pass

    def cellSize(self):
        return 1

    def cellBaselineOffset(self):
        return 1

    def drawWithFrame_inView_characterIndex_(self, fr, vi, i):
        pass

    def drawWithFrame_inView_characterIndex_layoutManager_(self, fr, vi, i, lm):
        pass

    def wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_(self, ev, fr, vi, i):
        return 1

    def trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_(
        self, ev, fr, vi, i, fl
    ):
        return 1

    def cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_(
        self, tc, fr, po, i
    ):
        return 1

    def imageForBounds_textContainer_characterIndex_(self, b, c, i):
        return 1

    def attachmentBoundsForTextContainer_proposedLineFragment_glyphPosition_characterIndex_(
        self, c, f, p, i
    ):
        return 1


class TestNSTextAttachment(TestCase):
    def testConstants(self):
        self.assertEqual(AppKit.NSAttachmentCharacter, chr(0xFFFC))

    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSTextAttachmentCell.wantsToTrackMouse)
        self.assertArgIsBOOL(AppKit.NSTextAttachmentCell.highlight_withFrame_inView_, 0)
        self.assertResultIsBOOL(
            AppKit.NSTextAttachmentCell.trackMouse_inRect_ofView_untilMouseUp_
        )
        self.assertArgIsBOOL(
            AppKit.NSTextAttachmentCell.trackMouse_inRect_ofView_untilMouseUp_, 3
        )
        self.assertResultIsBOOL(
            AppKit.NSTextAttachmentCell.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_  # noqa: B950
        )
        self.assertResultIsBOOL(
            AppKit.NSTextAttachmentCell.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_
        )
        self.assertArgIsBOOL(
            AppKit.NSTextAttachmentCell.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_,
            4,
        )

    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(AppKit.NSTextAttachment.allowsTextAttachmentView)
        self.assertArgIsBOOL(AppKit.NSTextAttachment.setAllowsTextAttachmentView_, 0)
        self.assertResultIsBOOL(AppKit.NSTextAttachment.usesTextAttachmentView)

        self.assertResultIsBOOL(
            AppKit.NSTextAttachmentViewProvider.tracksTextAttachmentViewBounds
        )
        self.assertArgIsBOOL(
            AppKit.NSTextAttachmentViewProvider.setTracksTextAttachmentViewBounds_, 0
        )

    @min_sdk_level("10.11")
    def testProtocolObjects(self):
        self.assertProtocolExists("NSTextAttachmentContainer")
        self.assertProtocolExists("NSTextAttachmentCell")

    def testProtocols(self):
        self.assertArgHasType(
            TestNSTextAttachmentHelper.imageForBounds_textContainer_characterIndex_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.imageForBounds_textContainer_characterIndex_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestNSTextAttachmentHelper.attachmentBoundsForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.attachmentBoundsForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            2,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.attachmentBoundsForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestNSTextAttachmentHelper.drawWithFrame_inView_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultIsBOOL(TestNSTextAttachmentHelper.wantsToTrackMouse)
        self.assertArgIsBOOL(TestNSTextAttachmentHelper.highlight_withFrame_inView_, 0)
        self.assertArgHasType(
            TestNSTextAttachmentHelper.highlight_withFrame_inView_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertResultIsBOOL(
            TestNSTextAttachmentHelper.trackMouse_inRect_ofView_untilMouseUp_
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.trackMouse_inRect_ofView_untilMouseUp_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgIsBOOL(
            TestNSTextAttachmentHelper.trackMouse_inRect_ofView_untilMouseUp_, 3
        )
        self.assertResultHasType(
            TestNSTextAttachmentHelper.cellSize, AppKit.NSSize.__typestr__
        )
        self.assertResultHasType(
            TestNSTextAttachmentHelper.cellBaselineOffset, AppKit.NSPoint.__typestr__
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_layoutManager_,
            0,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_layoutManager_,
            2,
            objc._C_NSUInteger,
        )
        self.assertResultIsBOOL(
            TestNSTextAttachmentHelper.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_,  # noqa: B950
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_,
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_,
            3,
            objc._C_NSUInteger,
        )

        self.assertResultHasType(
            TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            1,
            AppKit.NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            2,
            AppKit.NSPoint.__typestr__,
        )
        self.assertArgHasType(
            TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_,  # noqa: B950
            3,
            objc._C_NSUInteger,
        )
