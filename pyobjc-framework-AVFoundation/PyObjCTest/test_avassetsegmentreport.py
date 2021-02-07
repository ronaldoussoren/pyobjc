import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVAssetSegmentReport(TestCase):
    def test_constants(self):
        self.assertEqual(AVFoundation.AVAssetSegmentTypeInitialization, 1)
        self.assertEqual(AVFoundation.AVAssetSegmentTypeSeparable, 2)
