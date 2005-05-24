import unittest
from objc.test.initialize import OC_TestInitialize

class OC_TestInitializePython (OC_TestInitialize):
    def init(self):
        return super(OC_TestInitializePython, self).init()

class TestInitializing (unittest.TestCase):
    #
    # These tests make sure that we don't call retain/release on objects
    # that are not yet initialized.
    #
    def testDontRetainUnitialized1(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEquals(start, 0)

        o = OC_TestInitialize.alloc()
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

        o = o.init()
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

        s = o.dummy()
        self.assertEquals(s, u"hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

    def testDontRetainUnitialized2(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEquals(start, 0)

        o = OC_TestInitialize.makeInstance()
        self.assert_(isinstance(o, OC_TestInitialize))
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

        s = o.dummy()
        self.assertEquals(s, u"hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

    def testDontRetainUnitialized3(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEquals(start, 0)

        o = OC_TestInitializePython.makeInstance()
        self.assert_(isinstance(o, OC_TestInitializePython))
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

        s = o.dummy()
        self.assertEquals(s, u"hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEquals(v, start)

if __name__ == "__main__":
    unittest.main()
