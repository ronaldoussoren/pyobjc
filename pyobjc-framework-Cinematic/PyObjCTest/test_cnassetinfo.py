from PyObjCTools.TestSupport import TestCase, min_os_level

import Cinematic


class TestCNAssetInfo(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Cinematic.CNCinematicResourceVersion)
        self.assertEqual(Cinematic.CNCinematicResourceVersion1, 1)

        self.assertIsEnumType(Cinematic.CNCinematicCapability)
        self.assertEqual(Cinematic.CNCinematicCapabilityNone, 0)
        self.assertEqual(Cinematic.CNCinematicCapabilityRenderable, 1)
        self.assertEqual(Cinematic.CNCinematicCapabilityNeedsPreprocessing, 2)

        self.assertIsEnumType(Cinematic.CNResourceStatus)
        self.assertEqual(Cinematic.CNResourceStatusReady, 0)
        self.assertEqual(Cinematic.CNResourceStatusNeedsDownloading, 1)
        self.assertEqual(Cinematic.CNResourceStatusUnsupportedDevice, 2)
        self.assertEqual(Cinematic.CNResourceStatusUnsupportedAsset, 3)

    def test_methods(self):
        self.assertArgIsBlock(
            Cinematic.CNAssetInfo.loadFromAsset_completionHandler_, 1, b"v@@"
        )

        self.assertResultIsBOOL(
            Cinematic.CNCompositionInfo.insertTimeRange_ofCinematicAssetInfo_atTime_error_
        )
        self.assertArgIsOut(
            Cinematic.CNCompositionInfo.insertTimeRange_ofCinematicAssetInfo_atTime_error_,
            3,
        )

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            Cinematic.CNAssetPreprocessConfiguration.referenceSourceAssetTracks
        )
        self.assertArgIsBOOL(
            Cinematic.CNAssetPreprocessConfiguration.setReferenceSourceAssetTracks_, 0
        )

        self.assertArgIsBlock(
            Cinematic.CNAssetInfo.checkCinematicCapabilityForAsset_completionHandler_,
            1,
            b"vq",
        )

        self.assertArgIsBlock(
            Cinematic.CNAssetInfo.checkIfCinematic_completionHandler_, 1, b"vZ"
        )

        self.assertArgIsBlock(
            Cinematic.CNAssetInfo.downloadResourcesForVersions_timeout_completionHandler_,
            2,
            b"v@",
        )

        self.assertArgIsBlock(
            Cinematic.CNAssetInfo.downloadResourcesWithTimeout_completionHandler_,
            1,
            b"v@@",
        )

        self.assertArgIsBlock(
            Cinematic.CNAssetInfo.preprocessAssetWithConfiguration_completionHandler_,
            1,
            b"v@@",
        )

        self.assertResultIsBOOL(Cinematic.CNAssetInfo.isPreprocessed)
        self.assertArgIsBOOL(Cinematic.CNAssetInfo.setPreprocessed_, 0)
