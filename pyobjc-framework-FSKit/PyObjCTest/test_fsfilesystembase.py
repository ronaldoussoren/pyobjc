from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSFileSystemBaseHelper(FSKit.NSObject):
    def containerState(self):
        return 1

    def setContainerState_(self, a):
        pass

    def wipeResource_includingRanges_excludingRanges_completionHandler_(
        self, a, b, c, d
    ):
        pass


class TestFSFileSystemBase(TestCase):
    def test_protocols(self):
        self.assertProtocolExists("FSFileSystemBase")

    def test_protocol_methods(self):
        self.assertResulsHasType(TestFSFileSystemBaseHelper.containerState, b"Q")
        self.assertArgHasType(TestFSFileSystemBaseHelper.setContainerState_, 0, b"Q")

        self.assertArgIsBlock(
            TestFSFileSystemBaseHelper.wipeResource_includingRanges_excludingRanges_completionHandler_,
            3,
            b"v@",
        )
