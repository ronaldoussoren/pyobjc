from PyObjCTools.TestSupport import TestCase, min_os_level
import Vision


class TestVNClassifyImageRequest(TestCase):
    def test_constants(self):
        self.assertEqual(Vision.VNClassifyImageRequestRevision1, 1)
        self.assertEqual(Vision.VNClassifyImageRequestRevision2, 2)

    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(
            Vision.VNClassifyImageRequest.knownClassificationsForRevision_error_, 1
        )

    @min_os_level("12.0")
    def test_methods12_0(self):
        self.assertArgIsOut(
            Vision.VNClassifyImageRequest.supportedIdentifiersAndReturnError_, 0
        )
