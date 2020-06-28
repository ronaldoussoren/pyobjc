from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCTensorParameter(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.TestMLCTensorParameter.isUpdatable)
        self.assertArgIsBOOL(MLCompute.TestMLCTensorParameter.setIsUpdatable_, 0)
