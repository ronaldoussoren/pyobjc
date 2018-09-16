from PyObjCTools.TestSupport import *

import CoreMedia

class TestCMTime (TestCase):
    def test_constants(self):
        self.assertEqual(CoreMedia.kCMTimeMaxTimescale, 0x7fffffff)

        self.assertEqual(CoreMedia.kCMTimeFlags_Valid, 1<<0)
        self.assertEqual(CoreMedia.kCMTimeFlags_HasBeenRounded, 1<<1)
        self.assertEqual(CoreMedia.kCMTimeFlags_PositiveInfinity, 1<<2)
        self.assertEqual(CoreMedia.kCMTimeFlags_NegativeInfinity, 1<<3)
        self.assertEqual(CoreMedia.kCMTimeFlags_Indefinite, 1<<4)
        self.assertEqual(CoreMedia.kCMTimeFlags_ImpliedValueFlagsMask, CoreMedia.kCMTimeFlags_PositiveInfinity | CoreMedia.kCMTimeFlags_NegativeInfinity | CoreMedia.kCMTimeFlags_Indefinite)

        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_RoundHalfAwayFromZero, 1)
        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_RoundTowardZero, 2)
        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_RoundAwayFromZero, 3)
        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_QuickTime, 4)
        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_RoundTowardPositiveInfinity, 5)
        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_RoundTowardNegativeInfinity, 6)
        self.assertEqual(CoreMedia.kCMTimeRoundingMethod_Default, CoreMedia.kCMTimeRoundingMethod_RoundHalfAwayFromZero)

    def test_structs(self):
        v = CoreMedia.CMTime()
        self.assertEqual(v.value, 0)
        self.assertEqual(v.timescale, 0)
        self.assertEqual(v.flags, 0)
        self.assertEqual(v.epoch, 0)

    def test_contants(self):
        self.assertIsInstance(CoreMedia.kCMTimeInvalid, CoreMedia.CMTime)
        self.assertIsInstance(CoreMedia.kCMTimeIndefinite, CoreMedia.CMTime)
        self.assertIsInstance(CoreMedia.kCMTimePositiveInfinity, CoreMedia.CMTime)
        self.assertIsInstance(CoreMedia.kCMTimeNegativeInfinity, CoreMedia.CMTime)
        self.assertIsInstance(CoreMedia.kCMTimeZero, CoreMedia.CMTime)

        self.assertIsInstance(CoreMedia.kCMTimeValueKey, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeScaleKey, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeEpochKey, unicode)
        self.assertIsInstance(CoreMedia.kCMTimeFlagsKey, unicode)

    def test_functions(self):
        CoreMedia.CMTIME_IS_VALID
        CoreMedia.CMTIME_IS_INVALID
        CoreMedia.CMTIME_IS_POSITIVE_INFINITY
        CoreMedia.CMTIME_IS_NEGATIVE_INFINITY
        CoreMedia.CMTIME_IS_INDEFINITE
        CoreMedia.CMTIME_IS_NUMERIC
        CoreMedia.CMTIME_HAS_BEEN_ROUNDED

        CoreMedia.CMTimeMake
        CoreMedia.CMTimeMakeWithEpoch
        CoreMedia.CMTimeMakeWithSeconds
        CoreMedia.CMTimeGetSeconds
        CoreMedia.CMTimeConvertScale
        CoreMedia.CMTimeAdd
        CoreMedia.CMTimeSubtract
        CoreMedia.CMTimeMultiply
        CoreMedia.CMTimeMultiplyByFloat64
        CoreMedia.CMTimeCompare

        self.assertFalse(hasattr(CoreMedia, 'CMTIME_COMPARE_INLINE'))

        CoreMedia.CMTimeMinimum
        CoreMedia.CMTimeMaximum
        CoreMedia.CMTimeAbsoluteValue

        self.assertResultIsCFRetained(CoreMedia.CMTimeCopyAsDictionary)

        CoreMedia.CMTimeMakeFromDictionary

        self.assertResultIsCFRetained(CoreMedia.CMTimeCopyDescription)

        CoreMedia.CMTimeShow

    @min_os_level('10.10')
    def test_functions10_10(self):
        CoreMedia.CMTimeMultiplyByRatio





if __name__ == "__main__":
    main()
