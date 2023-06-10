"""
Python mapping for the QuartzCore framework.

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _setup():
    import sys

    import Foundation
    import objc
    from . import _metadata, _quartzcore

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz.QuartzCore",
        frameworkIdentifier="com.apple.QuartzCore",
        frameworkPath=objc.pathForFramework(
            "/System/Library/Frameworks/QuartzCore.framework"
        ),
        globals_dict=globals(),
        inline_list=None,
        parents=(
            _quartzcore,
            Foundation,
        ),
        metadict=_metadata.__dict__,
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func

    del sys.modules["Quartz.QuartzCore._metadata"]

    def CIVector__getitem__(self, idx):
        if isinstance(idx, slice):
            start, stop, step = idx.indices(self.count())
            return [self[i] for i in range(start, stop, step)]

        if idx < 0:
            new = self.count() + idx
            if new < 0:
                raise IndexError(idx)
            idx = new

        return self.valueAtIndex_(idx)

    objc.addConvenienceForClass(
        "CIVector",
        (("__len__", lambda self: self.count()), ("__getitem__", CIVector__getitem__)),
    )

    objc.addConvenienceForClass(
        "CIContext",
        (
            ("__getitem__", lambda self, key: self.objectForKey_(key)),
            (
                "__setitem__",
                lambda self, key, value: self.setObject_forKey_(value, key),
            ),
        ),
    )
    objc.addConvenienceForClass(
        "CIContextImpl",
        (
            ("__getitem__", lambda self, key: self.objectForKey_(key)),
            (
                "__setitem__",
                lambda self, key, value: self.setObject_forKey_(value, key),
            ),
        ),
    )

    objc.addConvenienceForBasicSequence("QCStructure", True)


globals().pop("_setup")()
