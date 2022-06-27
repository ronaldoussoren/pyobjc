from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLAContext_Authorization(TestCase):
    @min_os_level("13.0")
    def test_methods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LAContext.evaluateRight_localizedReason_reply_, 2, b"v@"
        )
        self.assertArgIsBlock(
            LocalAuthentication.LAContext.evaluateRight_localizedReason_reply_, 2, b"v@"
        )
