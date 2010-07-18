from PyObjCTools.TestSupport import *
import objc
import sys

NSObject = objc.lookUpClass('NSObject')
#_NSZombie = objc.lookUpClass('_NSZombie')
NSProxy = objc.lookUpClass('NSProxy')



class MethodAccessTest (TestCase):

    def testObjCObject(self):
        # Trying to access the methods of objc.objc_object should not
        # crash the interpreter.
        self.assertRaises(AttributeError, getattr, objc.objc_object.pyobjc_classMethods, 'func_code')
        self.assertRaises(AttributeError, getattr, objc.objc_object.pyobjc_instanceMethods, 'func_code')

    def testNSProxyStuff(self):
        # NSProxy is incompatitble with pyobjc_{class,instance}Methods, but
        # this should not crash the interpreter
        self.assertRaises(AttributeError, getattr, NSProxy.pyobjc_instanceMethods, 'foobar')
        self.assertRaises(AttributeError, getattr, NSProxy.pyobjc_classMethods, 'foobar')
        self.assertRaises(AttributeError, getattr, NSProxy, 'foobar')
#
#    if sys.platform == 'darwin':
#        def testNSZombie(self):
#            self.assertRaises(AttributeError, getattr, _NSZombie.pyobjc_instanceMethods, "foobar")
#            self.assertRaises(AttributeError, getattr, _NSZombie.pyobjc_classMethods, "foobar")
#            self.assertRaises(AttributeError, getattr, _NSZombie, "foobar")
#

    def testDir(self):
        o = NSObject.new()

        d = dir(o.pyobjc_instanceMethods)
        self.assertGreaterThan(len(d), 10)
        self.assertIn("init", d)

        d = dir(NSObject.pyobjc_classMethods)
        self.assertGreaterThan(len(d), 10)
        self.assertIn("alloc", d)

    def testDict(self):
        o = NSObject.new()

        d = o.pyobjc_instanceMethods.__dict__.keys()
        self.assertGreaterThan(len(d), 10)
        self.assertIn("init", d)

        d = NSObject.pyobjc_classMethods.__dict__.keys()
        self.assertGreaterThan(len(d), 10)
        self.assertIn("alloc", d)

        #d = o.pyobjc_classMethods.__dict__.keys()
        #self.assertGreaterThan(len(d), 10)
        #self.assertIn("alloc", d)

    def testAttributes(self):
        o = NSObject.new()

        self.assertHasAttr(o.pyobjc_instanceMethods, "init")
        #self.assertHasAttr(o.pyobjc_classMethods, "alloc")

        self.assertHasAttr(NSObject.pyobjc_classMethods, "alloc")

class ClassAndInstanceMethods(TestCase):
    def testClassThroughInstance(self):
        # Class methods are not accessible through instances.
        self.assertRaises(AttributeError, getattr, NSObject.new(), 'alloc')

if __name__ == "__main__":
    main()
