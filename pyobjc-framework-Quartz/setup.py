''' 
Wrappers for frameworks 'CoreGraphics', 'ImageIO', 'QuartzCore', 
'QuartzFilters', 'ImageKit', 'PDFKit' and 'CoreVideo'.

All frameworks can be accessed by importing the 'Quartz' module.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: The actual wrappers are subpackages of ``Quartz``, they are not toplevel
packages to avoid name clashes with Apple provided wrappers for CoreGraphics.
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
    CV_CFLAGS=["-DWITH_CORE_VIDEO"]
else:
    CV_CFLAGS=[]


setup(
    name='pyobjc-framework-Quartz',
    version='2.0',
    description = "Wrappers for the Quartz frameworks on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "Quartz", "Quartz.CoreGraphics", "Quartz.ImageIO", "Quartz.QuartzCore", "Quartz.CoreVideo", "Quartz.QuartzComposer", "Quartz.ImageKit", "Quartz.PDFKit", "Quartz.QuartzFilters" ],
    package_dir = { '': 'Lib' },
    setup_requires = [ 
    ],
    install_requires = [ 
        'pyobjc-core>=2.0',
        'pyobjc-framework-Cocoa>=2.0',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('Quartz'),

    # The package is actually zip-safe, but py2app isn't fully zip-aware yet.
    zip_safe = False,

    ext_modules = [
        # CoreVideo
        Extension('Quartz.CoreVideo._CVPixelBuffer',
            [ 'Modules/_CVPixelBuffer.m' ],
            extra_compile_args=CV_CFLAGS),

        # CoreGraphics
        Extension('Quartz.CoreGraphics._inlines',
            [ 'Modules/_CoreGraphics_inlines.m' ]),
        Extension('Quartz.CoreGraphics._callbacks',
            [ 'Modules/_callbacks.m' ]),
        Extension('Quartz.CoreGraphics._doubleindirect',
            [ 'Modules/_doubleindirect.m' ]),
        Extension('Quartz.CoreGraphics._sortandmap',
            [ 'Modules/_sortandmap.m' ]),
    ],
)
