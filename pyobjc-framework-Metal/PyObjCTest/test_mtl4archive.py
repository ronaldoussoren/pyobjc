import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestMTL4ArchiveHelper(Metal.NSObject):
    def newComputePipelineStateWithDescriptor_error_(self, a, b):
        return 1

    def newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_error_(
        self, a, b, c
    ):
        return 1

    def newRenderPipelineStateWithDescriptor_error_(self, a, b):
        return 1

    def newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_error_(
        self, a, b, c
    ):
        return 1

    def newBinaryFunctionWithDescriptor_error_(self, a, b):
        pass


class TestMTL4Archive(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4Archive", Metal)

    def test_protocol_methods(self):
        self.assertResultIsRetained(
            TestMTL4ArchiveHelper.newComputePipelineStateWithDescriptor_error_
        )
        self.assertArgIsOut(
            TestMTL4ArchiveHelper.newComputePipelineStateWithDescriptor_error_, 1
        )

        self.assertResultIsRetained(
            TestMTL4ArchiveHelper.newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_error_
        )
        self.assertArgIsOut(
            TestMTL4ArchiveHelper.newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_error_,
            2,
        )

        self.assertResultIsRetained(
            TestMTL4ArchiveHelper.newRenderPipelineStateWithDescriptor_error_
        )
        self.assertArgIsOut(
            TestMTL4ArchiveHelper.newRenderPipelineStateWithDescriptor_error_, 1
        )

        self.assertResultIsRetained(
            TestMTL4ArchiveHelper.newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_error_
        )
        self.assertArgIsOut(
            TestMTL4ArchiveHelper.newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_error_,
            2,
        )

        self.assertResultIsRetained(
            TestMTL4ArchiveHelper.newBinaryFunctionWithDescriptor_error_
        )
        self.assertArgIsOut(
            TestMTL4ArchiveHelper.newBinaryFunctionWithDescriptor_error_,
            1,
        )
