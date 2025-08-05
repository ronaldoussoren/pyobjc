import Metal
from PyObjCTools.TestSupport import TestCase, min_sdk_level

MTLNewLibraryCompletionHandler = b"v@@"
MTL4NewBinaryFunctionCompletionHandler = b"v@@"
MTLNewRenderPipelineStateCompletionHandler = b"v@@"
MTLNewDynamicLibraryCompletionHandler = b"v@@"
MTLNewComputePipelineStateCompletionHandler = b"v@@"
MTL4NewMachineLearningPipelineStateCompletionHandler = b"v@@"


class TestMTL4CompilerHelper(Metal.NSObject):
    def newLibraryWithDescriptor_error_(self, a, b):
        return 1

    def newDynamicLibrary_error_(self, a, b):
        return 1

    def newDynamicLibraryWithURL_error_(self, a, b):
        return 1

    def newComputePipelineStateWithDescriptor_compilerTaskOptions_error_(self, a, b, c):
        return 1

    def newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error_(
        self, a, b, c, d
    ):
        return 1

    def newRenderPipelineStateWithDescriptor_(self, a):
        return 1

    def newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error_(
        self, a, b, c, d
    ):
        return 1

    def newRenderPipelineStateBySpecializationWithDescriptor_pipeline_error_(
        self, a, b, c
    ):
        return 1

    def newBinaryFunctionWithDescriptor_compilerTaskOptions_error_(self, a, b, c):
        return 1

    def newLibraryWithDescriptor_completionHandler_(self, a, b):
        pass

    def newDynamicLibrary_completionHandler_(self, a, b):
        pass

    def newComputePipelineStateWithDescriptor_compilerTaskOptions_completionHandler_(
        self, a, b, c
    ):
        pass

    def newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_completionHandler_(
        self, a, b, c, d
    ):
        return 1

    def newRenderPipelineStateWithDescriptor_compilerTaskOptions_completionHandler_(
        self, a, b, c
    ):
        pass

    def newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_completionHandler_(
        self, a, b, c, d
    ):
        pass

    def newRenderPipelineStateBySpecializationWithDescriptor_pipeline_completionHandler_(
        self, a, b, c
    ):
        pass

    def newBinaryFunctionWithDescriptor_compilerTaskOptions_completionHandler_(
        self, a, b, c
    ):
        pass

    def newMachineLearningPipelineStateWithDescriptor_error_(self, a, b):
        pass

    def newMachineLearningPipelineStateWithDescriptor_completionHandler_(self, a, b):
        pass


class TestMTL4Compiler(TestCase):
    @min_sdk_level("26.0")
    def test_protocols(self):
        self.assertProtocolExists("MTL4Compiler")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestMTL4CompilerHelper.newLibraryWithDescriptor_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTL4CompilerHelper.newDynamicLibrary_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTL4CompilerHelper.newDynamicLibraryWithURL_error_, 1, b"o^@"
        )
        self.assertArgHasType(
            TestMTL4CompilerHelper.newDynamicLibrary_error_, 1, b"o^@"
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newComputePipelineStateWithDescriptor_compilerTaskOptions_error_,
            2,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error_,
            3,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newComputePipelineStateWithDescriptor_compilerTaskOptions_error_,
            2,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_error_,
            3,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newRenderPipelineStateBySpecializationWithDescriptor_pipeline_error_,
            2,
            b"o^@",
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newBinaryFunctionWithDescriptor_compilerTaskOptions_error_,
            2,
            b"o^@",
        )

        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newLibraryWithDescriptor_completionHandler_,
            1,
            MTLNewLibraryCompletionHandler,
        )
        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newDynamicLibrary_completionHandler_,
            1,
            MTLNewLibraryCompletionHandler,
        )

        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newComputePipelineStateWithDescriptor_compilerTaskOptions_completionHandler_,
            2,
            MTLNewComputePipelineStateCompletionHandler,
        )
        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newComputePipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_completionHandler_,
            3,
            MTLNewComputePipelineStateCompletionHandler,
        )
        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newRenderPipelineStateWithDescriptor_compilerTaskOptions_completionHandler_,
            2,
            MTLNewRenderPipelineStateCompletionHandler,
        )
        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newRenderPipelineStateWithDescriptor_dynamicLinkingDescriptor_compilerTaskOptions_completionHandler_,
            3,
            MTLNewRenderPipelineStateCompletionHandler,
        )
        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newRenderPipelineStateBySpecializationWithDescriptor_pipeline_completionHandler_,
            2,
            MTLNewRenderPipelineStateCompletionHandler,
        )
        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newBinaryFunctionWithDescriptor_compilerTaskOptions_completionHandler_,
            2,
            MTL4NewBinaryFunctionCompletionHandler,
        )

        self.assertArgHasType(
            TestMTL4CompilerHelper.newMachineLearningPipelineStateWithDescriptor_error_,
            1,
            b"o^@",
        )

        self.assertArgIsBlock(
            TestMTL4CompilerHelper.newMachineLearningPipelineStateWithDescriptor_completionHandler_,
            1,
            MTL4NewMachineLearningPipelineStateCompletionHandler,
        )
