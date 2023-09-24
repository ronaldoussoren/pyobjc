from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNTrackTranslationalImageRegistrationRequest(TestCase):
    def test_constants(self):
        self.assertEqual(
            Vision.VNTrackTranslationalImageRegistrationRequestRevision1, 1
        )

    @min_os_level("14.9")
    def test_methods(self):
        self.assertArgIsBlock(
            Vision.VNTrackTranslationalImageRegistrationRequest.initWithCompletionHandler_,
            0,
            b"v@@",
        )
