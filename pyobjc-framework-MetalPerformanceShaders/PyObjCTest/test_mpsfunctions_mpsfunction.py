from PyObjCTools.TestSupport import TestCase, min_os_level
import MetalPerformanceShaders


class TestMPSFunctions_MPSFunction(TestCase):

    @min_os_level("27.0")
    def test_methods27_0(self):
        self.assertResultIsRetained(
            MetalPerformanceShaders.MPSFunction.copyWithZone_device_
        )

        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSFunction.supportsSecureCoding
        )
