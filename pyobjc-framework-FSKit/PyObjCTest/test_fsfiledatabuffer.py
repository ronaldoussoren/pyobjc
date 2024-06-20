from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertResultIsVariableSize(FSKit.FSFileDataBuffer.bytes)
        self.assertResultIsVariableSize(FSKit.FSMutableFileDataBuffer.mutableBytes)
