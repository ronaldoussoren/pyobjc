from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:
    import Vision

    class TestVNDetectFaceLandmarksRequest(TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNRequestFaceLandmarksConstellationNotDefined, 0)
            self.assertEqual(Vision.VNRequestFaceLandmarksConstellation65Points, 1)
            self.assertEqual(Vision.VNRequestFaceLandmarksConstellation76Points, 2)

            self.assertEqual(Vision.VNDetectFaceLandmarksRequestRevision2, 2)
            self.assertEqual(Vision.VNDetectFaceLandmarksRequestRevision3, 3)

        @min_os_level("10.15")
        def test_methods10_15(self):
            self.assertResultIsBOOL(
                Vision.VNDetectFaceLandmarksRequest.revision_supportsConstellation_
            )


if __name__ == "__main__":
    main()
