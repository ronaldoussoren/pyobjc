from PyObjCTools.TestSupport import TestCase, min_sdk_level
import Vision  # noqa: F401


class TestVNFaceObservationAccepting(TestCase):
    @min_sdk_level("10.13")
    def testProtocols10_13(self):
        self.assertProtocolExists("VNFaceObservationAccepting")
