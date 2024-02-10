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

    del sys.modules["CoreML._metadata"]


globals().pop("_setup")()
