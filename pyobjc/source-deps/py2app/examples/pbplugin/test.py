import os
from Foundation import *
bndl = NSBundle.bundleWithPath_(os.path.abspath('dist/PyTestPlugin.pbplugin'))
PyTestPlugin = bndl.classNamed_('PyTestPlugin')
NSLog(u'PyTestPlugin = %r' % (PyTestPlugin,))
PyTestPlugin.alloc().init()
