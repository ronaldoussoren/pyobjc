from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCEmbeddingDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(
            MLCompute.MLCEmbeddingDescriptor.scalesGradientByFrequency
        )

        self.assertArgIsBOOL(
            MLCompute.MLCEmbeddingDescriptor.descriptorWithEmbeddingCount_embeddingDimension_paddingIndex_maximumNorm_pNorm_scalesGradientByFrequency_,  # noqa: B950
            5,
        )
