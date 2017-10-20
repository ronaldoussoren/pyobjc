'''
Wrappers for the "LaunchServices" framework on macOS. The API's in this
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

VERSION="4.0.1b1"

setup(
    name='pyobjc-framework-LaunchServices',
    description = "Wrappers for the framework LaunchServices on macOS",
    packages = [ "LaunchServices" ],
    version=VERSION,
    install_requires = [
        'pyobjc-core>='+VERSION,
        'pyobjc-framework-Cocoa>='+VERSION,
    ],
    long_description=__doc__,
)
