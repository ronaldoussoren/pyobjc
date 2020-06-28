from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCPoolingDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCPoolingDescriptor.countIncludesPadding)
        self.assertArgIsBOOL(
            MLCompute.MLCPoolingDescriptor.averagePoolingDescriptorWithKernelSizes_strides_dilationRates_paddingPolicies_paddingSizes_countIncludesPadding_,  # noqa: B950
            5,
        )
