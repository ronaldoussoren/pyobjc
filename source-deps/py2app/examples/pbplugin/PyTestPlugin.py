from Foundation import *
import objc
import sys

class PyTestPlugin(NSObject):
    __bundle_hack__ = True
    def init(self):
        self = super(PyTestPlugin, self).init()
        print 'class load!!'
        print "Hello from py2app"
        print "frozen", repr(getattr(sys, "frozen", None))
        return self

print "PyTestPlugin"
