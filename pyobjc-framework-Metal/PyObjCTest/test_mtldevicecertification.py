import Metal
from PyObjCTools.TestSupport import TestCase


class TestMTLDeviceCertification(TestCase):
    def test_constants(self):
        self.assertIsTypedEnum(Metal.NSDeviceCertification, int)
        self.assertIsInstance(Metal.NSDeviceCertificationiPhonePerformanceGaming, int)

        self.assertIsTypedEnum(Metal.NSProcessPerformanceProfile, int)
        self.assertIsInstance(Metal.NSProcessPerformanceProfileDefault, int)
        self.assertIsInstance(Metal.NSProcessPerformanceProfileSustained, int)
        self.assertIsInstance(
            Metal.NSProcessInfoPerformanceProfileDidChangeNotification, str
        )
