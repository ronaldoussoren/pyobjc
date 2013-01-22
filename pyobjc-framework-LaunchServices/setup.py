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

NOTE: This wrapper is not complete, this will change in a future version.
'''
from pyobjc_setup import setup

setup(
    name='pyobjc-framework-LaunchServices',
    version="2.5.1",
    description = "Wrappers for the framework LaunchServices on Mac OS X",
    packages = [ "LaunchServices" ],
    setup_requires = [
        'pyobjc-core>=2.5.1',
    ],
    install_requires = [
        'pyobjc-core>=2.5.1',
        'pyobjc-framework-Cocoa>=2.5.1',
    ],
)
