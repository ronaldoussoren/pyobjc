import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLTensorHelper(Metal.NSObject):
    def gpuResourceID(self):
        return 1

    def bufferOffset(self):
        return 1

    def dataType(self):
        return 1

    def usage(self):
        return 1

    def replaceSliceOrigin_sliceDimensions_withBytes_strides_(self, a, b, c, d):
        pass

    def getBytes_strides_fromSliceOrigin_sliceDimensions_(self, a, b, c, d):
        pass


class TestMTLTensor(TestCase):
    def test_enum(self):
        self.assertIsEnumType(Metal.MTLTensorDataType)
        self.assertEqual(Metal.MTLTensorDataTypeNone, Metal.MTLDataTypeNone)
        self.assertEqual(Metal.MTLTensorDataTypeFloat32, Metal.MTLDataTypeFloat)
        self.assertEqual(Metal.MTLTensorDataTypeFloat16, Metal.MTLDataTypeHalf)
        self.assertEqual(Metal.MTLTensorDataTypeBFloat16, Metal.MTLDataTypeBFloat)
        self.assertEqual(Metal.MTLTensorDataTypeInt8, Metal.MTLDataTypeChar)
        self.assertEqual(Metal.MTLTensorDataTypeUInt8, Metal.MTLDataTypeUChar)
        self.assertEqual(Metal.MTLTensorDataTypeInt16, Metal.MTLDataTypeShort)
        self.assertEqual(Metal.MTLTensorDataTypeUInt16, Metal.MTLDataTypeUShort)
        self.assertEqual(Metal.MTLTensorDataTypeInt32, Metal.MTLDataTypeInt)
        self.assertEqual(Metal.MTLTensorDataTypeUInt32, Metal.MTLDataTypeUInt)

        self.assertEqual(Metal.MTL_TENSOR_MAX_RANK, 16)

        self.assertIsEnumType(Metal.MTLTensorError)
        self.assertEqual(Metal.MTLTensorErrorNone, 0)
        self.assertEqual(Metal.MTLTensorErrorInternalError, 1)
        self.assertEqual(Metal.MTLTensorErrorInvalidDescriptor, 2)

        self.assertIsEnumType(Metal.MTLTensorUsage)
        self.assertEqual(Metal.MTLTensorUsageCompute, 1 << 0)
        self.assertEqual(Metal.MTLTensorUsageRender, 1 << 1)
        self.assertEqual(Metal.MTLTensorUsageMachineLearning, 1 << 2)

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLTensor")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLTensorHelper.gpuResourceID, Metal.MTLResourceID.__typestr__
        )
        self.assertResultHasType(TestMTLTensorHelper.bufferOffset, b"Q")
        self.assertResultHasType(TestMTLTensorHelper.dataType, b"q")
        self.assertResultHasType(TestMTLTensorHelper.usage, b"Q")

        self.assertArgHasType(
            TestMTLTensorHelper.replaceSliceOrigin_sliceDimensions_withBytes_strides_,
            2,
            b"n^v",
        )
        self.assertArgIsVariableSize(
            TestMTLTensorHelper.replaceSliceOrigin_sliceDimensions_withBytes_strides_, 2
        )

        self.assertArgHasType(
            TestMTLTensorHelper.getBytes_strides_fromSliceOrigin_sliceDimensions_,
            0,
            b"o^v",
        )
        self.assertArgIsVariableSize(
            TestMTLTensorHelper.getBytes_strides_fromSliceOrigin_sliceDimensions_, 0
        )
