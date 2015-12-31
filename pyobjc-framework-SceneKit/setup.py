'''
Wrappers for the "SceneKit" framework on MacOS X introduced in Mac OS X 10.8.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

setup(
    name='pyobjc-framework-SceneKit',
    version="3.1b1",
    description = "Wrappers for the framework SceneKit on Mac OS X",
    long_description=__doc__,
    packages = [ "SceneKit" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
        'pyobjc-framework-Quartz>=3.1b1',
    ],
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
    min_os_level="10.7"
)
