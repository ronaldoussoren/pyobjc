import InputMethodKit
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestIMKCandidates(TestCase):
    def testConstants(self):
        self.assertEqual(InputMethodKit.kIMKSingleColumnScrollingCandidatePanel, 1)
        self.assertEqual(InputMethodKit.kIMKScrollingGridCandidatePanel, 2)
        self.assertEqual(InputMethodKit.kIMKSingleRowSteppingCandidatePanel, 3)

        self.assertEqual(InputMethodKit.kIMKLocateCandidatesAboveHint, 1)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesBelowHint, 2)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesLeftHint, 3)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesRightHint, 4)

        self.assertEqual(InputMethodKit.kIMKMain, 0)
        self.assertEqual(InputMethodKit.kIMKAnnotation, 1)
        self.assertEqual(InputMethodKit.kIMKSubList, 2)

        self.assertIsInstance(InputMethodKit.IMKCandidatesOpacityAttributeName, str)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(InputMethodKit.IMKCandidatesSendServerKeyEventFirst, str)

    def testMethods(self):
        self.assertResultIsBOOL(InputMethodKit.IMKCandidates.isVisible)
        self.assertResultIsBOOL(InputMethodKit.IMKCandidates.dismissesAutomatically)
        self.assertArgIsBOOL(InputMethodKit.IMKCandidates.setDismissesAutomatically_, 0)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(
            InputMethodKit.IMKCandidates.selectCandidateWithIdentifier_
        )
