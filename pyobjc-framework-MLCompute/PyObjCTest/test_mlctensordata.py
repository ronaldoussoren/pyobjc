from PyObjCTools.TestSupport import TestCase, min_os_level

import MLCompute
import objc


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

    @min_os_level("11.3")
    def test_methods11_3(self):
        self.assertArgIsIn(
            MLCompute.MLCTensorData.dataWithBytesNoCopy_length_deallocator_, 0
        )
        self.assertArgSizeInArg(
            MLCompute.MLCTensorData.dataWithBytesNoCopy_length_deallocator_, 0, 1
        )
        self.assertArgIsBlock(
            MLCompute.MLCTensorData.dataWithBytesNoCopy_length_deallocator_,
            2,
            b"vn^v" + objc._C_NSUInteger,
        )
