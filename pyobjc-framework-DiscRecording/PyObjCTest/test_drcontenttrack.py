from PyObjCTools.TestSupport import *

import DiscRecording

class TestDRContentTrack (TestCase):
    def testFunctions(self):
        self.assertResultIsCFRetained(DiscRecording.DRFilesystemTrackCreate)

        DiscRecording.DRFilesystemTrackEstimateOverhead

        self.assertResultIsCFRetained(DiscRecording.DRAudioTrackCreate)
        self.assertArgIsIn(DiscRecording.DRAudioTrackCreate, 0)

        self.assertResultIsCFRetained(DiscRecording.DRAudioTrackCreateWithURL)

if __name__ == "__main__":
    main()
