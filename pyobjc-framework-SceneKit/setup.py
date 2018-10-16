'''
Wrappers for the "SceneKit" framework on macOS introduced in macOS 10.8.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-SceneKit',
    description = "Wrappers for the framework SceneKit on macOS",
    min_os_level="10.7",
    packages = [ "SceneKit" ],
    ext_modules = [
        Extension("SceneKit._SceneKit",
            [ "Modules/_SceneKit.m" ],
            extra_link_args=["-framework", "SceneKit"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_SceneKit')
            ]
        ),
        Extension("SceneKit._inlines",
            [ "Modules/_SceneKit_inlines.m" ],
            extra_link_args=["-framework", "SceneKit"],
        ),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
        'pyobjc-framework-Quartz>='+VERSION,
    ],
    long_description=__doc__,
)
