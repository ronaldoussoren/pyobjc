from PyObjCTools.TestSupport import TestCase

import ClassKit  # noqa: F401


class TestCLSActivityHelper(ClassKit.NSObject):
    def updateDescendantsOfContext_completion_(self, a, b):
        pass


class TestCLSActivity(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("CLSContextProvider")

    def test_methods(self):
        self.assertArgIsBlock(
            TestCLSActivityHelper.updateDescendantsOfContext_completion_, 1, b"v@"
        )
