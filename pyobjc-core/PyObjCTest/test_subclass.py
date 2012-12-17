from PyObjCTools.TestSupport import *
import objc
from PyObjCTest.testbndl import PyObjC_TestClass3
import sys
import types

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')
NSArray = objc.lookUpClass('NSArray')
NSAutoreleasePool = objc.lookUpClass('NSAutoreleasePool')

class TestSubclassing(TestCase):
    def testMethodRaise(self):
        # Defining a method whose name is a keyword followed by two underscores
        # should define the method name without underscores in the runtime,
        # and this method should be accesible both with and without the
        # underscores.

        class RaiseClass (NSObject):
            def raise__(self):
                pass

        self.assertNotHasAttr(NSObject, 'raise__')
        self.assertNotHasAttr(NSObject, 'raise')

        self.assertHasAttr(RaiseClass, 'raise__')
        self.assertHasAttr(RaiseClass, 'raise')
        self.assertEqual(RaiseClass.raise__.selector, b'raise')
        self.assertEqual(getattr(RaiseClass, 'raise').selector, b'raise')

    def testMIObjC(self):
        try:
            class MIClass1(NSObject, NSArray):
                pass
            self.fail("Can multiple inherit from two objc classes")
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
                return objc.super(Level2Class, self).hello()

            def description(self):
                return objc.super(Level2Class, self).description()

        obj = Level1Class.alloc().init()
        v = obj.hello()
        self.assertEqual(v, "level1")

        obj = Level2Class.alloc().init()
        v = obj.hello()
        self.assertEqual(v, "level2")

        v = obj.superHello()
        self.assertEqual(v, "level1")

        v = obj.description()
        # this may be a bit hardwired for comfort
        self.assertEqual(v.find("<Level2Class"), 0)

    def testMethodSignature(self):
        class Signature (NSObject):
            def test_x_(self, arg, x):
                pass
            test_x_ = objc.selector(test_x_, signature=b'v@:@i')

        v = Signature.new()

        self.assertIsInstance(v, Signature)

        self.assertEqual(v.methodSignatureForSelector_('foo:'), None)

        x = v.methodSignatureForSelector_('test:x:')
        self.assertIsNotNone(x)

        self.assertEqual(x.methodReturnType(), b'v')
        self.assertEqual(x.numberOfArguments(), 4)
        self.assertEqual(x.getArgumentTypeAtIndex_(0), b'@')
        self.assertEqual(x.getArgumentTypeAtIndex_(1), b':')
        self.assertEqual(x.getArgumentTypeAtIndex_(2), b'@')
        self.assertEqual(x.getArgumentTypeAtIndex_(3), b'i')


class TestSelectors(TestCase):
    def testSelectorRepr(self):
        class SelectorRepr(NSObject):
            def foo(self):
                pass

        self.assertTrue(repr(SelectorRepr.foo).startswith('<unbound selector foo of SelectorRepr at'))


class TestCopying (TestCase):

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

        self.assertFalse((o.copyWithZone_.__metadata__()['classmethod']))
        self.assertTrue(o.copyWithZone_.__metadata__()['retval']['already_retained'])
        #self.assertTrue(o.copyWithZone_.callable == MyCopyClass.__dict__['copyWithZone_'].callable)

        o = MyCopyClass.alloc().init()
        o.foobar = 1

        self.assertEqual(o.foobar, 1)

        # Make a copy from ObjC (see testbundle.m)
        c = PyObjC_TestClass3.copyValue_(o)

        self.assertIsInstance(c, MyCopyClass)
        self.assertEqual(c.foobar, 2)


    def testMultipleInheritance1(self):
        # New-style class mixin
        class MixinClass1 (object):
            def mixinMethod(self):
                return "foo"

        class MITestClass1 (NSObject, MixinClass1):
            def init(self):
                return NSObject.pyobjc_instanceMethods.init(self)

        self.assertHasAttr(MITestClass1, 'mixinMethod')

        o = MITestClass1.alloc().init()
        self.assertEqual(o.mixinMethod(), "foo")

    def testMultipleInheritance2(self):
        # old-style class mixin
        class MixinClass2:
            def mixinMethod(self):
                return "foo"

        class MITestClass2 (NSObject, MixinClass2):
            def init(self):
                return NSObject.pyobjc_instanceMethods.init(self)

        self.assertHasAttr(MITestClass2, 'mixinMethod')

        o = MITestClass2.alloc().init()
        self.assertEqual(o.mixinMethod(), "foo")

