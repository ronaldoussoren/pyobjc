from PyObjCTools.TestSupport import TestCase, min_os_level, skipUnless
import LocalAuthentication


class TestLARight_UI(TestCase):
    @skipUnless(
        hasattr(
            LocalAuthentication.LARight,
            "authorizeWithLocalizedReason_inPresentationContext_completion_",
        ),
        "method not present",
    )
    @min_os_level("13.0")
    def testMethods13_0(self):
        self.assertArgIsBlock(
            LocalAuthentication.LARight.authorizeWithLocalizedReason_inPresentationContext_completion_,
            2,
            b"v@",
        )
