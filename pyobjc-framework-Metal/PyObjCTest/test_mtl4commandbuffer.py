import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4CommandBufferHelper(Metal.NSObject):
    def renderCommandEncoderWithDescriptor_options_(self, a, b):
        return 1

    def useResidencySets_count_(self, a, b):
        pass

    def writeTimestampIntoHeap_atIndex_(self, a, b):
        pass

    def resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence_(
        self, a, b, c, d, e
    ):
        pass


class TestMTL4CommandBuffer(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4CommandBuffer")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTL4CommandBufferHelper.renderCommandEncoderWithDescriptor_options_,
            1,
            b"Q",
        )

        self.assertArgHasType(
            TestMTL4CommandBufferHelper.useResidencySets_count_, 0, b"n^@"
        )
        self.assertArgSizeInArg(
            TestMTL4CommandBufferHelper.useResidencySets_count_, 0, 1
        )
        self.assertArgHasType(
            TestMTL4CommandBufferHelper.useResidencySets_count_, 1, b"Q"
        )

        self.assertArgHasType(
            TestMTL4CommandBufferHelper.writeTimestampIntoHeap_atIndex_, 1, b"Q"
        )
        self.assertArgHasType(
            TestMTL4CommandBufferHelper.resolveCounterHeap_withRange_intoBuffer_waitFence_updateFence_,
            1,
            Metal.NSRange.__typestr__,
        )
