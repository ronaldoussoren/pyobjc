"""
Python mapping for the PrintCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""
from functools import wraps as _wraps


def _setup():
    import sys

    import Cocoa
    import objc
    from . import _metadata, _PrintCore

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="PrintCore",
        frameworkIdentifier="com.apple.ApplicationServices",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/ApplicationServices.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(_PrintCore, Cocoa),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["PrintCore._metadata"]


globals().pop("_setup")()

#
# PMRetain and PMRelease are "generic" functions
# where the argument can be an instance of a number
# of PrintCore types.
#
# The code below ensures these functions actually
# work as expected.
#

import PrintCore as _PrintCore  # isort:ignore  # noqa: E402

_PMRetain = _PrintCore.PMRetain

_PMRelease = _PrintCore.PMRelease

del _PrintCore


@_wraps(_PMRetain)
def PMRetain(value):
    return _PMRetain(value.__pointer__)


@_wraps(_PMRelease)
def PMRelease(value):
    return _PMRelease(value.__pointer__)
