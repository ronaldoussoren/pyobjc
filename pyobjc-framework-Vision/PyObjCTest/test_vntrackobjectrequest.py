from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTrackObjectRequest(TestCase):
    @min_os_level("10.13")
    def testMethods10_13(self):
        self.assertArgIsBlock(
            Vision.VNTrackObjectRequest.initWithDetectedObjectObservation_completionHandler_,  # noqa: B950
            1,
            b"v@@",
        )
        self.assertArgIsBlock(
            Vision.VNTrackObjectRequest.initWithCompletionHandler_, 0, b"v@@"
        )

    def test_constants(self):
        self.assertEqual(Vision.VNTrackObjectRequestRevision1, 1)
        self.assertEqual(Vision.VNTrackObjectRequestRevision2, 2)
