"""
Python mapping for the Metal framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Metal
    import objc
    from . import _metadata, _MetalPerformanceShaders
    from ._inlines import _inline_list_

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MetalPerformanceShaders",
        frameworkIdentifier="com.apple.MetalPerformanceShaders.MetalPerformanceShaders",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MetalPerformanceShaders.framework"
        ),
        globals_dict=globals(),
        inline_list=_inline_list_,
        parents=(
            _MetalPerformanceShaders,
            Metal,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("MMPSAccelerationStructureGroupTKMeshBufferAllocator", b"init"),
        ("MPSAccelerationStructure", b"init"),
        ("MPSRayIntersector", b"init"),
        ("MPSCNNMultiaryKernel", b"initWithDevice:"),
        ("MPSMatrixSum", b"initWithDevice:"),
        ("MPSNNGraph", b"initWithDevice:"),
        ("MPSNNImageNode", b"init"),
        ("MPSNNStateNode", b"init"),
        ("MPSNNFilterNode", b"init"),
        ("MPSNNGradientFilterNode", b"gradientFilterWithSources:"),
        ("MPSNNGradientFilterNode", b"gradientFiltersWithSources:"),
        ("MPSNNGradientFilterNode", b"gradientFilterWithSource:"),
        ("MPSNNGradientFilterNode", b"gradientFiltersWithSource:"),
        ("MPSCNNBinaryConvolutionNode", b"convolutionGradientState"),
        ("MPSCNNConvolutionTransposeNode", b"convolutionGradientState"),
        ("MPSCNNNeuronNode", b"init"),
        ("MPSCNNNeuronPReLUNode", b"initWithSource:"),
        ("MPSCNNNeuronPReLUNode", b"nodeWithSource:"),
        ("MPSCNNNeuronGradientNode", b"init"),
        ("MPSNNBinaryArithmeticNode", b"gradientFilterWithSources:"),
        ("MPSCNNLossNode", b"gradientFilterWithSources:"),
        ("MPSCNNYOLOLossNode", b"gradientFilterWithSources:"),
        ("MPSNNConcatenationNode", b"gradientFilterWithSources:"),
        ("MPSNNLossGradientNode", b"gradientFilterWithSources:"),
        ("MPSNNInitialGradientNode", b"gradientFilterWithSources:"),
        ("MPSCNNArithmeticGradientState", b"init"),
        ("MPSCNNArithmetic", b"initWithDevice:"),
        ("MPSCNNArithmeticGradient", b"initWithDevice:"),
        ("MPSCNNArithmeticGradient", b"initWithDevice:isSecondarySourceFilter:"),
        ("MPSCNNUpsampling", b"initWithDevice:"),
        ("MPSCNNConvolution", b"initWithDevice:"),
        ("MPSCNNConvolutionGradient", b"initWithDevice:"),
        ("MPSCNNFullyConnected", b"initWithDevice:"),
        ("MPSCNNFullyConnectedGradient", b"initWithDevice:"),
        ("MPSCNNConvolutionTranspose", b"initWithDevice:"),
        ("MPSCNNConvolutionTransposeGradient", b"initWithDevice:"),
        ("MPSCNNBinaryConvolution", b"initWithDevice:"),
        ("MPSCNNBinaryFullyConnected", b"initWithDevice:"),
        ("MPSNNResizeBilinear", b"initWithDevice:"),
        ("MPSNNCropAndResizeBilinear", b"initWithDevice:"),
        ("MPSCNNBatchNormalizationState", b"initWithResource:"),
        (
            "MPSCNNBatchNormalizationState",
            b"temporaryStateWithCommandBuffer:bufferSize:",
        ),
        (
            "MPSCNNBatchNormalizationState",
            b"temporaryStateWithCommandBuffer:textureDescriptor:",
        ),
        ("MPSCNNBatchNormalization", b"initWithDevice:"),
        (
            "MPSCNNBatchNormalization",
            b"encodeToCommandBuffer:sourceImage:destinationState:destinationImage:",
        ),
        (
            "MPSCNNBatchNormalization",
            b"encodeToCommandBuffer:sourceImage:destinationState:destinationStateIsTemporary:",
        ),
        (
            "MPSCNNBatchNormalization",
            b"encodeToCommandBuffer:sourceImage:destinationStates:destinationImages:",
        ),
        (
            "MPSCNNBatchNormalization",
            b"encodeToCommandBuffer:sourceImage:destinationStates:destinationStateIsTemporary:",
        ),
        (
            "MPSCNNBatchNormalizationStatistics",
            b"encodeToCommandBuffer:sourceImage:destinationImages:",
        ),
        (
            "MPSCNNBatchNormalizationStatistics",
            b"encodeToCommandBuffer:sourceImage:destinationImage:",
        ),
        ("MPSCNNBatchNormalizationStatistics", b"encodeToCommandBuffer:sourceImage:"),
        ("MPSCNNBatchNormalizationStatistics", b"encodeToCommandBuffer:sourceImages:"),
        ("MPSCNNBatchNormalizationState", b"initWithResource:"),
        (
            "MPSCNNBatchNormalizationGradient",
            b"encodeToCommandBuffer:primaryImage:secondaryImage:destinationImage:",
        ),
        (
            "MPSCNNBatchNormalizationGradient",
            b"encodeToCommandBuffer:primaryImages:secondaryImages:destinationImages:",
        ),
        (
            "MPSCNNBatchNormalizationGradient",
            b"encodeToCommandBuffer:primaryImage:secondaryImage:",
        ),
        (
            "MPSCNNBatchNormalizationGradient",
            b"encodeToCommandBuffer:primaryImages:secondaryImages:",
        ),
        (
            "MPSCNNBatchNormalizationStatisticsGradient",
            b"encodeToCommandBuffer:sourceGradient:sourceImage:gradientState:",
        ),
        (
            "MPSCNNBatchNormalizationStatisticsGradient",
            b"encodeToCommandBuffer:sourceGradient:sourceImage:gradientState:destinationGradient:",
        ),
        (
            "MPSCNNBatchNormalizationStatisticsGradient",
            b"encodeToCommandBuffer:sourceGradients:sourceImages:gradientStates:destinationGradients:",
        ),
        ("MPSCNNLossDataDescriptor", b"init"),
        ("MPSCNNLossLabels", b"init"),
        ("MPSCNNLossDescriptor", b"init"),
        ("MPSCNNLoss", b"initWithDevice:"),
        ("MPSCNNYOLOLossDescriptor", b"init"),
        ("MPSCNNYOLOLoss", b"initWithDevice:"),
        ("MPSNNForwardLoss", b"initWithDevice:"),
        ("MPSNNLossGradient", b"initWithDevice:"),
        ("MPSRNNImageInferenceLayer", b"initWithDevice:"),
        ("MPSRNNMatrixInferenceLayer", b"initWithDevice:"),
        ("MPSRNNMatrixTrainingLayer", b"initWithDevice:"),
        ("MPSNNReduceUnary", b"initWithDevice:"),
        ("MPSNNReduceBinary", b"initWithDevice:"),
        ("MPSNNNeuronDescriptor", b"init"),
        ("MPSCNNNeuron", b"initWithDevice:"),
        ("MPSCNNNeuronGradient", b"initWithDevice:"),
        ("MPSCNNNeuronLinear", b"initWithDevice:"),
        ("MPSCNNNeuronReLU", b"initWithDevice:"),
        ("MPSCNNNeuronPReLU", b"initWithDevice:"),
        ("MPSCNNNeuronHardSigmoid", b"initWithDevice:"),
        ("MPSCNNNeuronTanH", b"initWithDevice:"),
        ("MPSCNNNeuronSoftPlus", b"initWithDevice:"),
        ("MPSCNNNeuronELU", b"initWithDevice:"),
        ("MPSCNNNeuronReLUN", b"initWithDevice:"),
        ("MPSCNNNeuronPower", b"initWithDevice:"),
        ("MPSCNNNeuronExponential", b"initWithDevice:"),
        ("MPSCNNNeuronLogarithm", b"initWithDevice:"),
        ("MPSNNOptimizer", b"initWithDevice:"),
        ("MPSNNOptimizerStochasticGradientDescent", b"initWithDevice:"),
        ("MPSNNOptimizerRMSProp", b"initWithDevice:"),
        ("MPSNNOptimizerAdam", b"initWithDevice:"),
        ("MPSCNNPooling", b"initWithDevice:"),
        ("MPSCNNPoolingGradient", b"initWithDevice:"),
        (
            "MPSCNNDilatedPoolingMaxGradient",
            b"initWithDevice:kernelWidth:kernelHeight:strideInPixelsX:strideInPixelsY:",
        ),
        (
            "MPSCNNInstanceNormalizationGradientState",
            b"temporaryStateWithCommandBuffer:textureDescriptor:",
        ),
        (
            "MPSCNNInstanceNormalizationGradientState",
            b"temporaryStateWithCommandBuffer:",
        ),
        (
            "MPSCNNInstanceNormalizationGradientState",
            b"temporaryStateWithCommandBuffer:bufferSize:",
        ),
        (
            "MPSCNNInstanceNormalizationGradientState",
            b"initWithDevice:textureDescriptor:",
        ),
        ("MPSCNNInstanceNormalizationGradientState", b"initWithResource:"),
        ("MPSCNNInstanceNormalizationGradientState", b"initWithDevice::bufferSize:"),
        ("MPSCNNInstanceNormalization", b"initWithDevice:"),
        ("MPSCNNSpatialNormalization", b"initWithDevice:"),
        ("MPSCNNLocalContrastNormalization", b"initWithDevice:"),
        ("MPSCNNCrossChannelNormalization", b"initWithDevice:"),
        ("MPSCNNDropoutGradientState", b"init"),
        ("MPSCNNDropout", b"initWithDevice:"),
        ("MPSCNNDropoutGradient", b"initWithDevice:"),
        (
            "MPSCNNGroupNormalizationGradientState",
            b"temporaryStateWithCommandBuffer:textureDescriptor:",
        ),
        ("MPSCNNGroupNormalizationGradientState", b"temporaryStateWithCommandBuffer:"),
        (
            "MPSCNNGroupNormalizationGradientState",
            b"temporaryStateWithCommandBuffer:bufferSize:",
        ),
        ("MPSCNNGroupNormalizationGradientState", b"initWithDevice:textureDescriptor:"),
        ("MPSCNNGroupNormalizationGradientState", b"initWithResource:"),
        ("MPSCNNGroupNormalizationGradientState", b"initWithDevice::bufferSize:"),
        ("MPSCNNGroupNormalization", b"initWithDevice:"),
        ("MPSNDArrayMultiaryBase", b"initWithDevice:"),
        ("MPSNDArrayMultiaryGradientKernel", b"initWithDevice:sourceCount:"),
        ("MPSNDArrayUnaryKernel", b"initWithDevice:sourceCount:"),
        (
            "MPSNDArrayUnaryGradientKernel",
            b"initWithDevice:sourceCount:sourceGradientIndex:",
        ),
        ("MPSNDArrayBinaryKernel", b"initWithDevice:sourceCount:"),
        (
            "MPSNDArrayBinaryPrimaryGradientKernel",
            b"initWithDevice:sourceCount:sourceGradientIndex:",
        ),
        (
            "MPSNDArrayBinarySecondaryGradientKernel",
            b"initWithDevice:sourceCount:sourceGradientIndex:",
        ),
        ("MPSCommandBuffer", b"init"),
        ("MPSKeyedUnarchiver", b"unarchivedObjectOfClasses:fromData:error:"),
        ("MPSKeyedUnarchiver", b"unarchivedObjectOfClass:fromData:error:"),
        ("MPSKeyedUnarchiver", b"init"),
        ("MPSKeyedUnarchiver", b"initForReadingFromData:error:"),
        ("MPSKeyedUnarchiver", b"unarchiveObjectWithData:"),
        ("MPSKeyedUnarchiver", b"unarchiveTopLevelObjectWithData:error:"),
        ("MPSKeyedUnarchiver", b"unarchiveObjectWithFile:"),
        ("MPSKeyedUnarchiver", b"initForReadingWithData:"),
        ("MPSNDArrayDescriptor", b"init"),
        ("MPSNDArray", b"init"),
        ("MPSTemporaryNDArray", b"initWithDevice:descriptor:"),
        ("MPSState", b"init"),
        ("MPSImage", b"init"),
        ("MPSTemporaryImage", b"initWithDevice:imageDescriptor:"),
        ("MPSMatrix", b"init"),
        ("MPSVector", b"init"),
        ("MPSTemporaryMatrix", b"initWithBuffer:descriptor:"),
        ("MPSTemporaryVector", b"initWithBuffer:descriptor:"),
        ("MPSImageThresholdBinary", b"initWithDevice:"),
        ("MPSImageThresholdBinaryInverse", b"initWithDevice:"),
        ("MPSImageThresholdTruncate", b"initWithDevice:"),
        ("MPSImageThresholdToZero", b"initWithDevice:"),
        ("MPSImageThresholdToZeroInverse", b"initWithDevice:"),
        ("MPSImageArithmetic", b"initWithDevice:"),
        ("MPSImageReduceUnary", b"initWithDevice:"),
        ("MPSImageMedian", b"initWithDevice:"),
        ("MPSImageAreaMax", b"initWithDevice:"),
        ("MPSImageDilate", b"initWithDevice:"),
        ("MPSImageBox", b"initWithDevice:"),
        ("MPSImageGaussianBlur", b"initWithDevice:"),
        ("MPSImageGuidedFilter", b"initWithDevice:"),
        ("MPSImageFindKeypoints", b"initWithDevice:"),
        ("MPSMatrixFindTopK", b"initWithDevice:"),
        ("MPSMatrixRandom", b"initWithDevice:"),
        ("MPSMatrixMultiplication", b"initWithDevice:"),
        ("MPSMatrixVectorMultiplication", b"initWithDevice:"),
        ("MPSMatrixCopyDescriptor", b"init"),
        ("MPSMatrixCopy", b"initWithDevice:"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["MetalPerformanceShaders._metadata"]


globals().pop("_setup")()
