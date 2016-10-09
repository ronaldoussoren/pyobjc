'''
Wrappers for the "CoreData" framework on MacOSX. The Core Data framework
provides generalized and automated solutions to common tasks associated
with object life-cycle and object graph management, including persistence.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import *
import os

VERSION="3.2a1"

setup(
    name='pyobjc-framework-CoreData',
    version=VERSION,
    description = "Wrappers for the framework CoreData on Mac OS X",
    long_description=__doc__,
    packages = [ "CoreData" ],
    setup_requires = [
        'pyobjc-core>=' + VERSION,
    ],
    install_requires = [
        'pyobjc-core>=' + VERSION,
        'pyobjc-framework-Cocoa>=' + VERSION,
    ],
    ext_modules = [
        Extension("CoreData._CoreData",
            [ "Modules/_CoreData.m" ],
            extra_link_args=["-framework", "CoreData"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_CoreData')
            ]
        ),
    ],

)
