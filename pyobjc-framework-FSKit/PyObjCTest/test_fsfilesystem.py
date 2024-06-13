from PyObjCTools.TestSupport import TestCase

import FSKit  # noqa: F401


class TestFSFileSystemHelper(TestCase):
    def loadResource_options_replyHandler_(self, a, b, c):
        pass


class TestFSFileSystem(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSFileSystemOperations")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFSFileSystemHelper.loadResource_options_replyHandler_, 2, b"v@@"
        )
