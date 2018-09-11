from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMTimeRange (TestCase):
    def test_structs(self):
        v = CoreMedia.CMTimeRange()
        self.assertEqual(v.start, CoreMedia.CMTime())
        self.assertEqual(v.duration, CoreMedia.CMTime())

        v = CoreMedia.CMTimeMapping()
        self.assertEqual(v.source, CoreMedia.CMTimeRange())
        self.assertEqual(v.target, CoreMedia.CMTimeRange())

    def test_constants(self):
        self.assertIsInstance(CoreMedia.kCMTimeRangeZero, CoreMedia.CMTimeRange)
        self.assertIsInstance(CoreMedia.kCMTimeRangeInvalid, CoreMedia.CMTimeRange)

        self.assertIsInstance(CoreMedia.kCMTimeRangeStartKey, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeRangeDurationKey, unicode)

    @min_os_level('10.11')
    def test_constants10_11(self):
        self.assertIsInstance(CoreMedia.kCMTimeMappingInvalid, CoreMedia.CMTimeMapping)

        self.assertIsInstance(CoreMedia.kCMTimeMappingSourceKey, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeMappingTargetKey, unicode)

    def test_functions(self):
        CoreMedia.CMTIMERANGE_IS_VALID
        CoreMedia.CMTIMERANGE_IS_INVALID
        CoreMedia.CMTIMERANGE_IS_INDEFINITE
        CoreMedia.CMTIMERANGE_IS_EMPTY

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

        CoreMedia.CMTIMEMAPPING_IS_VALID
        CoreMedia.CMTIMEMAPPING_IS_INVALID
        CoreMedia.CMTIMEMAPPING_IS_EMPTY

    @min_os_level('10.11')
    def test_functions10_11(self):
        CoreMedia.CMTimeMappingMake
        CoreMedia.CMTimeMappingMakeEmpty

        self.assertResultIsCFRetained(CoreMedia.CMTimeMappingCopyAsDictionary)

        CoreMedia.CMTimeMappingMakeFromDictionary

        self.assertResultIsCFRetained(CoreMedia.CMTimeMappingCopyDescription)

        CoreMedia.CMTimeMappingShow

    @min_os_level('10.14')
    def test_functions10_14(self):
        CoreMedia.CMTimeFoldIntoRange

if __name__ == "__main__":
    main()
