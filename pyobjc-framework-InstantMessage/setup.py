''' 
Wrappers for "InstantMessage" framework on MacOSX 10.5 or later. This framework
allows you to access iChat information, as well as a way to provide an 
auxilliary video source to iChat Theater.

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
    name='pyobjc-framework-InstantMessage',
    version='2.2b3',
    description = "Wrappers for the framework InstantMessage on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "InstantMessage" ],
    package_dir = { '': 'Lib' },
    install_requires = [ 
        'pyobjc-core>=2.2b3',
        'pyobjc-framework-Cocoa>=2.2b3',
        'pyobjc-framework-Quartz>=2.2b3',
    ],
    package_data = { 
        '': ['*.bridgesupport'] 
    },
    test_suite='PyObjCTest',
    cmdclass = extra_cmdclass,
    options = extra_options('InstantMessage'),
    zip_safe = True,
)
