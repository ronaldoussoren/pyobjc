from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertResultIsVariableSize(FSKit.FSFileDataBuffer.bytes)
        self.assertArgIsBlock(FSKit.FSFileDataBuffer.withBytes_, 0, b"vn^v")
        self.assertResultIsVariableSize(FSKit.FSMutableFileDataBuffer.mutableBytes)
        self.assertArgIsBlock(FSKit.FSFileDataBuffer.withMutableBytes_, 0, b"vN^v")
