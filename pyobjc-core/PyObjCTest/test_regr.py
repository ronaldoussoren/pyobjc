from __future__ import unicode_literals
from PyObjCTools.TestSupport import *
from PyObjCTest import structargs
from PyObjCTest import testbndl
from PyObjCTest import copying

import objc, sys
from PyObjCTest.fnd import NSObject, NSAutoreleasePool

rct = structargs.StructArgClass.someRect.__metadata__()['retval']['type']

class OCTestRegrWithGetItem (NSObject):
    def objectForKey_(self, k):
        return "ofk: %s"%(k,)

    def __getitem__(self, k):
        return "gi: %s"%(k,)

class OCTestRegrWithGetItem2 (OCTestRegrWithGetItem):
    def objectForKey_(self, k):
        return "ofk2: %s"%(k,)

class ReturnAStruct (NSObject):
    def someRectWithRect_(self, aRect):
        ((x, y), (h, w)) = aRect
        return ((x,y),(h,w))
    someRectWithRect_ = objc.selector(someRectWithRect_, signature=rct + b'@:' + rct)


class TestRegressions(TestCase):
    def testNSObjectRespondsToCommonMethods(self):
        self.assertTrue(NSObject.pyobjc_classMethods.respondsToSelector_('alloc'))
        self.assertTrue(NSObject.instancesRespondToSelector_('init'))
        self.assertFalse(NSObject.instancesRespondToSelector_('frodel'))


    def testDeallocUninit(self):
        import objc

        import warnings
        warnings.filterwarnings('ignore',
            category=objc.UninitializedDeallocWarning)

        try:
            for clsName in [ 'NSURL', 'NSObject', 'NSArray' ]:
                d = objc.lookUpClass(clsName).alloc()
                del d

        finally:
            del warnings.filters[0]

        # Check that we generate a warning for unitialized objects that
        # get deallocated
        import sys
        if sys.version_info[0] == 2:
            from StringIO import StringIO
        else:
            from io import StringIO
        warnings.filterwarnings('always',
            category=objc.UninitializedDeallocWarning)
        sys.stderr = buf = StringIO()
        try:
            d = NSObject.alloc()
            del d

        finally:
            del warnings.filters[0]
            sys.stderr = sys.__stderr__

        # A warning is three lines: location info, source code, empty line
        self.assertEqual(len(buf.getvalue().split('\n')), 3)

    def testOneWayMethods(self):
        # This one should be in test_methods*.py
        from PyObjCTest.initialize import OC_TestInitialize

        o = OC_TestInitialize.alloc().init()
        self.assertEqual(objc.splitSignature(o.onewayVoidMethod.signature), (objc._C_ONEWAY + objc._C_VOID, objc._C_ID, objc._C_SEL))

        # Make sure we can call the method
        o.onewayVoidMethod()
        self.assertEqual(o.isInitialized(), -1)


    def testNoneAsSelf (self):
        class SelfIsNone (NSObject):
            def f(x):
                pass

        self.assertRaises(TypeError, NSObject.pyobjc_instanceMethods.description, None)
        self.assertRaises(TypeError, SelfIsNone.pyobjc_instanceMethods.f, None)

    def testOneArgumentTooMany (self):
        class ClsIsNone (NSObject):
            @classmethod
            def f(cls):
                pass

        object = NSObject.alloc().init()

        self.assertRaises(TypeError, object.description, None)
        self.assertRaises(TypeError, object.description, "twelf")
        self.assertRaises(TypeError, NSObject.description, None)
        self.assertRaises(TypeError, ClsIsNone.f, None)


    def testStructArgs (self):
        # Like AppKit.test.test_nsimage.TestNSImage.test_compositePoint
        # unlike that this one doesn't crash on darwin/x86, makeing it less
        # likely that libffi is at fault

        o = structargs.StructArgClass.alloc().init()
        v = o.compP_aRect_anOp_((1,2), ((3,4),(5,6)), 7)
        self.assertEqual(v, "aP:{1, 2} aR:{{3, 4}, {5, 6}} anO:7")

    def testInitialize(self):
        calls=[]
        self.assertEqual(len(calls), 0)

        class InitializeTestClass (NSObject):
            @classmethod
            def initialize(cls):
                calls.append(repr(cls))

        o = InitializeTestClass.new()
        self.assertEqual(len(calls), 1)
        o = InitializeTestClass.new()
        self.assertEqual(len(calls), 1)

    def testPrivateIntrospection(self):
        o = testbndl.PyObjC_TestClass4.alloc().init()
        self.assertEqual(o._privateMethodWithArg_(1.5), 1)
        self.assertEqual(o._privateMethodWithArg_(-2.5), -2)

        imp = testbndl.PyObjC_TestClass4.instanceMethodForSelector_('_privateMethodWithArg:')
        self.assertEqual(imp.signature, b'i@:f')

        sel = testbndl.PyObjC_TestClass4._privateMethodWithArg_
        self.assertEqual(sel.signature, b'i@:f')

    def testStructReturnPy(self):
        o = ReturnAStruct.alloc().init()
        p = structargs.StructArgClass.alloc().init()

        v = p.someRectWithObject_X_Y_H_W_(o, 1, 2, 3, 4)
        self.assertEqual(v, ((1,2),(3,4)))

    def testStructReturn(self):
        o = structargs.StructArgClass.alloc().init()
        v = o.someRect()
        self.assertEqual(v, ((1,2),(3,4)))



