import CoreMedia
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestCMTimeRange(TestCase):
    def test_structs(self):
        v = CoreMedia.CMTimeRange()
        self.assertEqual(v.start, CoreMedia.CMTime())
        self.assertEqual(v.duration, CoreMedia.CMTime())
        self.assertPickleRoundTrips(v)

        v = CoreMedia.CMTimeMapping()
        self.assertEqual(v.source, CoreMedia.CMTimeRange())
        self.assertEqual(v.target, CoreMedia.CMTimeRange())
        self.assertPickleRoundTrips(v)

    def test_constants(self):
        self.assertIsInstance(CoreMedia.kCMTimeRangeZero, CoreMedia.CMTimeRange)
        self.assertIsInstance(CoreMedia.kCMTimeRangeInvalid, CoreMedia.CMTimeRange)

        self.assertIsInstance(CoreMedia.kCMTimeRangeStartKey, str)
        self.assertIsInstance(CoreMedia.kCMTimeRangeDurationKey, str)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(CoreMedia.kCMTimeMappingInvalid, CoreMedia.CMTimeMapping)

        self.assertIsInstance(CoreMedia.kCMTimeMappingSourceKey, str)
        self.assertIsInstance(CoreMedia.kCMTimeMappingTargetKey, str)

    def test_functions(self):
        rng = CoreMedia.CMTimeRange(
            start=CoreMedia.CMTimeMake(100, 1), duration=CoreMedia.CMTimeMake(80, 1)
        )
        self.assertTrue(CoreMedia.CMTIMERANGE_IS_VALID(rng))
        self.assertFalse(CoreMedia.CMTIMERANGE_IS_INVALID(rng))

        rng = CoreMedia.CMTimeRange(
            start=CoreMedia.CMTimeMake(100, 1), duration=CoreMedia.kCMTimeInvalid
        )
        self.assertTrue(CoreMedia.CMTIMERANGE_IS_INVALID(rng))
        self.assertFalse(CoreMedia.CMTIMERANGE_IS_VALID(rng))

        rng = CoreMedia.CMTimeRange(
            start=CoreMedia.CMTimeMake(100, 1), duration=CoreMedia.kCMTimeIndefinite
        )
        self.assertTrue(CoreMedia.CMTIMERANGE_IS_INDEFINITE(rng))

        rng = CoreMedia.CMTimeRange(
            duration=CoreMedia.CMTimeMake(100, 1), start=CoreMedia.kCMTimeIndefinite
        )
        self.assertTrue(CoreMedia.CMTIMERANGE_IS_INDEFINITE(rng))

        rng = CoreMedia.CMTimeRange(
            duration=CoreMedia.CMTimeMake(100, 1), start=CoreMedia.CMTimeMake(0, 1)
        )
        self.assertFalse(CoreMedia.CMTIMERANGE_IS_INDEFINITE(rng))

        rng = CoreMedia.CMTimeRange(
            start=CoreMedia.CMTimeMake(100, 1), duration=CoreMedia.CMTimeMake(0, 1)
        )
        self.assertTrue(CoreMedia.CMTIMERANGE_IS_EMPTY(rng))

        rng = CoreMedia.CMTimeRange(
            start=CoreMedia.CMTimeMake(100, 1), duration=CoreMedia.CMTimeMake(10, 1)
        )
        self.assertFalse(CoreMedia.CMTIMERANGE_IS_EMPTY(rng))

        CoreMedia.CMTimeRangeMake
        CoreMedia.CMTimeRangeGetUnion
        CoreMedia.CMTimeRangeGetIntersection
        CoreMedia.CMTimeRangeEqual
        CoreMedia.CMTimeRangeContainsTime
        CoreMedia.CMTimeRangeContainsTimeRange
        CoreMedia.CMTimeRangeGetEnd
        CoreMedia.CMTimeMapTimeFromRangeToRange
        CoreMedia.CMTimeClampToRange
        CoreMedia.CMTimeMapDurationFromRangeToRange
        CoreMedia.CMTimeRangeFromTimeToTime

        self.assertResultIsCFRetained(CoreMedia.CMTimeRangeCopyAsDictionary)

        CoreMedia.CMTimeRangeMakeFromDictionary

        self.assertResultIsCFRetained(CoreMedia.CMTimeRangeCopyDescription)

        CoreMedia.CMTimeRangeShow

        mp = CoreMedia.CMTimeMappingMakeEmpty(rng)
        self.assertTrue(CoreMedia.CMTIMEMAPPING_IS_EMPTY(mp))
        self.assertTrue(CoreMedia.CMTIMEMAPPING_IS_VALID(mp))
        self.assertFalse(CoreMedia.CMTIMEMAPPING_IS_INVALID(mp))

        mp = CoreMedia.CMTimeMappingMake(
            rng,
            CoreMedia.CMTimeRange(
                start=CoreMedia.CMTimeMake(100, 1), duration=CoreMedia.kCMTimeInvalid
            ),
        )
        self.assertFalse(CoreMedia.CMTIMEMAPPING_IS_VALID(mp))
        self.assertTrue(CoreMedia.CMTIMEMAPPING_IS_INVALID(mp))

        mp = CoreMedia.CMTimeMappingMake(rng, rng)
        self.assertFalse(CoreMedia.CMTIMEMAPPING_IS_EMPTY(mp))

    @min_os_level("10.11")
    def test_functions10_11(self):
        CoreMedia.CMTimeMappingMake
        CoreMedia.CMTimeMappingMakeEmpty

        self.assertResultIsCFRetained(CoreMedia.CMTimeMappingCopyAsDictionary)

        CoreMedia.CMTimeMappingMakeFromDictionary

        self.assertResultIsCFRetained(CoreMedia.CMTimeMappingCopyDescription)

        CoreMedia.CMTimeMappingShow

    @min_os_level("10.14")
    def test_functions10_14(self):
        CoreMedia.CMTimeFoldIntoRange
