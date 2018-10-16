'''
Wrappers for the "UserNotifications" framework on macOS.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-UserNotifications',
    description = "Wrappers for the framework UserNotifications on macOS",
    min_os_level="10.14",
    packages = [ "UserNotifications" ],
    ext_modules = [
        Extension("UserNotifications._UserNotifications",
            [ "Modules/_UserNotifications.m" ],
            extra_link_args=["-framework", "UserNotifications"],
            depends=[
                os.path.join('Modules', fn)
                for fn in os.listdir('Modules')
                if fn.startswith('_UserNotifications')
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
