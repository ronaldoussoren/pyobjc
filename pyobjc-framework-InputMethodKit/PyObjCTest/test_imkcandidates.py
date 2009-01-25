
from PyObjCTools.TestSupport import *
from InputMethodKit import *

class TestIMKCandidates (TestCase):
    def testConstants(self):
        self.failUnlessEqual(kIMKSingleColumnScrollingCandidatePanel, 1)
        self.failUnlessEqual(kIMKScrollingGridCandidatePanel, 2)
        self.failUnlessEqual(kIMKSingleRowSteppingCandidatePanel, 3)

        self.failUnlessEqual(kIMKLocateCandidatesAboveHint, 1)
        self.failUnlessEqual(kIMKLocateCandidatesBelowHint, 2)
        self.failUnlessEqual(kIMKLocateCandidatesLeftHint, 3)
        self.failUnlessEqual(kIMKLocateCandidatesRightHint, 4)

        self.failUnlessIsInstance(IMKCandidatesOpacityAttributeName, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(IMKCandidates.isVisible)
        self.failUnlessResultIsBOOL(IMKCandidates.dismissesAutomatically)
        self.failUnlessArgIsBOOL(IMKCandidates.setDismissesAutomatically_, 0)


if __name__ == "__main__":
    main()
