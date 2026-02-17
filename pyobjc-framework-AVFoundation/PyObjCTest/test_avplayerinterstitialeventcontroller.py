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

        self.assertIsEnumType(AVFoundation.AVPlayerInterstitialEventTimelineOccupancy)
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventTimelineOccupancySinglePoint, 0
        )
        self.assertEqual(AVFoundation.AVPlayerInterstitialEventTimelineOccupancyFill, 1)

        self.assertIsEnumType(AVFoundation.AVPlayerInterstitialEventSkippableEventState)
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventSkippableEventStateNotSkippable, 0
        )
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventSkippableEventStateNotYetEligible, 1
        )
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventSkippableEventStateEligible, 2
        )
        self.assertEqual(
            AVFoundation.AVPlayerInterstitialEventSkippableEventStateNoLongerEligible, 3
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

    @min_os_level("26.0")
    def test_constants26_0(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeEventKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeStateKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventSkippableStateDidChangeSkipControlLabelKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventSkippedNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorCurrentEventSkippedEventKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledEventKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventWasUnscheduledErrorKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventDidFinishNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventDidFinishEventKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventDidFinishPlayoutTimeKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorInterstitialEventDidFinishDidPlayEntireEventKey,
            str,
        )

    @min_os_level("26.4")
    def test_constants26_4(self):
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorScheduleRequestCompletedNotification,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorScheduleRequestIdentifierKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorScheduleRequestResponseKey,
            str,
        )
        self.assertIsInstance(
            AVFoundation.AVPlayerInterstitialEventMonitorScheduleRequestErrorKey,
            str,
        )

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

    @min_os_level("15.0")
    def test_methods15_0(self):
        self.assertResultIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.supplementsPrimaryContent
        )
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.setSupplementsPrimaryContent_, 0
        )
        self.assertResultIsBOOL(AVFoundation.AVPlayerInterstitialEvent.contentMayVary)
        self.assertArgIsBOOL(
            AVFoundation.AVPlayerInterstitialEvent.setContentMayVary_, 0
        )

        self.assertResultHasType(
            AVFoundation.AVPlayerInterstitialEvent.plannedDuration,
            AVFoundation.CMTime.__typestr__,
        )

    @min_os_level("26.0")
    def test_methods26_0(self):
        self.assertResultHasType(
            AVFoundation.AVPlayerInterstitialEvent.skipControlTimeRange,
            AVFoundation.CMTimeRange.__typestr__,
        )
        self.assertResultHasType(
            AVFoundation.AVPlayerInterstitialEvent.skipControlTimeRange,
            AVFoundation.CMTimeRange.__typestr__,
        )
