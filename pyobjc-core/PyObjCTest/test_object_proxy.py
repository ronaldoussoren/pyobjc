from PyObjCTools.TestSupport import TestCase, pyobjc_options, cast_ulonglong
from PyObjCTest.objectint import OC_ObjectInt
import copy
import objc

# XXX: Some of the tests in test_*_proxy can
#      be replaced by subclasses of the tests
#      in this file.

# XXX: Check the NSObject header files for the
#      full public API of NSObject and add tests
#      as needed.

NSOrderedAscending = -1
NSOrderedSame = 0
NSOrderedDescending = 1

NSNumber = objc.lookUpClass("NSNumber")


class SomeObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"<SomeObject a={self.a!r} b={self.b!r}>"

    def __hash__(self):
        return hash((self.a, self.b))

    def __eq__(self, other):
        if not isinstance(other, SomeObject):
            return False
        return (self.a, self.b) == (other.a, other.b)


class NoObjectiveC(str):
    # XXX: Move to utility module
    @property
    def __pyobjc_object__(self):
        raise TypeError("Cannot proxy")


class TestPythonProxy(TestCase):
    value = SomeObject(a=42, b="hello")
    different = SomeObject(a=43, b="hello")

    def test_simple_copy(self):
        result = OC_ObjectInt.copyObject_(self.value)
        self.assertEqual(result, self.value)
        self.assertIsInstance(result, type(self.value))
        self.assertIsNot(result, self.value)

    def test_simple_copy_with_zone(self):
        result = OC_ObjectInt.copyObject_withZone_(self.value, None)
        self.assertEqual(result, self.value)
        self.assertIsInstance(result, type(self.value))
        self.assertIsNot(result, self.value)

    def test_copy_without_helper(self):
        with pyobjc_options(_copy=None):
            with self.assertRaisesRegex(ValueError, "cannot copy Python objects"):
                OC_ObjectInt.copyObject_withZone_(self.value, None)

    def test_description(self):
        result = OC_ObjectInt.descriptionOf_(self.value)
        self.assertEqual(result, str(self.value))

    def test_hash(self):
        result = OC_ObjectInt.hashOf_(self.value)
        self.assertEqual(result, cast_ulonglong(hash(self.value)))

    def test_equal_trivial(self):
        result = OC_ObjectInt.object_equalTo_(self.value, self.value)
        self.assertIs(result, True)

        result = OC_ObjectInt.object_equalTo_(self.value, None)
        self.assertIs(result, False)

        result = OC_ObjectInt.object_equalTo_(self.value, self.different)
        self.assertIs(result, False)

    def test_compare_trivial(self):
        result = OC_ObjectInt.object_compareTo_(self.value, self.value)
        self.assertEqual(result, 0)

        with self.assertRaisesRegex(
            ValueError, "NSInvalidArgumentException - nil argument"
        ):
            OC_ObjectInt.object_compareTo_(self.value, None)

    # Some private NSObject methods
    def test_copyDescription(self):
        result = OC_ObjectInt.copyDescriptionOf_(self.value)
        self.assertEqual(result, str(self.value))

    def test_isNSArray(self):
        result = OC_ObjectInt.isNSArrayOf_(self.value)
        self.assertIs(result, False)

    def test_isNSDictionary(self):
        result = OC_ObjectInt.isNSDictionaryOf_(self.value)
        self.assertIs(result, False)

    def test_isNSSet(self):
        result = OC_ObjectInt.isNSSetOf_(self.value)
        self.assertIs(result, False)

    def test_isNSNumber(self):
        result = OC_ObjectInt.isNSNumberOf_(self.value)
        self.assertIs(result, False)

    def test_isNSData(self):
        result = OC_ObjectInt.isNSDataOf_(self.value)
        self.assertIs(result, False)

    def test_isNSDate(self):
        result = OC_ObjectInt.isNSDateOf_(self.value)
        self.assertIs(result, False)

    def test_isNSString(self):
        result = OC_ObjectInt.isNSStringOf_(self.value)
        self.assertIs(result, False)

    def test_isNSValue(self):
        result = OC_ObjectInt.isNSValueOf_(self.value)
        self.assertIs(result, False)


class Forwarder:
    def __init__(self):
        self.calls = []

    def voidSelector(self):
        self.calls.append(("voidSelector",))

    def idSelector(self):
        self.calls.append(("idSelector",))
        return "hello world"

    def selectorWithArg_andArg_(self, a, b):
        self.calls.append(("selectorWithArg:andArg:", a, b))
        return [a, b]


