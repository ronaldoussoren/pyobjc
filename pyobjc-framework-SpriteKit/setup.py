'''
Wrappers for the "SpriteKit" framework on MacOS X introduced in Mac OS X 10.9.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-SpriteKit',
    version=VERSION,
    description = "Wrappers for the framework SpriteKit on Mac OS X",
    long_description=__doc__,
    packages = [ "SpriteKit" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
        'pyobjc-framework-Quartz>=' + VERSION,
    ],
    ext_modules = [
        Extension("SpriteKit._SpriteKit",
            [ "Modules/_SpriteKit.m" ],
            extra_link_args=["-framework", "SpriteKit"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_SpriteKit')
            ]
        ),
    ],
    min_os_level="10.9",
)
