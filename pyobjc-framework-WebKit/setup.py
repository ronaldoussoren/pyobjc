''' 
Wrappers for the "WebKit" and "JavaScriptCore" frameworks on MacOSX. The
WebKit framework contains the views and support classes for creating a
browser. The JavaScriptCore framework implements a JavaScript interpreter.

These wrappers don't include documentation, please check Apple's documention
for information on how to use these frameworks and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-WebKit',
    version="2.3",
    description = "Wrappers for the framework WebKit on Mac OS X",
    packages = [ "WebKit", "JavaScriptCore" ],
    install_requires = [ 
        'pyobjc-core>=2.3',
        'pyobjc-framework-Cocoa>=2.3',
    ],
)
