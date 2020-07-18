from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCMultiheadAttentionDescriptor(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(MLCompute.MLCMultiheadAttentionDescriptor.hasBiases)
        self.assertResultIsBOOL(
            MLCompute.MLCMultiheadAttentionDescriptor.hasAttentionBiases
        )
        self.assertResultIsBOOL(
            MLCompute.MLCMultiheadAttentionDescriptor.addsZeroAttention
        )

        self.assertArgIsBOOL(
            MLCompute.MLCMultiheadAttentionDescriptor.descriptorWithModelDimension_keyDimension_valueDimension_headCount_dropout_hasBiases_hasAttentionBiases_addsZeroAttention_,  # noqa: B950
            5,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCMultiheadAttentionDescriptor.descriptorWithModelDimension_keyDimension_valueDimension_headCount_dropout_hasBiases_hasAttentionBiases_addsZeroAttention_,  # noqa: B950
            6,
        )
        self.assertArgIsBOOL(
            MLCompute.MLCMultiheadAttentionDescriptor.descriptorWithModelDimension_keyDimension_valueDimension_headCount_dropout_hasBiases_hasAttentionBiases_addsZeroAttention_,  # noqa: B950
            7,
        )
