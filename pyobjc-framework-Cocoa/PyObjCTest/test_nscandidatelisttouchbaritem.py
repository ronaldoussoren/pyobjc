import AppKit
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestNSCandidateListTouchBarItemHelper(AppKit.NSObject):
    def candidateListTouchBarItem_beginSelectingCandidateAtIndex_(self, item, index):
        pass

    def candidateListTouchBarItem_changeSelectionFromCandidateAtIndex_toIndex_(
        self, item, index, index2
    ):
        pass

    def candidateListTouchBarItem_endSelectingCandidateAtIndex_(self, item, index):
        pass

    def candidateListTouchBarItem_changedCandidateListVisibility_(self, item, flag):
        pass


class TestNSCandidateListTouchBarItem(TestCase):
    @min_sdk_level("10.12")
    def testProtocoObjects10_12(self):
        self.assertProtocolExists("NSCandidateListTouchBarItemDelegate")

    @min_os_level("10.12")
    def testConstants10_12(self):
        self.assertIsInstance(AppKit.NSTouchBarItemIdentifierCandidateList, str)

    @min_os_level("10.12")
    def testMethods10_12(self):
        self.assertResultIsBOOL(AppKit.NSCandidateListTouchBarItem.isCollapsed)
        self.assertArgIsBOOL(AppKit.NSCandidateListTouchBarItem.setCollapsed_, 0)

        self.assertResultIsBOOL(AppKit.NSCandidateListTouchBarItem.allowsCollapsing)
        self.assertArgIsBOOL(AppKit.NSCandidateListTouchBarItem.setAllowsCollapsing_, 0)

        self.assertResultIsBOOL(
            AppKit.NSCandidateListTouchBarItem.isCandidateListVisible
        )
        # self.assertArgIsBOOL(AppKit.NSCandidateListTouchBarItem.setCandidateListVisible_, 0)

        self.assertArgIsBOOL(
            AppKit.NSCandidateListTouchBarItem.updateWithInsertionPointVisibility_, 0
        )

        self.assertResultIsBOOL(
            AppKit.NSCandidateListTouchBarItem.allowsTextInputContextCandidates
        )
        self.assertArgIsBOOL(
            AppKit.NSCandidateListTouchBarItem.setAllowsTextInputContextCandidates_, 0
        )

        self.assertResultIsBlock(
            AppKit.NSCandidateListTouchBarItem.attributedStringForCandidate,
            b"@@" + objc._C_NSInteger,
        )
        self.assertArgIsBlock(
            AppKit.NSCandidateListTouchBarItem.setAttributedStringForCandidate_,
            0,
            b"@@" + objc._C_NSInteger,
        )

        self.assertArgHasType(
            TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_beginSelectingCandidateAtIndex_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_changeSelectionFromCandidateAtIndex_toIndex_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_changeSelectionFromCandidateAtIndex_toIndex_,  # noqa: B950
            2,
            objc._C_NSInteger,
        )
        self.assertArgHasType(
            TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_endSelectingCandidateAtIndex_,  # noqa: B950
            1,
            objc._C_NSInteger,
        )
        self.assertArgIsBOOL(
            TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_changedCandidateListVisibility_,  # noqa: B950
            1,
        )
