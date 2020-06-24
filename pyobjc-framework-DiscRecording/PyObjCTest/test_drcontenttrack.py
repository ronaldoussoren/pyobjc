import DiscRecording
from PyObjCTools.TestSupport import TestCase


class TestDRContentTrack(TestCase):
    def testFunctions(self):
        self.assertResultIsCFRetained(DiscRecording.DRFilesystemTrackCreate)

        DiscRecording.DRFilesystemTrackEstimateOverhead

        self.assertResultIsCFRetained(DiscRecording.DRAudioTrackCreate)
        self.assertArgIsIn(DiscRecording.DRAudioTrackCreate, 0)

        self.assertResultIsCFRetained(DiscRecording.DRAudioTrackCreateWithURL)
