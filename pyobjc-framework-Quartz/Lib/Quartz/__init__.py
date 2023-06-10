"""
Helper module that makes it easier to import all of Quartz
"""


def _setup():
    import AppKit
    import objc

    from . import (
        CoreGraphics,
        ImageIO,
        ImageKit,
        CoreVideo,
        QuartzCore,
        PDFKit,
        QuartzFilters,
        QuickLookUI,
        QuartzComposer,
    )

    dir_func, getattr_func = objc.createFrameworkDirAndGetattr(
        name="Quartz",
        frameworkIdentifier=None,
        frameworkPath=None,
        globals_dict=globals(),
        inline_list=None,
        parents=(
            CoreGraphics,
            ImageIO,
            ImageKit,
            CoreVideo,
            QuartzCore,
            PDFKit,
            QuartzFilters,
            QuickLookUI,
            QuartzComposer,
            AppKit,
        ),
        metadict={},
    )

    globals()["__dir__"] = dir_func
    globals()["__getattr__"] = getattr_func


globals().pop("_setup")()
