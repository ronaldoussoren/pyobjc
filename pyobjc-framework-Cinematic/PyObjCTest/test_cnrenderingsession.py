from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNRenderingSession(TestCase):
    def test_constants(self):
        self.assertIsEnumType(Cinematic.CNRenderingQuality)
        self.assertEqual(Cinematic.CNRenderingQualityThumbnail, 0)
        self.assertEqual(Cinematic.CNRenderingQualityPreview, 1)
        self.assertEqual(Cinematic.CNRenderingQualityExport, 2)
        self.assertEqual(Cinematic.CNRenderingQualityExportHigh, 3)

    def test_methods(self):
        self.assertArgIsBlock(
            Cinematic.CNRenderingSessionAttributes.loadFromAsset_completionHandler_,
            1,
            b"v@@",
        )

        self.assertResultIsBOOL(
            Cinematic.CNRenderingSession.encodeRenderToCommandBuffer_frameAttributes_sourceImage_sourceDisparity_destinationImage_
        )
        self.assertResultIsBOOL(
            Cinematic.CNRenderingSession.encodeRenderToCommandBuffer_frameAttributes_sourceImage_sourceDisparity_destinationRGBA_
        )
