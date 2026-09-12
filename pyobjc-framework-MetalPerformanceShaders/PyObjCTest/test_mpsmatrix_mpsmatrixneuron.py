from PyObjCTools.TestSupport import TestCase, min_os_level

import MetalPerformanceShaders


class TestMPSMatrix_MPSMatrixNeuron(TestCase):
    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixNeuron.copyWithZone_device_
        )
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSMatrixNeuronGradient.copyWithZone_device_
        )
