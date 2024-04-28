"""
Python mapping for the CoreML framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _CoreML

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="CoreML",
        frameworkIdentifier="com.apple.CoreML",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/CoreML.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _CoreML,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for clsname in (
        "MLComputePlan",
        "MLComputePlanCost",
        "MLComputePlanDeviceUsage",
        "MLModelStructureNeuralNetwork",
        "MLModelStructurePipeline",
        "MLModelStructureProgram",
        "MLModelStructureProgramArgument",
        "MLModelStructureProgramBinding",
        "MLModelStructureProgramBlock",
        "MLModelStructureProgramFunction",
        "MLModelStructureProgramNamedValueType",
        "MLModelStructureProgramOperation",
        "MLModelStructureProgramValue",
        "MLModelStructureProgramValueType",
    ):
        try:
            objc.lookUpClass(clsname).__objc_final__ = True
        except objc.error:
            pass

    for cls, sel in (
        ("MLMetricKey", b"init"),
        ("MLMetricKey", b"new"),
        ("MLModelStructureProgramValue", b"init"),
        ("MLModelStructureProgramValue", b"new"),
        ("MLGPUComputeDevice", b"init"),
        ("MLGPUComputeDevice", b"new"),
        ("MLComputePlanDeviceUsage", b"init"),
        ("MLComputePlanDeviceUsage", b"new"),
        ("MLCPUComputeDevice", b"init"),
        ("MLCPUComputeDevice", b"new"),
        ("MLModelStructure", b"init"),
        ("MLModelStructure", b"new"),
        ("MLUpdateProgressHandlers", b"init"),
        ("MLUpdateProgressHandlers", b"new"),
        ("MLModelCollection", b"init"),
        ("MLModelCollection", b"new"),
        ("MLModelStructureProgramNamedValueType", b"init"),
        ("MLModelStructureProgramNamedValueType", b"new"),
        ("MLUpdateTask", b"init"),
        ("MLUpdateTask", b"new"),
        ("MLModelCollectionEntry", b"init"),
        ("MLModelCollectionEntry", b"new"),
        ("MLModelStructureProgramFunction", b"init"),
        ("MLModelStructureProgramFunction", b"new"),
        ("MLModelStructureProgram", b"init"),
        ("MLModelStructureProgram", b"new"),
        ("MLComputePlan", b"init"),
        ("MLComputePlan", b"new"),
        ("MLParameterKey", b"init"),
        ("MLParameterKey", b"new"),
        ("MLModelStructureProgramBinding", b"init"),
        ("MLModelStructureProgramBinding", b"new"),
        ("MLModelAsset", b"init"),
        ("MLModelAsset", b"new"),
        ("MLModelStructureProgramArgument", b"init"),
        ("MLModelStructureProgramArgument", b"new"),
        ("MLModelStructureProgramOperation", b"init"),
        ("MLModelStructureProgramOperation", b"new"),
        ("MLComputePlanCost", b"init"),
        ("MLComputePlanCost", b"new"),
        ("MLModelStructureNeuralNetwork", b"init"),
        ("MLModelStructureNeuralNetwork", b"new"),
        ("MLNeuralEngineComputeDevice", b"init"),
        ("MLNeuralEngineComputeDevice", b"new"),
        ("MLTask", b"init"),
        ("MLTask", b"new"),
        ("MLModelStructureNeuralNetworkLayer", b"init"),
        ("MLModelStructureNeuralNetworkLayer", b"new"),
        ("MLKey", b"init"),
        ("MLKey", b"new"),
        ("MLModelStructureProgramBlock", b"init"),
        ("MLModelStructureProgramBlock", b"new"),
        ("MLImageConstraint", b"init"),
        ("MLModelStructurePipeline", b"init"),
        ("MLModelStructurePipeline", b"new"),
        ("MLModelStructureProgramValueType", b"init"),
        ("MLModelStructureProgramValueType", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["CoreML._metadata"]


globals().pop("_setup")()
