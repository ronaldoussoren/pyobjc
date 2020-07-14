from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCYOLOLossDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCYOLOLossDescriptor.shouldRescore)
        self.assertArgIsBOOL(MLCompute.MLCYOLOLossDescriptor.setShouldRescore_, 0)
