#
#  Main.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

# 
# Upon an installation build, the project copies the PyObjC modules
# into the 'pyobjc' directory within the Resources directory of
# the app wrapper.  The following adjusts sys.path to include that
# directory.
#
import sys
import os.path
sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

#
# Import the components of the Python<->ObjC bridge.
#
import objc
import Foundation
import AppKit

#
# Automatically load any frameworks identified by the bootstrap
# process (the code in bin-python-main.m).
#
# If any of the frameworks have an Init.py, it will be executed
# and, as such, can be used to load/initialize any of the
# frameworks in the Python interpreter context.
#
pyFrameworkPathsIndex = sys.argv.index("-PyFrameworkPaths")
if not (pyFrameworkPathsIndex == -1):
  import string
  from Foundation import NSBundle
  paths = string.split(sys.argv[pyFrameworkPathsIndex + 1], ":")
  count = 0
  for path in paths:
    bundle = NSBundle.bundleWithPath_(path)
    bundle.principalClass()
    sys.path.insert(count, bundle.resourcePath())
    count = count + 1
    
    initPath = bundle.pathForResource_ofType_( "Init", "py")
    if initPath:
      execfile(initPath, globals(), locals())

#
# Import application specific componentry.  At the least, all
# classes necessary to load the main NIB file must be loaded here.
#
import MyAppDelegate

#
# Pass control to the Appkit.
#
# From this point on, application intiailization, execution and
# termination works exactly like any other Cocoa application.
#
sys.exit( AppKit.NSApplicationMain(sys.argv) )
