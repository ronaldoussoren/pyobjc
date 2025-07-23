from PyObjCTools.TestSupport import TestCase

import AVKit


class TestAVKitTypes(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVKit.AVVideoFrameAnalysisType)
        self.assertEqual(AVKit.AVVideoFrameAnalysisTypeNone, 0)
        self.assertEqual(AVKit.AVVideoFrameAnalysisTypeDefault, 1 << 0)
        self.assertEqual(AVKit.AVVideoFrameAnalysisTypeText, 1 << 1)
        self.assertEqual(AVKit.AVVideoFrameAnalysisTypeSubject, 1 << 2)
        self.assertEqual(AVKit.AVVideoFrameAnalysisTypeVisualSearch, 1 << 3)
        self.assertEqual(AVKit.AVVideoFrameAnalysisTypeMachineReadableCode, 1 << 4)

        self.assertIsEnumType(AVKit.AVDisplayDynamicRange)
        self.assertEqual(AVKit.AVDisplayDynamicRangeAutomatic, 0)
        self.assertEqual(AVKit.AVDisplayDynamicRangeStandard, 1)
        self.assertEqual(AVKit.AVDisplayDynamicRangeConstrainedHigh, 2)
        self.assertEqual(AVKit.AVDisplayDynamicRangeHigh, 3)
