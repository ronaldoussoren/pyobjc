import InputMethodKit
from PyObjCTools.TestSupport import TestCase


class TestIMKCandidates(TestCase):
    def test_enums(self):
        self.assertIsEnumType(InputMethodKit.IMKCandidatePanelType)
        self.assertEqual(InputMethodKit.kIMKSingleColumnScrollingCandidatePanel, 1)
        self.assertEqual(InputMethodKit.kIMKScrollingGridCandidatePanel, 2)
        self.assertEqual(InputMethodKit.kIMKSingleRowSteppingCandidatePanel, 3)

        self.assertIsEnumType(InputMethodKit.IMKCandidatesLocationHint)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesAboveHint, 1)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesBelowHint, 2)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesLeftHint, 3)
        self.assertEqual(InputMethodKit.kIMKLocateCandidatesRightHint, 4)

        self.assertIsEnumType(InputMethodKit.IMKStyleType)
        self.assertEqual(InputMethodKit.kIMKMain, 0)
        self.assertEqual(InputMethodKit.kIMKAnnotation, 1)
        self.assertEqual(InputMethodKit.kIMKSubList, 2)

    def test_constants(self):
        self.assertIsInstance(InputMethodKit.IMKCandidatesOpacityAttributeName, str)
        self.assertIsInstance(InputMethodKit.IMKCandidatesSendServerKeyEventFirst, str)

    def test_methods(self):
        self.assertResultIsBOOL(InputMethodKit.IMKCandidates.isVisible)
        self.assertResultIsBOOL(InputMethodKit.IMKCandidates.dismissesAutomatically)
        self.assertArgIsBOOL(InputMethodKit.IMKCandidates.setDismissesAutomatically_, 0)

        self.assertResultIsBOOL(
            InputMethodKit.IMKCandidates.selectCandidateWithIdentifier_
        )
