"""
Python mapping for the JavaScriptCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""

import objc as _objc


def _setup():
    import sys

    import CoreFoundation
    import objc
    from . import _metadata, _util, _JavaScriptCore

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="JavaScriptCore",
        frameworkIdentifier="com.apple.JavaScriptCore",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/JavaScriptCore.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _util,
            _JavaScriptCore,
            CoreFoundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["JavaScriptCore._metadata"]


globals().pop("_setup")()


def JSExportAs(PropertyName, Selector):
    return (
        _objc.selector(
            None,
            selector=Selector.selector
            + b"__JS_EXPORT_AS__"
            + PropertyName.encode()
            + b":",
            signature=Selector.signature + b"@",
            isRequired=False,
            isClassMethod=Selector.isClassMethod,
        ),
        Selector,
    )
