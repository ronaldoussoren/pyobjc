from PyObjCTools.TestSupport import TestCase, min_os_level
import CryptoTokenKit


class TestTKTokenConfiguration(TestCase):
    @min_os_level("10.15")
    def test_methods(self):
        self.assertArgIsOut(
            CryptoTokenKit.TKTokenConfiguration.keyForObjectID_error_, 1
        )
        self.assertArgIsOut(
            CryptoTokenKit.TKTokenConfiguration.certificateForObjectID_error_, 1
        )
