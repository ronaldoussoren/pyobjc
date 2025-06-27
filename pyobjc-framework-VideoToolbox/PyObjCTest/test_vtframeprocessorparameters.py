import VideoToolbox  # noqa: F401
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestVTFrameProcessorParameters(TestCase):
    @min_sdk_level("15.4")
    def test_protocols(self):
        self.assertProtocolExists("VTFrameProcessorParameters")
