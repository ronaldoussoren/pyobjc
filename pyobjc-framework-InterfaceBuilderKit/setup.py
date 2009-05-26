''' 
Wrappers for the framework "InterfaceBuilderKit" on MacOSX. This framework
is only available when you've installed Xcode 3.0 or later. 

The Interface Builder Kit is a framework containing the classes you use to 
implement custom plug-ins for Interface Builder. A plug-in injects one or 
more custom objects into Interface Builder's library window. From the library 
window, users can access your custom objects and drag them into their nib 
files just as they would the standard system controls. You can also use this 
framework to implement inspectors for manipulating your objects at runtime.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks

NOTE: To run the unittests for this framework use::

    $ env DYLD_FRAMEWORK_PATH="$(xcode-select -print-path)/Library/PrivateFrameworks/" python setup.py test

This is needed because the InterfaceBuilderKit framework won't load otherwise.
'''
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup
try:
    from PyObjCMetaData.commands import extra_cmdclass, extra_options
except ImportError:
    extra_cmdclass = {}
    extra_options = lambda name: {}

setup(
    name='pyobjc-framework-InterfaceBuilderKit',
    version='2.2b3',
    description = "Wrappers for the framework InterfaceBuilderKit on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "InterfaceBuilderKit" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b3', 
        'pyobjc-framework-Cocoa>=2.2b3', 
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('InterfaceBuilderKit'),
    zip_safe = True,
)
