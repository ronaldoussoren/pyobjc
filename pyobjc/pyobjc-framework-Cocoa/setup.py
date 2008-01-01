''' 
Wrappers for the core Cocoa frameworks: CoreFoundation, Foundation and
AppKit.

These wrappers don't include documentation, please check Apple's documention
for information on how to use these frameworks and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, Extension

import os
if int(os.uname()[2].split('.')[0]) <= 8:
    CFLAGS=["-DBUILD_TIGER"]
else:
    CFLAGS=[]

try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}


setup(
    name='pyobjc-framework-Cocoa',
    version='2.0',
    description = "Wrappers for the Cocoa frameworks on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "Cocoa", "CoreFoundation", "Foundation", "AppKit", "PyObjCTools" ],
    namespace_packages = ['PyObjCTools'],

    package_dir = { '': 'Lib' },
    setup_requires = [
        'bdist_mpkg>=0.4.2',
    ],
    install_requires = [ 
        'pyobjc-core>=2.0',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    zip_safe = False,

    entry_points = {
        'console_scripts': [
            "nibclassbuilder = PyObjCTools.NibClassBuilder.commandline"
        ],
    },
    test_suite='PyObjCTest',

    cmdclass = extra_cmdclass,
    options = extra_options('Cocoa'),

    ext_modules = [
        # CoreFoundation
        Extension('CoreFoundation._inlines', 
                [ 'Modules/_CoreFoundation_inlines.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFCalendar', 
                [ 'Modules/_CoreFoundation_CFCalendar.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFTree', 
                [ 'Modules/_CoreFoundation_CFTree.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFArray', 
                [ 'Modules/_CoreFoundation_CFArray.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFFileDescriptor', 
                [ 'Modules/_CoreFoundation_CFFileDescriptor.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFMachPort', 
                [ 'Modules/_CoreFoundation_CFMachPort.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFMessagePort', 
                [ 'Modules/_CoreFoundation_CFMessagePort.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFNumber', 
                [ 'Modules/_CoreFoundation_CFNumber.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFReadStream', 
                [ 'Modules/_CoreFoundation_CFReadStream.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFWriteStream', 
                [ 'Modules/_CoreFoundation_CFWriteStream.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFRunLoopObserver', 
                [ 'Modules/_CoreFoundation_CFRunLoopObserver.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CFRunLoopTimer', 
                [ 'Modules/_CoreFoundation_CFRunLoopTimer.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'CoreFoundation']),

        # Foundation
        Extension('Foundation._NSDecimal', 
                [ 'Modules/_Foundation_NSDecimal.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._functioncallbacks', 
                [ 'Modules/_Foundation_functioncallbacks.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._nscoder', 
                [ 'Modules/_Foundation_nscoder.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._typecode', 
                [ 'Modules/_Foundation_typecode.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._inlines', 
                [ 'Modules/_Foundation_inlines.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._data', 
                [ 'Modules/_Foundation_data.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._netservice', 
                [ 'Modules/_Foundation_netservice.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._string', 
                [ 'Modules/_Foundation_string.m' ],
                extra_compile_args=CFLAGS,
                extra_link_args=['-framework', 'Foundation']),

        # AppKit
        Extension("AppKit._inlines",
            [ "Modules/_AppKit_inlines.m" ],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._appmain",
            [ "Modules/_AppKit_appmain.m" ],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nsquickdrawview",
            [ "Modules/_AppKit_nsquickdrawview.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nsbezierpath",
            [ "Modules/_AppKit_nsbezierpath.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nsmatrix",
            [ "Modules/_AppKit_nsmatrix.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nsview",
            [ "Modules/_AppKit_nsview.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nsbitmap",
            [ "Modules/_AppKit_nsbitmap.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nsopengl",
            [ "Modules/_AppKit_nsopengl.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._nswindow",
            [ "Modules/_AppKit_nswindow.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._carbon",
            [ "Modules/_AppKit_carbon.m"],
            extra_compile_args=CFLAGS,
            extra_link_args=["-framework", "AppKit"]),
    ],
)
