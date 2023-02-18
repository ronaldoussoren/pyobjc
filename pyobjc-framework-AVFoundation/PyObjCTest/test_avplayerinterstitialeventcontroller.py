import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerInterstitialEventController(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(AVFoundation.AVPlayerInterstitialEventRestrictions)
        self.assertIsTypedEnum(AVFoundation.AVPlayerInterstitialEventCue, str)
        self.assertIsEnumType(
            AVFoundation.AVPlayerInterstitialEventAssetListResponseStatus
        )

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

        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventAssetListResponseStatusAvailable, 0
        )
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventAssetListResponseStatusCleared, 1
        )
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventAssetListResponseStatusUnavailable, 2
        )

    @min_os_level("11.3")
    def test_constants11_3(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerWaitingDuringInterstitialEventReason, str
        )

    @min_os_level("13.3")
    def test_constants13_3(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeEventKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeErrorKey,
            str,
        )

    @min_os_level("13.0")
    def test_constants13_0(self):
        self.assertIsInstance(AVFoundation.AVPlayerInterstitialEventNoCue, str)
        self.assertIsInstance(AVFoundation.AVPlayerInterstitialEventJoinCue, str)
        self.assertIsInstance(AVFoundation.AVPlayerInterstitialEventLeaveCue, str)

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerItem.automaticallyHandlesInterstitialEvents
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerItem.setAutomaticallyHandlesInterstitialEvents_, 0
        )

    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.alignsStartWithPrimarySegmentBoundary
        )
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.alignsResumptionWithPrimarySegmentBoundary
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayerInterstitialEvent.willPlayOnce)

        self.assertResultIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.alignsStartWithPrimarySegmentBoundary
        )
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.alignsResumptionWithPrimarySegmentBoundary
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayerInterstitialEvent.willPlayOnce)
