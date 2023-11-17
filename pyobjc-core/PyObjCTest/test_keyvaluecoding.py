# Tests for PyObjCTools.KeyValueCoding
import os

from PyObjCTools import KeyValueCoding
from PyObjCTools.TestSupport import TestCase
import objc


class TestHelpers(TestCase):
    def test_msum(self):
        self.assertEqual(KeyValueCoding.msum([1, 1e100, 1, -1e100] * 10000), 20000)
        self.assertEqual(KeyValueCoding.msum([1.0, 2.0, 3.0, 4.0]), 10.0)

    def test_keyCaps(self):
        self.assertEqual(KeyValueCoding.keyCaps("attr"), "Attr")
        self.assertEqual(KeyValueCoding.keyCaps("Attr"), "Attr")
        self.assertEqual(KeyValueCoding.keyCaps("AttR"), "AttR")
        self.assertEqual(KeyValueCoding.keyCaps("attr_with_value"), "Attr_with_value")

        self.assertEqual(KeyValueCoding.keyCaps(b"attr"), b"Attr")
        self.assertEqual(KeyValueCoding.keyCaps(b"Attr"), b"Attr")
        self.assertEqual(KeyValueCoding.keyCaps(b"AttR"), b"AttR")
        self.assertEqual(KeyValueCoding.keyCaps(b"attr_with_value"), b"Attr_with_value")


