from PyObjCTools.TestSupport import TestCase, min_os_level
import LocalAuthentication


class TestLARight_UI(TestCase):
    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LARight.authorizeWithLocalizedReason_inPresentationContext_completion_,
            2,
            b"v@",
        )
