import unittest
import objc
import sys


class MethodAccessTest (unittest.TestCase):

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
