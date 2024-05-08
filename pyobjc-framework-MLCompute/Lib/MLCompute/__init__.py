"""
Python mapping for the MLCompute framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="MLCompute",
        frameworkIdentifier="com.apple.MLCompute",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/MLCompute.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(Foundation,),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    for cls, sel in (
        ("MLCTensorParameter", b"init"),
        ("MLCTensorParameter", b"new"),
        ("MLCTensorOptimizerDeviceData", b"init"),
        ("MLCTensorOptimizerDeviceData", b"new"),
        ("MLCTensor", b"init"),
        ("MLCTensor", b"new"),
        ("MLCLSTMDescriptor", b"init"),
        ("MLCLSTMDescriptor", b"new"),
        ("MLCActivationDescriptor", b"init"),
        ("MLCActivationDescriptor", b"new"),
        ("MLCMatMulDescriptor", b"init"),
        ("MLCMatMulDescriptor", b"new"),
        ("MLCEmbeddingDescriptor", b"init"),
        ("MLCEmbeddingDescriptor", b"new"),
        ("MLCInferenceGraph", b"init"),
        ("MLCInferenceGraph", b"new"),
        ("MLCLayer", b"init"),
        ("MLCLayer", b"new"),
        ("MLCTensorDescriptor", b"init"),
        ("MLCTensorDescriptor", b"new"),
        ("MLCYOLOLossDescriptor", b"init"),
        ("MLCYOLOLossDescriptor", b"new"),
        ("MLCTensorData", b"init"),
        ("MLCTensorData", b"new"),
        ("MLCPoolingDescriptor", b"init"),
        ("MLCPoolingDescriptor", b"new"),
        ("MLCOptimizer", b"init"),
        ("MLCOptimizer", b"new"),
        ("MLCLossDescriptor", b"init"),
        ("MLCLossDescriptor", b"new"),
        ("MLCMultiheadAttentionDescriptor", b"init"),
        ("MLCMultiheadAttentionDescriptor", b"new"),
    ):
        objc.registerUnavailableMethod(cls, sel)

    del sys.modules["MLCompute._metadata"]


globals().pop("_setup")()
