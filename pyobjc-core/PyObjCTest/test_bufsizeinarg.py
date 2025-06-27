from PyObjCTools.TestSupport import TestCase
from PyObjCTest.bufsizeinarg import OC_ArgSizeInArg
import objc

NSArray = objc.lookUpClass("NSArray")

objc.loadBundleFunctions(
    None, globals(), [("CFArrayGetTypeID", objc._C_NSUInteger, "")]
)
CFArrayRef = objc.registerCFSignature(
    "CFArrayRef", b"^{__CFArray=}", CFArrayGetTypeID(), "NSArray"  # noqa: F821
)

for tp in (
    "char",
    "short",
    "int",
):
    for pfx in ("", "u"):
        objc.registerMetaDataForSelector(
            b"OC_ArgSizeInArg",
            f"{pfx}{tp}:array:".encode(),
            {
                "arguments": {
                    2
                    + 1: {
                        "type_modifier": objc._C_IN,
                        "c_array_length_in_arg": 2 + 0,
                        "null_accepted": False,
                    }
                }
            },
        )

    for pfx in ("", "u"):
        if tp == "char" and pfx == "u":
            # In recent(?) versions of clang @encode(unsigned char*) is
            # '*' and not '^C' :-((((
            objc.registerMetaDataForSelector(
                b"OC_ArgSizeInArg",
                f"p{pfx}{tp}:array:".encode(),
                {
                    "arguments": {
                        2 + 0: {"type_modifier": objc._C_IN, "type": "^C"},
                        2
                        + 1: {
                            "type_modifier": objc._C_IN,
                            "c_array_length_in_arg": 2 + 0,
                            "null_accepted": False,
                        },
                    }
                },
            )
        else:
            objc.registerMetaDataForSelector(
                b"OC_ArgSizeInArg",
                f"p{pfx}{tp}:array:".encode(),
                {
                    "arguments": {
                        2 + 0: {"type_modifier": objc._C_IN},
                        2
                        + 1: {
                            "type_modifier": objc._C_IN,
                            "c_array_length_in_arg": 2 + 0,
                            "null_accepted": False,
                        },
                    }
                },
            )

objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"long:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_LNG},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"ulong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_ULNG},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"longlong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_LNGLNG},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"ulonglong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_ULNGLNG},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)

objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"plong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_PTR + objc._C_LNG, "type_modifier": "n"},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"pulong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_PTR + objc._C_ULNG, "type_modifier": "n"},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"plonglong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_PTR + objc._C_LNGLNG, "type_modifier": "n"},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"pulonglong:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_PTR + objc._C_ULNGLNG, "type_modifier": "n"},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)

objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"intchar:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_CHAR_AS_INT},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)

objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"pintchar:array:",
    {
        "arguments": {
            2
            + 0: {
                "type": objc._C_PTR + objc._C_CHAR_AS_INT,
                "type_modifier": objc._C_IN,
            },
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)

objc.registerMetaDataForSelector(
    b"OC_ArgSizeInArg",
    b"pchar2:array:",
    {
        "arguments": {
            2 + 0: {"type": objc._C_PTR + objc._C_CHR, "type_modifier": objc._C_IN},
            2
            + 1: {
                "type_modifier": objc._C_IN,
                "c_array_length_in_arg": 2 + 0,
                "null_accepted": False,
            },
        }
    },
)

for tp in ("id", "cfarray", "nsrange", "cfrange", "float"):
    objc.registerMetaDataForSelector(
        b"OC_ArgSizeInArg",
        f"{tp}:array:".encode(),
        {
            "arguments": {
                2
                + 1: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 0,
                    "null_accepted": False,
                }
            }
        },
    )

    objc.registerMetaDataForSelector(
        b"OC_ArgSizeInArg",
        f"p{tp}:array:".encode(),
        {
            "arguments": {
                2
                + 0: {
                    "type_modifier": objc._C_IN,
                },
                2
                + 1: {
                    "type_modifier": objc._C_IN,
                    "c_array_length_in_arg": 2 + 0,
                    "null_accepted": False,
                },
            }
        },
    )