class TestPlainPythonMethods(TestCase):
    def test_call_void_selector(self):
        forwarder = Forwarder()

        result = OC_ObjectInt.voidSelectorOf_(forwarder)
        self.assertIs(result, None)

        self.assertEqual(forwarder.calls, [("voidSelector",)])

    def test_call_id_selector(self):
        forwarder = Forwarder()

        result = OC_ObjectInt.idSelectorOf_(forwarder)
        self.assertEqual(result, "hello world")

        self.assertEqual(forwarder.calls, [("idSelector",)])

    def test_call_selector_with_arguments(self):
        forwarder = Forwarder()

        result = OC_ObjectInt.selectorWithArg_andArg_of_("x", "y", forwarder)
        self.assertEqual(result, ["x", "y"])

        self.assertEqual(forwarder.calls, [("selectorWithArg:andArg:", "x", "y")])

    def test_no_such_selector(self):
        forwarder = Forwarder()

        with self.assertRaisesRegex(
            ValueError,
            "NSInvalidArgumentException - <PyObjCTest.test_object_proxy.Forwarder object at .*> does not recognize -nosuchSelector",
        ):
            OC_ObjectInt.nosuchSelectorOf_(forwarder)

    def test_not_method(self):
        value = Forwarder()
        value.attr = 42

        with self.assertRaisesRegex(
            ValueError, "NSInvalidArgumentException - <.*> does not recognize -value"
        ):
            OC_ObjectInt.invokeSelector_of_(b"value", value)

    def test_staticmethod(self):
        class Forwarder:
            @staticmethod
            def idSelector():
                return "who am I?"

        value = Forwarder()

        self.assertEqual(value.idSelector(), "who am I?")

        self.assertEqual(OC_ObjectInt.idSelectorOf_(value), "who am I?")

    def test_classmethod(self):
        class Forwarder:
            @classmethod
            def idSelector(cls):
                return "who am I?"

        value = Forwarder()

        self.assertEqual(value.idSelector(), "who am I?")

        # I don't particularly like this as this does not
        # match Objecive-C behaviour, but this behaviour has been
        # present for a very long time.
        self.assertEqual(OC_ObjectInt.idSelectorOf_(value), "who am I?")

    def test_method_with_incorrect_argcount(self):
        class Forwarder:
            def idSelector(self, arg):
                return 42

        value = Forwarder()
        with self.assertRaisesRegex(
            ValueError,
            "NSInvalidArgumentException - <.*> does not recognize -idSelector",
        ):
            OC_ObjectInt.idSelectorOf_(value)

        self.assertFalse(OC_ObjectInt.respondsToSelector_of_("idSelector", value))

    def test_no_class_method(self):
        value = object()

        m = OC_ObjectInt.methodSignatureForSelector_classOf_(
            b"selectorDoesNotExist", value
        )
        self.assertIs(m, None)

        value = NSNumber.numberWithLong_(42)
        m = OC_ObjectInt.methodSignatureForSelector_classOf_(
            b"selectorDoesNotExist", value
        )
        self.assertIs(m, None)

    def test_method_raises(self):
        class Forwarder:
            def idSelector(self):
                raise RuntimeError("go away!")

        value = Forwarder()
        with self.assertRaisesRegex(RuntimeError, "go away!"):
            value.idSelector()

        with self.assertRaisesRegex(RuntimeError, "go away!"):
            OC_ObjectInt.idSelectorOf_(value)

    def test_method_result_not_objc(self):
        class Forwarder:
            def idSelector(self):
                return NoObjectiveC()

        value = Forwarder()
        result = value.idSelector()
        self.assertIsInstance(result, NoObjectiveC)

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_ObjectInt.idSelectorOf_(value)

    def assert_typestr_similar(self, left, right):
        if left in (objc._C_CHR, objc._C_NSBOOL, objc._C_BOOL):
            if right not in (objc._C_CHR, objc._C_NSBOOL, objc._C_BOOL):
                self.fail(f"{left!r} not compatible with {right!r}")

            return

        self.assertEqual(left, right)

    def assert_method_signature(self, signature, typestr):
        parts = objc.splitSignature(typestr)
        rval = parts[0]
        args = parts[1:]

        self.assert_typestr_similar(signature.methodReturnType(), rval)
        self.assertEqual(signature.numberOfArguments(), len(args))
        for idx, arg in enumerate(args):
            self.assert_typestr_similar(signature.getArgumentTypeAtIndex_(idx), arg)

    def test_methodsignature_python(self):
        forwarder = Forwarder()

        with self.subTest("voidSelector"):
            m = OC_ObjectInt.methodSignatureForSelector_of_(b"voidSelector", forwarder)

            # For plain python objects we don't try to recognize if the method
            # implementation contains return statement with an argument.
            self.assert_method_signature(m, b"@@:")

        with self.subTest("idSelector"):
            m = OC_ObjectInt.methodSignatureForSelector_of_(b"idSelector", forwarder)
            self.assert_method_signature(m, b"@@:")

        with self.subTest("selectorWithArg:andArg:"):
            m = OC_ObjectInt.methodSignatureForSelector_of_(
                b"selectorWithArg:andArg:", forwarder
            )
            self.assert_method_signature(m, b"@@:@@")

    def test_methodsignature_objc(self):
        selectorTab = [
            (b"release", b"Vv@:"),
            (b"retain", b"@@:"),
            (b"dealloc", b"v@:"),
            (b"copy", b"@@:"),
            (b"copyWithZone:", b"@@:^{_NSZone=}"),
            (b"_copyDescription", b"@@:"),
            (b"doesNotRecognizeSelector:", b"v@::"),
            (b"respondsToSelector:", b"B@::"),
            (b"methodSignatureForSelector:", b"@@::"),
            (b"forwardInvocation:", b"v@:@"),
            (b"valueForKey:", b"@@:@"),
            (b"storedValueForKey:", b"@@:@"),
            (b"takeValue:forKey:", b"v@:@@"),
            (b"setValue:forKey:", b"v@:@@"),
            (b"takeStoredValue:forKey:", b"v@:@@"),
            (b"valuesForKeys:", b"@@:@"),
            (b"valueForKeyPath:", b"@@:@"),
            (b"takeValue:forKeyPath:", b"v@:@@"),
            (b"setValue:forKeyPath:", b"v@:@@"),
            (b"takeValuesFromDictionary:", b"v@:@"),
            (b"setValuesForKeysWithDictionary:", b"v@:@"),
            (b"unableToSetNilForKey:", b"v@:@"),
            (b"handleQueryWithUnboundKey:", b"@@:@"),
            (b"valueForUndefinedKey:", b"@@:@"),
            (b"handleTakeValue:forUnboundKey:", b"v@:@@"),
            (b"setValue:forUndefinedKey:", b"v@:@@"),
            (b"addObserver:forKeyPath:options:context:", b"v@:@@Q^v"),
            (b"removeObserver:forKeyPath:", b"v@:@@"),
            (b"hash", b"Q@:"),
            (b"isEqual:", b"B@:@"),
            (b"compare:", b"q@:@"),
            (b"encodeWithCoder:", b"v@:@"),
            (b"initWithCoder:", b"@@:@"),
            (b"awakeAfterUsingCoder:", b"@@:@"),
            (b"replacementObjectForArchiver:", b"@@:@"),
            (b"replacementObjectForPortCoder:", b"@@:@"),
            (b"replacementObjectForKeyedArchiver:", b"@@:@"),
            (b"replacementObjectForCoder:", b"@@:@"),
            (b"classForArchiver", b"#@:"),
            (b"classForCoder", b"#@:"),
            (b"classForPortCoder", b"#@:"),
            (b"isKindOfClass:", b"B@:#"),
            (b"isNSArray__", b"B@:"),
            (b"isNSDictionary__", b"B@:"),
            (b"isNSSet__", b"B@:"),
            (b"isNSNumber__", b"B@:"),
            (b"isNSData__", b"B@:"),
            (b"isNSDate__", b"B@:"),
            (b"isNSString__", b"B@:"),
            (b"isNSValue__", b"B@:"),
            (b"_cfTypeID", b"Q@:"),
        ]

        classSelectorTab = [
            (b"useStoredAccessor", b"B@:"),
            (b"accessInstanceVariablesDirectly", b"B@:"),
            (b"classForKeyedUnarchiver", b"#@:"),
            (b"classFallbacksForKeyedArchiver", b"@@:"),
        ]

        for value in [NSNumber.numberWithLong_(5), object()]:
            for selector, typestr in selectorTab:
                with self.subTest(type=type(value).__name__, selector=selector):
                    self.assertTrue(
                        OC_ObjectInt.respondsToSelector_of_(selector, value)
                    )

                    m = OC_ObjectInt.methodSignatureForSelector_of_(selector, value)
                    self.assertIsNot(m, None)
                    self.assert_method_signature(m, typestr)

            for selector, typestr in classSelectorTab:
                with self.subTest(type=type(value).__name__, selector=selector):
                    self.assertTrue(
                        OC_ObjectInt.respondsToSelector_classOf_(selector, value)
                    )

                    m = OC_ObjectInt.methodSignatureForSelector_classOf_(
                        selector, value
                    )
                    self.assertIsNot(m, None)
                    self.assert_method_signature(m, typestr)

    def test_cfTypeId(self):
        value = object()

        result = OC_ObjectInt.cfTypeIDOf_(value)
        self.assertIsInstance(result, int)

        result2 = OC_ObjectInt.directCfTypeIDOf_(value)
        self.assertIsInstance(result2, int)

        self.assertEqual(result, result2)

    def test_isKindOfClass(self):
        value = object()

        self.assertTrue(
            OC_ObjectInt.isKindOfClass_of_(objc.lookUpClass("NSProxy"), value)
        )
        self.assertTrue(
            OC_ObjectInt.isKindOfClass_of_(objc.lookUpClass("OC_PythonObject"), value)
        )
        self.assertFalse(
            OC_ObjectInt.isKindOfClass_of_(objc.lookUpClass("NSObject"), value)
        )

    def test_useStoredAccessor(self):
        value = object()

        self.assertTrue(OC_ObjectInt.useStoredAccessorForClassOf_(value))

    def test_accessInstanceVariablesDirectly(self):
        value = object()

        self.assertTrue(OC_ObjectInt.accessInstanceVariablesDirectlyForClassOf_(value))

    def test_fowarding_copy(self):
        class H:
            pass

        value = H()
        value.x = 42

        result = OC_ObjectInt.invokeCopyOf_(value)
        self.assertIsInstance(result, H)
        self.assertEqual(result.x, value.x)

    def test_fowarding_copyWithZone(self):
        class H:
            pass

        value = H()
        value.x = 42

        result = OC_ObjectInt.invokeCopyWithZoneOf_(value)
        self.assertIsInstance(result, H)
        self.assertEqual(result.x, value.x)

    def test_fowarding_description(self):
        val = object()
        result = OC_ObjectInt.invokeDescriptionOf_(val)
        self.assertEqual(result, repr(val))

    def test_fowarding_copyDescription(self):
        val = object()
        result = OC_ObjectInt.invokeCopyDescriptionOf_(val)
        self.assertEqual(result, repr(val))

    def test_fowarding_methodSignatureForSelector(self):
        value = object()
        result = OC_ObjectInt.invokeMethodSignatureForSelector_of_(
            b"description", value
        )
        result2 = OC_ObjectInt.methodSignatureForSelector_of_(b"description", value)

        self.assertEqual(result, result2)

    def test_fowarding_doesNotRecognizeSelector(self):
        value = object()

        with self.assertRaisesRegex(
            ValueError,
            "NSInvalidArgumentException - <object object at .*> does not recognize -description",
        ):
            OC_ObjectInt.invokeDoesNotRecognizeSelector_of_(b"description", value)

    def test_forwarding_hash(self):
        value = object()

        result = OC_ObjectInt.invokeHashOf_(value)
        self.assertEqual(result, cast_ulonglong(hash(value)))

    def test_forwarding_responsToSelector(self):
        class Forwarder:
            def idSelector(self):
                return 42

        value = Forwarder()
        self.assertTrue(OC_ObjectInt.invokeRespondsToSelector_of_("idSelector", value))
        self.assertFalse(
            OC_ObjectInt.invokeRespondsToSelector_of_("voidSelector", value)
        )

    def test_forwarding_classForKeyedArchiver(self):
        self.assertIs(
            OC_ObjectInt.invokeClassForKeyedArchiverOf_(object()),
            objc.lookUpClass("OC_PythonObject"),
        )

    def test_forwarding_classForArchiver(self):
        self.assertIs(
            OC_ObjectInt.invokeClassForArchiverOf_(object()),
            objc.lookUpClass("OC_PythonObject"),
        )

    def test_forwarding_classForCoder(self):
        self.assertIs(
            OC_ObjectInt.invokeClassForCoderOf_(object()),
            objc.lookUpClass("OC_PythonObject"),
        )

    def test_forwarding_classForPortCoder(self):
        self.assertIs(
            OC_ObjectInt.invokeClassForPortCoderOf_(object()),
            objc.lookUpClass("OC_PythonObject"),
        )

    def test_forwarding_replacementObjectForCoder_of_(self):
        value = object()
        self.assertIs(
            OC_ObjectInt.invokeReplacementObjectForCoder_of_(None, value), value
        )

    def test_forwarding_replacementObjectForPortCoder_of_(self):
        value = object()
        self.assertIs(
            OC_ObjectInt.invokeReplacementObjectForPortCoder_of_(None, value), value
        )

    def test_forwarding_replacementObjectForArchiver_(self):
        value = object()
        self.assertIs(
            OC_ObjectInt.invokeReplacementObjectForArchiver_of_(None, value), value
        )

    def test_forwarding_replacementObjectForKeyedArchiver_(self):
        value = object()
        self.assertIs(
            OC_ObjectInt.invokeReplacementObjectForKeyedArchiver_of_(None, value), value
        )

    # def test_forwarding_python(self):
    #     ... # This method is not needed, normal invocations get turned
    #         # into NSInvocations by the runtime.
    #         # XXX: ... except for special cases in the implmentation.


