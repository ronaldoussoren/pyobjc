import unittest
import objc
import sys


class MethodAccessTest (unittest.TestCase):

    def testObjCObject(self):
        # Trying to access the methods of objc.objc_object should not 
        # crash the interpreter.
        self.assertRaises(AttributeError, getattr, objc.objc_object.pyobjc_classMethods, 'func_code')
        self.assertRaises(AttributeError, getattr, objc.objc_object.pyobjc_instanceMethods, 'func_code')

    def testNSProxyStuff(self):
        # NSProxy is incompatitble with pyobjc_{class,instance}Methods, but 
        # this should not crash the interpreter
        self.assertRaises(AttributeError, getattr, objc.runtime.NSProxy.pyobjc_instanceMethods, 'foobar')
        self.assertRaises(AttributeError, getattr, objc.runtime.NSProxy.pyobjc_classMethods, 'foobar')
        self.assertRaises(AttributeError, getattr, objc.runtime.NSProxy, 'foobar')

    def testNSZombie(self):
        self.assertRaises(AttributeError, getattr, objc.runtime._NSZombie.pyobjc_instanceMethods, "foobar")
        self.assertRaises(AttributeError, getattr, objc.runtime._NSZombie.pyobjc_classMethods, "foobar")
        self.assertRaises(AttributeError, getattr, objc.runtime._NSZombie, "foobar")


    def testDir(self):
        o = objc.runtime.NSObject.new()

        d = dir(o.pyobjc_instanceMethods)
        self.assert_(len(d) > 10)
        self.assert_("init" in d)

        d = dir(o.pyobjc_classMethods)
        self.assert_(len(d) > 10)
        self.assert_("alloc" in d)

        d = dir(objc.runtime.NSObject.pyobjc_classMethods)
        self.assert_(len(d) > 10)
        self.assert_("alloc" in d)

    def testDict(self):
        o = objc.runtime.NSObject.new()

        d = o.pyobjc_instanceMethods.__dict__.keys()
        self.assert_(len(d) > 10)
        self.assert_("init" in d)

        d = objc.runtime.NSObject.pyobjc_classMethods.__dict__.keys()
        self.assert_(len(d) > 10)
        self.assert_("alloc" in d)

        d = o.pyobjc_classMethods.__dict__.keys()
        self.assert_(len(d) > 10)
        self.assert_("alloc" in d)

    def testAttributes(self):
        o = objc.runtime.NSObject.new()

        self.assert_(hasattr(o.pyobjc_instanceMethods, "init"))
        self.assert_(hasattr(o.pyobjc_classMethods, "alloc"))

        self.assert_(hasattr(objc.runtime.NSObject.pyobjc_classMethods, "alloc"))

if __name__ == "__main__":
    unittest.main()
