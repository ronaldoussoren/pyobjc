
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTextAttachmentHelper (NSObject):
    def drawWithFrame_inView_(self, fr, vi): pass
    def wantsToTrackMouse(self): return 1
    def highlight_withFrame_inView_(self, fl, fr, vi): pass
    def trackMouse_inRect_ofView_untilMouseUp_(self, ev, fr, vi, fl): pass
    def cellSize(self): return 1
    def cellBaselineOffset(self): return 1
    def drawWithFrame_inView_characterIndex_(self, fr, vi, i): pass
    def drawWithFrame_inView_characterIndex_layoutManager_(self, fr, vi, i, lm): pass
    def wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_(self, ev, fr, vi, i): return 1
    def trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_(self, ev, fr, vi, i, fl): return 1
    def cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_(self, tc, fr, po, i): return 1

class TestNSTextAttachment (TestCase):
    def testConstants(self):
        self.assertEqual(NSAttachmentCharacter, unichr(0xfffc))

    def testMethods(self):
        self.assertResultIsBOOL(NSTextAttachmentCell.wantsToTrackMouse)
        self.assertArgIsBOOL(NSTextAttachmentCell.highlight_withFrame_inView_, 0)
        self.assertResultIsBOOL(NSTextAttachmentCell.trackMouse_inRect_ofView_untilMouseUp_)
        self.assertArgIsBOOL(NSTextAttachmentCell.trackMouse_inRect_ofView_untilMouseUp_, 3)
        self.assertResultIsBOOL(NSTextAttachmentCell.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_)
        self.assertResultIsBOOL(NSTextAttachmentCell.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_)
        self.assertArgIsBOOL(NSTextAttachmentCell.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_, 4)

    def testProtocols(self):
        self.assertArgHasType(TestNSTextAttachmentHelper.drawWithFrame_inView_, 0, NSRect.__typestr__)
        self.assertResultIsBOOL(TestNSTextAttachmentHelper.wantsToTrackMouse)
        self.assertArgIsBOOL(TestNSTextAttachmentHelper.highlight_withFrame_inView_, 0)
        self.assertArgHasType(TestNSTextAttachmentHelper.highlight_withFrame_inView_, 1, NSRect.__typestr__)
        self.assertResultIsBOOL(TestNSTextAttachmentHelper.trackMouse_inRect_ofView_untilMouseUp_)
        self.assertArgHasType(TestNSTextAttachmentHelper.trackMouse_inRect_ofView_untilMouseUp_, 1, NSRect.__typestr__)
        self.assertArgIsBOOL(TestNSTextAttachmentHelper.trackMouse_inRect_ofView_untilMouseUp_, 3)
        self.assertResultHasType(TestNSTextAttachmentHelper.cellSize, NSSize.__typestr__)
        self.assertResultHasType(TestNSTextAttachmentHelper.cellBaselineOffset, NSPoint.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_, 0, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_, 2, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_layoutManager_, 0, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.drawWithFrame_inView_characterIndex_layoutManager_, 2, objc._C_NSUInteger)
        self.assertResultIsBOOL(TestNSTextAttachmentHelper.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_)
        self.assertArgHasType(TestNSTextAttachmentHelper.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_, 1, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.wantsToTrackMouseForEvent_inRect_ofView_atCharacterIndex_, 3, objc._C_NSUInteger)
        self.assertArgHasType(TestNSTextAttachmentHelper.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_, 1, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.trackMouse_inRect_ofView_atCharacterIndex_untilMouseUp_, 3, objc._C_NSUInteger)

        self.assertResultHasType(TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 1, NSRect.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 2, NSPoint.__typestr__)
        self.assertArgHasType(TestNSTextAttachmentHelper.cellFrameForTextContainer_proposedLineFragment_glyphPosition_characterIndex_, 3, objc._C_NSUInteger)



if __name__ == "__main__":
    main()
