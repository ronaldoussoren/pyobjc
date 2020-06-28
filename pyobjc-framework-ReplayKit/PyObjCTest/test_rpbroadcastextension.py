from PyObjCTools.TestSupport import TestCase

import ReplayKit


class TestRPBroadcast(TestCase):
    def test_constants(self):
        self.assertEqual(ReplayKit.RPSampleBufferTypeVideo, 1)
        self.assertEqual(ReplayKit.RPSampleBufferTypeAudioApp, 2)
        self.assertEqual(ReplayKit.RPSampleBufferTypeAudioMic, 3)

        self.assertIsInstace(ReplayKit.RPVideoSampleOrientationKey, str)
        self.assertIsInstace(ReplayKit.RPApplicationInfoBundleIdentifierKey, str)

    def test_methods(self):
        self.asssertArgIsBlock(
            ReplayKit.NSExtensionContext.loadBroadcastingApplicationInfoWithCompletion_,
            0,
            b"v@@@",
        )
