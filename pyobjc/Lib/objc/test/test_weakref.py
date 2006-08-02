import unittest, weakref
from Foundation import NSObject

class OC_WeakrefTest1 (NSObject):
    pass

class OC_WeakrefTest2 (OC_WeakrefTest1):
    pass

class TestWeakrefs (unittest.TestCase):
    def testPureObjC(self):
        o = NSObject.new()
        self.assertRaises(TypeError, weakref.ref, o)

    def testFirstGenPython(self):
        o = OC_WeakrefTest1.new()
        self.assertRaises(TypeError, weakref.ref, o)

    def testSecondGenPython(self):
        o = OC_WeakrefTest2.new()
        self.assertRaises(TypeError, weakref.ref, o)

if __name__ == "__main__":
    unittest.main()
