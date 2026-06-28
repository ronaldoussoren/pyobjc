import objc
from PyObjCTools.TestSupport import TestCase


import SceneKit

SCNBindingBlock = b"v" + objc._C_UINT + objc._C_UINT + b"@@"


class TestSCNTransaction(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(SceneKit.SCNTransaction.disableActions)
        self.assertArgIsBOOL(SceneKit.SCNTransaction.setDisableActions_, 0)

        self.assertResultIsBlock(SceneKit.SCNTransaction.completionBlock, b"v")
        self.assertArgIsBlock(SceneKit.SCNTransaction.setCompletionBlock_, 0, b"v")
