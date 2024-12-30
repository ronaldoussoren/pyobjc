"""
XXX: Add tests that check that the type actually works as expected:

* Use struct value as method argument
* Return struct value from a method

Add tests for nested structs as well (that is assert that NSRect.location is
an NSPoint, but using our own types)
"""

import sys
import warnings
import gc

import objc
import pickle
import textwrap
import copy
from PyObjCTest.fnd import NSObject
from PyObjCTest.structs import OC_StructTest
from PyObjCTools.TestSupport import (
    TestCase,
    pyobjc_options,
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
            "FooStruct", b"{_FooStruct=ffff}", ["a", "b", "c", "d"], "docstring"
        )
        self.assertIsInstance(tp, type)
        self.assertEqual(tp.__typestr__, b"{_FooStruct=ffff}")
        self.assertEqual(tp.__doc__, "docstring")

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

        with self.assertRaisesRegex(
            TypeError, r"FooStruct\(\) does not have argument n"
        ):
            tp(n=4)

        with self.assertRaisesRegex(
            TypeError, r"FooStruct\(\) keywords must be strings"
        ):
            tp(**{1: 2})

        with self.assertRaisesRegex(UnicodeEncodeError, r".*surrogates not allowed"):
            tp(**{"\uDC00": 1})

        with self.assertRaisesRegex(
            TypeError, r"FooStruct\(\) got multiple values for keyword argument 'a'"
        ):
            tp(1, a=2)

    def test_api_misuse(self):
        with self.assertRaisesRegex(TypeError, "missing 3 required"):
            objc.createStructType()

        with self.assertRaisesRegex(
            TypeError, "fieldnames must be a sequence of strings"
        ):
            objc.createStructType("FooStruct", b"{_FooStruct=ffff}", 42)

        with self.assertRaisesRegex(
            TypeError, "fieldnames must be a sequence of strings"
        ):
            objc.createStructType(
                "FooStruct", b"{_FooStruct=ffff}", ["a", "b", 42, "d"], "docstring"
            )

        with self.assertRaises(UnicodeEncodeError):
            objc.createStructType(
                "FooStruct",
                b"{_FooStruct=ffff}",
                ["\U000fffff\uDBBB", "b", "c", "d"],
            )

    def test_copy_copy(self):
        Point = objc.createStructType("OCPoint", b"{_OCPoint=dd}", ["x", "y"])
        Line = objc.createStructType(
            "OCLine",
            b"{_OCLine={_OCPoint=dd}{_OCPoint=dd}}d",
            ["start", "stop", "width"],
        )

        start = Point(1, 2)
        stop = Point(3, 4)
        line = Line(start, stop)

        r = copy.copy(start)
        self.assertEqual(r, start)
        self.assertIsNot(r, start)

        r = copy.copy(line)
        self.assertEqual(r, line)
        self.assertIsNot(r, line)
        self.assertIs(r.start, start)
        self.assertIs(r.stop, stop)

    def test_copy_deepcopy(self):
        Point = objc.createStructType("OCPoint", b"{_OCPoint=dd}", ["x", "y"])
        Line = objc.createStructType(
            "OCLine",
            b"{_OCLine={_OCPoint=dd}{_OCPoint=dd}}d",
            ["start", "stop", "width"],
        )

        start = Point(1, 2)
        stop = Point(3, 4)
        line = Line(start, stop)

        r = copy.deepcopy(start)
        self.assertEqual(r, start)
        self.assertIsNot(r, start)

        r = copy.deepcopy(line)
        self.assertEqual(r, line)
        self.assertIsNot(r, line)
        self.assertIsNot(r.start, start)
        self.assertIsNot(r.stop, stop)

        line2 = Line(start, start)
        self.assertIs(line2.start, line2.stop)
        r = copy.deepcopy(line2)
        self.assertEqual(r, line2)
        self.assertIsNot(r, line2)
        self.assertIsNot(r.start, start)
        self.assertIsNot(r.stop, start)
        self.assertIs(r.start, r.stop)

    @min_python_release("3.13")
    def test_copy_replace(self):
        Point = objc.createStructType("OCPoint", b"{_OCPoint=dd}", ["x", "y"])
        Line = objc.createStructType(
            "OCLine",
            b"{_OCLine={_OCPoint=dd}{_OCPoint=dd}}d",
            ["start", "stop", "width"],
        )

        start = Point(1, 2)
        stop = Point(3, 4)
        line = Line(start, stop)

        r = copy.replace(start)
        self.assertEqual(r, start)

        r = copy.replace(start, x=9)
        self.assertIsInstance(r, Point)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 2)

        r = copy.replace(line)
        self.assertEqual(r, line)
        self.assertIs(r.start, start)
        self.assertIs(r.stop, stop)

        r = copy.replace(line, stop=start)
        self.assertIsInstance(r, Line)
        self.assertEqual(r.start, start)
        self.assertEqual(r.stop, start)

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

        v = tp0()
        w = objc.repythonify(v, tp0.__typestr__)
        self.assertEqual(v, w)

    def test_repythonify_empty_struct(self):
        self.assertEqual(objc.repythonify((), b"{struct_tag}"), ())
        self.assertEqual(objc.repythonify((), b"{struct_tag=}"), ())

    def test_repythonify_struct_with_fieldnames(self):
        self.assertEqual(objc.repythonify((1,), b'{struct_tag="field"i}'), (1,))

        with self.assertRaisesRegex(objc.error, "invalid embedded field name"):
            objc.repythonify((1,), b'{struct_tag="fieldi}')

    def test_repythonify_struct_with_invalid_field(self):
        with self.assertRaisesRegex(objc.error, "Unhandled type"):
            objc.repythonify((1,), b'{struct_tag="field"X}')

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
                v[0:1]

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                v[0] = 4

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                len(v)

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                v[0:1] = (1, 1)

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                1 in v  # noqa: B015

            with self.assertRaisesRegex(
                TypeError, "Instances of 'FooStruct' are not sequences"
            ):
                list(v)

            self.assertFalse(v == (1, 2))
            self.assertFalse(v == (1, 2, 3))
            self.assertFalse(v == (1,))
            self.assertTrue(v != (1, 2))
            self.assertTrue(v != (1, 2, 3))
            self.assertTrue(v != (1,))

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

            self.assertFalse(tp0(1, 2) == 4)
            self.assertTrue(tp0(1, 2) != 4)
            with self.assertRaisesRegex(
                TypeError, "Cannot compare instances of FooStruct and int"
            ):
                self.assertTrue(tp0(1, 2) < 4)
            with self.assertRaisesRegex(
                TypeError, "Cannot compare instances of FooStruct and int"
            ):
                self.assertTrue(tp0(1, 2) <= 4)
            with self.assertRaisesRegex(
                TypeError, "Cannot compare instances of FooStruct and int"
            ):
                self.assertTrue(tp0(1, 2) > 4)
            with self.assertRaisesRegex(
                TypeError, "Cannot compare instances of FooStruct and int"
            ):
                self.assertTrue(tp0(1, 2) >= 4)

            with pyobjc_options(structs_indexable=False):
                self.assertFalse(tp0(1, 2) == (1, 2))
                self.assertTrue(tp0(1, 2) != (1, 2))
                with self.assertRaisesRegex(
                    TypeError, "Cannot compare instances of FooStruct and tuple"
                ):
                    self.assertTrue(tp0(1, 2) < (1, 2))
                with self.assertRaisesRegex(
                    TypeError, "Cannot compare instances of FooStruct and tuple"
                ):
                    self.assertTrue(tp0(1, 2) <= (1, 2))
                with self.assertRaisesRegex(
                    TypeError, "Cannot compare instances of FooStruct and tuple"
                ):
                    self.assertTrue(tp0(1, 2) > (1, 2))
                with self.assertRaisesRegex(
                    TypeError, "Cannot compare instances of FooStruct and tuple"
                ):
                    self.assertTrue(tp0(1, 2) >= (1, 2))

            with pyobjc_options(structs_indexable=True):
                self.assertTrue(tp0(1, 2) == (1, 2))
                self.assertFalse(tp0(1, 2) != (1, 2))
                self.assertTrue(tp0(1, 2) != (2, 2))
                self.assertTrue(tp0(1, 2) != (1, 1))
                self.assertTrue(tp0(1, 2) < (2, 2))
                self.assertTrue(tp0(1, 2) <= (2, 2))
                self.assertTrue(tp0(1, 2) > (1, 1))
                self.assertFalse(tp0(1, 2) > (1, 2))
                self.assertTrue(tp0(1, 2) >= (1, 1))
                self.assertTrue(tp0(1, 2) >= (1, 2))
                self.assertFalse(tp0(1, 2) >= (1, 3))

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

            with self.assertRaisesRegex(TypeError, "must assign sequence to slice"):
                v[::2] = 1

            with self.assertRaisesRegex(
                TypeError, "slice assignment would change size of FooStruct2 instance"
            ):
                v[::2] = (1,)

            v[-8:] = (8, 9, 10)
            self.assertEqual(v.first, 8)
            self.assertEqual(v.second, 9)
            self.assertEqual(v.third, 10)

            self.assertEqual(v[-8:10], (8, 9, 10))

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

            with self.assertRaisesRegex(
                TypeError, "Cannot delete items in instances of FooStruct2"
            ):
                del v[1:3:2]

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

            with self.assertRaisesRegex(ValueError, "slice step cannot be zero"):
                v[::0]

            with self.assertRaisesRegex(ValueError, "slice step cannot be zero"):
                v[::0] = (1, 1)

            with self.assertRaisesRegex(
                TypeError, "Cannot delete item '0' in a FooStruct2 instance"
            ):
                del v[0]

            with self.assertRaisesRegex(
                TypeError, "Cannot delete items in instances of FooStruct2"
            ):
                del v[0:3]

            with self.assertRaisesRegex(TypeError, "Must assign sequence to slice"):
                v[0:3] = 1

            with self.assertRaisesRegex(
                TypeError, "Slice assignment would change size of FooStruct2 instance"
            ):
                v[0:3] = (1,)

            v = tp0(1, 2, 3)
            self.assertFalse(v == (1, 2, 4))
            self.assertFalse(v == (1, 2, 3, 4))
            self.assertFalse(v == (1, 2))
            self.assertTrue(v == (1, 2, 3))
            self.assertTrue(v != (1, 2, 4))
            self.assertTrue(v != (1, 2, 3, 4))
            self.assertTrue(v != (1,))
            self.assertFalse(v != (1, 2, 3))

            self.assertTrue(v < (1, 2, 3, 4))
            self.assertFalse(v < (1, 2))
            self.assertTrue(v <= (1, 2, 3, 4))
            self.assertFalse(v <= (1, 2))

            self.assertFalse(v > (1, 2, 3, 4))
            self.assertTrue(v > (1, 2))
            self.assertFalse(v >= (1, 2, 3, 4))
            self.assertTrue(v >= (1, 2))

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

    def test_struct_naming(self):
        self.assertEqual(GlobalType.__name__, "GlobalType")
        self.assertEqual(GlobalType.__module__, "PyObjCTest.test_structs")
        self.assertEqual(GlobalType.__qualname__, "GlobalType")

    def test_sizeof(self):
        self.assertIsInstance(GlobalType().__sizeof__(), int)

        tp0 = objc.createStructType(
            "FooStruct3", b'{FooStruct3="first"i"second"i"third"i}', None
        )

        self.assertGreater(tp0().__sizeof__(), GlobalType().__sizeof__())

    def test_struct_defaults(self):
        # - nested structs
        # - nested arrays
        BasicTypesStruct = objc.createStructType(
            "BasicTypesStruct",
            b"".join(
                [
                    b"{_BasicTypesStruct=" b'"char"',
                    objc._C_CHR,
                    b'"uchar"',
                    objc._C_UCHR,
                    b'"charint"',
                    objc._C_CHAR_AS_INT,
                    b'"chartext"',
                    objc._C_CHAR_AS_TEXT,
                    b'"UniChar"',
                    objc._C_UNICHAR,
                    b'"short"',
                    objc._C_SHT,
                    b'"ushort"',
                    objc._C_USHT,
                    b'"int"',
                    objc._C_INT,
                    b'"uint"',
                    objc._C_UINT,
                    b'"long"',
                    objc._C_LNG,
                    b'"ulong"',
                    objc._C_ULNG,
                    b'"longlong"',
                    objc._C_LNGLNG,
                    b'"ulonglong"',
                    objc._C_ULNGLNG,
                    b'"float"',
                    objc._C_FLT,
                    b'"double"',
                    objc._C_DBL,
                    b'"bool"',
                    objc._C_BOOL,
                    b'"BOOL"',
                    objc._C_NSBOOL,
                    b'"GlobalType"',
                    GlobalType.__typestr__,
                    b'"Unknown"',
                    b"{_UnknownStruct=ff}",
                    b'"array"',
                    objc._C_ARY_B,
                    b"10",
                    objc._C_INT,
                    objc._C_ARY_E,
                    b"}",
                ]
            ),
            None,
        )
        v = BasicTypesStruct()

        self.assertEqual(v.char, 0)
        self.assertIsInstance(v.char, int)
        self.assertEqual(v.uchar, 0)
        self.assertIsInstance(v.uchar, int)
        self.assertEqual(v.chartext, "\0")
        self.assertEqual(v.UniChar, "\0")
        self.assertEqual(v.charint, 0)
        self.assertIsInstance(v.charint, int)
        self.assertEqual(v.short, 0)
        self.assertIsInstance(v.short, int)
        self.assertEqual(v.ushort, 0)
        self.assertIsInstance(v.ushort, int)
        self.assertEqual(v.int, 0)
        self.assertIsInstance(v.int, int)
        self.assertEqual(v.uint, 0)
        self.assertIsInstance(v.uint, int)
        self.assertEqual(v.long, 0)
        self.assertIsInstance(v.long, int)
        self.assertEqual(v.ulong, 0)
        self.assertIsInstance(v.ulong, int)
        self.assertEqual(v.longlong, 0)
        self.assertIsInstance(v.longlong, int)
        self.assertEqual(v.ulonglong, 0)
        self.assertIsInstance(v.ulonglong, int)
        self.assertEqual(v.float, 0.0)
        self.assertIsInstance(v.float, float)
        self.assertEqual(v.double, 0.0)
        self.assertIsInstance(v.double, float)
        self.assertIs(v.bool, False)
        self.assertIs(v.BOOL, False)
        self.assertEqual(v.GlobalType, GlobalType(0, 0))
        self.assertIs(v.Unknown, None)
        self.assertIsInstance(v.GlobalType, GlobalType)

        # XXX: I don't like this...
        self.assertIs(v.array, None)

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

    def test_compare_error(self):
        v = GlobalType(1, 2)
        self.assertEqual(v.a, 1)
        self.assertEqual(v.b, 2)
        self.assertEqual(v[0], 1)
        self.assertEqual(v[1], 2)

        self.assertIn(1, v)

        class CannotCompare:
            def __eq__(self, other):
                raise RuntimeError("cannot compare me")

            def __ne__(self, other):
                raise RuntimeError("cannot compare me")

            def __lt__(self, other):
                raise RuntimeError("cannot compare me")

            def __le__(self, other):
                raise RuntimeError("cannot compare me")

            def __gt__(self, other):
                raise RuntimeError("cannot compare me")

            def __ge__(self, other):
                raise RuntimeError("cannot compare me")

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            CannotCompare() in v  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            GlobalType(CannotCompare(), 2) == (1, 2)  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            GlobalType(CannotCompare(), 2) != (1, 2)  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            GlobalType(CannotCompare(), 2) < (1, 2)  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            GlobalType(CannotCompare(), 2) <= (1, 2)  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            GlobalType(CannotCompare(), 2) > (1, 2)  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            GlobalType(CannotCompare(), 2) >= (1, 2)  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v == GlobalType(CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v == GlobalType(1, CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v != GlobalType(CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v != GlobalType(1, CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v < GlobalType(CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v < GlobalType(1, CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v <= GlobalType(CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v <= GlobalType(1, CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v > GlobalType(CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v > GlobalType(1, CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v >= GlobalType(CannotCompare())  # noqa: B015

        with self.assertRaisesRegex(RuntimeError, "cannot compare me"):
            v >= GlobalType(1, CannotCompare())  # noqa: B015

    def test_copy_error(self):
        class CopyError:
            def __deepcopy__(self, memo=None):
                raise RuntimeError("cannot copy me")

        v = GlobalType(1, CopyError())
        with self.assertRaisesRegex(RuntimeError, "cannot copy me"):
            v.copy()

        with self.assertRaisesRegex(RuntimeError, "cannot copy me"):
            v = GlobalType(1, CopyError())
            v._replace(a=2)

    def test_invalid_struct_encoding(self):
        with self.assertRaisesRegex(
            ValueError, "invalid signature: not a struct encoding"
        ):
            objc.createStructType("InvStruct", b"q", None)

        with self.assertRaisesRegex(
            ValueError, "invalid signature: not a struct encoding"
        ):
            objc.createStructType("InvStruct", b"q", ["a", "b"])

        with self.assertRaisesRegex(
            ValueError, "Invalid struct definition in type signature: {_FooStruct="
        ):
            objc.createStructType("InvStruct", b"{_FooStruct=", [])

        with self.assertRaisesRegex(
            ValueError, "invalid signature: embedded field name without end"
        ):
            objc.createStructType("InvStruct", b'{_FooStruct="af}', None)

        with self.assertRaisesRegex(
            ValueError, "invalid signature: unknown type coding 0x21"
        ):
            objc.createStructType("InvStruct", b'{_FooStruct="a"f"b"!"c"q}', None)

        with self.assertRaisesRegex(
            ValueError, "invalid signature: not a complete struct encoding"
        ):
            objc.createStructType("InvStruct", b'{_FooStruct="a"f', None)

        with self.assertRaisesRegex(
            ValueError, "invalid signature: not a complete struct encoding"
        ):
            objc.createStructType("InvStruct", b"{_FooStruct}", None)

    def test_repr(self):
        v = GlobalType("a", 4)
        self.assertEqual(repr(v), "<PyObjCTest.test_structs.GlobalType a='a' b=4>")

        v.b = v
        self.assertEqual(
            repr(v),
            "<PyObjCTest.test_structs.GlobalType a='a' b=<PyObjCTest.test_structs.GlobalType ...>>",
        )

        EmptyStruct = objc.createStructType("EmptyStruct", b"{EmptyStruct=}", None)
        self.assertEqual(repr(EmptyStruct()), "<EmptyStruct>")

    def test_packed(self):
        tp = objc.createStructType(
            "PackedStruct", b"{_PackedStruct=si}", ["a", "b"], pack=1
        )
        self.assertEqual(tp.__struct_pack__, 1)

        v = tp(1, 2)
        w = objc.repythonify(v, tp.__typestr__)
        self.assertEqual(v, w)

        tp = objc.createStructType(
            "PackedStruct2",
            b"".join(
                (
                    b"{_PackedStruct2=",
                    objc._C_CHAR_AS_INT,  # to ensure odd offset,
                    objc._C_SHT,
                    objc._C_INT,
                    objc._C_LNG,
                    objc._C_LNG_LNG,
                    objc._C_USHT,
                    objc._C_UINT,
                    objc._C_ULNG,
                    objc._C_ULNG_LNG,
                    objc._C_FLT,
                    objc._C_DBL,
                    b"}",
                )
            ),
            ["c", "s", "i", "l", "ll", "us", "ui", "ul", "ull", "f", "d"],
            pack=1,
        )
        self.assertEqual(tp.__struct_pack__, 1)

        v = tp()
        w = objc.repythonify(v, tp.__typestr__)
        self.assertEqual(v, w)

    def test_invalid_packed(self):
        with self.assertRaisesRegex(objc.error, "invalid type encoding"):
            objc.createStructType(
                "InvalidPackedStruct", b"{_InvalidPackedStruct=hi}", ["a", "b"], pack=1
            )


class TestStructAlias(TestCase):
    def test_register_struct_alias(self):
        OtherType = objc.registerStructAlias(b"{_OtherType=ff}", GlobalType)
        self.assertIs(OtherType, GlobalType)

        with self.assertRaisesRegex(
            TypeError, "a bytes-like object is required, not 'str'"
        ):
            objc.registerStructAlias("{foo=ff}", GlobalType)

        with self.assertRaisesRegex(
            TypeError,
            r"registerStructAlias\(\) missing 1 required positional argument: 'structType'",
        ):
            objc.registerStructAlias("{foo=ff}")

        with self.assertRaisesRegex(TypeError, "struct type is not valid"):
            objc.registerStructAlias(b"{foo=ff}", None)

        with self.assertRaisesRegex(ValueError, "typestr too long"):
            objc.registerStructAlias(b"{foo=" + b"f" * 2000 + b"}", GlobalType)

        with self.assertRaisesRegex(ValueError, "Bad type string"):
            objc.registerStructAlias(b'{foo="hello"f"worldf}', GlobalType)

        with self.assertRaisesRegex(ValueError, "Bad type string"):
            objc.registerStructAlias(b"{foo=ff", GlobalType)

    def test_create_struct_alias(self):
        self.assertNotHasAttr(objc.ivar, "XxxOtherType")
        SomeOtherType = objc.createStructAlias(
            "XxxOtherType", b"{_SomeOtherType=ff}", GlobalType
        )
        self.assertIs(SomeOtherType, GlobalType)
        self.assertHasAttr(objc.ivar, "XxxOtherType")

    def test_alias_for_different_shape(self):
        # XXX: See sources, the test if for the current behaviour, but
        # that's suboptimal at best. The bridge should check that
        # the struct encodings are similar enough.
        OtherType = objc.registerStructAlias(b"{_OtherShaped=fff}", GlobalType)
        self.assertIs(OtherType, GlobalType)

        v = objc.repythonify((1, 2, 3), b"{_OtherShaped=fff}")
        self.assertEqual(v, GlobalType(1, 2))

    def test_gc(self):
        flag = False

        class Dummy:
            def __del__(self):
                nonlocal flag
                flag = True

        v = GlobalType()
        v.a = v
        v.b = Dummy()

        self.assertFalse(flag)
        del v

        self.assertFalse(flag)
        gc.collect()
        self.assertTrue(flag)


class TestInternals(TestCase):
    def test_functions_overridden(self):
        self.assertIsNot(objc.registerStructAlias, objc._objc.registerStructAlias)
