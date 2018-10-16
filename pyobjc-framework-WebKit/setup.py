'''
Wrappers for the "WebKit" and "JavaScriptCore" frameworks on macOS. The
WebKit framework contains the views and support classes for creating a
browser. The JavaScriptCore framework implements a JavaScript interpreter.

These wrappers don't include documentation, please check Apple's documention
for information on how to use these frameworks and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup, Extension
import os

VERSION="5.1"

setup(
    name='pyobjc-framework-WebKit',
    description = "Wrappers for the framework WebKit on macOS",
    packages = [ "WebKit", "JavaScriptCore" ],
    ext_modules = [
        Extension("WebKit._WebKit",
            [ "Modules/_WebKit.m" ],
            extra_link_args=["-framework", "WebKit"],
            depends=[
                os.path.join('Modules', fn)
                    for fn in os.listdir('Modules')
                    if fn.startswith('_WebKit')
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
