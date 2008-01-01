from Foundation import *
import objc
import sys

class PyTestPlugin(NSObject):
    def init(self):
        self = super(PyTestPlugin, self).init()
        print 'class load!!'
        print "Hello from py2app"
        print "frozen", repr(getattr(sys, "frozen", None))
        return self

class PyTestPlugin2(NSObject):
    pass

print "PyTestPlugin", __name__
print u"[inside] currentBundle %r" % (objc.currentBundle(),)
