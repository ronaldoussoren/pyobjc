import datetime
import decimal

import Cocoa
from objc._pythonify import OC_PythonFloat
from PyObjCTools import Conversion
from PyObjCTools.TestSupport import TestCase
import objc


class TestConversion(TestCase):
    def test_toPythonDecimal(self):
        v = Cocoa.NSDecimalNumber.decimalNumberWithString_("42.5")
        d = Conversion.toPythonDecimal(v)
        self.assertIsInstance(d, decimal.Decimal)
        self.assertEqual(str(d), "42.5")

    def test_fromPythonDecimal(self):
        d = decimal.Decimal("42.5")
        self.assertIsInstance(d, decimal.Decimal)

        v = Conversion.fromPythonDecimal(d)
        self.assertIsInstance(v, Cocoa.NSDecimalNumber)
        self.assertEqual(str(v), "42.5")

    def test_serializePropertyList(self):
        self.assertRaises(ValueError, Conversion.serializePropertyList, {}, "invalid")

        v = Conversion.serializePropertyList({"a": 42}, "xml")
        self.assertTrue(bytes(v).startswith(b"<?xml"))

        v = Conversion.serializePropertyList({"a": 42}, "binary")
        self.assertTrue(bytes(v).startswith(b"bplist"))

        self.assertRaises(
            ValueError, Conversion.serializePropertyList, {"a": 42}, "ascii"
        )

        self.assertRaises(
            ValueError,
            Conversion.serializePropertyList,
            Cocoa.NSObject.alloc().init(),
            "xml",
        )

    def test_deserializePropertyList(self):
        in_val = {"a": 42}

        for fmt in ("xml", "binary"):
            data = Conversion.serializePropertyList(in_val, fmt)

            out_val = Conversion.deserializePropertyList(data)

            self.assertEqual(in_val, out_val)

            bytes_data = bytes(data)
            out_val = Conversion.deserializePropertyList(bytes_data)
            self.assertEqual(in_val, out_val)

            if fmt == "xml":
                str_data = bytes_data.decode("utf-8")
                out_val = Conversion.deserializePropertyList(str_data)

                self.assertEqual(in_val, out_val)

            self.assertRaises(ValueError, Conversion.deserializePropertyList, data[:-2])

    def test_propertyListFromPythonCollection(self):
        for value, result_type in (
            ({"a": 42}, Cocoa.NSDictionary),
            ([42], Cocoa.NSArray),
            ((42,), Cocoa.NSArray),
            ({42}, Cocoa.NSSet),
            (frozenset({42}), Cocoa.NSSet),
            (datetime.datetime.now(), Cocoa.NSDate),
            (datetime.date.today(), Cocoa.NSDate),
        ):
            with self.subTest(value=value, type=type(value).__name__):
                v = Conversion.propertyListFromPythonCollection(value)
                self.assertIsInstance(v, result_type)

                if isinstance(value, datetime.datetime):
                    # XXX: This is a bit of a hack and avoids a test problem during
                    # summer time
                    self.assertEqual(
                        int(v.timeIntervalSince1970()), int(value.timestamp())
                    )
                else:
                    self.assertEqual(v, value)

        with self.subTest("decimal"):
            v = Conversion.propertyListFromPythonCollection(decimal.Decimal(1))
            self.assertIsInstance(v, Cocoa.NSDecimalNumber)

        with self.subTest("invalid dict"):
            with self.assertRaises(TypeError):
                Conversion.propertyListFromPythonCollection({42: 43})

        with self.subTest("unknown type"):
            with self.assertRaises(TypeError):
                Conversion.propertyListFromPythonCollection(dir)

        with self.subTest("conversion helper"):

            def helper(v):
                return str(v)

            v = Conversion.propertyListFromPythonCollection(dir, helper)
            self.assertEqual(v, str(dir))

        with self.subTest("nested conversion"):
            value = [{"a": 42}, {"b": [1]}, {()}]

            v = Conversion.propertyListFromPythonCollection(value)

            self.assertIsInstance(v[0], Cocoa.NSDictionary)
            self.assertIsInstance(v[1], Cocoa.NSDictionary)
            self.assertIsInstance(v[1]["b"], Cocoa.NSArray)
            self.assertIsInstance(v[2], Cocoa.NSSet)
            self.assertIsInstance(next(iter(v[2])), Cocoa.NSArray)

    def test_pythonCollectionFromPropertyList(self):
        with self.subTest("dict"):
            value = Cocoa.NSDictionary.dictionaryWithDictionary_({"a": 42})
            self.assertIsInstance(value, Cocoa.NSDictionary)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, dict)
            self.assertEqual(v, {"a": 42})
            self.assertNotIsInstance(next(iter(v.keys())), objc.pyobjc_unicode)

        with self.subTest("list/tuple"):
            value = Cocoa.NSArray.arrayWithArray_(["a", 42])
            self.assertIsInstance(value, Cocoa.NSArray)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, list)
            self.assertEqual(v, ["a", 42])

        with self.subTest("set"):
            value = Cocoa.NSSet.setWithSet_({"a", 42})
            self.assertIsInstance(value, Cocoa.NSSet)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, set)
            self.assertEqual(v, {"a", 42})

        with self.subTest("bytes"):
            value = Cocoa.NSData.dataWithData_(b"hello")
            self.assertIsInstance(value, Cocoa.NSData)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, bytes)
            self.assertEqual(v, b"hello")

        with self.subTest("str"):
            value = Cocoa.NSString.stringWithString_("hello").nsstring()
            self.assertIsInstance(value, Cocoa.NSString)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, str)
            self.assertEqual(v, "hello")

        with self.subTest("float"):
            value = Cocoa.NSNumber.numberWithDouble_(1.5)
            self.assertIsInstance(value, Cocoa.NSNumber)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, float)
            self.assertNotIsInstance(v, OC_PythonFloat)
            self.assertEqual(v, 1.5)

        with self.subTest("int"):
            value = Cocoa.NSNumber.numberWithLong_(42)
            self.assertIsInstance(value, Cocoa.NSNumber)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, int)
            self.assertNotIsInstance(v, OC_PythonFloat)
            self.assertEqual(v, 42)

        with self.subTest("date"):
            value = Cocoa.NSDate.date()
            self.assertIsInstance(value, Cocoa.NSDate)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, datetime.datetime)

        with self.subTest("decimal"):
            value = Cocoa.NSDecimalNumber.decimalNumberWithString_("42.5")
            self.assertIsInstance(value, Cocoa.NSDecimalNumber)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIsInstance(v, decimal.Decimal)
            self.assertEqual(v, decimal.Decimal("42.5"))

        with self.subTest("None"):
            value = Cocoa.NSNull.null()
            self.assertIsInstance(value, Cocoa.NSNull)

            v = Conversion.pythonCollectionFromPropertyList(value)
            self.assertIs(v, None)

        with self.subTest("unknown type"):
            value = Cocoa.NSObject.alloc().init()

            with self.assertRaises(TypeError):
                Conversion.pythonCollectionFromPropertyList(value)

        with self.subTest("conversion helper"):

            def helper(value):
                return str(value)

            value = Cocoa.NSObject.alloc().init()

            v = Conversion.pythonCollectionFromPropertyList(value, helper)
            self.assertEqual(v, str(value))

        with self.subTest("nested"):
            value = Cocoa.NSMutableArray.array()
            value.append(Cocoa.NSArray.arrayWithArray_([1, 2]))
            value.append(
                Cocoa.NSDictionary.dictionaryWithDictionary_(
                    {42: Cocoa.NSArray.arrayWithArray_([4, 5])}
                )
            )
            value.append(
                Cocoa.NSSet.setWithSet_({Cocoa.NSArray.arrayWithArray_([4, 5])})
            )

            v = Conversion.pythonCollectionFromPropertyList(value)
            # self.assertEqual(v, value)

            self.assertIsInstance(v, list)
            self.assertEqual(len(v), 3)
            self.assertIsInstance(v[0], list)
            self.assertEqual(v[0], [1, 2])
            self.assertIsInstance(v[1], dict)
            self.assertIsInstance(v[1][42], list)
            self.assertEqual(v[1][42], [4, 5])
            self.assertIsInstance(v[2], set)
            self.assertIsInstance(next(iter(v[2])), tuple)
            self.assertEqual(next(iter(v[2])), (4, 5))
