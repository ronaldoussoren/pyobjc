from PyObjCTools.TestSupport import TestCase, min_os_level

import PencilKit


class TestPKStrokePath(TestCase):
    @min_os_level("10.16")
    def test_methods(self):
        self.assertArgIsOut(
            PencilKit.PKStrokePath.enumerateInterpolatedPointsInRange_strideByDistance_usingBlock_,
            2,
            b"v@o^Z",
        )
        self.assertArgIsOut(
            PencilKit.PKStrokePath.enumerateInterpolatedPointsInRange_strideByTime_usingBlock_,
            2,
            b"v@o^Z",
        )
        self.assertArgIsOut(
            PencilKit.PKStrokePath.enumerateInterpolatedPointsInRange_strideByParametricStep_usingBlock_,
            2,
            b"v@o^Z",
        )
