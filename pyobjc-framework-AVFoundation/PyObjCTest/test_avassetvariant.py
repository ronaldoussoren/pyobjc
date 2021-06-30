import AVFoundation
from PyObjCTools.TestSupport import TestCase


class TestAVAssetVariant(TestCase):
    def test_constants(self):
        self.assertEqual(AVFoundation.AVEnvironmentalConditionDefault, 0)
        self.assertEqual(
            AVFoundation.AVEnvironmentalConditionOnExpensiveNetwork, 1 << 0
        )
