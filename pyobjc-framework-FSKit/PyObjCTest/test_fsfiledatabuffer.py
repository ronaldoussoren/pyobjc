from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSClient(TestCase):
    def test_methods(self):
        self.assertResultHasVariableLength(FSKit.FSFileDataBuffer.bytes)
        self.assertResultHasVariableLength(FSKit.FSMutableFileDataBuffer.mutableBytes)
