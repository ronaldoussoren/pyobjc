'''
Wrappers for the "CoreData" framework on macOS. The Core Data framework
provides generalized and automated solutions to common tasks associated
with object life-cycle and object graph management, including persistence.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import *
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-CoreData',
    description = "Wrappers for the framework CoreData on macOS",
    packages = [ "CoreData" ],
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
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
