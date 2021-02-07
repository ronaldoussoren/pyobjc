from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSImage_MPSImageHistogram(TestCase):
    def test_structs(self):
        v = MetalPerformanceShaders.MPSImageKeypointRangeInfo()
        self.assertIsInstance(v.maximumKeypoints, int)
        self.assertIsInstance(v.minimumThresholdValue, float)

        self.assertNotHasAttr(MetalPerformanceShaders, "MPSImageKeypointData")
        # v = MetalPerformanceShaders.MPSImageKeypointData()
        # self.assertIsInstance(v.keypointCoordinate, objc.vector_ushort2)
        # self.assertIsInstance(v.keypointColorValue, float)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageFindKeypoints.initWithDevice_info_, 1
        )
