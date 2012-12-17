from PyObjCTools.TestSupport import *
import objc
import warnings
import sys
import platform

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')

# XXX : This is a really dumb way to detect < 10.3
if not NSObject.instancesRespondToSelector_('setValue:forKey:'):
    # Defining protocols in an MH_BUNDLE makes < 10.3 explode
    OC_TestProtocol = None
else:
    from PyObjCTest.protocol import OC_TestProtocol

MyProto = objc.informal_protocol("MyProto", (
    objc.selector(None, selector=b"testMethod", signature=b"I@:", isRequired=1),
    objc.selector(None, selector=b"testMethod2:", signature=b"v@:i", isRequired=0)
))

class TestInformalProtocols(TestCase):


    def testMissingProto(self):
        class ProtoClass1 (NSObject):
            def testMethod(self):
                pass
        self.assertEqual(ProtoClass1.testMethod.signature, b"I@:")


    def doIncompleteClass(self):
        class ProtoClass2 (NSObject, MyProto):
            def testMethod2_(self, x):
                pass

    def testIncompleteClass(self):
        self.assertRaises(TypeError, self.doIncompleteClass)


    @onlyIf(sys.version_info[:2] < (3,2), "not valid for python 3.3 and later")
    def testOptional(self):
        class ProtoClass3 (NSObject, MyProto):
            def testMethod(self):
                pass



if (sys.maxsize < 2 ** 32 or platform.mac_ver()[0] >= '10.7') and sys.version_info[0] == 2:
    EmptyProtocol = objc.formal_protocol("EmptyProtocol", None, ())

    MyProtocol = objc.formal_protocol("MyProtocol", None, (
        objc.selector(None, selector=b"protoMethod", signature=b"I@:"),
        objc.selector(None, selector=b"anotherProto:with:", signature=b"v@:ii"),
    ))

    MyOtherProtocol = objc.formal_protocol("MyOtherProtocol",
            (MyProtocol,), [
                objc.selector(None, selector=b"yetAnother:", signature=b"i@:I")
            ])

    MyClassProtocol = objc.formal_protocol("MyClassProtocol", None, [
        objc.selector(None, selector=b"anAnotherOne:", signature=b"i@:i"),
        objc.selector(None, selector=b"aClassOne:", signature=b"@@:i", isClassMethod=1),
    ])

    if OC_TestProtocol is not None:

        class TestFormalOCProtocols(TestCase):
            def testMethodInfo(self):
                actual = OC_TestProtocol.instanceMethods()
                actual.sort(key=lambda item: item['selector'])
                expected = [
                    {'required': True, 'selector': b'method1', 'typestr': b'i@:'},
                    {'required': True, 'selector': b'method2:', 'typestr': b'v@:i'}
                ]
                self.assertEqual(actual, expected)
                self.assertEqual(OC_TestProtocol.classMethods(), [])

                self.assertEqual(OC_TestProtocol.descriptionForInstanceMethod_(b"method1"), (b"method1", b"i@:"))
                self.assertEqual(OC_TestProtocol.descriptionForInstanceMethod_(b"method2:"), (b"method2:", b"v@:i"))

            def testImplementFormalProtocol(self):

                class MyClassNotImplementingProtocol(NSObject):
                    pass

                self.assertFalse(MyClassNotImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))

                try:
                    class MyClassNotAlsoImplementingProtocol(NSObject, OC_TestProtocol):
                        def method1(self): pass

                    self.fail("class not implementing protocol, yet created")
                except TypeError:
                    pass

                class MyClassImplementingProtocol(NSObject, OC_TestProtocol):
                    def method1(self): pass
                    def method2_(self, a): pass

                self.assertTrue(MyClassImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))



                # The PyObjC implementation of formal protocols is slightly looser
                # than Objective-C itself: you can inherit part of the protocol
                # from the superclass.
                # XXX: not really: you won't inherit the right signatures by default

                class MyClassImplementingHalfOfProtocol(NSObject):
                    def method1(self): pass
                    method1 = objc.selector(method1, signature=b'i@:')

                self.assertFalse(MyClassImplementingHalfOfProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))

                class MyClassImplementingAllOfProtocol(MyClassImplementingHalfOfProtocol, OC_TestProtocol):
                    def method2_(self, v): pass

                self.assertTrue(MyClassImplementingAllOfProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))




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

            self.assertTrue(MyOtherProtocol.conformsTo_(MyProtocol))


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

            self.assertEqual(MyClassImplementingMyProtocol.protoMethod.signature, b"I@:")
            self.assertEqual(MyClassImplementingMyProtocol.anotherProto_with_.signature, b"v@:ii")
            self.assertTrue(MyClassImplementingMyProtocol.pyobjc_classMethods.conformsToProtocol_(MyProtocol))

            class MyClassImplementingMyOtherProtocol(NSObject, MyOtherProtocol):
                def protoMethod(self): pass
                def anotherProto_with_(self, a1, a2): pass
                def yetAnother_(self, a): pass

            self.assertEqual(MyClassImplementingMyOtherProtocol.protoMethod.signature, b"I@:")
            self.assertEqual(MyClassImplementingMyOtherProtocol.anotherProto_with_.signature, b"v@:ii")
            self.assertEqual(MyClassImplementingMyOtherProtocol.yetAnother_.signature, b"i@:I")
            self.assertTrue(MyClassImplementingMyOtherProtocol.pyobjc_classMethods.conformsToProtocol_(MyProtocol))
            self.assertTrue(MyClassImplementingMyOtherProtocol.pyobjc_classMethods.conformsToProtocol_(MyOtherProtocol))

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

            self.assertEqual(ImplementingMyClassProtocol.anAnotherOne_.signature, b'i@:i')
            self.assertEqual(ImplementingMyClassProtocol.aClassOne_.isClassMethod, True)
            self.assertEqual(ImplementingMyClassProtocol.aClassOne_.signature, b'@@:i')

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
                    objc.selector(None, selector=b'fooMethod:', signature=b'v@:i'),
                    "hello",
                ])

        def testMethodInfo(self):
            self.assertEqual(MyProtocol.instanceMethods(), [
                {'typestr': b'I@:', 'required': True, 'selector': b'protoMethod'},
                {'typestr': b'v@:ii', 'required': True, 'selector': b'anotherProto:with:'},
            ])
            self.assertEqual(MyProtocol.classMethods(), [
            ])
            self.assertEqual(
                    MyProtocol.descriptionForInstanceMethod_(b"protoMethod"),
                        ("protoMethod", "I@:"))

            self.assertEqual(
                    MyProtocol.descriptionForInstanceMethod_(b"nosuchmethod"),
                        None)

            self.assertEqual(MyClassProtocol.classMethods(), [
                {'required': True, 'selector': 'aClassOne:', 'typestr': '@@:i'}
            ])
            self.assertEqual(MyProtocol.classMethods(), [
            ])
            self.assertEqual(
                    MyClassProtocol.descriptionForClassMethod_(b"aClassOne:"),
                        ("aClassOne:", "@@:i"))

            self.assertEqual(
                    MyClassProtocol.descriptionForClassMethod_(b"nosuchmethod"),
                        None)


        def dont_testObjCInterface(self):
            # TODO: tests that access the Objective-C interface of protocols
            # (those methods should be forwarded to the underlying object, as
            #  with objc.pyobjc_unicode).
            # NOTE: This is not very important, the only methods that are not
            # explicitly wrapped should be compatibility methods that will
            # cause a warning when called.
            self.assertEqual(1, 0)

if __name__ == '__main__':
    main()
