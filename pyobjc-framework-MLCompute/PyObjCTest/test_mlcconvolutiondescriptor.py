from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCConvolutionDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            MLCompute.MLCConvolutionDescriptor.isConvolutionTranspose
        )
        self.assertResultIsBOOL(
            MLCompute.MLCConvolutionDescriptor.usesDepthwiseConvolution
        )
