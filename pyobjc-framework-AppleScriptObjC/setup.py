'''
Wrappers for framework 'AppleScriptObjC' on MacOSX 10.6. This framework is
not useful for most users, it provides additional functionality for AppleScript
based application bundles.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''

from pyobjc_setup import setup

setup(
    min_os_level='10.6',
    name='pyobjc-framework-AppleScriptObjC',
    version="2.5.1",
    description = "Wrappers for the framework AppleScriptObjC on Mac OS X",
    packages = [ "AppleScriptObjC" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
)
