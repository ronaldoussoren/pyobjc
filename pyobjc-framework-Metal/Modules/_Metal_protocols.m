static void __attribute__((__used__))
use_protocols(void)
{
    PyObject* p __attribute__((__unused__));
#if 0
    p = PyObjC_IdToPython(@protocol(MTKViewDelegate));
    Py_XDECREF(p);
#endif

#if PyObjC_BUILD_RELEASE >= 1011
    p = PyObjC_IdToPython(@protocol(MTLRenderCommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLComputeCommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLBlitCommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLCommandQueue));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1013
    p = PyObjC_IdToPython(@protocol(MTLArgumentEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFence));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLCaptureScope));
    Py_XDECREF(p);

#endif

#if PyObjC_BUILD_RELEASE >= 1015
    p = PyObjC_IdToPython(@protocol(MTLCounter));
    Py_XDECREF(p);

    p = PyObjC_IdToPython(@protocol(MTLCounterSet));
    Py_XDECREF(p);

    p = PyObjC_IdToPython(@protocol(MTLCounterSampleBuffer));
    Py_XDECREF(p);

#endif
#if PyObjC_BUILD_RELEASE >= 1016
    p = PyObjC_IdToPython(@protocol(MTLBinaryArchive));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLDynamicLibrary));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionHandle));
    Py_XDECREF(p);
    // p = PyObjC_IdToPython(@protocol(MTLFunctionLogContainer));
    // Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLogDebugLocation));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLog));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIntersectionFunctionTable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLVisibleFunctionTable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLAccelerationStructureCommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLLogContainer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLogDebugLocation));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLFunctionLog));
    Py_XDECREF(p);
    // p = PyObjC_IdToPython(@protocol(MTLIndirectComputeCommand));
    // Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1300
    p = PyObjC_IdToPython(@protocol(MTLBinding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLBufferBinding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLThreadgroupBinding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLTextureBinding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLObjectPayloadBinding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIOCommandBuffer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIOCommandQueue));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIOScratchBuffer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIOScratchBufferAllocator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLIOFileHandle));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1500
    p = PyObjC_IdToPython(@protocol(MTLLogState));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLResidencySet));
    Py_XDECREF(p);
#endif
#if PyObjC_BUILD_RELEASE >= 1500
    p = PyObjC_IdToPython(@protocol(MTL4Archive));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4ArgumentTable));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4BinaryFunction));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CommandAllocator));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CommandBuffer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CommandQueue));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CommitFeedback));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4Compiler));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CompilerTask));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4ComputeCommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4CounterHeap));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4MachineLearningCommandEncoder));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4MachineLearningPipelineState));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4PipelineDataSetSerializer));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLTensorBinding));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLComputePipelineState));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLRenderPipelineState));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLResourceViewPool));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLTensor));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTLTextureViewPool));
    Py_XDECREF(p);
    p = PyObjC_IdToPython(@protocol(MTL4RenderCommandEncoder));
    Py_XDECREF(p);
#endif
}
