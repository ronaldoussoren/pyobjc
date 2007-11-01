import objc.test
import objc
from objc.test.testbndl import PyObjC_TestClass3
import sys
import types

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')
NSArray = objc.lookUpClass('NSArray')
NSAutoreleasePool = objc.lookUpClass('NSAutoreleasePool')

class TestSubclassing(objc.test.TestCase):
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
            class MIClass1(NSObject, NSArray):
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


class TestSelectors(objc.test.TestCase):
    def testSelectorRepr(self):
        class SelectorRepr(NSObject):
            def foo(self):
                pass

        self.assert_(repr(SelectorRepr.foo).startswith('<unbound selector foo of SelectorRepr at'))


class TestCopying (objc.test.TestCase):

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
                signature=NSObject.copyWithZone_.signature,
                isClassMethod=0)


        # Make sure the runtime correctly marked our copyWithZone_
        # implementation.
        o = MyCopyClass.alloc().init()

        self.assert_ (not (o.copyWithZone_.__metadata__()['classmethod']))
        self.assert_(o.copyWithZone_.__metadata__()['retval']['already_retained'])
        #self.assert_(o.copyWithZone_.callable == MyCopyClass.__dict__['copyWithZone_'].callable)

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

        class MITestClass1 (NSObject, MixinClass1):
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

        class MITestClass2 (NSObject, MixinClass2):
            def init(self):
                return NSObject.init(self)

        self.assert_(hasattr(MITestClass2, 'mixinMethod'))

        o = MITestClass2.alloc().init()
        self.assertEquals(o.mixinMethod(), "foo")

class TestClassMethods (objc.test.TestCase):

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


class TestOverridingSpecials(objc.test.TestCase):
    def testOverrideSpecialMethods(self):
        aList = [0]

        class ClassWithAlloc(NSObject):
            def alloc(cls):
                aList[0] += 1
                return objc.super(ClassWithAlloc, cls).alloc()

            
        self.assertEquals(aList[0], 0)
        o = ClassWithAlloc.alloc().init()
        self.assertEquals(aList[0], 1)
        self.assert_(isinstance(o, NSObject))
        del o

        class ClassWithRetaining(NSObject):
            def retain(self):
                aList.append('retain')
                return super(ClassWithRetaining, self).retain()

            def release(self):
                aList.append('release')
                return super(ClassWithRetaining, self).release()

            def __del__(self):
                aList.append('__del__')

        del aList[:]
        o = ClassWithRetaining.alloc().init()
        v = o.retainCount()
        o.retain()
        self.assertEquals(aList, ['retain'])
        self.assertEquals(o.retainCount(), v+1)
        o.release()
        self.assertEquals(aList, ['retain', 'release'])
        self.assertEquals(o.retainCount(), v)
        del o

        self.assertEquals(aList, ['retain', 'release', 'release', '__del__'])

        # Test again, now remove all python references and create one
        # again.
        del aList[:]
        pool = NSAutoreleasePool.alloc().init()
        o = ClassWithRetaining.alloc().init()
        v = NSArray.arrayWithArray_([o])
        del o
        self.assertEquals(aList, ['retain'])
        o = v[0]
        self.assertEquals(aList, ['retain'])
        del v
        del o
        del pool
        
        self.assertEquals(aList, ['retain', 'release', 'release', '__del__'])

        class ClassWithRetainCount(NSObject):
            def retainCount(self):
                aList.append('retainCount')
                return super(ClassWithRetainCount, self).retainCount()
        
        del aList[:]
        o = ClassWithRetainCount.alloc().init()
        self.assertEquals(aList, [])
        v = o.retainCount()
        self.assert_(isinstance(v, int))
        self.assertEquals(aList, ['retainCount'])
        del o

    def testOverrideDealloc(self):
        aList = []

        class Dummy:
            def __del__(self):
                aList.append('__del__')

        self.assertEquals(aList, [])
        Dummy()
        self.assertEquals(aList, ['__del__'])

        class ClassWithDealloc(NSObject):
            def init(self):
                self = super(ClassWithDealloc, self).init()
                if self is not None:
                    self.obj = Dummy()
                return self

            def dealloc(self):
                aList.append('dealloc')
                return super(ClassWithDealloc, self).dealloc()

        del aList[:]
        o = ClassWithDealloc.alloc().init()
        self.assertEquals(aList, [])
        del o
        self.assertEquals(len(aList), 2)
        self.assert_('dealloc' in aList)
        self.assert_('__del__' in aList)

        class SubClassWithDealloc(ClassWithDealloc):
            def dealloc(self):
                aList.append('dealloc.dealloc')
                return super(SubClassWithDealloc, self).dealloc()

        del aList[:]
        o = SubClassWithDealloc.alloc().init()
        self.assertEquals(aList, [])
        del o
        self.assertEquals(len(aList), 3)
        self.assert_('dealloc.dealloc' in aList)
        self.assert_('dealloc' in aList)
        self.assert_('__del__' in aList)

        class ClassWithDeallocAndDel(NSObject):
            def init(self):
                self = super(ClassWithDeallocAndDel, self).init()
                if self is not None:
                    self.obj = Dummy()
                return self

            def dealloc(self):
                aList.append('dealloc')
                return super(ClassWithDeallocAndDel, self).dealloc()

            def __del__(self):
                aList.append('mydel')

        del aList[:]
        o = ClassWithDeallocAndDel.alloc().init()
        self.assertEquals(aList, [])
        del o
        self.assertEquals(len(aList), 3)
        self.assert_('mydel' in aList)
        self.assert_('dealloc' in aList)
        self.assert_('__del__' in aList)

    def testMethodNames(self):

        class MethodNamesClass (NSObject):
            def someName_andArg_(self, name, arg):
                pass

            def _someName_andArg_(self, name, arg):
                pass


            def raise__(self):
                pass

            def froobnicate__(self):
                pass

        # XXX: workaround for a 'feature' in class-builder.m, that code 
        # ignores methods whose name starts with two underscores. That code
        # is not necessary, or the other ways of adding methods to a class
        # should be changed.
        def __foo_bar__(self, a, b, c):
            pass

        MethodNamesClass.__foo_bar__ = __foo_bar__

        self.assertEquals(MethodNamesClass.someName_andArg_.selector,
                'someName:andArg:')
        self.assertEquals(MethodNamesClass._someName_andArg_.selector,
                '_someName:andArg:')
        self.assertEquals(MethodNamesClass.__foo_bar__.selector,
                '__foo_bar__')
        self.assertEquals(MethodNamesClass.raise__.selector,
                'raise')
        self.assertEquals(MethodNamesClass.froobnicate__.selector,
                'froobnicate::')


if __name__ == '__main__':
    objc.test.main()
