import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTLTextureViewPoolHelper(Metal.NSObject):
    def setTextureView_atIndex_(self, a, b):
        return 1

    def setTextureView_descriptor_atIndex_(self, a, b, c):
        return 1

    def setTextureViewFromBuffer_descriptor_offset_bytesPerRow_atIndex_(
        self, a, b, c, d, e
    ):
        return 1


class TestMTLTextureViewPool(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTLTextureViewPool")

    def test_protocol_methods(self):
        self.assertResultHasType(
            TestMTLTextureViewPoolHelper.setTextureView_atIndex_,
            Metal.MTLResourceID.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureViewPoolHelper.setTextureView_atIndex_, 1, b"Q"
        )

        self.assertResultHasType(
            TestMTLTextureViewPoolHelper.setTextureView_descriptor_atIndex_,
            Metal.MTLResourceID.__typestr__,
        )
        self.assertArgHasType(
            TestMTLTextureViewPoolHelper.setTextureView_descriptor_atIndex_, 2, b"Q"
        )

        self.assertArgHasType(
            TestMTLTextureViewPoolHelper.setTextureViewFromBuffer_descriptor_offset_bytesPerRow_atIndex_,
            2,
            b"Q",
        )
        self.assertArgHasType(
            TestMTLTextureViewPoolHelper.setTextureViewFromBuffer_descriptor_offset_bytesPerRow_atIndex_,
            3,
            b"Q",
        )
        self.assertArgHasType(
            TestMTLTextureViewPoolHelper.setTextureViewFromBuffer_descriptor_offset_bytesPerRow_atIndex_,
            4,
            b"Q",
        )
