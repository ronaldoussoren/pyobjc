from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import Vision

    class TestVNGenerateImageFeaturePrintRequest(TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNGenerateImageFeaturePrintRequestRevision1, 1)


if __name__ == "__main__":
    main()
