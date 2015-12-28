from PyObjCTools.TestSupport import *

import AVFoundation


class TestAVSampleCursor (TestCase):
    @min_os_level('10.10')
    def testMethods10_10(self):
        self.assertArgHasType(AVFoundation.AVSampleCursor.stepByDecodeTime_wasPinned_, 1, b'o^Z')
        self.assertArgHasType(AVFoundation.AVSampleCursor.stepByPresentationTime_wasPinned_, 1, b'o^Z')

        self.assertResultIsBOOL(AVFoundation.AVSampleCursor.samplesWithEarlierDecodeTimeStampsMayHaveLaterPresentationTimeStampsThanCursor_)
        self.assertResultIsBOOL(AVFoundation.AVSampleCursor.samplesWithLaterDecodeTimeStampsMayHaveEarlierPresentationTimeStampsThanCursor_)

    def testStructs(self):
        v = AVFoundation.AVSampleCursorSyncInfo()
        self.assertIsInstance(v.sampleIsFullSync, bool)
        self.assertIsInstance(v.sampleIsPartialSync, bool)
        self.assertIsInstance(v.sampleIsDroppable, bool)

        v = AVFoundation.AVSampleCursorDependencyInfo()
        self.assertIsInstance(v.sampleIndicatesWhetherItHasDependentSamples, bool)
        self.assertIsInstance(v.sampleHasDependentSamples, bool)
        self.assertIsInstance(v.sampleIndicatesWhetherItDependsOnOthers, bool)
        self.assertIsInstance(v.sampleDependsOnOthers, bool)
        self.assertIsInstance(v.sampleIndicatesWhetherItHasRedundantCoding, bool)
        self.assertIsInstance(v.sampleHasRedundantCoding, bool)

        v = AVFoundation.AVSampleCursorStorageRange()
        self.assertIsInstance(v.offset, (int, long))
        self.assertIsInstance(v.length, (int, long))

        v = AVFoundation.AVSampleCursorChunkInfo()
        self.assertIsInstance(v.chunkSampleCount, (int, long))
        self.assertIsInstance(v.chunkHasUniformSampleSizes, bool)
        self.assertIsInstance(v.chunkHasUniformSampleDurations, bool)
        self.assertIsInstance(v.chunkHasUniformFormatDescriptions, bool)

if __name__ == "__main__":
    main()
