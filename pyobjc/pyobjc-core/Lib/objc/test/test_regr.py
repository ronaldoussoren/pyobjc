import objc.test
from objc.test import structargs
from objc.test import testbndl

import objc, sys
from objc.test.fnd import NSObject


class TestRegressions(objc.test.TestCase):
    def testNSObjectRespondsToCommonMethods(self):
        self.assert_(NSObject.pyobjc_classMethods.respondsToSelector_('alloc'))
        self.assert_(NSObject.instancesRespondToSelector_('init'))
        self.assert_(not NSObject.instancesRespondToSelector_('frodel'))


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
        import StringIO
        warnings.filterwarnings('always',
            category=objc.UninitializedDeallocWarning)
        sys.stderr = io = StringIO.StringIO()
        try:
            d = NSObject.alloc()
            del d

        finally:
            del warnings.filters[0]
            sys.stderr = sys.__stderr__

        # A warning is three lines: location info, source code, empty line
        self.assertEquals(len(io.getvalue().split('\n')), 3)

    def testOneWayMethods(self):
        # This one should be in test_methods*.py
        from objc.test.initialize import OC_TestInitialize

        o = OC_TestInitialize.alloc().init()
        self.assertEquals(objc.splitSignature(o.onewayVoidMethod.signature), (objc._C_ONEWAY + objc._C_VOID, objc._C_ID, objc._C_SEL))

        # Make sure we can call the method
        o.onewayVoidMethod()
        self.assertEquals(o.isInitialized(), -1)


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
        from objc.test.structargs import StructArgClass

        o = StructArgClass.alloc().init()
        v = o.compP_aRect_anOp_((1,2), ((3,4),(5,6)), 7)
        self.assertEquals(v, u"aP:{1, 2} aR:{{3, 4}, {5, 6}} anO:7")

    def testInitialize(self):
        calls=[]
        self.assertEquals(len(calls), 0)

        class InitializeTestClass (NSObject):
            @classmethod
            def initialize(cls):
                calls.append(repr(cls))

        o = InitializeTestClass.new()
        self.assertEquals(len(calls), 1)
        o = InitializeTestClass.new()
        self.assertEquals(len(calls), 1)

    def testPrivateIntrospection(self):
        o = testbndl.PyObjC_TestClass4.alloc().init()
        self.assertEquals(o._privateMethodWithArg_(1.5), 1)
        self.assertEquals(o._privateMethodWithArg_(-2.5), -2)

        imp = testbndl.PyObjC_TestClass4.instanceMethodForSelector_('_privateMethodWithArg:')
        self.assertEquals(imp.signature, 'i@:f')

        sel = testbndl.PyObjC_TestClass4._privateMethodWithArg_
        self.assertEquals(sel.signature, 'i@:f')


if sys.byteorder == 'little':
    # i386 has specific stack alignment requirements.

    class AlignmentTestClass(NSObject):
        def testWithObject_(self, obj):
            return obj.stackPtr()


    def testStackPtr(self):
        o = structargs.StructArgClass.alloc().init()

        p = self.AlignmentTestClass.alloc().init()
        self.assertEquals(p.testWithObject_(o) % 16, o.stackPtr() % 16)

if __name__ == '__main__':
    objc.test.main()
