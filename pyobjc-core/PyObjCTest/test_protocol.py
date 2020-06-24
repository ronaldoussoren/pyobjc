import objc
from PyObjCTest.protocol import OC_TestProtocol
from PyObjCTools.TestSupport import TestCase

# Most useful systems will at least have 'NSObject'.
NSObject = objc.lookUpClass("NSObject")


MyProto = objc.informal_protocol(
    "MyProto",
    (
        objc.selector(None, selector=b"testMethod", signature=b"I@:", isRequired=1),
        objc.selector(None, selector=b"testMethod2:", signature=b"v@:i", isRequired=0),
    ),
)

MyProto3 = objc.informal_protocol(
    "MyProto3",
    (
        objc.selector(None, selector=b"testMethod", signature=b"I@:", isRequired=1),
        objc.selector(None, selector=b"testMethod2:", signature=b"v@:i", isRequired=0),
    ),
)


class TestInformalProtocols(TestCase):
    def testMissingProto(self):
        class ProtoClass1(NSObject):
            def testMethod(self):
                pass

        self.assertEqual(ProtoClass1.testMethod.signature, b"I@:")

    def doIncompleteClass(self):
        class ProtoClass2(NSObject, MyProto):
            def testMethod2_(self, x):
                pass

    def testIncompleteClass(self):
        self.assertRaises(TypeError, self.doIncompleteClass)
        self.assertRaises(objc.error, objc.lookUpClass, "ProtoClass2")

        for cls in objc.getClassList():
            self.assertNotEqual(cls.__name__, "ProtoClass2")


EmptyProtocol = objc.formal_protocol("EmptyProtocol", None, ())

MyProtocol = objc.formal_protocol(
    "MyProtocol",
    None,
    (
        objc.selector(None, selector=b"protoMethod", signature=b"I@:"),
        objc.selector(None, selector=b"anotherProto:with:", signature=b"v@:ii"),
    ),
)

MyOtherProtocol = objc.formal_protocol(
    "MyOtherProtocol",
    (MyProtocol,),
    [objc.selector(None, selector=b"yetAnother:", signature=b"i@:I")],
)

MyClassProtocol = objc.formal_protocol(
    "MyClassProtocol",
    None,
    [
        objc.selector(None, selector=b"anAnotherOne:", signature=b"i@:i"),
        objc.selector(None, selector=b"aClassOne:", signature=b"@@:i", isClassMethod=1),
    ],
)


class TestFormalOCProtocols(TestCase):
    def testMethodInfo(self):
        actual = OC_TestProtocol.instanceMethods()
        actual.sort(key=lambda item: item["selector"])
        expected = [
            {"required": True, "selector": b"method1", "typestr": b"i@:"},
            {"required": True, "selector": b"method2:", "typestr": b"v@:i"},
        ]
        self.assertEqual(actual, expected)
        self.assertEqual(OC_TestProtocol.classMethods(), [])

        self.assertEqual(
            OC_TestProtocol.descriptionForInstanceMethod_(b"method1"),
            (b"method1", b"i@:"),
        )
        self.assertEqual(
            OC_TestProtocol.descriptionForInstanceMethod_(b"method2:"),
            (b"method2:", b"v@:i"),
        )

    def testImplementFormalProtocol(self):
        class MyClassNotImplementingProtocol(NSObject):
            pass

        self.assertFalse(
            MyClassNotImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )

        try:

            class MyClassNotAlsoImplementingProtocol(NSObject, OC_TestProtocol):
                def method1(self):
                    pass

            self.fail("class not implementing protocol, yet created")
        except TypeError:
            pass

        class MyClassImplementingProtocol(NSObject, protocols=[OC_TestProtocol]):
            def method1(self):
                pass

            def method2_(self, a):
                pass

        self.assertTrue(
            MyClassImplementingProtocol.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )

        # The PyObjC implementation of formal protocols is slightly looser
        # than Objective-C itself: you can inherit part of the protocol
        # from the superclass.
        # XXX: not really: you won't inherit the right signatures by default

        class MyClassImplementingHalfOfProtocol(NSObject):
            def method1(self):
                pass

            method1 = objc.selector(method1, signature=b"i@:")

        self.assertFalse(
            MyClassImplementingHalfOfProtocol.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )

        class MyClassImplementingAllOfProtocol(
            MyClassImplementingHalfOfProtocol, protocols=[OC_TestProtocol]
        ):
            def method2_(self, v):
                pass

        self.assertTrue(
            MyClassImplementingAllOfProtocol.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )


