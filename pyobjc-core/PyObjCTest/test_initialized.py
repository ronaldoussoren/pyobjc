import objc
from PyObjCTest.initialize import OC_TestInitialize
from PyObjCTools.TestSupport import TestCase


class OC_TestInitializePython(OC_TestInitialize):
    def init(self):
        return objc.super(OC_TestInitializePython, self).init()


OBJECT_LIST = []


class OC_TestInitializePython2(OC_TestInitialize):
    def init(self):
        self = objc.super(OC_TestInitializePython2, self).init()
        OBJECT_LIST.append(self)
        return self


class TestInitializing(TestCase):
    #
    # These tests make sure that we don't call retain/release on objects
    # that are not yet initialized.
    #
    def testDontRetainUnitialized1(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEqual(start, 0)

        o = OC_TestInitialize.alloc()
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

        o = o.init()
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

        s = o.dummy()
        self.assertEqual(s, "hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

    def testDontRetainUnitialized2(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEqual(start, 0)

        o = OC_TestInitialize.makeInstance()
        self.assertIsInstance(o, OC_TestInitialize)
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

        s = o.dummy()
        self.assertEqual(s, "hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

    def testDontRetainUnitialized3(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEqual(start, 0)

        o = OC_TestInitializePython.makeInstance()
        self.assertIsInstance(o, OC_TestInitializePython)
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

        s = o.dummy()
        self.assertEqual(s, "hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

    def testDontRetainUnitialized4(self):
        start = OC_TestInitialize.numUninitialized()
        self.assertEqual(start, 0)

        o = OC_TestInitializePython2.makeInstance()
        self.assertIsInstance(o, OC_TestInitializePython2)
        self.assertIs(OBJECT_LIST[-1], o)
        del OBJECT_LIST[-1]

        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)

        s = o.dummy()
        self.assertEqual(s, "hello")
        v = OC_TestInitialize.numUninitialized()
        self.assertEqual(v, start)