class TestPythonMisc(TestCase):
    def test_cannot_depythonify_copy(self):
        class Helper:
            def __copy__(self):
                return NoObjectiveC()

        value = Helper()
        result = copy.copy(value)
        self.assertIsInstance(result, NoObjectiveC)

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_ObjectInt.copyObject_withZone_(value, None)

    def test_copy_raises(self):
        class Helper:
            def __copy__(self):
                raise TypeError("Cannot copy this object")

        value = Helper()

        with self.assertRaisesRegex(TypeError, "Cannot copy this object"):
            copy.copy(value)

        with self.assertRaisesRegex(TypeError, "Cannot copy this object"):
            OC_ObjectInt.copyObject_withZone_(value, None)

    def test_cannot_depythonify_description(self):
        class Helper:
            def __repr__(self):
                return NoObjectiveC()

        value = Helper()
        self.assertIsInstance(repr(value), NoObjectiveC)

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            OC_ObjectInt.descriptionOf_(value)

    def test_description_raises(self):
        class Helper:
            def __repr__(self):
                raise TypeError("Cannot find repr")

        value = Helper()
        with self.assertRaisesRegex(TypeError, "Cannot find repr"):
            repr(value)

        with self.assertRaisesRegex(TypeError, "Cannot find repr"):
            OC_ObjectInt.descriptionOf_(value)

    def test_hash_unhashable(self):
        class Helper:
            __hash__ = None

        value = Helper()

        with self.assertRaises(TypeError):
            hash(value)

        result = OC_ObjectInt.hashOf_(value)
        self.assertEqual(result, cast_ulonglong(id(value)))

    def test_equal_failure(self):
        class Helper:
            def __eq__(self, other):
                raise TypeError("Cannot compare")

        value = Helper()

        with self.assertRaisesRegex(TypeError, "Cannot compare"):
            value == 42  # noqa: B015

        result = OC_ObjectInt.object_equalTo_(value, 42)
        self.assertIs(result, False)

    def test_compare_failure(self):
        class Helper:
            def __eq__(self, other):
                raise TypeError("Cannot compare")

        value = Helper()

        with self.assertRaisesRegex(TypeError, "Cannot compare"):
            OC_ObjectInt.object_compareTo_(value, 42)

    def test_compare_order(self):
        class Container:
            def __init__(self, v):
                self._v = v

            def __eq__(self, other):
                return self._v == other._v

            def __ne__(self, other):
                return self._v != other._v

            def __lt__(self, other):
                return self._v < other._v

            def __le__(self, other):
                return self._v <= other._v

            def __gt__(self, other):
                return self._v > other._v

            def __ge__(self, other):
                return self._v >= other._v

        one = Container(1)
        one_b = Container(1)
        two = Container(2)

        # Self-test for Container():

        self.assertTrue(one == one_b)
        self.assertFalse(one == two)
        self.assertFalse(one != one_b)
        self.assertTrue(one != two)

        self.assertTrue(one < two)
        self.assertTrue(one <= one)
        self.assertTrue(one <= two)

        self.assertTrue(two > one)
        self.assertTrue(two >= one)
        self.assertTrue(two >= two)

        # Actual test:

        self.assertTrue(one < two)
        result = OC_ObjectInt.object_compareTo_(one, two)
        self.assertEqual(result, NSOrderedAscending)

        self.assertTrue(one == one_b)
        result = OC_ObjectInt.object_compareTo_(one, one_b)
        self.assertEqual(result, NSOrderedSame)

        self.assertTrue(two > one)
        result = OC_ObjectInt.object_compareTo_(two, one)
        self.assertEqual(result, NSOrderedDescending)
