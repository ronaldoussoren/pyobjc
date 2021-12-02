import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVSampleCursor(TestCase):
    @min_os_level("10.10")
    def testMethods10_10(self):
        self.assertArgHasType(
            AVFoundation.AVSampleCursor.stepByDecodeTime_wasPinned_, 1, b"o^Z"
        )
        self.assertArgHasType(
            AVFoundation.AVSampleCursor.stepByPresentationTime_wasPinned_,
            1,
            b"o^Z",  # noqa: B950
        )

        self.assertResultIsBOOL(
            AVFoundation.AVSampleCursor.samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor_  # noqa: B950
        )
        self.assertResultIsBOOL(
            AVFoundation.AVSampleCursor.samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor_  # noqa: B950
        )

    def testStructs(self):
        v = AVFoundation.AVSampleCursorSyncInfo()
        self.assertIsInstance(v.sampleIsFullSync, bool)
        self.assertIsInstance(v.sampleIsPartialSync, bool)
        self.assertIsInstance(v.sampleIsDroppable, bool)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVSampleCursorDependencyInfo()
        self.assertIsInstance(
            v.sampleIndicatesWhetherItHasDependentSamples, bool
        )  # noqa: B950
        self.assertIsInstance(v.sampleHasDependentSamples, bool)
        self.assertIsInstance(v.sampleIndicatesWhetherItDependsOnOthers, bool)
        self.assertIsInstance(v.sampleDependsOnOthers, bool)
        self.assertIsInstance(
            v.sampleIndicatesWhetherItHasRedundantCoding, bool
        )  # noqa: B950
        self.assertIsInstance(v.sampleHasRedundantCoding, bool)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVSampleCursorStorageRange()
        self.assertIsInstance(v.offset, int)
        self.assertIsInstance(v.length, int)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVSampleCursorChunkInfo()
        self.assertIsInstance(v.chunkSampleCount, int)
        self.assertIsInstance(v.chunkHasUniformSampleSizes, bool)
        self.assertIsInstance(v.chunkHasUniformSampleDurations, bool)
        self.assertIsInstance(v.chunkHasUniformFormatDescriptions, bool)
        self.assertPickleRoundTrips(v)

        v = AVFoundation.AVSampleCursorAudioDependencyInfo()
        self.assertIsInstance(v.audioSampleIsIndependentlyDecodable, bool)
        self.assertIsInstance(v.audioSamplePacketRefreshCount, int)
        self.assertPickleRoundTrips(v)
