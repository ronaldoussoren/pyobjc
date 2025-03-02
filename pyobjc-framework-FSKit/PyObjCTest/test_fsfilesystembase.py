from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSFileSystemBaseHelper(FSKit.NSObject):
    def wipeResource_completionHandler_(self, a, b):
        pass


class TestFSFileSystemBase(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSFileSystemBase")

    def test_protocol_methods(self):
        self.assertArgIsBlock(
            TestFSFileSystemBaseHelper.wipeResource_completionHandler_,
            1,
            b"v@",
        )
