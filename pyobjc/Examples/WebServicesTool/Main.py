import sys
import os.path

sys.path.insert(0, os.path.join(sys.path[0], "pyobjc"))

import objc
import Foundation
import AppKit

# automatically load frameworks that were linked into the bootstrap tooll
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

import WSTApplicationDelegateClass
import WSTConnectionWindowControllerClass

sys.exit( AppKit.NSApplicationMain(sys.argv) )
