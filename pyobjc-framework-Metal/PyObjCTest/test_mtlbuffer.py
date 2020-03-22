import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level
import objc


class TestMTLBufferHelper(Metal.NSObject):
    def length(self):
        return 1

    def contents(self):
        return 1

    def didModifyRange_(self, a):
        pass

    def newTextureWithDescriptor_offset_bytesPerRow_(self, a, b, c):
        return 1

    def addDebugMarker_range_(self, a, b):
        pass


class TestMTLBuffer(TestCase):
    @min_sdk_level("10.13")
    def test_protocols10_13(self):
        objc.protocolNamed("MTLBuffer")

    def test_methods(self):
        self.assertResultHasType(TestMTLBufferHelper.length, objc._C_NSUInteger)

        self.assertResultHasType(
            TestMTLBufferHelper.contents, objc._C_PTR + objc._C_VOID
        )
        self.assertResultIsVariableSize(TestMTLBufferHelper.contents)

        self.assertArgHasType(
            TestMTLBufferHelper.didModifyRange_, 0, Metal.NSRange.__typestr__
        )

        self.assertArgHasType(
            TestMTLBufferHelper.newTextureWithDescriptor_offset_bytesPerRow_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTLBufferHelper.newTextureWithDescriptor_offset_bytesPerRow_,
            2,
            objc._C_NSUInteger,
        )

        self.assertArgHasType(
            TestMTLBufferHelper.addDebugMarker_range_, 1, Metal.NSRange.__typestr__
        )