class TestClassMethods (TestCase):

    def testClassMethod(self):
        """ check that classmethod()-s are converted to selectors """

        class ClassMethodTest (NSObject):
            def clsMeth(self):
                return "hello"
            clsMeth = classmethod(clsMeth)

        self.assertIsInstance(ClassMethodTest.clsMeth, objc.selector)
        self.assertTrue(ClassMethodTest.clsMeth.isClassMethod)

    def testStaticMethod(self):
        """ check that staticmethod()-s are not converted to selectors """

        class StaticMethodTest (NSObject):
            def stMeth(self):
                return "hello"
            stMeth = staticmethod(stMeth)

        def func(): pass

        self.assertIsInstance(StaticMethodTest.stMeth, type(func))


class TestOverridingSpecials(TestCase):
    def testOverrideSpecialMethods(self):
        aList = [0]

        class ClassWithAlloc(NSObject):
            def alloc(cls):
                aList[0] += 1
                return objc.super(ClassWithAlloc, cls).alloc()


        self.assertEqual(aList[0], 0)
        o = ClassWithAlloc.alloc().init()
        self.assertEqual(aList[0], 1)
        self.assertIsInstance(o, NSObject)
        del o

        class ClassWithRetaining(NSObject):
            def retain(self):
                aList.append('retain')
                v =  objc.super(ClassWithRetaining, self).retain()
                return v

            def release(self):
                aList.append('release')
                return objc.super(ClassWithRetaining, self).release()

            def __del__(self):
                aList.append('__del__')


        del aList[:]
        o = ClassWithRetaining.alloc().init()
        v = o.retainCount()
        o.retain()
        self.assertEqual(aList, ['retain'])
        self.assertEqual(o.retainCount(), v+1)
        o.release()
        self.assertEqual(aList, ['retain', 'release'])
        self.assertEqual(o.retainCount(), v)
        del o

        self.assertEqual(aList, ['retain', 'release', 'release', '__del__'])

        # Test again, now remove all python references and create one
        # again.
        del aList[:]
        pool = NSAutoreleasePool.alloc().init()
        o = ClassWithRetaining.alloc().init()
        v = NSArray.arrayWithArray_([o])
        del o
        self.assertEqual(aList, ['retain'])
        o = v[0]
        self.assertEqual(aList, ['retain'])
        del v
        del o
        del pool

        self.assertEqual(aList, ['retain', 'release', 'release', '__del__'])

        class ClassWithRetainCount(NSObject):
            def retainCount(self):
                aList.append('retainCount')
                return objc.super(ClassWithRetainCount, self).retainCount()

        del aList[:]
        o = ClassWithRetainCount.alloc().init()
        self.assertEqual(aList, [])
        v = o.retainCount()
        self.assertIsInstance(v, int)
        self.assertEqual(aList, ['retainCount'])
        del o

    def testOverrideDealloc(self):
        aList = []

        class Dummy:
            def __del__(self):
                aList.append('__del__')

        self.assertEqual(aList, [])
        Dummy()
        self.assertEqual(aList, ['__del__'])

        class ClassWithDealloc(NSObject):
            def init(self):
                self = objc.super(ClassWithDealloc, self).init()
                if self is not None:
                    self.obj = Dummy()
                return self

            def dealloc(self):
                aList.append('dealloc')
                return objc.super(ClassWithDealloc, self).dealloc()

        del aList[:]
        o = ClassWithDealloc.alloc().init()
        self.assertEqual(aList, [])
        del o
        self.assertEqual(len(aList), 2)
        self.assertIn('dealloc', aList)
        self.assertIn('__del__', aList)

        class SubClassWithDealloc(ClassWithDealloc):
            def dealloc(self):
                aList.append('dealloc.dealloc')
                return objc.super(SubClassWithDealloc, self).dealloc()

        del aList[:]
        o = SubClassWithDealloc.alloc().init()
        self.assertEqual(aList, [])
        del o
        self.assertEqual(len(aList), 3)
        self.assertIn('dealloc.dealloc', aList)
        self.assertIn('dealloc', aList)
        self.assertIn('__del__', aList)

        class ClassWithDeallocAndDel(NSObject):
            def init(self):
                self = objc.super(ClassWithDeallocAndDel, self).init()
                if self is not None:
                    self.obj = Dummy()
                return self

            def dealloc(self):
                aList.append('dealloc')
                return objc.super(ClassWithDeallocAndDel, self).dealloc()

            def __del__(self):
                aList.append('mydel')

        del aList[:]
        o = ClassWithDeallocAndDel.alloc().init()
        self.assertEqual(aList, [])
        del o
        self.assertEqual(len(aList), 3)
        self.assertIn('mydel', aList)
        self.assertIn('dealloc', aList)
        self.assertIn('__del__', aList)

    def testMethodNames(self):

        class MethodNamesClass (NSObject):
            def someName_andArg_(self, name, arg):
                pass

            def _someName_andArg_(self, name, arg):
                pass


            def raise__(self):
                pass

            def froobnicate__(self, a, b):
                pass

        # XXX: workaround for a 'feature' in class-builder.m, that code
        # ignores methods whose name starts with two underscores. That code
        # is not necessary, or the other ways of adding methods to a class
        # should be changed.
        def __foo_bar__(self, a, b, c):
            pass

        MethodNamesClass.__foo_bar__ = __foo_bar__

        self.assertEqual(MethodNamesClass.someName_andArg_.selector,
                b'someName:andArg:')
        self.assertEqual(MethodNamesClass._someName_andArg_.selector,
                b'_someName:andArg:')
        self.assertEqual(MethodNamesClass.__foo_bar__.selector,
                b'__foo_bar__')
        self.assertEqual(MethodNamesClass.raise__.selector,
                b'raise')
        self.assertEqual(MethodNamesClass.froobnicate__.selector,
                b'froobnicate::')

    def testOverrideRespondsToSelector(self):
        class OC_RespondsClass (NSObject):
            def initWithList_(self, lst):
                objc.super(OC_RespondsClass, self).init()
                self.lst = lst
                return self

            def respondsToSelector_(self, selector):
                self.lst.append(selector)
                return objc.super(OC_RespondsClass, self).respondsToSelector_(selector)

        lst = []
        o = OC_RespondsClass.alloc().initWithList_(lst)

        self.assertEqual(lst, [])

        b = o.respondsToSelector_('init')
        self.assertTrue(b)
        self.assertEqual(lst, ['init'])

        b = o.respondsToSelector_('alloc')
        self.assertFalse(b)
        self.assertEqual(lst, ['init', 'alloc'])

    def testOverrideInstancesRespondToSelector(self):
        lst = []
        class OC_InstancesRespondClass (NSObject):

            @classmethod
            def instancesRespondToSelector_(cls, selector):
                lst.append(selector)
                return objc.super(OC_InstancesRespondClass, cls).instancesRespondToSelector_(selector)

        self.assertEqual(lst, [])

        b = OC_InstancesRespondClass.instancesRespondToSelector_('init')
        self.assertTrue(b)
        self.assertEqual(lst, ['init'])

        b = OC_InstancesRespondClass.instancesRespondToSelector_('alloc')
        self.assertFalse(b)
        self.assertEqual(lst, ['init', 'alloc'])

    def testImplementingSetValueForKey(self):
        values = {}
        class CrashTest (NSObject):
            def setValue_forKey_(self, v, k):
                values[k] = v

        o = CrashTest.alloc().init()
        o.setValue_forKey_(42,"key")

        self.assertEqual(values, {"key":42})


if __name__ == '__main__':
    main()