class TestBasicArraySizes(TestCase):
    def test_char_as_int(self):
        self.assertArgHasType(OC_ArgSizeInArg.intchar_array_, 0, objc._C_CHAR_AS_INT)
        v = OC_ArgSizeInArg.intchar_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_char(self):
        v = OC_ArgSizeInArg.char_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_uchar(self):
        v = OC_ArgSizeInArg.uchar_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_short(self):
        v = OC_ArgSizeInArg.short_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_ushort(self):
        v = OC_ArgSizeInArg.ushort_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_int(self):
        v = OC_ArgSizeInArg.int_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_uint(self):
        v = OC_ArgSizeInArg.uint_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_long(self):
        v = OC_ArgSizeInArg.long_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_ulong(self):
        v = OC_ArgSizeInArg.ulong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_longlong(self):
        v = OC_ArgSizeInArg.longlong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_ulonglong(self):
        v = OC_ArgSizeInArg.ulonglong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_cfrange(self):
        v = OC_ArgSizeInArg.cfrange_array_((3, 5), range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_nsrange(self):
        v = OC_ArgSizeInArg.nsrange_array_((3, 5), range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_cfarray(self):
        v = OC_ArgSizeInArg.cfarray_array_(["A"] * 5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_id(self):
        v = OC_ArgSizeInArg.id_array_(["A"] * 5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

        v = OC_ArgSizeInArg.id_array_(None, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, [])

        with self.assertRaisesRegex(
            TypeError, "Don't know how to extract count from encoding: @"
        ):
            v = OC_ArgSizeInArg.id_array_(objc.lookUpClass("NSObject").new(), range(50))

    def test_float(self):
        with self.assertRaisesRegex(
            TypeError, "Don't know how to extract count from encoding: f"
        ):
            OC_ArgSizeInArg.float_array_(5.0, range(50))


class TestIndirectArraySizes(TestCase):
    def test_char_as_int(self):
        v = OC_ArgSizeInArg.pintchar_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_char(self):
        v = OC_ArgSizeInArg.pchar_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

        v = OC_ArgSizeInArg.pchar2_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_uchar(self):
        v = OC_ArgSizeInArg.puchar_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_short(self):
        v = OC_ArgSizeInArg.pshort_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_ushort(self):
        v = OC_ArgSizeInArg.pushort_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_int(self):
        v = OC_ArgSizeInArg.pint_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_uint(self):
        v = OC_ArgSizeInArg.puint_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_long(self):
        v = OC_ArgSizeInArg.plong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_ulong(self):
        v = OC_ArgSizeInArg.pulong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_longlong(self):
        v = OC_ArgSizeInArg.plonglong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_ulonglong(self):
        v = OC_ArgSizeInArg.pulonglong_array_(5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_cfrange(self):
        v = OC_ArgSizeInArg.pcfrange_array_((3, 5), range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_nsrange(self):
        v = OC_ArgSizeInArg.pnsrange_array_((3, 5), range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_cfarray(self):
        v = OC_ArgSizeInArg.pcfarray_array_(["A"] * 5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

    def test_id(self):
        v = OC_ArgSizeInArg.pid_array_(["A"] * 5, range(50))
        self.assertIsInstance(v, NSArray)
        self.assertEqual(v, range(5))

        v = OC_ArgSizeInArg.pid_array_(None, range(50))
        self.assertIs(v, None)

        v = OC_ArgSizeInArg.pid_array_(objc.NULL, range(50))
        self.assertIs(v, None)

    def test_float(self):
        with self.assertRaisesRegex(
            TypeError, "Don't know how to extract count from encoding: f"
        ):
            OC_ArgSizeInArg.float_array_(5.0, range(50))