class TestArrayOperators(TestCase):
    def test_unknown_function(self):
        values = [{"a": 1}]

        with self.assertRaisesRegex(
            KeyError, "Array operator @nofunction not implemented"
        ):
            KeyValueCoding.getKeyPath(values, "@nofunction.a")

    def test_sum(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        values = [{"a": 1}, {"a": 2, "b": 4}, {"a": 3, "b": 2}, {"a": 4}]
        self.assertEqual(arrayOperators.sum(values, "a"), 10)
        self.assertEqual(arrayOperators.sum(values, "b"), 6)
        self.assertEqual(arrayOperators.sum(values, "c"), 0)
        self.assertEqual(arrayOperators.sum([], "b"), 0)
        with self.assertRaisesRegex(KeyError, ""):
            arrayOperators.sum([], ())  # XXX

        self.assertEqual(KeyValueCoding.getKeyPath(values, "@sum.a"), 10)
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@sum.b"), 6)
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@sum.c"), 0)

    def test_avg(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        values = [{"a": 1}, {"a": 2, "b": 4}, {"a": 3, "b": 2}, {"a": 4}]
        self.assertEqual(arrayOperators.avg(values, "a"), 2.5)
        self.assertEqual(arrayOperators.avg(values, "b"), 1.5)
        self.assertEqual(arrayOperators.avg(values, "c"), 0)
        self.assertEqual(arrayOperators.avg([], "b"), 0)
        with self.assertRaisesRegex(KeyError, ""):
            arrayOperators.avg([], ())  # XXX

        self.assertEqual(KeyValueCoding.getKeyPath(values, "@avg.a"), 2.5)
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@avg.b"), 1.5)
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@avg.c"), 0)

    def test_count(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        values = [{"a": 1}, {"a": 2, "b": 4}, {"a": 3, "b": 2}, {"a": 4}]
        self.assertEqual(arrayOperators.count(values, "a"), len(values))
        self.assertEqual(arrayOperators.count(values, "b"), len(values))
        self.assertEqual(arrayOperators.count(values, ()), len(values))
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@count"), len(values))
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@count.a"), len(values))

    def test_max(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        values = [{"a": 1}, {"a": 2, "b": 5}, {"a": 3, "b": 2}, {"a": 4}]
        self.assertEqual(arrayOperators.max(values, "a"), 4)
        self.assertEqual(arrayOperators.max(values, "b"), 5)
        with self.assertRaisesRegex(KeyError, ""):
            arrayOperators.max(values, ())  # XXX
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@max.a"), 4)

    def test_min(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        values = [{"a": 1}, {"a": 2, "b": 5}, {"a": 3, "b": 2}, {"a": 4}]
        self.assertEqual(arrayOperators.min(values, "a"), 1)
        self.assertEqual(arrayOperators.min(values, "b"), 2)
        with self.assertRaisesRegex(KeyError, ""):
            arrayOperators.min(values, ())  # XXX
        self.assertEqual(KeyValueCoding.getKeyPath(values, "@min.a"), 1)

    def test_unionOfObjects(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        values = [{"a": {"b": 1}}, {"a": {"b": 1}}, {"a": {"b": 2}}, {"a": {"b": 3}}]

        self.assertEqual(
            arrayOperators.unionOfObjects(values, ("a", "b")), [1, 1, 2, 3]
        )
        self.assertEqual(
            KeyValueCoding.getKeyPath(values, "@unionOfObjects.a.b"), [1, 1, 2, 3]
        )

        values.append({"a": {}})
        with self.assertRaisesRegex(KeyError, "Key b does not exist"):
            arrayOperators.unionOfObjects(values, ("a", "b"))

    def test_distinctUnionOfObjects(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        class Int:
            def __init__(self, value):
                self._value = value

            def __repr__(self):
                return "Int(%r)" % (self._value)

            def __eq__(self, other):
                if isinstance(other, int):
                    return self._value == other

                elif isinstance(other, Int):
                    return self._value == other._value

                else:
                    return False

            def __hash__(self):
                raise TypeError

        values = [
            {"a": {"b": 1}},
            {"a": {"b": Int(1)}},
            {"a": {"b": 2}},
            {"a": {"b": Int(3)}},
            {"a": {"b": Int(3)}},
        ]

        self.assertEqual(
            arrayOperators.distinctUnionOfObjects(values, ("a", "b")), [1, 2, 3]
        )
        self.assertEqual(
            KeyValueCoding.getKeyPath(values, "@distinctUnionOfObjects.a.b"), [1, 2, 3]
        )

        values.append({"a": {}})
        with self.assertRaisesRegex(KeyError, "Key b does not exist"):
            arrayOperators.distinctUnionOfObjects(values, ("a", "b"))
        with self.assertRaisesRegex(KeyError, "Key b does not exist"):
            KeyValueCoding.getKeyPath(values, "@distinctUnionOfObjects.a.b")

        class Rec:
            def __init__(self, b):
                self.b = b

            def __eq__(self, other):
                return type(self) is type(other) and self.b == other.b

            def __hash__(self):
                raise TypeError

        values = [{"a": Rec(1)}, {"a": Rec(1)}, {"a": Rec(2)}, {"a": Rec(3)}]
        self.assertEqual(
            arrayOperators.distinctUnionOfObjects(values, ("a", "b")), [1, 2, 3]
        )

    def test_unionOfArrays(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        class Rec:
            def __init__(self, **kwds):
                for k, v in kwds.items():
                    setattr(self, k, v)

            def __eq__(self, other):
                return type(self) is type(other) and self.__dict__ == other.__dict__

            def __hash__(self):
                raise TypeError

        class Str:
            def __init__(self, value):
                self._value = value

            def __repr__(self):
                return "Str(%r)" % (self._value)

            def __eq__(self, other):
                if isinstance(other, str):
                    return self._value == other

                elif isinstance(other, Str):
                    return self._value == other._value

                else:
                    return False

            def __hash__(self):
                raise TypeError

        transactions = [
            [
                {"payee": "Green Power", "amount": 120.0},
                {"payee": "Green Power", "amount": 150.0},
                {"payee": Str("Green Power"), "amount": 170.0},
                Rec(payee="Car Loan", amount=250.0),
                {"payee": "Car Loan", "amount": 250.0},
                {"payee": "Car Loan", "amount": 250.0},
                {"payee": Str("General Cable"), "amount": 120.0},
                {"payee": "General Cable", "amount": 155.0},
                Rec(payee="General Cable", amount=120.0),
                {"payee": "Mortgage", "amount": 1250.0},
                {"payee": "Mortgage", "amount": 1250.0},
                {"payee": "Mortgage", "amount": 1250.0},
                {"payee": "Animal Hospital", "amount": 600.0},
            ],
            [
                {"payee": "General Cable - Cottage", "amount": 120.0},
                {"payee": "General Cable - Cottage", "amount": 155.0},
                Rec(payee="General Cable - Cottage", amount=120.0),
                {"payee": "Second Mortgage", "amount": 1250.0},
                {"payee": "Second Mortgage", "amount": 1250.0},
                {"payee": Str("Second Mortgage"), "amount": 1250.0},
                {"payee": "Hobby Shop", "amount": 600.0},
            ],
        ]

        self.assertEqual(
            arrayOperators.distinctUnionOfArrays(transactions, ("payee",)),
            [
                "Green Power",
                "Car Loan",
                "General Cable",
                "Mortgage",
                "Animal Hospital",
                "General Cable - Cottage",
                "Second Mortgage",
                "Hobby Shop",
            ],
        )
        self.assertEqual(
            KeyValueCoding.getKeyPath(transactions, "@distinctUnionOfArrays.payee"),
            [
                "Green Power",
                "Car Loan",
                "General Cable",
                "Mortgage",
                "Animal Hospital",
                "General Cable - Cottage",
                "Second Mortgage",
                "Hobby Shop",
            ],
        )
        self.assertEqual(
            arrayOperators.unionOfArrays(transactions, ("payee",)),
            [
                "Green Power",
                "Green Power",
                "Green Power",
                "Car Loan",
                "Car Loan",
                "Car Loan",
                "General Cable",
                "General Cable",
                "General Cable",
                "Mortgage",
                "Mortgage",
                "Mortgage",
                "Animal Hospital",
                "General Cable - Cottage",
                "General Cable - Cottage",
                "General Cable - Cottage",
                "Second Mortgage",
                "Second Mortgage",
                "Second Mortgage",
                "Hobby Shop",
            ],
        )
        self.assertEqual(
            KeyValueCoding.getKeyPath(transactions, "@unionOfArrays.payee"),
            [
                "Green Power",
                "Green Power",
                "Green Power",
                "Car Loan",
                "Car Loan",
                "Car Loan",
                "General Cable",
                "General Cable",
                "General Cable",
                "Mortgage",
                "Mortgage",
                "Mortgage",
                "Animal Hospital",
                "General Cable - Cottage",
                "General Cable - Cottage",
                "General Cable - Cottage",
                "Second Mortgage",
                "Second Mortgage",
                "Second Mortgage",
                "Hobby Shop",
            ],
        )

        with self.assertRaisesRegex(KeyError, "Key d does not exist"):
            arrayOperators.unionOfArrays(transactions, "date")
        with self.assertRaisesRegex(KeyError, "Key d does not exist"):
            arrayOperators.distinctUnionOfArrays(transactions, "date")

    def test_unionOfArrays_variations(self):
        lst = [[{"a": 1}, {"a": 2}, {"a": 1}, {"a": 3}, {"a": 2}]]

        arrayOperators = KeyValueCoding._ArrayOperators
        self.assertEqual(arrayOperators.distinctUnionOfArrays(lst, "a"), [1, 2, 3])

        lst = [[{"a": [1]}, {"a": [2]}, {"a": [1]}], [{"a": 3}, {"a": [2]}]]

        arrayOperators = KeyValueCoding._ArrayOperators
        self.assertEqual(arrayOperators.distinctUnionOfArrays(lst, "a"), [[1], [2], 3])

    def testUnionOfSets(self):
        arrayOperators = KeyValueCoding._ArrayOperators

        class Rec:
            def __init__(self, n):
                self.n = n

            def __eq__(self, other):
                return self.n == other.n

            def __hash__(self):
                return hash(self.n)

        values = {frozenset({Rec(1), Rec(1), Rec(2)}), frozenset({Rec(1), Rec(3)})}

        self.assertEqual(arrayOperators.distinctUnionOfSets(values, "n"), {1, 2, 3})


null = objc.lookUpClass("NSNull").null()


class TestPythonObject(TestCase):
    def test_dict_get(self):
        d = {"a": 1}
        self.assertEqual(KeyValueCoding.getKey(d, "a"), 1)
        with self.assertRaisesRegex(KeyError, "Key b does not exist"):
            KeyValueCoding.getKey(d, "b")

    def test_array_get(self):
        lst = [{"a": 1, "b": 2}, {"a": 2}]
        self.assertEqual(KeyValueCoding.getKey(lst, "a"), [1, 2])
        self.assertEqual(KeyValueCoding.getKey(lst, "b"), [2, null])

    def test_attr_get(self):
        class Record:
            __slots__ = ("slot1", "__dict__")

            def __init__(self, **kwds):
                for k, v in kwds.items():
                    setattr(self, k, v)

            @property
            def prop1(self):
                return "a property"

        r = Record(slot1=42, attr1="a")

        self.assertEqual(KeyValueCoding.getKey(r, "slot1"), 42)
        self.assertEqual(KeyValueCoding.getKey(r, "attr1"), "a")
        self.assertEqual(KeyValueCoding.getKey(r, "prop1"), "a property")
        self.assertEqual(KeyValueCoding.getKeyPath(r, "slot1"), 42)
        self.assertEqual(KeyValueCoding.getKeyPath(r, "attr1"), "a")
        self.assertEqual(KeyValueCoding.getKeyPath(r, "prop1"), "a property")

        r = Record(attr1=Record(attr2="b", attr3=[Record(a=1), Record(a=2, b="b")]))
        with self.assertRaisesRegex(KeyError, "Key slot1 does not exist"):
            KeyValueCoding.getKey(r, "slot1")
        with self.assertRaisesRegex(KeyError, "Key attr99 does not exist"):
            KeyValueCoding.getKey(r, "attr99")
        with self.assertRaisesRegex(KeyError, "Key slot1 does not exist"):
            KeyValueCoding.getKeyPath(r, "slot1")
        with self.assertRaisesRegex(KeyError, "Key attr99 does not exist"):
            KeyValueCoding.getKeyPath(r, "attr99")

        self.assertEqual(KeyValueCoding.getKeyPath(r, "attr1.attr2"), "b")
        self.assertEqual(KeyValueCoding.getKeyPath(r, "attr1.attr3.a"), [1, 2])
        self.assertEqual(KeyValueCoding.getKeyPath(r, "attr1.attr3.b"), [null, "b"])
        with self.assertRaisesRegex(KeyError, "Key attr3 does not exist"):
            KeyValueCoding.getKeyPath(r, "attr3")
        with self.assertRaisesRegex(KeyError, "Key attr9 does not exist"):
            KeyValueCoding.getKeyPath(r, "attr1.attr9")

    def test_cocoa_get(self):
        r = objc.lookUpClass("NSObject").alloc().init()
        self.assertEqual(KeyValueCoding.getKey(r, "description"), r.description())
        self.assertEqual(KeyValueCoding.getKeyPath(r, "description"), r.description())
        self.assertEqual(
            KeyValueCoding.getKeyPath(r, "description.length"), len(r.description())
        )
        with self.assertRaisesRegex(
            KeyError,
            r"NSUnknownKeyException - \[.*\]: this class is not key value coding-compliant for the key nosuchattr.",
        ):
            KeyValueCoding.getKey(r, "nosuchattr")
        with self.assertRaisesRegex(
            KeyError,
            r"NSUnknownKeyException - \[.*\]: this class is not key value coding-compliant for the key nosuchattr.",
        ):
            KeyValueCoding.getKeyPath(r, "description.nosuchattr")

    def test_accessor_get(self):
        class Object:
            def get_attr1(self):
                return "attr1"

            def getAttr1(self):
                return "Attr1"

            def attr1(self):
                return ".attr1"

            def get_attr2(self):
                return "attr2"

            def attr2(self):
                return ".attr2"

            def attr3(self):
                return ".attr3"

            def isAttr4(self):
                return "attr4?"

            @objc.selector
            def attrsel(self):
                return "selattr"

        r = Object()
        self.assertEqual(KeyValueCoding.getKey(r, "attr1"), "Attr1")
        self.assertEqual(KeyValueCoding.getKey(r, "attr2"), "attr2")
        self.assertEqual(KeyValueCoding.getKey(r, "attr3"), ".attr3")
        self.assertEqual(KeyValueCoding.getKey(r, "attr4"), "attr4?")
        self.assertEqual(KeyValueCoding.getKey(r, "attrsel"), "selattr")

        t = Object()
        o = objc.lookUpClass("NSObject").alloc().init()
        lst = []

        r.attr5 = t.isAttr4
        r.attr6 = o.description
        r.attr7 = lst.__len__
        r.attr8 = os.getpid
        r.attr9 = "attribute 9"

        self.assertEqual(KeyValueCoding.getKey(r, "attr5"), t.isAttr4)
        self.assertEqual(KeyValueCoding.getKey(r, "attr6"), r.attr6)
        self.assertEqual(KeyValueCoding.getKey(r, "attr7"), lst.__len__)
        self.assertEqual(KeyValueCoding.getKey(r, "attr8"), os.getpid())
        self.assertEqual(KeyValueCoding.getKey(r, "attr9"), "attribute 9")
        self.assertEqual(KeyValueCoding.getKey(1.5, "hex"), (1.5).hex())

    def test_none_get(self):
        self.assertEqual(KeyValueCoding.getKey(None, "a"), None)
        self.assertEqual(KeyValueCoding.getKeyPath(None, "a"), None)

    def test_none_set(self):
        # setKey(None, 'any', 'value') is documented as a no-op
        # check that this doesn't raise an exception.
        v = None
        KeyValueCoding.setKey(v, "a", 42)
        KeyValueCoding.setKeyPath(v, "a", 42)

    def test_dict_set(self):
        v = {"a": 42, "c": {}}

        KeyValueCoding.setKey(v, "a", 43)
        KeyValueCoding.setKey(v, "b", "B")
        self.assertEqual(v, {"a": 43, "b": "B", "c": {}})

        KeyValueCoding.setKeyPath(v, "a", 44)
        KeyValueCoding.setKeyPath(v, "b", "C")
        KeyValueCoding.setKeyPath(v, "c.a", "A")
        self.assertEqual(v, {"a": 44, "b": "C", "c": {"a": "A"}})

    def test_attr_set(self):
        class R:
            @property
            def attr3(self):
                return self._attr3

            @attr3.setter
            def attr3(self, v):
                self._attr3 = v * 2

            @property
            def attr4(self):
                return self._attr4

            def attr6(self):
                return self._attr6

        r = R()
        r._attr1 = 42
        r._attr4 = 43
        r.attr5 = {}
        r._attr6 = 9

        KeyValueCoding.setKey(r, "attr1", 1)
        KeyValueCoding.setKey(r, "attr2", 2)
        KeyValueCoding.setKey(r, "attr3", 3)
        with self.assertRaisesRegex(KeyError, "Key attr4 does not exist"):
            KeyValueCoding.setKey(r, "attr4", 4)
        KeyValueCoding.setKey(r, "attr6", 7)

        self.assertEqual(r._attr1, 1)
        self.assertEqual(r.attr2, 2)
        self.assertEqual(r.attr3, 6)
        self.assertEqual(r._attr3, 6)
        self.assertEqual(r._attr6, 7)

        KeyValueCoding.setKeyPath(r, "attr1", "one")
        KeyValueCoding.setKeyPath(r, "attr2", "two")
        KeyValueCoding.setKeyPath(r, "attr3", "three")
        KeyValueCoding.setKeyPath(r, "attr5.sub1", 3)
        KeyValueCoding.setKeyPath(r, "attr6", "seven")

        self.assertEqual(r._attr1, "one")
        self.assertEqual(r.attr2, "two")
        self.assertEqual(r.attr3, "threethree")
        self.assertEqual(r._attr3, "threethree")
        self.assertEqual(r.attr5, {"sub1": 3})
        self.assertEqual(r._attr6, "seven")

    def test_cocoa_set(self):
        o = objc.lookUpClass("NSMutableDictionary").alloc().init()
        KeyValueCoding.setKey(o, "attr", "value")
        self.assertEqual(o, {"attr": "value"})

        KeyValueCoding.setKeyPath(o, "attr", "value2")
        self.assertEqual(o, {"attr": "value2"})

        o = objc.lookUpClass("NSObject").alloc().init()
        with self.assertRaisesRegex(
            KeyError,
            r"NSUnknownKeyException - \[.*\]: this class is not key value coding-compliant for the key description.",
        ):
            KeyValueCoding.setKey(o, "description", "hello")
        with self.assertRaisesRegex(
            KeyError,
            r"NSUnknownKeyException - \[.*\]: this class is not key value coding-compliant for the key description.",
        ):
            KeyValueCoding.setKeyPath(o, "description", "hello")

    def test_accessor(self):
        class Record:
            def __init__(self):
                self._attr1 = 1
                self._attr2 = 2
                self._attr3 = 3

            def attr1(self):
                return self._attr1

            def setAttr1_(self, value):
                self._attr1 = (1, value)

            def setAttr1(self, value):
                self._attr1 = (2, value)

            def set_attr1(self, value):
                self._attr1 = (3, value)

            def setAttr2(self, value):
                self._attr2 = (2, value)

            def set_attr2(self, value):
                self._attr2 = (3, value)

            def set_attr3(self, value):
                self._attr3 = (3, value)

            set_no_attr = 4

        o = Record()
        self.assertEqual(o._attr1, 1)
        self.assertEqual(o._attr2, 2)
        self.assertEqual(o._attr3, 3)
        self.assertEqual(o.set_no_attr, 4)

        KeyValueCoding.setKey(o, "attr1", 9)
        KeyValueCoding.setKey(o, "attr2", 10)
        KeyValueCoding.setKey(o, "attr3", 11)
        KeyValueCoding.setKey(o, "no_attr", 12)

        self.assertEqual(o._attr1, (1, 9))
        self.assertEqual(o._attr2, (2, 10))
        self.assertEqual(o._attr3, (3, 11))
        self.assertEqual(o.no_attr, 12)

        KeyValueCoding.setKeyPath(o, "attr1", 29)
        KeyValueCoding.setKeyPath(o, "attr2", 210)
        KeyValueCoding.setKeyPath(o, "attr3", 211)

        self.assertEqual(o._attr1, (1, 29))
        self.assertEqual(o._attr2, (2, 210))
        self.assertEqual(o._attr3, (3, 211))

        o._attr1 = {"a": "b"}
        KeyValueCoding.setKeyPath(o, "attr1.a", 30)
        self.assertEqual(o._attr1, {"a": 30})

    def testMixedGraph(self):
        arr = objc.lookUpClass("NSMutableArray").alloc().init()
        d1 = objc.lookUpClass("NSMutableDictionary").alloc().init()
        d2 = objc.lookUpClass("NSMutableDictionary").alloc().init()
        d3 = {}

        root = {"a": arr, "d": d2}

        arr.addObject_(d1)
        arr.addObject_(d3)
        d1["k"] = 1
        d3["k"] = 2

        KeyValueCoding.setKeyPath(root, "d.a", "the letter A")
        self.assertEqual(d2, {"a": "the letter A"})

        self.assertEqual(KeyValueCoding.getKeyPath(root, "d.a"), "the letter A")
        self.assertEqual(KeyValueCoding.getKeyPath(arr, "k"), [1, 2])
        self.assertEqual(KeyValueCoding.getKeyPath(root, "a.k"), [1, 2])

    def testMixedGraph2(self):
        arr = objc.lookUpClass("NSMutableArray").alloc().init()
        d1 = objc.lookUpClass("NSMutableDictionary").alloc().init()
        d2 = objc.lookUpClass("NSMutableDictionary").alloc().init()
        d3 = {}

        root = objc.lookUpClass("NSMutableDictionary").dictionaryWithDictionary_(
            {"a": arr, "d": d2}
        )

        arr.addObject_(d1)
        arr.addObject_(d3)
        d1["k"] = 1
        d3["k"] = 2

        KeyValueCoding.setKeyPath(root, "d.a", "the letter A")
        self.assertEqual(d2, {"a": "the letter A"})

        self.assertEqual(KeyValueCoding.getKeyPath(root, "d.a"), "the letter A")
        self.assertEqual(KeyValueCoding.getKeyPath(arr, "k"), [1, 2])
        self.assertEqual(KeyValueCoding.getKeyPath(root, "a.k"), [1, 2])


class TestKVCHelper(TestCase):
    def setUp(self):
        self._orig = {
            "getKey": KeyValueCoding.getKey,
            "setKey": KeyValueCoding.setKey,
            "getKeyPath": KeyValueCoding.getKeyPath,
            "setKeyPath": KeyValueCoding.setKeyPath,
        }
        self._trace = []

        def getKey(obj, k):
            self._trace.append(("get", obj, k))

        def setKey(obj, k, v):
            self._trace.append(("set", obj, k, v))

        def getKeyPath(obj, k):
            self._trace.append(("get-path", obj, k))

        def setKeyPath(obj, k, v):
            self._trace.append(("set-path", obj, k, v))

        KeyValueCoding.getKey = getKey
        KeyValueCoding.setKey = setKey
        KeyValueCoding.getKeyPath = getKeyPath
        KeyValueCoding.setKeyPath = setKeyPath

    def tearDown(self):
        for k in self._orig:
            setattr(KeyValueCoding, k, self._orig[k])

    def test_repr(self):
        for o in [object(), 42, "42", b"42"]:
            self.assertEqual(repr(KeyValueCoding.kvc(o)), repr(o))

    def test_attribute_access(self):
        v = object()
        o = KeyValueCoding.kvc(v)
        o.key
        o.key2
        getattr(o, "key3.key4")
        self.assertEqual(
            self._trace,
            [("get", v, "key"), ("get", v, "key2"), ("get", v, "key3.key4")],
        )
        self._trace[:] = []

        o.key = 42
        setattr(o, "key3.key4", 99)
        self.assertEqual(
            self._trace, [("set", v, "key", 42), ("set", v, "key3.key4", 99)]
        )
        self._trace[:] = []

        class Object:
            pass

        v = Object()
        o = KeyValueCoding.kvc(v)
        o.key = 42
        o._key = 99
        self.assertEqual(self._trace, [("set", v, "key", 42)])
        self.assertEqual(o._key, 99)
        self.assertIn("_key", o.__dict__)
        self.assertNotIn("key", o.__dict__)

    def test_item_access(self):
        v = object()
        o = KeyValueCoding.kvc(v)
        o["key"]
        o["key2"]
        o["key3.key4"]
        self.assertEqual(
            self._trace,
            [
                ("get-path", v, "key"),
                ("get-path", v, "key2"),
                ("get-path", v, "key3.key4"),
            ],
        )
        self._trace[:] = []

        o["key"] = 42
        o["key3.key4"] = 99
        self.assertEqual(
            self._trace, [("set-path", v, "key", 42), ("set-path", v, "key3.key4", 99)]
        )
        self._trace[:] = []

        with self.assertRaisesRegex(TypeError, "Keys must be strings"):
            o[42]
        with self.assertRaisesRegex(TypeError, "Keys must be strings"):
            o[42] = 99
