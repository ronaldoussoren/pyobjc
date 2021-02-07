from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCTensorParameter(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCTensorParameter.isUpdatable)
        self.assertArgIsBOOL(MLCompute.MLCTensorParameter.setIsUpdatable_, 0)
