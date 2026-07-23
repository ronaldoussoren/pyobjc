import CoreFoundation
import objc
import warnings
from PyObjCTools.TestSupport import TestCase, NoObjCClass


class TestCFBag(TestCase):
    def test_creation(self):
        with self.assertRaisesRegex(TypeError, "expected 3 arguments, got 0"):
            CoreFoundation.CFBagCreate()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFBagCreate(NoObjCClass(), [1, 2], 2)

        with self.assertRaisesRegex(TypeError, "converting to a C array"):
            CoreFoundation.CFBagCreate(None, 0, 1)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            CoreFoundation.CFBagCreate(None, [1, 2], "two")

        bag = CoreFoundation.CFBagCreate(None, [1, 1, 2, 3, 4], 5)
        self.assertIsInstance(bag, CoreFoundation.CFBagRef)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, 1), 2)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, 3), 1)

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreFoundation.CFBagCreateMutable()
        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreFoundation.CFBagCreateMutable()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFBagCreateMutable(NoObjCClass(), 0)

        with self.assertRaisesRegex(
            ValueError, "depythonifying 'long long', got 'str'"
        ):
            CoreFoundation.CFBagCreateMutable(None, "none")

        bag = CoreFoundation.CFBagCreateMutable(None, 0)
        self.assertIsInstance(bag, CoreFoundation.CFBagRef)
        CoreFoundation.CFBagAddValue(bag, 9)
        CoreFoundation.CFBagAddValue(bag, 8)
        CoreFoundation.CFBagAddValue(bag, 9)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, 9), 2)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, 8), 1)

    def test_apply_function(self):
        items = []
        contexts = []

        bag = CoreFoundation.CFBagCreate(None, [1, 1, 2, 3, 4], 5)

        def func(item, context):
            items.append(item * item)
            contexts.append(context)

        CoreFoundation.CFBagApplyFunction(bag, func, 99)
        items.sort()
        self.assertEqual(items, [1, 1, 4, 9, 16])
        self.assertEqual(contexts, [99, 99, 99, 99, 99])

    def test_typeid(self):
        v = CoreFoundation.CFBagGetTypeID()
        self.assertIsInstance(v, int)

    def test_copy(self):
        bag = CoreFoundation.CFBagCreate(None, [1, 1, 2, 3, 4], 5)
        self.assertIsInstance(bag, CoreFoundation.CFBagRef)
        bag2 = CoreFoundation.CFBagCreateCopy(None, bag)
        self.assertIsInstance(bag2, CoreFoundation.CFBagRef)
        bag3 = CoreFoundation.CFBagCreateMutableCopy(None, 0, bag)
        self.assertIsInstance(bag3, CoreFoundation.CFBagRef)
        self.assertIsNot(bag3, bag)

    def test_inspect(self):
        bag = CoreFoundation.CFBagCreate(
            None, ["Hello", 42, "World", 42, "a", "a", "a"], 7
        )
        self.assertIsInstance(bag, CoreFoundation.CFBagRef)
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 7)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, "Hello"), 1)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, 42), 2)
        self.assertEqual(CoreFoundation.CFBagGetCountOfValue(bag, "a"), 3)
        self.assertTrue(CoreFoundation.CFBagContainsValue(bag, "a"))
        self.assertFalse(CoreFoundation.CFBagContainsValue(bag, "b"))

        v = CoreFoundation.CFBagGetValue(bag, "b")
        self.assertIs(v, None)
        v = CoreFoundation.CFBagGetValue(bag, "a")
        self.assertEqual(v, "a")
        exists, value = CoreFoundation.CFBagGetValueIfPresent(bag, "a", None)
        self.assertTrue(exists)
        self.assertEqual(value, "a")
        exists, value = CoreFoundation.CFBagGetValueIfPresent(bag, "b", None)
        self.assertFalse(exists)
        self.assertIs(value, None)

        with self.assertRaisesRegex(TypeError, "expected 2 arguments, got 0"):
            CoreFoundation.CFBagGetValues()

        with self.assertRaisesRegex(TypeError, "Cannot proxy"):
            CoreFoundation.CFBagGetValues(NoObjCClass(), None)

        with self.assertRaisesRegex(ValueError, "'values' must be None"):
            CoreFoundation.CFBagGetValues(bag, 42)

        values = set(CoreFoundation.CFBagGetValues(bag, None))
        expected = {"Hello", 42, "World", "a"}
        self.assertEqual(values, expected)

        with warnings.catch_warnings():
            warnings.simplefilter("error", category=DeprecationWarning)
            with self.assertRaisesRegex(
                DeprecationWarning, "leaving of the second argument is deprecated"
            ):
                CoreFoundation.CFBagGetValues(bag)

        with warnings.catch_warnings(record=True) as wrns:
            warnings.simplefilter("always", category=DeprecationWarning)
            CoreFoundation.CFBagGetValues(bag)

        with warnings.catch_warnings(record=True) as wrns:
            warnings.simplefilter("always", category=DeprecationWarning)
            with self.assertRaisesRegex(TypeError, "Cannot proxy"):
                CoreFoundation.CFBagGetValues(NoObjCClass())

        self.assertEqual(len(wrns), 1)
        self.assertEqual(wrns[0].category, DeprecationWarning)

    def test_mutation(self):
        bag = CoreFoundation.CFBagCreateMutable(None, 0)
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 0)
        CoreFoundation.CFBagAddValue(bag, "hello")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 1)
        CoreFoundation.CFBagAddValue(bag, "hello")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 2)
        CoreFoundation.CFBagReplaceValue(bag, "hello")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 2)
        CoreFoundation.CFBagReplaceValue(bag, "world")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 2)
        CoreFoundation.CFBagSetValue(bag, "world")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 3)
        CoreFoundation.CFBagSetValue(bag, "world")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 3)
        CoreFoundation.CFBagRemoveValue(bag, "hello")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 2)
        CoreFoundation.CFBagRemoveValue(bag, "hello")
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 1)
        CoreFoundation.CFBagRemoveAllValues(bag)
        self.assertEqual(CoreFoundation.CFBagGetCount(bag), 0)

    def test_functions(self):
        self.assertArgHasType(CoreFoundation.CFBagGetCountOfValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBagContainsValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBagGetValue, 1, b"@")
        self.assertResultHasType(CoreFoundation.CFBagGetValue, b"@")
        self.assertArgHasType(CoreFoundation.CFBagGetValueIfPresent, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBagGetValueIfPresent, 2, b"o^@")
        self.assertResultHasType(CoreFoundation.CFBagGetValueIfPresent, objc._C_NSBOOL)
        self.assertArgIsFunction(CoreFoundation.CFBagApplyFunction, 1, b"v@@", False)
        self.assertArgHasType(CoreFoundation.CFBagApplyFunction, 2, b"@")
        self.assertArgHasType(CoreFoundation.CFBagAddValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBagReplaceValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBagSetValue, 1, b"@")
        self.assertArgHasType(CoreFoundation.CFBagRemoveValue, 1, b"@")
