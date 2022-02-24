from PyObjCTools.TestSupport import TestCase, min_os_level
import CoreML


class TestMLMultiArray(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(CoreML.MLMultiArrayDataType)

    def testConstants(self):
        self.assertEqual(CoreML.MLMultiArrayDataTypeDouble, 0x10000 | 64)
        self.assertEqual(CoreML.MLMultiArrayDataTypeFloat64, 0x10000 | 64)
        self.assertEqual(CoreML.MLMultiArrayDataTypeFloat32, 0x10000 | 32)
        self.assertEqual(CoreML.MLMultiArrayDataTypeFloat16, 0x10000 | 16)
        self.assertEqual(CoreML.MLMultiArrayDataTypeFloat, 0x10000 | 32)
        self.assertEqual(CoreML.MLMultiArrayDataTypeInt32, 0x20000 | 32)

    @min_os_level("10.13")
    def testMethods(self):
        self.assertArgIsOut(CoreML.MLMultiArray.initWithShape_dataType_error_, 2)

        self.assertResultIsVariableSize(CoreML.MLMultiArray.dataPointer)

        self.assertArgIsVariableSize(
            CoreML.MLMultiArray.initWithDataPointer_shape_dataType_strides_deallocator_error_,
            0,
        )
        self.assertArgIsBlock(
            CoreML.MLMultiArray.initWithDataPointer_shape_dataType_strides_deallocator_error_,
            4,
            b"v^v",
        )
        self.assertArgIsOut(
            CoreML.MLMultiArray.initWithDataPointer_shape_dataType_strides_deallocator_error_,
            5,
        )
