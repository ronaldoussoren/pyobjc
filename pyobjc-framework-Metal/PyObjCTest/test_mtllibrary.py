import Metal
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level
import objc


class TestMTLLibraryHelper(Metal.NSObject):
    def functionType(self):
        return 1

    def patchType(self):
        return 1

    def patchControlPointCount(self):
        return 1

    def newArgumentEncoderWithBufferIndex_(self, a):
        return 1

    def newArgumentEncoderWithBufferIndex_reflection_(self, a, b):
        return 1

    def newFunctionWithName_constantValues_error_(self, a, b, c):
        return 1

    def newFunctionWithName_constantValues_completionHandler_(self, a, b, c):
        pass

    def options(self):
        return 1

    def newFunctionWithDescriptor_completionHandler_(self, a, b):
        pass

    def newFunctionWithDescriptor(self):
        return 1

    def newIntersectionFunctionWithDescriptor_completionHandler_(self, a, b):
        pass

    def newIntersectionFunctionWithDescriptor_error_(self, a, b):
        return 1

    def type(self):  # noqa: A003
        pass

    def newFunctionWithDescriptor_error_(self, a, b):
        pass


class TestMTLLibrary(TestCase):
    def test_constants(self):
        self.assertEqual(Metal.MTLPatchTypeNone, 0)
        self.assertEqual(Metal.MTLPatchTypeTriangle, 1)
        self.assertEqual(Metal.MTLPatchTypeQuad, 2)

        self.assertEqual(Metal.MTLFunctionTypeVertex, 1)
        self.assertEqual(Metal.MTLFunctionTypeFragment, 2)
        self.assertEqual(Metal.MTLFunctionTypeKernel, 3)
        self.assertEqual(Metal.MTLFunctionTypeVisible, 5)
        self.assertEqual(Metal.MTLFunctionTypeIntersection, 6)

        self.assertEqual(Metal.MTLLanguageVersion1_0, (1 << 16))
        self.assertEqual(Metal.MTLLanguageVersion1_1, (1 << 16) + 1)
        self.assertEqual(Metal.MTLLanguageVersion1_2, (1 << 16) + 2)
        self.assertEqual(Metal.MTLLanguageVersion2_0, (2 << 16))
        self.assertEqual(Metal.MTLLanguageVersion2_1, (2 << 16) + 1)
        self.assertEqual(Metal.MTLLanguageVersion2_2, (2 << 16) + 2)
        self.assertEqual(Metal.MTLLanguageVersion2_3, (2 << 16) + 3)

        self.assertEqual(Metal.MTLLibraryErrorUnsupported, 1)
        self.assertEqual(Metal.MTLLibraryErrorInternal, 2)
        self.assertEqual(Metal.MTLLibraryErrorCompileFailure, 3)
        self.assertEqual(Metal.MTLLibraryErrorCompileWarning, 4)
        self.assertEqual(Metal.MTLLibraryErrorFunctionNotFound, 5)
        self.assertEqual(Metal.MTLLibraryErrorFileNotFound, 6)

    @min_os_level("10.11")
    def test_constants10_11(self):
        self.assertIsInstance(Metal.MTLLibraryErrorDomain, str)

    @min_sdk_level("10.11")
    def test_protocols(self):
        objc.protocolNamed("MTLFunction")
        objc.protocolNamed("MTLLibrary")

    def test_methods(self):
        self.assertResultHasType(TestMTLLibraryHelper.functionType, objc._C_NSUInteger)
        self.assertResultHasType(TestMTLLibraryHelper.patchType, objc._C_NSUInteger)
        self.assertResultHasType(
            TestMTLLibraryHelper.patchControlPointCount, objc._C_NSInteger
        )

        self.assertArgHasType(
            TestMTLLibraryHelper.newArgumentEncoderWithBufferIndex_,
            0,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLLibraryHelper.newArgumentEncoderWithBufferIndex_reflection_,
            0,
            objc._C_NSUInteger,
        )

        self.assertArgIsOut(
            TestMTLLibraryHelper.newFunctionWithName_constantValues_error_, 2
        )
        self.assertArgIsBlock(
            TestMTLLibraryHelper.newFunctionWithName_constantValues_completionHandler_,
            2,
            b"v@@",
        )
        self.assertResultHasType(TestMTLLibraryHelper.options, objc._C_NSUInteger)
        self.assertArgIsBlock(
            TestMTLLibraryHelper.newFunctionWithDescriptor_completionHandler_, 1, b"v@@"
        )
        self.assertArgIsOut(TestMTLLibraryHelper.newFunctionWithDescriptor_error_, 1)
        self.assertArgIsBlock(
            TestMTLLibraryHelper.newIntersectionFunctionWithDescriptor_completionHandler_,
            1,
            b"v@@",
        )
        self.assertArgIsOut(
            TestMTLLibraryHelper.newIntersectionFunctionWithDescriptor_error_, 1
        )
        self.assertResultHasType(TestMTLLibraryHelper.type, objc._C_NSInteger)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(Metal.MTLVertexAttribute.alloc().init().isActive)

        self.assertResultIsBOOL(Metal.MTLCompileOptions.alloc().init().fastMathEnabled)
        self.assertArgIsBOOL(
            Metal.MTLCompileOptions.alloc().init().setFastMathEnabled_, 0
        )

        self.assertResultIsBOOL(Metal.MTLVertexAttribute.alloc().init().isActive)

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertResultIsBOOL(Metal.MTLVertexAttribute.alloc().init().isPatchData)
        self.assertResultIsBOOL(
            Metal.MTLVertexAttribute.alloc().init().isPatchControlPointData
        )

        self.assertResultIsBOOL(Metal.MTLAttribute.alloc().init().isActive)
        self.assertResultIsBOOL(Metal.MTLAttribute.alloc().init().isPatchData)
        self.assertResultIsBOOL(
            Metal.MTLAttribute.alloc().init().isPatchControlPointData
        )

        self.assertResultIsBOOL(Metal.MTLFunctionConstant.alloc().init().required)
