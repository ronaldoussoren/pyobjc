from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSCandidateListTouchBarItemHelper (NSObject):
    def candidateListTouchBarItem_beginSelectingCandidateAtIndex_(self, item, index): pass
    def candidateListTouchBarItem_changeSelectionFromCandidateAtIndex_toIndex_(self, item, index, index2): pass
    def candidateListTouchBarItem_endSelectingCandidateAtIndex_(self, item, index): pass
    def candidateListTouchBarItem_changedCandidateListVisibility_(self, item, flag): pass

class TestNSCandidateListTouchBarItem (TestCase):
    @min_sdk_level('10.12')
    def testProtocoObjects10_12(self):
        objc.protocolNamed('NSCandidateListTouchBarItemDelegate')

    @min_os_level('10.12')
    def testConstants10_12(self):
        self.assertIsInstance(NSTouchBarItemIdentifierCandidateList, unicode)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSCandidateListTouchBarItem.isCollapsed)
        self.assertArgIsBOOL(NSCandidateListTouchBarItem.setCollapsed_, 0)

        self.assertResultIsBOOL(NSCandidateListTouchBarItem.allowsCollapsing)
        self.assertArgIsBOOL(NSCandidateListTouchBarItem.setAllowsCollapsing_, 0)

        self.assertResultIsBOOL(NSCandidateListTouchBarItem.isCandidateListVisible)
        #self.assertArgIsBOOL(NSCandidateListTouchBarItem.setCandidateListVisible_, 0)

        self.assertArgIsBOOL(NSCandidateListTouchBarItem.updateWithInsertionPointVisibility_, 0)

        self.assertResultIsBOOL(NSCandidateListTouchBarItem.allowsTextInputContextCandidates)
        self.assertArgIsBOOL(NSCandidateListTouchBarItem.setAllowsTextInputContextCandidates_, 0)

        self.assertResultIsBlock(NSCandidateListTouchBarItem.attributedStringForCandidate, b'@@' + objc._C_NSInteger)
        self.assertArgIsBlock(NSCandidateListTouchBarItem.setAttributedStringForCandidate_, 0, b'@@' + objc._C_NSInteger)

        self.assertArgHasType(TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_beginSelectingCandidateAtIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_changeSelectionFromCandidateAtIndex_toIndex_, 1, objc._C_NSInteger)
        self.assertArgHasType(TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_changeSelectionFromCandidateAtIndex_toIndex_, 2, objc._C_NSInteger)
        self.assertArgHasType(TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_endSelectingCandidateAtIndex_, 1, objc._C_NSInteger)
        self.assertArgIsBOOL(TestNSCandidateListTouchBarItemHelper.candidateListTouchBarItem_changedCandidateListVisibility_, 1)

if __name__ == "__main__":
    main()
