''' 
Wrappers for framework 'AppleScriptObjC' on MacOSX 10.6. This framework is
not useful for most users, it provides additional functionality for AppleScript
based application bundles.

These wrappers don't include documentation, please check Apple's documention
for information on how to use this framework and PyObjC's documentation
for general tips and tricks regarding the translation between Python
and (Objective-)C frameworks
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
    name='pyobjc-framework-AppleScriptObjC',
    version='2.2b3',
    description = "Wrappers for the framework AppleScriptObjC on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "AppleScriptObjC" ],
    package_dir = { 
        '': 'Lib' 
    },
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
    ],
    dependency_links = [],
    package_data = { 
        '': ['*.xml'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('AppleScriptObjC'),
    zip_safe = True,
)
