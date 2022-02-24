import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerInterstitialEventController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVPlayerInterstitialEventRestrictions)

    def testConstants(self):
        self.assertEqual(AVFoundation.AVPlayerInterstitialEventRestrictionNone, 0)
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventRestrictionConstrainsSeekingForwardInPrimaryContent,
            1 << 0,
        )
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventRestrictionRequiresPlaybackAtPreferredRateForAdvancement,
            1 << 2,
        )

        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventRestrictionDefaultPolicy,
            AVFoundation.AVPlayerInterstitialEventRestrictionNone,
        )

    @min_os_level("11.3")
    def test_constants11_3(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingDuringInterstitialEventReason, str
        )

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.automaticallyHandlesInterstitialEvents
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setAutomaticallyHandlesInterstitialEvents_, 0
        )
