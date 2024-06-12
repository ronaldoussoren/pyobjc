"""
Wrappers for the "Quartz" related frameworks on macOS. These frameworks
provide a number of graphics related API's.

The frameworks wrapped by this package are:

   * CoreGraphics - 2D Graphics, based on the PDF model

   * ImageIO - Reading and writing images

   * QuartzComposer - Working with "Quartz Composer" compositions

   * QuartzCore  - Image processing and video image manipulation

   * QuarzFilters - Image effects

   * ImageKit - iPhoto-like views

   * PDFKit - Working with PDF files

   * CoreVideo - Managing digital video

All frameworks can be accessed by importing the 'Quartz' module.

These wrappers don't include documentation, please check Apple's documentation
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: The actual wrappers are subpackages of ``Quartz``, they are not toplevel
packages to avoid name clashes with Apple provided wrappers for CoreGraphics.

WARNING: Running the unittests will change your display settings during the
testrun, which will probably mess up your window layout.

NEWS
====

2.4
---

* Add wrapper for ``CGBitmapContextCreateWithData``

"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))


from pyobjc_setup import Extension, setup  # noqa: E402

VERSION = "10.3.2"

setup(
    name="pyobjc-framework-Quartz",
    description="Wrappers for the Quartz frameworks on macOS",
    packages=[
        "Quartz",
        "Quartz.CoreGraphics",
        "Quartz.CoreVideo",
        "Quartz.ImageIO",
        "Quartz.ImageKit",
        "Quartz.PDFKit",
        "Quartz.QuartzComposer",
        "Quartz.QuartzCore",
        "Quartz.QuartzFilters",
        "Quartz.QuickLookUI",
    ],
    ext_modules=[
        # CoreVideo
        Extension(
            "Quartz.CoreVideo._CVPixelBuffer",
            ["Modules/_CVPixelBuffer.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
        # CoreGraphics
        Extension(
            "Quartz.CoreGraphics._inlines",
            ["Modules/_CoreGraphics_inlines.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
        Extension(
            "Quartz.CoreGraphics._callbacks",
            ["Modules/_callbacks.m"],
            extra_compile_args=["-Wno-deprecated-declarations"],
            extra_link_args=["-framework", "Quartz"],
            # py_limited_api=True,
        ),
        Extension(
            "Quartz.CoreGraphics._doubleindirect",
            ["Modules/_doubleindirect.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
        Extension(
            "Quartz.CoreGraphics._sortandmap",
            ["Modules/_sortandmap.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
        Extension(
            "Quartz.CoreGraphics._coregraphics",
            ["Modules/_coregraphics.m"],
            extra_link_args=["-framework", "ApplicationServices"],
            # py_limited_api=True,
        ),
        Extension(
            "Quartz.ImageKit._imagekit",
            ["Modules/_imagekit.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
        Extension(
            "Quartz.PDFKit._PDFKit",
            ["Modules/_PDFKit.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
        Extension(
            "Quartz.QuartzCore._quartzcore",
            ["Modules/_quartzcore.m"],
            extra_link_args=["-framework", "QuartzCore"],
            py_limited_api=True,
            depends=["Modules/_CoreImage_protocols.m"],
        ),
        Extension(
            "Quartz.QuickLookUI._QuickLookUI",
            ["Modules/_QuickLookUI.m"],
            extra_link_args=["-framework", "Quartz"],
            py_limited_api=True,
        ),
    ],
    version=VERSION,
    install_requires=["pyobjc-core>=" + VERSION, "pyobjc-framework-Cocoa>=" + VERSION],
    long_description=__doc__,
)
