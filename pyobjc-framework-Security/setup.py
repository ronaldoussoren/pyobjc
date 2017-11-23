'''
Wrappers for the "Security" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="4.1b1"

setup(
    name='pyobjc-framework-Security',
    description = "Wrappers for the framework Security on macOS",
    packages = [ "Security" ],
    #ext_modules = [
    #    Extension('Security._inlines',
    #        [ 'Modules/_Security_inlines.m' ],
    #        extra_link_args=['-framework', 'Security']),
    #    Extension("Security._Security",
    #        [ "Modules/_Security.m" ],
    #        extra_link_args=["-framework", "Security"],
    #        depends=[
    #            os.path.join('Modules', fn)
    #            for fn in os.listdir('Modules')
    #            if fn.startswith('_Security')
    #        ]
    #    ),
    #],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
