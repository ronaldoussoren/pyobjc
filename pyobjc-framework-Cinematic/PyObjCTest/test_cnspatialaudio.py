from PyObjCTools.TestSupport import TestCase, min_os_level

import Cinematic


class TestCNSpatialAudio(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Cinematic.CNSpatialAudioRenderingStyle)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleCinematic, 0)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleStudio, 1)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleInFrame, 2)
        self.assertEqual(
            Cinematic.CNSpatialAudioRenderingStyleCinematicBackgroundStem, 3
        )
        self.assertEqual(
            Cinematic.CNSpatialAudioRenderingStyleCinematicForegroundStem, 4
        )
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleStudioForegroundStem, 5)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleInFrameForegroundStem, 6)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleStandard, 7)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleStudioBackgroundStem, 8)
        self.assertEqual(Cinematic.CNSpatialAudioRenderingStyleInFrameBackgroundStem, 9)

        self.assertIsEnumType(Cinematic.CNSpatialAudioContentType)
        self.assertEqual(Cinematic.CNSpatialAudioContentTypeStereo, 0)
        self.assertEqual(Cinematic.CNSpatialAudioContentTypeSpatial, 1)

    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(Cinematic.CNAssetSpatialAudioInfo.isSupported)

        self.assertArgIsBlock(
            Cinematic.CNAssetSpatialAudioInfo.checkIfContainsSpatialAudio_completionHandlder_,
            1,
            b"vZ",
        )
        self.assertArgIsBlock(
            Cinematic.CNAssetSpatialAudioInfo.loadFromAsset_completionHandlder_,
            1,
            b"v@@",
        )
