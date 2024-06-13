from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSUnaryFileSystemHelper(FSKit.NSObject):
    def loadResource_options_replyHandler_(self, a, b, c):
        pass


class TestFSUnaryFileSystem(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSUnaryFileSystemOperations")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFSUnaryFileSystemHelper.loadResource_options_replyHandler_, 2, b"v@@"
        )
