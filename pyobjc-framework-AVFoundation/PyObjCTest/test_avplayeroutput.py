import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVPlayerOutput(TestCase):
    def test_constants(self):
        self.assertIsEnumType(AVFoundation.CMTagCollectionVideoOutputPreset)
        self.assertEqual(AVFoundation.kCMTagCollectionVideoOutputPreset_Monoscopic, 0)
        self.assertEqual(AVFoundation.kCMTagCollectionVideoOutputPreset_Stereoscopic, 1)

    @min_os_level("14.2")
    def test_methods(self):
        self.assertArgIsOut(
            AVFoundation.AVPlayerVideoOutput.copyTaggedBufferGroupForHostTime_presentationTimeStamp_activeConfiguration_,
            1,
        )
        self.assertArgIsOut(
            AVFoundation.AVPlayerVideoOutput.copyTaggedBufferGroupForHostTime_presentationTimeStamp_activeConfiguration_,
            2,
        )

    @min_os_level("14.2")
    def test_functions(self):
        self.assertArgIsOut(AVFoundation.CMTagCollectionCreateWithVideoOutputPreset, 2)
        self.assertArgIsCFRetained(
            AVFoundation.CMTagCollectionCreateWithVideoOutputPreset, 2
        )
