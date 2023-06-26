from PyObjCTools.TestSupport import TestCase, min_sdk_level
import CoreML  # noqa: F401


class TestMLComputeDeviceProtocol(TestCase):
    @min_sdk_level("14.0")
    def test_functions(self):
        self.assertProtocolExists("MLComputeDeviceProtocol")
