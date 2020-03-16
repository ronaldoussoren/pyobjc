import sys


if sys.maxsize >= 2 ** 32:
    from PyObjCTools.TestSupport import TestCase
    import Vision

    class TestVNImageRegistrationRequest(TestCase):
        def test_constants(self):
            self.assertEqual(Vision.VNTranslationalImageRegistrationRequestRevision1, 1)
            self.assertEqual(Vision.VNHomographicImageRegistrationRequestRevision1, 1)
