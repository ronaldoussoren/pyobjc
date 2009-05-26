''' 
Wrappers for the "LaunchServices" framework on MacOSX. The API's in this 
framework enable applications to open other applictions or their document
files, simularly to how the Dock or Finder do that. 

A number of tasks that can be implemented using this framework:

 * Launch or activate applications

 * Open documents in other applications

 * Identify the preferred application for opening a document

 * Register information about the kinds of documents an application
   can open (UTI's)

 * Obtain information for showing a document (display name, icon, ...)

 * Maintain and update the contents of the Recent Items menu.

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
    name='pyobjc-framework-LaunchServices',
    version='2.2b3',
    description = "Wrappers for the framework LaunchServices on Mac OS X",
    long_description = __doc__,
    author='Ronald Oussoren',
    author_email='pyobjc-dev@lists.sourceforge.net',
    url='http://pyobjc.sourceforge.net',
    platforms = [ "MacOS X" ],
    packages = [ "LaunchServices" ],
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
    options = extra_options('LaunchServices'),
    zip_safe = True,
)
