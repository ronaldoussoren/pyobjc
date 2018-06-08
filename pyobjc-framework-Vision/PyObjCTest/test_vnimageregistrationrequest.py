from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2**32:
    import Vision

    class TestVNImageRegistrationRequest (TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNTranslationalImageRegistrationRequestRevision1, 1)
            self.assertEqual(Vision.VNHomographicImageRegistrationRequestRevision1, 1)



if __name__ == "__main__":
    main()