class TestFormalProtocols(TestCase):
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

            class MyClassImplementingAnotherObject2(NSObject, 10):
                pass

            self.fail()
        except TypeError:
            pass

        try:

            class MyClassImplementingAnotherObject3(NSObject, int):
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

        class MyClassImplementingMyProtocol2(NSObject, MyProtocol):
            def protoMethod(self):
                return 1

            def anotherProto_with_(self, a1, a2):
                pass

        self.assertEqual(MyClassImplementingMyProtocol.protoMethod.signature, b"I@:")
        self.assertEqual(
            MyClassImplementingMyProtocol.anotherProto_with_.signature, b"v@:ii"
        )
        self.assertTrue(
            MyClassImplementingMyProtocol.pyobjc_classMethods.conformsToProtocol_(
                MyProtocol
            )
        )

        class MyClassImplementingMyOtherProtocol(NSObject, MyOtherProtocol):
            def protoMethod(self):
                pass

            def anotherProto_with_(self, a1, a2):
                pass

            def yetAnother_(self, a):
                pass

        self.assertEqual(
            MyClassImplementingMyOtherProtocol.protoMethod.signature, b"I@:"
        )
        self.assertEqual(
            MyClassImplementingMyOtherProtocol.anotherProto_with_.signature, b"v@:ii"
        )
        self.assertEqual(
            MyClassImplementingMyOtherProtocol.yetAnother_.signature, b"i@:I"
        )
        self.assertTrue(
            MyClassImplementingMyOtherProtocol.pyobjc_classMethods.conformsToProtocol_(
                MyProtocol
            )
        )
        self.assertTrue(
            MyClassImplementingMyOtherProtocol.pyobjc_classMethods.conformsToProtocol_(
                MyOtherProtocol
            )
        )

        try:

            class ImplementingMyClassProtocol2(NSObject, MyClassProtocol):
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

        self.assertEqual(ImplementingMyClassProtocol.anAnotherOne_.signature, b"i@:i")
        self.assertEqual(ImplementingMyClassProtocol.aClassOne_.isClassMethod, True)
        self.assertEqual(ImplementingMyClassProtocol.aClassOne_.signature, b"@@:i")

        # TODO: protocol with class and instance method with different
        # signatures.
        # TODO: should not need to specify classmethod() if it can be
        # deduced from the protocol

    def testIncorrectlyDefiningFormalProtocols(self):
        # Some bad calls to objc.formal_protocol
        self.assertRaises(TypeError, objc.formal_protocol, [], None, ())
        self.assertRaises(TypeError, objc.formal_protocol, "supers", (NSObject,), ())
        self.assertRaises(
            TypeError,
            objc.formal_protocol,
            "supers",
            objc.protocolNamed("NSLocking"),
            (),
        )
        self.assertRaises(
            TypeError,
            objc.formal_protocol,
            "supers",
            [objc.protocolNamed("NSLocking"), "hello"],
            (),
        )
        self.assertRaises(
            TypeError,
            objc.formal_protocol,
            "supers",
            None,
            [
                objc.selector(None, selector=b"fooMethod:", signature=b"v@:i"),
                "hello",
            ],  # noqa: E231
        )

    def testMethodInfo(self):
        self.assertEqual(
            MyProtocol.instanceMethods(),
            [
                {"typestr": b"I@:", "required": True, "selector": b"protoMethod"},
                {
                    "typestr": b"v@:ii",
                    "required": True,
                    "selector": b"anotherProto:with:",
                },
            ],
        )
        self.assertEqual(MyProtocol.classMethods(), [])
        self.assertEqual(
            MyProtocol.descriptionForInstanceMethod_(b"protoMethod"),
            (b"protoMethod", b"I@:"),
        )

        self.assertEqual(
            MyProtocol.descriptionForInstanceMethod_(b"nosuchmethod"), None
        )

        self.assertEqual(
            MyClassProtocol.classMethods(),
            [{"required": True, "selector": b"aClassOne:", "typestr": b"@@:i"}],
        )
        self.assertEqual(MyProtocol.classMethods(), [])
        self.assertEqual(
            MyClassProtocol.descriptionForClassMethod_(b"aClassOne:"),
            (b"aClassOne:", b"@@:i"),
        )

        self.assertEqual(
            MyClassProtocol.descriptionForClassMethod_(b"nosuchmethod"), None
        )

    def dont_testObjCInterface(self):
        # TODO: tests that access the Objective-C interface of protocols
        # (those methods should be forwarded to the underlying object, as
        #  with objc.pyobjc_unicode).
        # NOTE: This is not very important, the only methods that are not
        # explicitly wrapped should be compatibility methods that will
        # cause a warning when called.
        self.assertEqual(1, 0)


class Test3InformalProtocols(TestCase):
    def testOptional(self):
        class ProtoClass3(NSObject, protocols=[MyProto3]):
            def testMethod(self):
                pass


EmptyProtocol3 = objc.formal_protocol("EmptyProtocol3", None, ())

MyProtocol3 = objc.formal_protocol(
    "MyProtocol3",
    None,
    (
        objc.selector(None, selector=b"protoMethod", signature=b"I@:"),
        objc.selector(None, selector=b"anotherProto:with:", signature=b"v@:ii"),
    ),
)

MyOtherProtocol3 = objc.formal_protocol(
    "MyOtherProtocol3",
    (MyProtocol3,),
    [objc.selector(None, selector=b"yetAnother:", signature=b"i@:I")],
)

MyClassProtocol3 = objc.formal_protocol(
    "MyClassProtocol3",
    None,
    [
        objc.selector(None, selector=b"anAnotherOne:", signature=b"i@:i"),
        objc.selector(None, selector=b"aClassOne:", signature=b"@@:i", isClassMethod=1),
    ],
)


