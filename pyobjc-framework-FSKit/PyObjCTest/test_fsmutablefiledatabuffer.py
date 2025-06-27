from PyObjCTools.TestSupport import TestCase

import FSKit


class TestFSMutableFileDataBuffer(TestCase):
    def test_methods(self):
        self.assertResultIsVariableSize(FSKit.FSMutableFileDataBuffer.mutableBytes)
