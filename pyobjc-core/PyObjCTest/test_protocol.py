import objc
from PyObjCTest.protocol import OC_TestProtocol
from PyObjCTools.TestSupport import (
    TestCase,
    expectedFailureIf,
    os_release,
    os_level_key,
)

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
    def test_repr(self):
        v = repr(MyProto)
        self.assertRegex(v, "<objc.informal_protocol 'MyProto' at .*>")

    def test_creation_errors(self):
        with self.assertRaisesRegex(
            TypeError, r"informal_protocol\(\) argument 1 must be str, not int"
        ):
            objc.informal_protocol(42, ())

        with self.assertRaisesRegex(TypeError, r"'int' object is not iterable"):
            objc.informal_protocol("name", 42)

        with self.assertRaisesRegex(TypeError, r"Item 0 is not a selector"):
            objc.informal_protocol("name", (42,))

        with self.assertRaisesRegex(TypeError, r"Item 1 is not a selector"):
            objc.informal_protocol(
                "name",
                (
                    objc.selector(
                        None,
                        selector=b"incompleteMethod",
                        signature=b"I@:",
                        isRequired=1,
                    ),
                    42,
                ),
            )

        with self.assertRaisesRegex(TypeError, r"Item 1 is a native selector"):
            objc.informal_protocol(
                "name",
                (
                    objc.selector(
                        None,
                        selector=b"incompleteMethod",
                        signature=b"I@:",
                        isRequired=1,
                    ),
                    NSObject.pyobjc_instanceMethods.description,
                ),
            )

        with self.assertRaisesRegex(TypeError, r"Item 0 has a callable"):
            objc.informal_protocol(
                "name",
                (
                    objc.selector(
                        lambda self: 42,
                        selector=b"incompleteMethod",
                        signature=b"I@:",
                        isRequired=1,
                    ),
                ),
            )

    def testMissingProto(self):
        class ProtoClass1(NSObject):
            def testMethod(self):
                pass

        self.assertEqual(ProtoClass1.testMethod.signature, b"I@:")

    def testIncompleteClass(self):
        with self.assertRaisesRegex(
            TypeError,
            "class does not fully implemented protocol 'MyProto': "
            "no implementation for instance method 'testMethod'",
        ):

            class ProtoClass2A(NSObject, protocols=[MyProto]):
                def testMethod2_(self, x):
                    pass

        with self.assertRaisesRegex(objc.error, "^ProtoClass2A$"):
            objc.lookUpClass("ProtoClass2A")

        for cls in objc.getClassList():
            self.assertNotEqual(cls.__name__, "ProtoClass2")

    def testInvalidMethodType(self):
        with self.assertRaisesRegex(
            TypeError,
            "class does not correctly implement protocol 'MyProto': "
            "the signature for method testMethod is '@@:' instead of 'I@:'",
        ):

            class ProtoClass2(NSObject, protocols=[MyProto]):
                def testMethod2_(self, x):
                    pass

                @objc.typedSelector(b"@@:")
                def testMethod(self):
                    pass

        with self.assertRaisesRegex(objc.error, "^ProtoClass2$"):
            objc.lookUpClass("ProtoClass2")

        for cls in objc.getClassList():
            self.assertNotEqual(cls.__name__, "ProtoClass2")

    def test_cleanup_protocol(self):
        SomeProto = objc.informal_protocol(
            "SomeProto",
            (
                objc.selector(
                    None, selector=b"cleanupMethod", signature=b"I@:", isRequired=1
                ),
            ),
        )

        class ClassImplementingSomeProto1(NSObject):
            def cleanupMethod(self):
                return 1

        self.assertResultHasType(ClassImplementingSomeProto1.cleanupMethod, b"I")

        # XXX: This won't cause GC for the value due to how
        #      the bridge is implemented...
        del SomeProto

        class ClassImplementingSomeProto2(NSObject):
            def cleanupMethod(self):
                return 1

        self.assertResultHasType(ClassImplementingSomeProto2.cleanupMethod, b"I")


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

        with self.assertRaisesRegex(ValueError, "depythonifying 'SEL', got 'int'"):
            OC_TestProtocol.descriptionForInstanceMethod_(42)

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

            @classmethod
            def aClassOne_(self, a):
                pass

        self.assertEqual(ImplementingMyClassProtocol.anAnotherOne_.signature, b"i@:i")
        self.assertEqual(ImplementingMyClassProtocol.aClassOne_.isClassMethod, True)
        self.assertEqual(ImplementingMyClassProtocol.aClassOne_.signature, b"@@:i")

        # TODO: protocol with class and instance method with different
        # signatures.
        # TODO: should not need to specify classmethod() if it can be
        # deduced from the protocol

    def testIncorrectlyDefiningFormalProtocols(self):
        # Some bad calls to objc.formal_protocol
        with self.assertRaisesRegex(
            TypeError, r"formal_protocol\(\) argument 1 must be str, not list"
        ):
            objc.formal_protocol([], None, ())

        with self.assertRaisesRegex(
            TypeError, "supers need to be None or a sequence of objc.formal_protocols"
        ):
            objc.formal_protocol("supers", (NSObject,), ())

        with self.assertRaisesRegex(
            TypeError, "supers need to be None or a sequence of objc.formal_protocols"
        ):
            objc.formal_protocol("supers", objc.protocolNamed("NSLocking"), ())

        with self.assertRaisesRegex(
            TypeError, "Selectors is not a list of objc.selector instances"
        ):
            objc.formal_protocol("supers", [objc.protocolNamed("NSLocking")], "hello")

        with self.assertRaisesRegex(
            TypeError, "Selectors is not a list of objc.selector instances"
        ):
            objc.formal_protocol(
                "supers",
                [objc.protocolNamed("NSLocking")],
                [
                    objc.selector(None, selector=b"fooMethod:", signature=b"v@:i"),
                    "hello",
                ],
            )

        with self.assertRaisesRegex(
            TypeError, ".*selectors need to be a sequence of objc.selector instances"
        ):
            objc.formal_protocol("selectors", None, 42)

    @expectedFailureIf(os_level_key(os_release()) < os_level_key("10.12"))
    def testMethodInfo(self):
        # Protocol creation bug in at least 10.11
        self.assertCountEqual(
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

        with self.assertRaisesRegex(ValueError, "depythonifying 'SEL', got 'int'"):
            MyClassProtocol.descriptionForClassMethod_(42)

    def test_method_of_wrong_kind_instance(self):
        class ClassWithClassMethodBase1(NSObject):
            @classmethod
            def protoMethod(self):
                return 42

        with self.assertRaisesRegex(
            TypeError,
            "class does not fully implemented protocol 'MyProtocol': "
            "no implementation for instance method 'protoMethod'",
        ):

            class ClassWithClassMethod(
                ClassWithClassMethodBase1, protocols=[MyProtocol]
            ):
                def anotherProto_with_(self, a, b):
                    pass

    def test_method_of_wrong_kind_class(self):
        class ClassWithClassMethodBase2(NSObject):
            @objc.typedSelector(b"@@:i")
            def aClassOne_(self, a):
                return a

        self.assertIsInstance(ClassWithClassMethodBase2.aClassOne_, objc.selector)
        self.assertFalse(ClassWithClassMethodBase2.aClassOne_.isClassMethod)
        self.assertEqual(ClassWithClassMethodBase2.aClassOne_.selector, b"aClassOne:")

        with self.assertRaisesRegex(
            TypeError,
            "class does not fully implemented protocol 'MyClassProtocol': no implementation for class method 'aClassOne:'",
        ):

            class ClassWithInstanceMethod(
                ClassWithClassMethodBase2, protocols=[MyClassProtocol]
            ):
                def anAnotherOne_(self, a):
                    return a

    def test_inherit_implementation_all(self):
        class ClassWithClassMethodBase3(NSObject):
            @objc.typedSelector(b"@@:i")
            @classmethod
            def aClassOne_(self, a):
                return a

            @objc.typedSelector(b"i@:i")
            def anAnotherOne_(self, a):
                return a

        class ClassWithInstanceMethod3(
            ClassWithClassMethodBase3, protocols=[MyClassProtocol]
        ):
            pass

    def test_protocol_with_tuples(self):
        my_protocol = objc.formal_protocol(
            "NestedSelectors",
            None,
            [
                objc.selector(None, selector=b"firstMethod", signature=b"I@:"),
                (
                    objc.selector(None, selector=b"secondMethod", signature=b"Q@:"),
                    objc.selector(None, selector=b"thirdMethod", signature=b"d@:"),
                ),
            ],
        )

        self.assertCountEqual(
            my_protocol.instanceMethods(),
            [
                {"selector": b"firstMethod", "typestr": b"I@:", "required": True},
                {"selector": b"secondMethod", "typestr": b"Q@:", "required": True},
                {"selector": b"thirdMethod", "typestr": b"d@:", "required": True},
            ],
        )

        with self.assertRaisesRegex(TypeError, "Selectors is not a list of "):
            objc.formal_protocol(
                "NestedSelectors2",
                None,
                [
                    objc.selector(None, selector=b"firstMethod", signature=b"I@:"),
                    (objc.selector(None, selector=b"secondMethod", signature=b"Q@:"),),
                ],
            )

        with self.assertRaisesRegex(TypeError, "Selectors is not a list of "):
            objc.formal_protocol(
                "NestedSelectors3",
                None,
                [
                    objc.selector(None, selector=b"firstMethod", signature=b"I@:"),
                    (
                        objc.selector(None, selector=b"secondMethod", signature=b"Q@:"),
                        objc.selector(None, selector=b"thirdMethod", signature=b"Q@:"),
                        objc.selector(None, selector=b"fourthMethod", signature=b"Q@:"),
                    ),
                ],
            )

        with self.assertRaisesRegex(TypeError, "Selectors is not a list of "):
            objc.formal_protocol(
                "NestedSelectors4",
                None,
                [
                    objc.selector(None, selector=b"firstMethod", signature=b"I@:"),
                    (
                        objc.selector(None, selector=b"secondMethod", signature=b"Q@:"),
                        42,
                    ),
                ],
            )

        with self.assertRaisesRegex(TypeError, "Selectors is not a list of "):
            objc.formal_protocol(
                "NestedSelectors5",
                None,
                [
                    objc.selector(None, selector=b"firstMethod", signature=b"I@:"),
                    (
                        42,
                        objc.selector(None, selector=b"secondMethod", signature=b"Q@:"),
                    ),
                ],
            )


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

MyProtocol4 = objc.formal_protocol(
    "MyProtocol4",
    None,
    (
        objc.selector(
            None, selector=b"proto4Method", signature=b"I@:", isRequired=False
        ),
    ),
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
        # try:
        #    cls = objc.lookUpClass("MyClassImplementingNSObject")
        # except objc.error:
        #    pass
        # else:
        #    import inspect
        #    print("XXX already defined", inspect.getsourcefile(cls), isnpect.getsourcelines(cls)[-1])
        #    pass

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

    def test_inherit_with_optional(self):
        # First a class that doesn't implemented the protocol
        # method. Is OK because the method is optional
        class ImplementingProto4(NSObject, protocols=[MyProtocol4]):
            pass

        # Then a class that does implemented the protocol method,
        # which affects the type signature.
        class ImplementingProto4A(NSObject, protocols=[MyProtocol4]):
            def proto4Method(self):
                return 1

        self.assertTrue(ImplementingProto4.conformsToProtocol_(MyProtocol4))
        self.assertTrue(ImplementingProto4A.conformsToProtocol_(MyProtocol4))

        self.assertResultHasType(ImplementingProto4A.proto4Method, b"I")

    def testImplementAnotherObject(self):
        anObject = NSObject.alloc().init()

        with self.assertRaisesRegex(
            TypeError,
            "protocols list contains object that isn't an Objective-C protocol, but type NSObject",
        ):

            class MyClassImplementingAnotherObject(NSObject, protocols=[anObject]):
                pass

        with self.assertRaisesRegex(
            TypeError,
            "protocols list contains object that isn't an Objective-C protocol, but type int",
        ):

            class MyClassImplementingAnotherObject2(NSObject, protocols=[10]):
                pass

        with self.assertRaisesRegex(
            TypeError,
            "protocols list contains object that isn't an Objective-C protocol, but type type",
        ):

            class MyClassImplementingAnotherObject3(NSObject, protocols=[int]):
                pass

    def testIncorrectlyDefiningFormalProtocols(self):
        # Some bad calls to objc.formal_protocol
        with self.assertRaisesRegex(
            TypeError, r"formal_protocol\(\) argument 1 must be str, not list"
        ):
            objc.formal_protocol([], None, ())
        with self.assertRaisesRegex(
            TypeError, "supers need to be None or a sequence of objc.formal_protocols"
        ):
            objc.formal_protocol("supers", (NSObject,), ())
        with self.assertRaisesRegex(
            TypeError, "supers need to be None or a sequence of objc.formal_protocols"
        ):
            objc.formal_protocol(
                "supers",
                objc.protocolNamed("NSLocking"),
                (),
            )
        with self.assertRaisesRegex(
            TypeError, "supers need to be None or a sequence of objc.formal_protocols"
        ):
            objc.formal_protocol(
                "supers",
                [objc.protocolNamed("NSLocking"), "hello"],
                (),
            )
        with self.assertRaisesRegex(
            TypeError, "Selectors is not a list of objc.selector instances"
        ):
            objc.formal_protocol(
                "supers",
                None,
                [
                    objc.selector(None, selector=b"fooMethod:", signature=b"v@:i"),
                    "hello",
                ],
            )

    @expectedFailureIf(os_level_key(os_release()) < os_level_key("10.12"))
    def testMethodInfo(self):
        # Protocol creation bug in at least 10.11
        self.assertCountEqual(
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

    def test_protocol_methods(self):
        v = objc.protocolNamed("NSObject")
        self.assertEqual(v.name(), "NSObject")

        w = objc.protocolNamed("OC_TestProtocol2")
        self.assertEqual(w.name(), "OC_TestProtocol2")

        self.assertFalse(v.conformsTo_(w))
        self.assertTrue(v.conformsTo_(v))

        with self.assertRaisesRegex(
            TypeError, "argument 1 must be objc.formal_protocol, not int"
        ):
            v.conformsTo_(42)

        with self.assertRaisesRegex(
            TypeError, r"function takes exactly 1 argument \(2 given\)"
        ):
            v.conformsTo_(w, v)

        with self.assertRaisesRegex(
            TypeError, r"function takes exactly 1 argument \(3 given\)"
        ):
            v.conformsTo_(w, w, v)

        with self.assertRaisesRegex(
            TypeError, r"function takes exactly 1 argument \(0 given\)"
        ):
            v.conformsTo_()

    def test_protocol_subclassing_nsobject(self):
        class OC_EmptyClass(
            NSObject, protocols=[objc.protocolNamed("OC_NSObjectBased")]
        ):
            pass
