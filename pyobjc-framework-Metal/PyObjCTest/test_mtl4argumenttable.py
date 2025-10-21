import Metal
import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestMTL4ArgumentTableHelper(Metal.NSObject):
    def setAddress_atIndex_(self, a, b):
        pass

    def setAddress_attributeStride_atIndex_(self, a, b, c):
        pass

    def setResource_atBufferIndex_(self, a, b):
        pass

    def setTexture_atIndex_(self, a, b):
        pass

    def setSamplerState_atIndex_(self, a, b):
        pass


class TestMTL4ArgumentTable(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(Metal.MTL4ArgumentTableDescriptor.initializeBindings)
        self.assertArgIsBOOL(
            Metal.MTL4ArgumentTableDescriptor.setInitializeBindings_, 0
        )

        self.assertResultIsBOOL(
            Metal.MTL4ArgumentTableDescriptor.supportAttributeStrides
        )
        self.assertArgIsBOOL(
            Metal.MTL4ArgumentTableDescriptor.setSupportAttributeStrides_, 0
        )

    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4ArgumentTable")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setAddress_atIndex_, 1, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setAddress_attributeStride_atIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setAddress_attributeStride_atIndex_,
            2,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setResource_atBufferIndex_,
            1,
            objc._C_NSUInteger,
        )
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setTexture_atIndex_, 1, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setSamplerState_atIndex_, 1, objc._C_NSUInteger
        )
        self.assertArgHasType(
            TestMTL4ArgumentTableHelper.setSamplerState_atIndex_, 1, objc._C_NSUInteger
        )
