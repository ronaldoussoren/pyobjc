from PyObjCTools.TestSupport import *
import objc
import warnings
import sys

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

# XXX : This is a really dumb way to detect < 10.3
if not NSObject.instancesRespondToSelector_('setValue:forKey:'):
    # Defining protocols in an MH_BUNDLE makes < 10.3 explode
    OC_TestProtocol = None
else:
    from PyObjCTest.protocol import OC_TestProtocol

MyProto = objc.informal_protocol("MyProto", (
    objc.selector(None, selector="testMethod", signature="I@:", isRequired=1),
    objc.selector(None, selector="testMethod2:", signature="v@:i", isRequired=0)
))

class TestInformalProtocols(TestCase):


    def testMissingProto(self):
        class ProtoClass1 (NSObject):
            def testMethod(self):
                pass
        self.assertEquals(ProtoClass1.testMethod.signature, "I@:")


    def doIncompleteClass(self):
        class ProtoClass2 (NSObject, MyProto):
            def testMethod2_(self, x):
                pass

    def testIncompleteClass(self):
        self.assertRaises(TypeError, self.doIncompleteClass)


    def testOptional(self):
        class ProtoClass3 (NSObject, MyProto):
            def testMethod(self):
                pass



if sys.maxint < 2 ** 32:
    EmptyProtocol = objc.formal_protocol("EmptyProtocol", None, ())

    MyProtocol = objc.formal_protocol("MyProtocol", None, (
        objc.selector(None, selector="protoMethod", signature="I@:"),
        objc.selector(None, selector="anotherProto:with:", signature="v@:ii"),
    ))

    MyOtherProtocol = objc.formal_protocol("MyOtherProtocol", 
            (MyProtocol,), [
                objc.selector(None, selector="yetAnother:", signature="i@:I")
            ])

    MyClassProtocol = objc.formal_protocol("MyClassProtocol", None, [
        objc.selector(None, selector="anAnotherOne:", signature="i@:i"),
        objc.selector(None, selector="aClassOne:", signature="@@:i", isClassMethod=1),
    ])

    if OC_TestProtocol is not None:

        class TestFormalOCProtocols(TestCase):
            
            def testImplementFormalProtocol(self):

                class MyClassNotImplementingProtocol(NSObject):
                    pass

                self.assert_(not MyClassNotImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))

                try:
                    class MyClassNotAlsoImplementingProtocol(NSObject, OC_TestProtocol):
                        def method1(self): pass

                    self.fail("class not implementing protocol, yet created")
                except TypeError:
                    pass

                class MyClassImplementingProtocol(NSObject, OC_TestProtocol):
                    def method1(self): pass
                    def method2_(self, a): pass

                self.assert_(MyClassImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))



                # The PyObjC implementation of formal protocols is slightly looser
                # than Objective-C itself: you can inherit part of the protocol
                # from the superclass.
                # XXX: not really: you won't inherit the right signatures by default

                class MyClassImplementingHalfOfProtocol(NSObject):
                        def method1(self): pass
                        method1 = objc.selector(method1, signature='i@:')

                self.assert_(not MyClassImplementingHalfOfProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))

                class MyClassImplementingAllOfProtocol(MyClassImplementingHalfOfProtocol, OC_TestProtocol):
                        def method2_(self, v): pass

                self.assert_(MyClassImplementingAllOfProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))




    class TestFormalProtocols (TestCase):
        # Implement unittests for formal protocols here.
        #

        def testImplementAnotherObject(self):
            anObject = NSObject.alloc().init()

            try:
                class MyClassImplementingAnotherObject(NSObject, anObject):
                        pass
                self.fail()
            except TypeError: 
                pass

            try:
                class MyClassImplementingAnotherObject(NSObject, 10):
                        pass
                self.fail()
            except TypeError: 
                pass

            try:
                class MyClassImplementingAnotherObject(NSObject, int):
                        pass
                self.fail()
            except TypeError: 
                pass

        def dont_testDefiningingProtocols(self):

            # Pretty useless, but should work

            self.assert_(MyOtherProtocol.conformsTo_(MyProtocol))


            try:
                class MyClassImplementingMyProtocol(NSObject, MyProtocol):
                    pass

                # Declare to implement a protocol, but don't do it?
                self.fail()
            except TypeError:
                pass


            class MyClassImplementingMyProtocol(NSObject, MyProtocol):
                def protoMethod(self):
                    return 1

                def anotherProto_with_(self, a1, a2):
                    pass

            self.assertEquals(MyClassImplementingMyProtocol.protoMethod.signature, "I@:")
            self.assertEquals(MyClassImplementingMyProtocol.anotherProto_with_.signature, "v@:ii")
            self.assert_(MyClassImplementingMyProtocol.pyobjc_classMethods.conformsToProtocol_(MyProtocol))

            class MyClassImplementingMyOtherProtocol(NSObject, MyOtherProtocol):
                def protoMethod(self): pass
                def anotherProto_with_(self, a1, a2): pass
                def yetAnother_(self, a): pass

            self.assertEquals(MyClassImplementingMyOtherProtocol.protoMethod.signature, "I@:")
            self.assertEquals(MyClassImplementingMyOtherProtocol.anotherProto_with_.signature, "v@:ii")
            self.assertEquals(MyClassImplementingMyOtherProtocol.yetAnother_.signature, "i@:I")
            self.assert_(MyClassImplementingMyOtherProtocol.pyobjc_classMethods.conformsToProtocol_(MyProtocol))
            self.assert_(MyClassImplementingMyOtherProtocol.pyobjc_classMethods.conformsToProtocol_(MyOtherProtocol))

            try:
                class ImplementingMyClassProtocol(NSObject, MyClassProtocol):
                    pass

                self.fail()
            except TypeError:
                pass

            class ImplementingMyClassProtocol(NSObject, MyClassProtocol):
                    def anAnotherOne_(self, a):
                        pass

                    def aClassOne_(self, a):
                        pass

                    aClassOne_ = classmethod(aClassOne_)

            self.assertEquals(ImplementingMyClassProtocol.anAnotherOne_.signature, 'i@:i')
            self.assertEquals(ImplementingMyClassProtocol.aClassOne_.isClassMethod, True)
            self.assertEquals(ImplementingMyClassProtocol.aClassOne_.signature,'@@:i')

            # TODO: protocol with class and instance method with different
            # signatures.
            # TODO: should not need to specify classmethod() if it can be 
            # deduced from the protocol


        def testIncorrectlyDefiningFormalProtocols(self):
            # Some bad calls to objc.formal_protocol
            self.assertRaises(TypeError, objc.formal_protocol, [], None, ())
            self.assertRaises(TypeError, objc.formal_protocol, 'supers', (NSObject,) , ())
            self.assertRaises(TypeError, objc.formal_protocol, 'supers', objc.protocolNamed('NSLocking') , ())
            self.assertRaises(TypeError, objc.formal_protocol, 'supers', [
                    objc.protocolNamed('NSLocking'),
                    "hello",
                ], ())
            self.assertRaises(TypeError, objc.formal_protocol, 'supers', None, [
                    objc.selector(None, selector='fooMethod:', signature='v@:i'),
                    "hello",
                ])

        def testMethodInfo(self):
            self.assertEquals(
                    MyProtocol.descriptionForInstanceMethod_("protoMethod"),
                        ("protoMethod", "I@:"))

            self.assertEquals(
                    MyProtocol.descriptionForInstanceMethod_("nosuchmethod"),
                        None)

            self.assertEquals(
                    MyClassProtocol.descriptionForClassMethod_("aClassOne:"),
                        ("aClassOne:", "@@:i"))

            self.assertEquals(
                    MyClassProtocol.descriptionForClassMethod_("nosuchmethod"),
                        None)


        def dont_testObjCInterface(self):
            # TODO: tests that access the Objective-C interface of protocols
            # (those methods should be forwarded to the underlying object, as 
            #  with objc.pyobjc_unicode).
            # NOTE: This is not very important, the only methods that are not
            # explicitly wrapped should be compatibility methods that will
            # cause a warning when called.
            self.assertEquals(1, 0)

if __name__ == '__main__':
    main()
