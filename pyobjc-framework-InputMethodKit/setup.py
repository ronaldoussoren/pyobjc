'''
Wrappers for the "InputMethodKit" framework on MacOSX 10.5 or later. The
interfaces in this framework allow you to develop input methods.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

setup(
    min_os_level='10.5',
    name='pyobjc-framework-InputMethodKit',
    version="2.5.1",
    description = "Wrappers for the framework InputMethodKit on Mac OS X",
    packages = [ "InputMethodKit" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
    ext_modules = [
        Extension("InputMethodKit._InputMethodKit",
            [ "Modules/_InputMethodKit.m" ],
            extra_link_args=["-framework", "InputMethodKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_InputMethodKit')
            ]
       ),
   ]
)
