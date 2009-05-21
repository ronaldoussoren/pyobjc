"""
Tests for accessing methods through classes and instances
"""
from PyObjCTools.TestSupport import *
from PyObjCTest.clinmeth import *
import objc

class TestClassMethods (TestCase):
    # Some very basic tests that check that getattr on instances doesn't
    # return a class method and that getattr on classes prefers classmethods
    # over instance methods (and v.v. for getattr on instances)

    def testViaClass(self):
        m = PyObjC_ClsInst1.clsmeth
        self.assert_( isinstance(m, objc.selector) )
        self.assert_( m.isClassMethod )

        self.assertEquals(m(), 4)

    def testViaInstance(self):
        o = PyObjC_ClsInst1.alloc().init()
        self.assertRaises(AttributeError, getattr, o, "clsmeth")

    def testClassAndInstanceViaClass(self):
        m = PyObjC_ClsInst1.both
        self.assert_( isinstance(m, objc.selector) )
        self.assert_( m.__metadata__()['classmethod'] )

        self.assertEquals(m(), 3)

    def testClassAndInstanceViaInstance(self):
        o = PyObjC_ClsInst1.alloc().init()
        m = o.both
        self.assert_( isinstance(m, objc.selector) )
        self.assert_( not m.isClassMethod )

        self.assertEquals(m(), 2)


class TestInstanceMethods (TestCase):
    # Check that instance methods can be accessed through the instance, and 
    # also through the class when no class method of the same name is 
    # available.

    def testViaClass(self):
        m = PyObjC_ClsInst1.instance
        self.assert_( isinstance(m, objc.selector) )
        self.assert_( not m.isClassMethod )

        self.assertRaises(TypeError, m)

    def testViaInstance(self):
        o = PyObjC_ClsInst1.alloc().init()
        m = o.instance

        self.assert_( isinstance(m, objc.selector) )
        self.assert_( not m.isClassMethod )

        self.assertEquals(m(), 1)

class TestSuper (TestCase):
    # Tests that check if super() behaves as expected (which is the most likely
    # reason for failure).

    def testClassMethod(self):
        cls = PyObjC_ClsInst2

        self.assertEquals(cls.clsmeth(), 40)
        self.assertEquals(objc.super(cls, cls).clsmeth(), 4)

    def testInstanceMethod(self):
        o = PyObjC_ClsInst2.alloc().init()

        self.assertEquals(o.instance(), 10)
        self.assertEquals(super(PyObjC_ClsInst2, o).instance(), 1)

    def testBoth(self):
        o = PyObjC_ClsInst2.alloc().init()

        self.assertEquals(o.both(), 20)
        self.assertEquals(objc.super(PyObjC_ClsInst2, o).both(), 2)

        cls = PyObjC_ClsInst2

        self.assertEquals(cls.both(), 30)
        self.assertEquals(objc.super(cls, cls).both(), 3)


if __name__ == "__main__":
    main()

