from PyObjCTools.TestSupport import TestCase

import Cinematic


class TestCNAssetInfo(TestCase):
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
