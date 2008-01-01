import os
import objc
from Foundation import *
import sys
try:
    set
except NameError:
    from sets import Set as set
old_path = set(sys.path)
old_modules = set(sys.modules)
bndl = NSBundle.bundleWithPath_(os.path.abspath('dist/PyTestPlugin.pbplugin'))
NSLog(u'currentBundle = %r' % (objc.currentBundle(),))
PyTestPlugin = bndl.classNamed_('PyTestPlugin')
NSLog(u'PyTestPlugin = %r' % (PyTestPlugin,))
PyTestPlugin.alloc().init()
NSLog(u'currentBundle = %r' % (objc.currentBundle(),))
NSLog(u'paths changed: %r' % (set(sys.path) - old_path))
NSLog(u'new modules: %r' % (set(sys.modules) - old_modules))