class TestFormalOCProtocols2(TestCase):
    def testImplementFormalProtocol(self):
        class MyClassNotImplementingProtocolA(NSObject):
            pass

        self.assertFalse(
            MyClassNotImplementingProtocolA.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )

        try:

            class MyClassNotAlsoImplementingProtocolA(
                NSObject, protocols=[OC_TestProtocol]
            ):
                def method1(self):
                    pass

            self.fail("class not implementing protocol, yet created")
        except TypeError:
            pass

        class MyClassImplementingProtocolA(NSObject, protocols=[OC_TestProtocol]):
            def method1(self):
                pass

            def method2_(self, a):
                pass

        self.assertTrue(
            MyClassImplementingProtocolA.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )

        # The PyObjC implementation of formal protocols is slightly looser
        # than Objective-C itself: you can inherit part of the protocol
        # from the superclass.
        # XXX: not really: you won't inherit the right signatures by default

        class MyClassImplementingHalfOfProtocolA(NSObject):
            def method1(self):
                pass

            method1 = objc.selector(method1, signature=b"i@:")

        self.assertFalse(
            MyClassImplementingHalfOfProtocolA.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )

        class MyClassImplementingAllOfProtocolA(
            MyClassImplementingHalfOfProtocolA, protocols=[OC_TestProtocol]
        ):
            def method2_(self, v):
                pass

        self.assertTrue(
            MyClassImplementingAllOfProtocolA.pyobjc_classMethods.conformsToProtocol_(
                OC_TestProtocol
            )
        )


class TestFormalProtocols2(TestCase):
    # Implement unittests for formal protocols here.
    #

    def testInheritedProtocol(self):
        class MyClassImplementingNSObject(
            NSObject, protocols=[objc.protocolNamed("OC_TestProtocol2")]
        ):
            def method(self):
                return 1

            @classmethod
            def classMethod(self):
                return 2

            def anotherMethod(self):
                return 4

        self.assertTrue(
            MyClassImplementingNSObject.conformsToProtocol_(
                objc.protocolNamed("OC_TestProtocol2")
            )
        )

    def testInheritedProtocol2(self):
        class MyClassImplementingNSObject2(NSObject):
            __pyobjc_protocols__ = [objc.protocolNamed("OC_TestProtocol2")]

            def method(self):
                return 1

            @classmethod
            def classMethod(self):
                return 2

            def anotherMethod(self):
                return 4

        self.assertTrue(
            MyClassImplementingNSObject2.conformsToProtocol_(
                objc.protocolNamed("OC_TestProtocol2")
            )
        )

    def testImplementAnotherObject(self):
        anObject = NSObject.alloc().init()

        try:

            class MyClassImplementingAnotherObject(NSObject, protocols=[anObject]):
                pass

            self.fail("Can create class that implements an object???")
        except TypeError:
            pass

        try:

            class MyClassImplementingAnotherObject2(NSObject, protocols=[10]):
                pass

            self.fail()
        except TypeError:
            pass

        try:

            class MyClassImplementingAnotherObject3(NSObject, protocols=[int]):
                pass

            self.fail()
        except TypeError:
            pass

    def testIncorrectlyDefiningFormalProtocols(self):
        # Some bad calls to objc.formal_protocol
        self.assertRaises(TypeError, objc.formal_protocol, [], None, ())
        self.assertRaises(TypeError, objc.formal_protocol, "supers", (NSObject,), ())
        self.assertRaises(
            TypeError,
            objc.formal_protocol,
            "supers",
            objc.protocolNamed("NSLocking"),
            (),
        )
        self.assertRaises(
            TypeError,
            objc.formal_protocol,
            "supers",
            [objc.protocolNamed("NSLocking"), "hello"],
            (),
        )
        self.assertRaises(
            TypeError,
            objc.formal_protocol,
            "supers",
            None,
            [objc.selector(None, selector=b"fooMethod:", signature=b"v@:i"), "hello"],
        )

    def testMethodInfo(self):
        self.assertEqual(
            MyProtocol3.instanceMethods(),
            [
                {"typestr": b"I@:", "required": True, "selector": b"protoMethod"},
                {
                    "typestr": b"v@:ii",
                    "required": True,
                    "selector": b"anotherProto:with:",
                },
            ],
        )
        self.assertEqual(MyProtocol3.classMethods(), [])
        self.assertEqual(
            MyProtocol3.descriptionForInstanceMethod_(b"protoMethod"),
            (b"protoMethod", b"I@:"),
        )

        self.assertEqual(
            MyProtocol3.descriptionForInstanceMethod_(b"nosuchmethod"), None
        )

        self.assertEqual(
            MyClassProtocol3.classMethods(),
            [{"required": True, "selector": b"aClassOne:", "typestr": b"@@:i"}],
        )
        self.assertEqual(MyProtocol3.classMethods(), [])
        self.assertEqual(
            MyClassProtocol3.descriptionForClassMethod_(b"aClassOne:"),
            (b"aClassOne:", b"@@:i"),
        )

        self.assertEqual(
            MyClassProtocol3.descriptionForClassMethod_(b"nosuchmethod"), None
        )
