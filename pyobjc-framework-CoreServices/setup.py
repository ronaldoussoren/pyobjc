'''
Wrappers for the "CoreServices" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

subpackages = [ "CoreServices.%s"%(fn,) for fn in os.listdir('Lib/CoreServices') if os.path.exists(os.path.join('Lib/CoreServices', fn, "__init__.py"))]

setup(
    name='pyobjc-framework-CoreServices',
    description = "Wrappers for the framework CoreServices on macOS",
    packages = [ "CoreServices" ] + subpackages,
    ext_modules = [
        Extension('CoreServices._inlines',
            [ 'Modules/_CoreServices_inlines.m' ],
            extra_link_args=['-framework', 'CoreServices']),
    ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-FSEvents>='+VERSION,
    ],
    long_description=__doc__,
)
