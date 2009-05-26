''' 
Wrappers for the "Quartz" related frameworks on MacOSX. These frameworks
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

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: The actual wrappers are subpackages of ``Quartz``, they are not toplevel
packages to avoid name clashes with Apple provided wrappers for CoreGraphics.

WARNING: Running the unittests will change your display settings during the
testrun, which will probably mess up your window layout.
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

import os

if int(os.uname()[2].split('.')[0]) > 8:
    CV_CFLAGS=["-DWITH_CORE_VIDEO", "-isysroot", "/"]
else:
    CV_CFLAGS=[]

if int(os.uname()[2].split('.')[0]) > 8:
    CFLAGS = [ "-isysroot", "/" ]
else:
    CFLAGS=[ "-DNO_OBJC2_RUNTIME", "-DOS_TIGER" ]

setup(
    name='pyobjc-framework-Quartz',
    version='2.2b3',
    description = "Wrappers for the Quartz frameworks on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "Quartz", "Quartz.CoreGraphics", "Quartz.ImageIO", "Quartz.QuartzCore", "Quartz.CoreVideo", "Quartz.QuartzComposer", "Quartz.ImageKit", "Quartz.PDFKit", "Quartz.QuartzFilters" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('Quartz'),
    zip_safe = True,
    ext_modules = [
        # CoreVideo
        Extension('Quartz.CoreVideo._CVPixelBuffer',
            [ 'Modules/_CVPixelBuffer.m' ],
            extra_compile_args=CV_CFLAGS + CFLAGS),

        # CoreGraphics
        Extension('Quartz.CoreGraphics._inlines',
            [ 'Modules/_CoreGraphics_inlines.m' ],
            extra_compile_args=CFLAGS),
        Extension('Quartz.CoreGraphics._callbacks',
            [ 'Modules/_callbacks.m' ],
            extra_compile_args=CFLAGS),
        Extension('Quartz.CoreGraphics._doubleindirect',
            [ 'Modules/_doubleindirect.m' ],
            extra_compile_args=CFLAGS),
        Extension('Quartz.CoreGraphics._sortandmap',
            [ 'Modules/_sortandmap.m' ],
            extra_compile_args=CFLAGS),
        Extension('Quartz.CoreGraphics._coregraphics',
            [ 'Modules/_coregraphics.m' ],
            extra_compile_args=CFLAGS),
    ],
)
