from PyObjCTools.TestSupport import TestCase

import ClassKit  # noqa: F401
import objc


class TestCLSActivityHelper(ClassKit.NSObject):
    def updateDescendantsOfContext_completion_(self, a, b):
        pass


class TestCLSActivity(TestCase):
    def test_protocols(self):
        objc.protocolNamed("CLSContextProvider")

    def test_methods(self):
        self.assertArgIsBlock(
            TestCLSActivityHelper.updateDescendantsOfContext_completion_, 1, b"v@"
        )
