"""
XXX: Add tests that check that the type actually works as expected:

* Use struct value as method argument
* Return struct value from a method

Add tests for nested structs as well (that is assert that NSRect.location is
an NSPoint, but using our own types)
"""
import sys
import warnings

import objc
import pickle
import textwrap
from PyObjCTest.fnd import NSObject
from PyObjCTest.structs import OC_StructTest
from PyObjCTools.TestSupport import (
    TestCase,
    pyobjc_options,
    expectedFailure,
    min_python_release,
)

PTR_SIZE = 8

# Used in the pickle test, and therefore needs a fully qualified name
GlobalType = objc.createStructType(
    "PyObjCTest.test_structs.GlobalType", b"{_GlobalType=ff}", ["a", "b"]
)


class TestStructs(TestCase):
    def testCreateExplicit(self):
        tp = objc.createStructType(
            "FooStruct", b"{_FooStruct=ffff}", ["a", "b", "c", "d"]
        )
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_FooStruct=ffff}")

        self.assertEqual(tp._fields, ("a", "b", "c", "d"))

        if sys.version_info[:2] >= (3, 10):
            self.assertEqual(tp.__match_args__, ("a", "b", "c", "d"))

        o = tp()
        self.assertHasAttr(o, "a")
        self.assertHasAttr(o, "b")
        self.assertHasAttr(o, "c")
        self.assertHasAttr(o, "d")

        with warnings.catch_warnings(record=True):
            self.assertEqual(len(o), 4)

        self.assertHasAttr(objc.ivar, "FooStruct")
        v = objc.ivar.FooStruct()
        self.assertIsInstance(v, objc.ivar)
        self.assertEqual(v.__typestr__, tp.__typestr__)

        self.assertIsSubclass(tp, objc._structwrapper)

    def testNamedTupleAPI(self):
        Point = objc.createStructType("OCPoint", b"{_OCPoint=dd}", ["x", "y"])
        Line = objc.createStructType(
            "OCLine",
            b"{_OCLine={_OCPoint=dd}{_OCPoint=dd}}d",
            ["start", "stop", "width"],
        )

        self.assertEqual(Point._fields, ("x", "y"))
        self.assertEqual(Line._fields, ("start", "stop", "width"))

        p = Point(3, 4)
        self.assertEqual(p.x, 3.0)
        self.assertEqual(p.y, 4.0)

        self.assertEqual(p._asdict(), {"x": 3.0, "y": 4.0})

        with self.assertRaisesRegex(
            TypeError, "_replace called with positional arguments"
        ):
            p._replace(42)

        with self.assertRaisesRegex(
            AttributeError, "OCPoint' object has no attribute 'invalid'"
        ):
            p._replace(invalid=9)

        p2 = p._replace(y=5)
        self.assertEqual(p.x, 3.0)
        self.assertEqual(p.y, 4.0)
        self.assertEqual(p2.x, 3.0)
        self.assertEqual(p2.y, 5)

        ln = Line(Point(1, 2), Point(8, 9), 7)
        self.assertEqual(ln.start.x, 1.0)
        self.assertEqual(ln.start.y, 2.0)
        self.assertEqual(ln.stop.x, 8.0)
        self.assertEqual(ln.stop.y, 9.0)
        self.assertEqual(ln.width, 7.0)

        self.assertEqual(
            ln._asdict(), {"start": Point(1, 2), "stop": Point(8, 9), "width": 7.0}
        )

        ln2 = ln._replace(stop=Point(3, 4), width=0.5)
        self.assertEqual(ln.start.x, 1.0)
        self.assertEqual(ln.start.y, 2.0)
        self.assertEqual(ln.stop.x, 8.0)
        self.assertEqual(ln.stop.y, 9.0)
        self.assertEqual(ln.width, 7.0)

        self.assertEqual(ln2.start.x, 1.0)
        self.assertEqual(ln2.start.y, 2.0)
        self.assertEqual(ln2.stop.x, 3.0)
        self.assertEqual(ln2.stop.y, 4.0)
        self.assertEqual(ln2.width, 0.5)

    def testCreateImplicit(self):
        tp = objc.createStructType("BarStruct", b'{_BarStruct="e"f"f"f"g"f"h"f}', None)
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_BarStruct=ffff}")

        o = tp()
        self.assertHasAttr(o, "e")
        self.assertHasAttr(o, "f")
        self.assertHasAttr(o, "g")
        self.assertHasAttr(o, "h")

        self.assertEqual(tp._fields, ("e", "f", "g", "h"))

        with self.assertRaisesRegex(
            ValueError, "invalid signature: not all fields have an embedded name"
        ):
            objc.createStructType("Foo2", b'{_Foo=f"a"}', None)
        with self.assertRaisesRegex(
            ValueError, "invalid signature: not a complete struct encoding"
        ):
            objc.createStructType("Foo3", b'{_Foo="a"f', None)  # XX
        with self.assertRaisesRegex(
            ValueError, "invalid signature: not a struct encoding"
        ):
            objc.createStructType("Foo4", b'^{_Foo="a"f}', None)

    def testPointerFields(self):
        # Note: the created type won't be all that useful unless the pointer
        # happens to be something that PyObjC knows how to deal with, this is
        # more a check to see if createStructType knows how to cope with
        # non-trivial types.
        tp = objc.createStructType(
            "XBarStruct", b'{_XBarStruct="e"^f"f"^f"g"^@"h"f}', None
        )
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_XBarStruct=^f^f^@f}")

        o = tp()
        self.assertHasAttr(o, "e")
        self.assertHasAttr(o, "f")
        self.assertHasAttr(o, "g")
        self.assertHasAttr(o, "h")

    def testEmbeddedFields(self):
        with pyobjc_options(structs_indexable=False):
            tp = objc.createStructType(
                "BarStruct", b'{FooStruct="first"i"second"i}', None
            )

            v = OC_StructTest.createWithFirst_andSecond_(1, 2)
            self.assertIsInstance(v, tp)

            x = OC_StructTest.sumFields_(v)
            self.assertEqual(x, v.first + v.second)
            self.assertEqual(v.first, 1)
            self.assertEqual(v.second, 2)

            self.assertHasAttr(objc.ivar, "BarStruct")
            v = objc.ivar.BarStruct()
            self.assertEqual(v.__typestr__, b"{FooStruct=ii}")

    def testStructCallback(self):
        """
        Regression test for an issue reported on the PyObjC mailinglist.
        """
        with pyobjc_options(structs_indexable=False):
            tp = objc.createStructType(
                "FooStruct", b'{FooStruct="first"i"second"i}', None
            )

            StructArrayDelegate = objc.informal_protocol(
                "StructArrayDelegate",
                [
                    objc.selector(
                        None, b"arrayOf4Structs:", signature=b"@@:[4{FooStruct=ii}]"
                    )
                ],
            )
            self.assertIsInstance(StructArrayDelegate, objc.informal_protocol)

            class OC_PyStruct(NSObject):
                def arrayOf4Structs_(self, value):
                    return value

            self.assertEqual(
                OC_PyStruct.arrayOf4Structs_.signature,
                b"@@:[4{FooStruct=" + objc._C_INT + objc._C_INT + b"}]",
            )

            o = OC_PyStruct.alloc().init()
            v = OC_StructTest.callArrayOf4Structs_(o)
            self.assertEqual(len(v), 4)
            for i in range(3):
                self.assertIsInstance(v[i], tp)

            self.assertEqual(v[0], tp(1, 2))
            self.assertEqual(v[1], tp(3, 4))
            self.assertEqual(v[2], tp(5, 6))
            self.assertEqual(v[3], tp(7, 8))

    def testStructSize(self):
        tp0 = objc.createStructType("FooStruct", b"{FooStruct=}", None)
        tp1 = objc.createStructType("FooStruct", b'{FooStruct="first"i}', None)
        tp2 = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        self.assertEqual(sys.getsizeof(tp0()) + 1 * PTR_SIZE, sys.getsizeof(tp1()))
        self.assertEqual(sys.getsizeof(tp0()) + 2 * PTR_SIZE, sys.getsizeof(tp2()))

    def testStructNotWritable(self):
        tp0 = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        with pyobjc_options(structs_indexable=False, structs_writable=False):
            v = tp0(1, 2)

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are read-only"
            ):
                v.first = 42

        with pyobjc_options(structs_indexable=True, structs_writable=False):
            v = tp0(1, 2)

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are read-only"
            ):
                v.first = 42

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are read-only"
            ):
                v[0] = 42

    def testStructNotSequence(self):
        tp0 = objc.createStructType("FooStruct", b'{FooStruct="first"i"second"i}', None)

        with pyobjc_options(structs_indexable=False, structs_writable=True):
            v = tp0(1, 2)

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                v[0]

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                v[0] = 4

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                len(v)

            self.assertFalse(v == (1, 2))

            self.assertTrue(tp0(1, 2) == tp0(1, 2))
            self.assertFalse(tp0(1, 2) == tp0(1, 3))

            self.assertTrue(tp0(1, 2) != tp0(1, 3))
            self.assertFalse(tp0(1, 2) != tp0(1, 2))

            self.assertTrue(tp0(1, 2) <= tp0(1, 2))
            self.assertTrue(tp0(1, 2) <= tp0(1, 3))
            self.assertFalse(tp0(1, 2) <= tp0(0, 2))
            self.assertFalse(tp0(1, 2) <= tp0(1, 1))

            self.assertTrue(tp0(1, 2) >= tp0(1, 2))
            self.assertTrue(tp0(1, 2) >= tp0(1, 1))
            self.assertFalse(tp0(1, 2) >= tp0(2, 2))
            self.assertFalse(tp0(1, 2) >= tp0(1, 3))

            self.assertTrue(tp0(1, 2) < tp0(1, 3))
            self.assertFalse(tp0(1, 2) < tp0(1, 2))
            self.assertFalse(tp0(1, 2) < tp0(1, 1))

            self.assertTrue(tp0(1, 2) > tp0(1, 1))
            self.assertFalse(tp0(1, 2) > tp0(1, 2))
            self.assertFalse(tp0(1, 2) > tp0(1, 3))

    def testStructConstruction(self):
        with pyobjc_options(structs_indexable=False):
            tp0 = objc.createStructType(
                "FooStruct", b'{FooStruct="first"i"second"i}', None
            )

            v = tp0()
            self.assertEqual(v.first, 0)
            self.assertEqual(v.second, 0)

            v = tp0(2, 3)
            self.assertEqual(v.first, 2)
            self.assertEqual(v.second, 3)

            with self.assertRaisesRegex(
                TypeError, r"FooStruct\(\) takes at most 2 arguments \(3 given\)"
            ):
                tp0(4, 5, 6)

    def test_struct_as_sequence(self):
        tp0 = objc.createStructType(
            "FooStruct2", b'{FooStruct2="first"i"second"i"third"i}', None
        )

        with pyobjc_options(structs_indexable=True, structs_writable=True):
            v = tp0(1, 2, 3)

            #  Read (item, slice)
            self.assertEqual(v[0], 1)
            self.assertEqual(v[-1], 3)
            self.assertEqual(v[:], (1, 2, 3))

            self.assertEqual(v[-4:8], (1, 2, 3))

            self.assertEqual(v[1:2], (2,))
            self.assertEqual(v[::2], (1, 3))

            with self.assertRaisesRegex(IndexError, "FooStruct2 index out of range"):
                v[5]

            with self.assertRaisesRegex(IndexError, "FooStruct2 index out of range"):
                v[-6]

            with self.assertRaisesRegex(
                IndexError, "cannot fit 'int' into an index-sized integer"
            ):
                v[2**68]

            self.assertEqual(v[2**68 :], ())
            self.assertEqual(v[2**68 : 2**68 + 3], ())

            # Write (item, slice)
            v[0] = 4
            self.assertEqual(v.first, 4)

            v[0:2] = iter((9, 10))
            self.assertEqual(v.first, 9)
            self.assertEqual(v.second, 10)
            self.assertEqual(v.third, 3)

            v[::2] = (-1, -2)
            self.assertEqual(v.first, -1)
            self.assertEqual(v.second, 10)
            self.assertEqual(v.third, -2)

            with self.assertRaisesRegex(
                TypeError, "Slice assignment would change size of FooStruct2 instance"
            ):
                v[:] = range(10)

            with self.assertRaisesRegex(TypeError, "Must assign sequence to slice"):
                v[:] = 42

            with self.assertRaisesRegex(IndexError, "FooStruct2 index out of range"):
                v[5] = 42

            with self.assertRaisesRegex(IndexError, "FooStruct2 index out of range"):
                v[-6] = 42

            with self.assertRaisesRegex(
                IndexError, "cannot fit 'int' into an index-sized integer"
            ):
                v[2**68] = 4

            with self.assertRaisesRegex(
                TypeError, "Slice assignment would change size of FooStruct2 instance"
            ):
                v[2**68 :] = (4,)

            # Delete (item slice)
            with self.assertRaisesRegex(
                TypeError, "Cannot delete item '1' in a FooStruct2 instance"
            ):
                del v[1]

            with self.assertRaisesRegex(
                TypeError, "Cannot delete items in instances of FooStruct2"
            ):
                del v[1:3]

            # Wrong type
            with self.assertRaisesRegex(
                TypeError, "Struct indices must be integers, not str"
            ):
                v["first"]

            with self.assertRaisesRegex(
                TypeError, "Struct indices must be integers, not str"
            ):
                v["first"] = 22

            v = tp0(1, 2, 3)
            self.assertIn(2, v)
            self.assertNotIn(9, v)

            with self.assertRaisesRegex(TypeError, "FooStruct2 objects are unhashable"):
                hash(v)

    def test_struct_as_attributes(self):
        tp0 = objc.createStructType(
            "FooStruct4", b'{FooStruct4="first"i"second"i"third"i}', None
        )

        with pyobjc_options(structs_indexable=False, structs_writable=True):
            v = tp0(1, 2, 3)

            #  Read
            self.assertEqual(v.first, 1)

            # Write
            v.first = 4

            # Delete
            with self.assertRaisesRegex(
                TypeError, "Cannot delete attributes of FooStruct4"
            ):
                del v.second

    def test_no_sublcassing(self):
        tp0 = objc.createStructType(
            "FooStruct5", b'{FooStruct4="first"i"second"i"third"i}', None
        )

        with self.assertRaisesRegex(
            TypeError, "type 'FooStruct5' is not an acceptable base type"
        ):

            class MyStruct(tp0):
                pass

    def test_struct_pickling(self):
        orig = GlobalType(9, 10)
        self.assertEqual(orig.a, 9.0)
        self.assertEqual(orig.b, 10.0)

        buf = pickle.dumps(orig)
        self.assertIsInstance(buf, bytes)

        copy = pickle.loads(buf)
        self.assertIsInstance(copy, GlobalType)
        self.assertEqual(copy.a, 9.0)
        self.assertEqual(copy.b, 10.0)

        self.assertEqual(copy, orig)

    @expectedFailure
    def test_struct_naming(self):
        self.assertEqual(GlobalType.__name__, "GlobalType")
        self.assertEqual(GlobalType.__module__, "PyObjCTest.test_structs")
        self.assertEqual(GlobalType.__qualname__, "PyObjCTest.test_structs.GlobalType")

    def test_sizeof(self):
        self.assertIsInstance(GlobalType().__sizeof__(), int)

        tp0 = objc.createStructType(
            "FooStruct3", b'{FooStruct3="first"i"second"i"third"i}', None
        )

        self.assertGreater(tp0().__sizeof__(), GlobalType().__sizeof__())

    def todo_test_struct_defaults(self):
        # Check default values for various types
        # - char, unsigned char, char_as_int, char_as_text
        # - short,  unsigned short
        # - int,  unsigned int
        # - long,  unsigned long
        # - long long,  unsigned long long
        # - float
        # - double
        # - bool, BOOL
        # - nested structs
        # - nested arrays
        self.fail()

    @min_python_release("3.10")
    def test_using_match(self):
        PointStruct = objc.createStructType(
            "PointStruct", b"{_PointStruct=ff}", ["x", "y"]
        )
        self.assertIsInstance(PointStruct, type)
        self.assertEqual(PointStruct.__match_args__, ("x", "y"))

        o = PointStruct(x=40, y=42)

        # The match statement is executed with an # exec
        # statement because it is invalid before Python 3.10
        ns = locals().copy()
        exec(
            textwrap.dedent(
                """\
             match o:
                 case PointStruct(x=_ as x, y=_ as y):
                     pass
        """
            ),
            ns,
            ns,
        )

        self.assertEqual(ns["x"], o.x)
        self.assertEqual(ns["y"], o.y)

        ns = locals().copy()
        exec(
            textwrap.dedent(
                """\
             match o:
                 case PointStruct(_ as x, _ as y):
                     pass
        """
            ),
            ns,
            ns,
        )
