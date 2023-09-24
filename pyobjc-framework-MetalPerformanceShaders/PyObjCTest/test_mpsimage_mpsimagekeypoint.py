from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSImage_MPSImageHistogram(TestCase):
    def test_structs(self):
        v = MetalPerformanceShaders.MPSImageKeypointRangeInfo()
        self.assertIsInstance(v.maximumKeypoints, int)
        self.assertIsInstance(v.minimumThresholdValue, float)
        self.assertPickleRoundTrips(v)

        self.assertEqual(
            MetalPerformanceShaders.MPSImageKeypointData.__typestr__,
            b"{MPSImageKeypointData=<2S>f}",
        )
        v = MetalPerformanceShaders.MPSImageKeypointData()
        self.assertIs(v.keypointCoordinate, None)
        self.assertIsInstance(v.keypointColorValue, float)

    @min_os_level("10.13")
    def test_methods(self):
        self.assertArgIsIn(
            MetalPerformanceShaders.MPSImageFindKeypoints.initWithDevice_info_, 1
        )
