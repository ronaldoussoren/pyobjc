from PyObjCTools.TestSupport import *
import objc
import warnings
import platform
import sys

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass('NSObject')


# XXX : This is a really dumb way to detect < 10.3
if not NSObject.instancesRespondToSelector_('setValue:forKey:'):
    # Defining protocols in an MH_BUNDLE makes < 10.3 explode
    OC_TestProtocol = None
else:
    from PyObjCTest.protocol import OC_TestProtocol


MyProto3 = objc.informal_protocol("MyProto3", (
    objc.selector(None, selector=b"testMethod", signature=b"I@:", isRequired=1),
    objc.selector(None, selector=b"testMethod2:", signature=b"v@:i", isRequired=0)
))

class Test3InformalProtocols(TestCase):
    def testOptional(self):
        class ProtoClass3 (NSObject, protocols=[MyProto3]):
            def testMethod(self):
                pass




if (sys.maxsize < 2 ** 32) or (platform.mac_ver()[0] >= '10.7'):
    EmptyProtocol3 = objc.formal_protocol("EmptyProtocol3", None, ())


    MyProtocol3 = objc.formal_protocol("MyProtocol3", None, (
        objc.selector(None, selector=b"protoMethod", signature=b"I@:"),
        objc.selector(None, selector=b"anotherProto:with:", signature=b"v@:ii"),
    ))

    MyOtherProtocol3 = objc.formal_protocol("MyOtherProtocol3",
            (MyProtocol3,), [
                objc.selector(None, selector=b"yetAnother:", signature=b"i@:I")
            ])

    MyClassProtocol3 = objc.formal_protocol("MyClassProtocol3", None, [
        objc.selector(None, selector=b"anAnotherOne:", signature=b"i@:i"),
        objc.selector(None, selector=b"aClassOne:", signature=b"@@:i", isClassMethod=1),
    ])

    if OC_TestProtocol is not None:

        class TestFormalOCProtocols(TestCase):

            def testImplementFormalProtocol(self):

                class MyClassNotImplementingProtocol(NSObject):
                    pass

                self.assertFalse(MyClassNotImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))

                try:
                    class MyClassNotAlsoImplementingProtocol(NSObject, protocols=[OC_TestProtocol]):
                        def method1(self): pass

                    self.fail("class not implementing protocol, yet created")
                except TypeError:
                    pass

                class MyClassImplementingProtocol(NSObject, protocols=[OC_TestProtocol]):
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

                class MyClassImplementingAllOfProtocol(MyClassImplementingHalfOfProtocol, protocols=[OC_TestProtocol]):
                    def method2_(self, v): pass

                self.assertTrue(MyClassImplementingAllOfProtocol.pyobjc_classMethods.conformsToProtocol_(OC_TestProtocol))




    class TestFormalProtocols (TestCase):
        # Implement unittests for formal protocols here.
        #

        def testImplementAnotherObject(self):
            anObject = NSObject.alloc().init()

            try:
                class MyClassImplementingAnotherObject(NSObject, protocols=[anObject]):
                    pass
                self.fail("Can create class that implements an object???")
            except TypeError:
                pass

            try:
                class MyClassImplementingAnotherObject(NSObject, protocols=[10]):
                    pass
                self.fail()
            except TypeError:
                pass

            try:
                class MyClassImplementingAnotherObject(NSObject, protocols=[int]):
                    pass
                self.fail()
            except TypeError:
                pass



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
            self.assertEqual(MyProtocol3.instanceMethods(), [
                {'typestr': b'I@:', 'required': True, 'selector': b'protoMethod'},
                {'typestr': b'v@:ii', 'required': True, 'selector': b'anotherProto:with:'},
            ])
            self.assertEqual(MyProtocol3.classMethods(), [
            ])
            self.assertEqual(
                    MyProtocol3.descriptionForInstanceMethod_(b"protoMethod"),
                        (b"protoMethod", b"I@:"))

            self.assertEqual(
                    MyProtocol3.descriptionForInstanceMethod_(b"nosuchmethod"),
                        None)

            self.assertEqual(MyClassProtocol3.classMethods(), [
                {'required': True, 'selector': b'aClassOne:', 'typestr': b'@@:i'}
            ])
            self.assertEqual(MyProtocol3.classMethods(), [
            ])
            self.assertEqual(
                    MyClassProtocol3.descriptionForClassMethod_(b"aClassOne:"),
                        (b"aClassOne:", b"@@:i"))

            self.assertEqual(
                    MyClassProtocol3.descriptionForClassMethod_(b"nosuchmethod"),
                        None)


if __name__ == '__main__':
    main()
