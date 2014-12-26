'''
Wrappers for "InstantMessage" framework on MacOSX 10.5 or later. This framework
allows you to access iChat information, as well as a way to provide an
auxilliary video source to iChat Theater.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

Note that this framework is deprecated in OSX 10.9, use the Social framework
instead if you target that OSX release.
'''
from pyobjc_setup import setup
setup(
    min_os_level='10.5',
    name='pyobjc-framework-InstantMessage',
    version="3.1b1",
    description = "Wrappers for the framework InstantMessage on Mac OS X",
    long_description=__doc__,
    packages = [ "InstantMessage" ],
    setup_requires = [
        'pyobjc-core>=3.1b1',
    ],
    install_requires = [
        'pyobjc-core>=3.1b1',
        'pyobjc-framework-Cocoa>=3.1b1',
        'pyobjc-framework-Quartz>=3.1b1',
    ],
)
