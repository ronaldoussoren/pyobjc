
from PyObjCTools.TestSupport import *
from InputMethodKit import *

class TestIMKCandidates (TestCase):
    def testConstants(self):
        self.assertEqual(kIMKSingleColumnScrollingCandidatePanel, 1)
        self.assertEqual(kIMKScrollingGridCandidatePanel, 2)
        self.assertEqual(kIMKSingleRowSteppingCandidatePanel, 3)

        self.assertEqual(kIMKLocateCandidatesAboveHint, 1)
        self.assertEqual(kIMKLocateCandidatesBelowHint, 2)
        self.assertEqual(kIMKLocateCandidatesLeftHint, 3)
        self.assertEqual(kIMKLocateCandidatesRightHint, 4)

        self.assertIsInstance(IMKCandidatesOpacityAttributeName, unicode)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(IMKCandidatesSendServerKeyEventFirst, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(IMKCandidates.isVisible)
        self.assertResultIsBOOL(IMKCandidates.dismissesAutomatically)
        self.assertArgIsBOOL(IMKCandidates.setDismissesAutomatically_, 0)


if __name__ == "__main__":
    main()
