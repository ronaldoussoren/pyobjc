from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import Vision

    class TestVNClassifyImageRequest(TestCase):
        @min_os_level("10.15")
        def test_methods(self):
            self.assertArgIsOut(
                Vision.VNClassifyImageRequest.knownClassificationsForRevision_error_, 1
            )

        def test_constants(self):
            self.assertEqual(Vision.VNClassifyImageRequestRevision1, 1)


if __name__ == "__main__":
    main()
