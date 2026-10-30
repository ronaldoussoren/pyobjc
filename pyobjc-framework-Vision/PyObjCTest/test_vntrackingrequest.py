from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNRequest(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Vision.VNRequestTrackingLevel)
        self.assertEqual(Vision.VNRequestTrackingLevelAccurate, 0)
        self.assertEqual(Vision.VNRequestTrackingLevelFast, 1)

    @min_os_level("10.13")
    def test_methods10_13(self):
        self.assertResultIsBOOL(Vision.VNTrackingRequest.isLastFrame)
        self.assertArgIsBOOL(Vision.VNTrackingRequest.setLastFrame_, 0)
        self.assertArgIsBlock(
            Vision.VNTrackingRequest.initWithCompletionHandler_, 0, b"v@@"
        )

    @min_os_level("14.0")
    def test_methods14_0(self):
        self.assertArgIsOut(
            Vision.VNTrackingRequest.supportedNumberOfTrackersAndReturnError_, 0
        )
