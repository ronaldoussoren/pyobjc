from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTrackHomographicImageRegistrationRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNTrackHomographicImageRegistrationRequestRevision1, 1)

    @min_os_level("14.0")
    def test_methods(self):
        self.assertArgIsBlock(
            Vision.VNTrackHomographicImageRegistrationRequest.initWithCompletionHandler_,
            0,
            b"v@@",
        )
