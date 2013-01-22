'''
Wrappers for framework 'CoreLocation' on MacOSX 10.6. This framework provides
an interface for dealing with the physical location of a machine, which allows
for geo-aware applications.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

setup(
    min_os_level='10.6',
    name='pyobjc-framework-CoreLocation',
    version="2.5.1",
    description = "Wrappers for the framework CoreLocation on Mac OS X",
    packages = [ "CoreLocation" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
    ext_modules = [
        Extension("CoreLocation._CoreLocation",
                [ "Modules/_CoreLocation.m" ],
                extra_link_args=["-framework", "CoreLocation"],
                depends=[
                    os.path.join('Modules', fn)
                        for fn in os.listdir('Modules')
                        if fn.startswith('_CoreLocation')
                ]
        ),
    ]
)
