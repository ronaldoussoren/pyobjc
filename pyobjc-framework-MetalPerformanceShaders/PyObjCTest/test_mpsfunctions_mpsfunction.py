from PyObjCTools.TestSupport import TestCase, min_os_level
import MetalPerformanceShaders


class TestMPSFunctions_MPSFunction(TestCase):
    @min_os_level("27.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            MetalPerformanceShaders.MPSFunction.supportsSecureCoding
        )
