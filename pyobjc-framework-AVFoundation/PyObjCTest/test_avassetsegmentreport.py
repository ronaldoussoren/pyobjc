import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVAssetSegmentReport(TestCase):

    def test_enums(self):
        self.assertIsEnumType(AVFoundation.AVAssetSegmentType)
        self.assertEqual(AVFoundation.AVAssetSegmentTypeInitialization, 1)
        self.assertEqual(AVFoundation.AVAssetSegmentTypeSeparable, 2)
