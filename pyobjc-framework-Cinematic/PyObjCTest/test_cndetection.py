from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNDetection(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Cinematic.CNDetectionType)
        self.assertEqual(Cinematic.CNDetectionTypeUnknown, 0)
        self.assertEqual(Cinematic.CNDetectionTypeHumanFace, 1)
        self.assertEqual(Cinematic.CNDetectionTypeHumanHead, 2)
        self.assertEqual(Cinematic.CNDetectionTypeHumanTorso, 3)
        self.assertEqual(Cinematic.CNDetectionTypeCatBody, 4)
        self.assertEqual(Cinematic.CNDetectionTypeDogBody, 5)
        self.assertEqual(Cinematic.CNDetectionTypeCatHead, 9)
        self.assertEqual(Cinematic.CNDetectionTypeDogHead, 10)
        self.assertEqual(Cinematic.CNDetectionTypeSportsBall, 11)
        self.assertEqual(Cinematic.CNDetectionTypeAutoFocus, 100)
        self.assertEqual(Cinematic.CNDetectionTypeFixedFocus, 101)
        self.assertEqual(Cinematic.CNDetectionTypeCustom, 102)

    def test_methods(self):
        self.assertResultIsBOOL(Cinematic.CNDetection.isValidDetectionID_)
        self.assertResultIsBOOL(Cinematic.CNDetection.isValidDetectionGroupID_)