if sys.byteorder == 'little':
    # i386 has specific stack alignment requirements.

    class AlignmentTestClass(NSObject):
        def testWithObject_(self, obj):
            return obj.stackPtr()


    def testStackPtr(self):
        o = structargs.StructArgClass.alloc().init()

        p = self.AlignmentTestClass.alloc().init()
        self.assertEqual(p.testWithObject_(o) % 16, o.stackPtr() % 16)



#
# Regression in retainCount management when a Python object
# is created from Objective-C. This only happened when the
# Python class has an implementation of the designated initializer.
#
# Mentioned by Dirk Stoop on the Pyobjc-dev mailing-list.
#

gDeallocCounter = 0
class OC_LeakTest_20090704_init (NSObject):
    def init(self):
        #self = super(OC_LeakTest_20090704_init, self).init()
        return self

    def dealloc(self):
        global gDeallocCounter
        gDeallocCounter += 1

class OC_LeakTest_20090704_noinit (NSObject):
    def dealloc(self):
        global gDeallocCounter
        gDeallocCounter += 1


class TestInitMemoryLeak (TestCase):
    def testNoPythonInit(self):
        # This test is basicly a self-test of the test-case, the
        # test even passed before the regression was fixed.

        global gDeallocCounter

        pool = NSAutoreleasePool.alloc().init()
        try:
            v = copying.OC_CopyHelper.newObjectOfClass_(OC_LeakTest_20090704_noinit)
            self.assertIsInstance(v, OC_LeakTest_20090704_noinit)

            gDeallocCounter = 0
            del v

        finally:
            del pool

        self.assertNotEqual(gDeallocCounter, 0)

    def testWithPythonInit(self):
        global gDeallocCounter

        pool = NSAutoreleasePool.alloc().init()
        try:
            v = copying.OC_CopyHelper.newObjectOfClass_(OC_LeakTest_20090704_init)
            self.assertIsInstance(v, OC_LeakTest_20090704_init)

            gDeallocCounter = 0
            del v

        finally:
            del pool

        self.assertNotEqual(gDeallocCounter, 0)

    def testInitFailureLeaks(self):
        NSData = objc.lookUpClass('NSData')
        import warnings
        warnings.filterwarnings('error',
            category=objc.UninitializedDeallocWarning)

        try:
            try:
                v = NSData.alloc().initWithContentsOfFile_("/etc/no-such-file.txt")
            finally:
                del warnings.filters[0]

        except objc.UninitializedDeallocWarning:
            self.fail("Unexpected raising of UninitializedDeallocWarning")

        self.assertFalse(v is not None)

    def testExplicitGetItem(self):
        v = OCTestRegrWithGetItem.alloc().init()

        self.assertEqual(v.objectForKey_("foo"), "ofk: foo")
        self.assertEqual(v["foo"], "gi: foo")

        v = OCTestRegrWithGetItem2.alloc().init()
        self.assertEqual(v.objectForKey_("foo"), "ofk2: foo")
        self.assertEqual(v["foo"], "gi: foo")


if __name__ == '__main__':
    main()
