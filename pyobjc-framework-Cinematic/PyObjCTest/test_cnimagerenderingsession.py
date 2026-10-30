from PyObjCTools.TestSupport import TestCase, min_os_level

import Cinematic


class TestCNImageRenderingSession(TestCase):
    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsBOOL(
            Cinematic.CNImageRenderingSessionConfiguration.isRenderingVersionSupported_
        )

        self.assertResultIsBOOL(
            Cinematic.CNImageRenderingSession.encodeRenderToCommandBuffer_sourceRGBA_sourceDisparity_destinationRGBA_fNumber_focusDisparity_
        )

        self.assertResultIsBOOL(
            Cinematic.CNImageRenderingSession.encodeTileRenderToCommandBuffer_sourceTileRGBA_sourceDisparity_destinationTileRGBA_fNumber_focusDisparity_sourceRGBASize_tileOffset_tileExtendOffset_
        )
