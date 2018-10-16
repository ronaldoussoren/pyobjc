'''
Wrappers for framework 'AppleScriptObjC' on macOS 10.6. This framework is
not useful for most users, it provides additional functionality for AppleScript
based application bundles.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

VERSION="5.1"

setup(
    name='pyobjc-framework-AppleScriptObjC',
    description = "Wrappers for the framework AppleScriptObjC on macOS",
    min_os_level='10.6',
    packages = [ "AppleScriptObjC" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
