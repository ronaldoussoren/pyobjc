import unittest
import objc
from objc.test.testbndl import PyObjC_TestClass3
import sys
import types

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

class TestSubclassing(unittest.TestCase):
    def testMethodRaise(self):
        # Defining a method whose name is a keyword followed by two underscores
        # should define the method name without underscores in the runtime,
        # and this method should be accesible both with and without the
        # underscores.

        class RaiseClass (NSObject):
            def raise__(self):
                pass

        self.assert_(not hasattr(NSObject, 'raise__'))
        self.assert_(not hasattr(NSObject, 'raise'))

        self.assert_(hasattr(RaiseClass, 'raise__'))
        self.assert_(hasattr(RaiseClass, 'raise'))
        self.assertEquals(RaiseClass.raise__.selector, 'raise')
        self.assertEquals(getattr(RaiseClass, 'raise').selector, 'raise')

    def testMIObjC(self):
        try:
            class MIClass1(NSObject, objc.runtime.NSArray):
                pass
            self.assert_(0)
        except TypeError:
            pass

    def testSubclassOfSubclass(self):
        class Level1Class (NSObject):
            def hello(self):
                return "level1"

        class Level2Class (Level1Class):
            def hello(self):
                return "level2"

            def superHello(self):
                return super(Level2Class, self).hello()

            def description(self):
                return super(Level2Class, self).description()

        obj = Level1Class.alloc().init()
        v = obj.hello()
        self.assertEquals(v, "level1")

        obj = Level2Class.alloc().init()
        v = obj.hello()
        self.assertEquals(v, "level2")

        v = obj.superHello()
        self.assertEquals(v, "level1")

        v = obj.description()
        # this may be a bit hardwired for comfort
        self.assert_(v.find("<Level2Class") == 0)
    
    def testUniqueNames(self):
        class SomeClass (NSObject): pass

        try:
            class SomeClass (NSObject): pass

            fail("Should not have been able to redefine the SomeClass class!")
        except objc.error, msg:
            self.assertEquals(str(msg), "Class already exists in Objective-C runtime")

    def testMethodSignature(self):
        class Signature (NSObject):
            def test_x_(self, arg, x):
                pass
            test_x_ = objc.selector(test_x_, signature='v@:@i')

        v = Signature.new()

        self.assert_(isinstance(v, Signature))

        self.assertEquals(v.methodSignatureForSelector_('foo:'), None)

        x = v.methodSignatureForSelector_('test:x:')
        self.assert_(x is not None)

        if sys.platform == 'darwin':
            self.assert_(x.methodReturnType() == 'v')
            self.assert_(x.numberOfArguments() == 4)
            self.assert_(x.getArgumentTypeAtIndex_(0) == '@')
            self.assert_(x.getArgumentTypeAtIndex_(1) == ':')
            self.assert_(x.getArgumentTypeAtIndex_(2) == '@')
            self.assert_(x.getArgumentTypeAtIndex_(3) == 'i')
        else:
            # On GNUstep the return-value of methodReturnType and
            # getArgumentTypeAtIndex_ includes "garbage" after the 
            # signature of the queried item. The garbage is the rest
            # of the signature string.
            self.assert_(x.methodReturnType().startswith('v'))
            self.assert_(x.numberOfArguments() == 4)
            self.assert_(x.getArgumentTypeAtIndex_(0).startswith('@'))
            self.assert_(x.getArgumentTypeAtIndex_(1).startswith(':'))
            self.assert_(x.getArgumentTypeAtIndex_(2).startswith('@'))
            self.assert_(x.getArgumentTypeAtIndex_(3).startswith('i'))


class TestSelectors(unittest.TestCase):
    def testSelectorRepr(self):
        class SelectorRepr(NSObject):
            def foo(self):
                pass

        self.assert_(repr(SelectorRepr.foo).startswith('<unbound selector foo of SelectorRepr at'))


class TestCopying (unittest.TestCase):

    def testCopy(self):
        class MyCopyClass (NSObject):
            def copyWithZone_(self, zone):
                # NSObject doesn't implement the copying protocol
                #o = super(MyCopyClass, self).copyWithZone_(zone)
                o = self.__class__.alloc().init()
                o.foobar = 2
                return o
            copyWithZone_ = objc.selector(
            	copyWithZone_, 
        	signature=objc.runtime.NSObject.copyWithZone_.signature,
        	isClassMethod=0)


        # Make sure the runtime correctly marked our copyWithZone_
        # implementation.
        self.assert_ (not (MyCopyClass.copyWithZone_.isClassMethod))
        self.assert_(MyCopyClass.copyWithZone_.doesDonateReference)

        o = MyCopyClass.alloc().init()
        o.foobar = 1

        self.assertEquals(o.foobar, 1)

        # Make a copy from ObjC (see testbundle.m)
        c = PyObjC_TestClass3.makeACopy_(o)
       
        self.assert_(isinstance(c, MyCopyClass))
        self.assertEquals(c.foobar, 2)


    def testMultipleInheritance1(self):
        # New-style class mixin
        class MixinClass1 (object):
            def mixinMethod(self):
                return "foo"

        class MITestClass1 (objc.runtime.NSObject, MixinClass1):
            def init(self):
                return NSObject.init(self)

        self.assert_(hasattr(MITestClass1, 'mixinMethod'))

        o = MITestClass1.alloc().init()
        self.assertEquals(o.mixinMethod(), "foo")

    def testMultipleInheritance2(self):
        # old-style class mixin
        class MixinClass2:
            def mixinMethod(self):
                return "foo"

        class MITestClass2 (objc.runtime.NSObject, MixinClass2):
            def init(self):
                return NSObject.init(self)

        self.assert_(hasattr(MITestClass2, 'mixinMethod'))

        o = MITestClass2.alloc().init()
        self.assertEquals(o.mixinMethod(), "foo")

class TestClassMethods (unittest.TestCase):

    def testClassMethod(self):
        """ check that classmethod()-s are converted to selectors """

        class ClassMethodTest (NSObject):
            def clsMeth(self):
                return "hello"
            clsMeth = classmethod(clsMeth)

        self.assert_(isinstance(ClassMethodTest.clsMeth, objc.selector))
        self.assert_(ClassMethodTest.clsMeth.isClassMethod)

    def testStaticMethod(self):
        """ check that staticmethod()-s are not converted to selectors """

        class StaticMethodTest (NSObject):
            def stMeth(self):
                return "hello"
            stMeth = staticmethod(stMeth)

        self.assert_(isinstance(StaticMethodTest.stMeth, types.FunctionType))

if __name__ == '__main__':
    unittest.main()
