from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCTensorDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCTensorDescriptor.sortedSequences)
