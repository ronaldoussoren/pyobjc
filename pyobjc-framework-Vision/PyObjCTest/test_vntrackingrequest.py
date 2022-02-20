from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNRequest(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Vision.VNRequestTrackingLevel)

    def testConstants(self):
        self.assertEqual(Vision.VNRequestTrackingLevelAccurate, 0)
        self.assertEqual(Vision.VNRequestTrackingLevelFast, 1)

    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertResultIsBOOL(Vision.VNTrackingRequest.isLastFrame)
        self.assertArgIsBOOL(Vision.VNTrackingRequest.setLastFrame_, 0)
        self.assertArgIsBlock(
            Vision.VNTrackingRequest.initWithCompletionHandler_, 0, b"v@@"
        )
