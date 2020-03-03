import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVComposition(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVMutableComposition.insertTimeRange_ofAsset_atTime_error_
        )
        self.assertArgIsOut(
            AVFoundation.AVMutableComposition.insertTimeRange_ofAsset_atTime_error_, 3
        )
