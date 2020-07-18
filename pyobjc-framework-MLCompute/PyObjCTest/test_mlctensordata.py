from PyObjCTools.TestSupport import TestCase

import MLCompute


class TestMLCTensorData(TestCase):
    def test_methods(self):
        self.assertArgIsIn(MLCompute.MLCTensorData.dataWithBytesNoCopy_length_, 0)
        self.assertArgSizeInArg(
            MLCompute.MLCTensorData.dataWithBytesNoCopy_length_, 0, 1
        )

        self.assertArgIsIn(
            MLCompute.MLCTensorData.dataWithImmutableBytesNoCopy_length_, 0
        )
        self.assertArgSizeInArg(
            MLCompute.MLCTensorData.dataWithImmutableBytesNoCopy_length_, 0, 1
        )
