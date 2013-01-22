'''
Wrappers for the core Cocoa frameworks: CoreFoundation, Foundation and
AppKit.

These wrappers don't include documentation, please check Apple's documention
for information on how to use these frameworks and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-Cocoa',
    version="2.5.1",
    description = "Wrappers for the Cocoa frameworks on Mac OS X",
    packages = [ "Cocoa", "CoreFoundation", "Foundation", "AppKit", "PyObjCTools" ],
    namespace_packages = ['PyObjCTools'],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
    ],
    ext_modules = [
        # CoreFoundation
        Extension('CoreFoundation._inlines',
                [ 'Modules/_CoreFoundation_inlines.m' ],
                extra_link_args=['-framework', 'CoreFoundation']),
        Extension('CoreFoundation._CoreFoundation',
            [ 'Modules/_CoreFoundation.m' ],
            extra_link_args=['-framework', 'CoreFoundation'],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_CoreFoundation') ]),

        # Foundation
        Extension('Foundation._inlines',
                [ 'Modules/_Foundation_inlines.m' ],
                extra_link_args=['-framework', 'Foundation']),
        Extension('Foundation._Foundation',
            [ 'Modules/_Foundation.m' ],
            extra_link_args=['-framework', 'Foundation'],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_Foundation') ]),

        # AppKit
        Extension("AppKit._inlines",
            [ "Modules/_AppKit_inlines.m" ],
            extra_link_args=["-framework", "AppKit"]),
        Extension("AppKit._AppKit",
            [ "Modules/_AppKit.m" ],
            extra_link_args=["-framework", "AppKit"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_AppKit') ]),


        #
        # Test support
        #
        Extension("PyObjCTest.testhelper",
            [ "Modules/testhelper.m"],
            extra_link_args=["-framework", "Foundation"]),
    ],
)
