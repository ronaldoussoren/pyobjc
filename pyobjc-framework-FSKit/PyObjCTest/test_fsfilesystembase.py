from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSFileSystemBaseHelper(FSKit.NSObject):
    def containerState(self):
        return 1

    def setContainerState_(self, a):
        pass

    def wipeResource_completionHandler_(self, a, b):
        pass


class TestFSFileSystemBase(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSFileSystemBase")

    def test_protocol_methods(self):
        self.assertResultHasType(TestFSFileSystemBaseHelper.containerState, b"q")
        self.assertArgHasType(TestFSFileSystemBaseHelper.setContainerState_, 0, b"q")

        self.assertArgIsBlock(
            TestFSFileSystemBaseHelper.wipeResource_completionHandler_,
            1,
            b"v@",
        )
