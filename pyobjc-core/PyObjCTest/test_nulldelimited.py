from PyObjCTools.TestSupport import TestCase
from PyObjCTest.nulldelimitedresult import OC_NullDelimitedResult

import objc

objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"intchars",
    {
        "retval": {
            "type": objc._C_PTR + objc._C_CHAR_AS_INT,
            "c_array_delimited_by_null": True,
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"chars2",
    {"retval": {"type": objc._C_PTR + objc._C_CHR, "c_array_delimited_by_null": True}},
)
objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"uchars2",
    {"retval": {"type": objc._C_PTR + objc._C_UCHR, "c_array_delimited_by_null": True}},
)

for selector in (
    b"voids",
    b"chars",
    b"uchars",
    b"shorts",
    b"ushorts",
    b"ints",
    b"uints",
    b"floats",
    b"objects",
    b"newrefsOfClass:",
    b"files",
):
    objc.registerMetaDataForSelector(
        b"OC_NullDelimitedResult",
        selector,
        {"retval": {"c_array_delimited_by_null": True}},
    )

objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"longs",
    {"retval": {"type": objc._C_PTR + objc._C_LNG, "c_array_delimited_by_null": True}},
)
objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"ulongs",
    {"retval": {"type": objc._C_PTR + objc._C_ULNG, "c_array_delimited_by_null": True}},
)
objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"longlongs",
    {
        "retval": {
            "type": objc._C_PTR + objc._C_LNG_LNG,
            "c_array_delimited_by_null": True,
        }
    },
)
objc.registerMetaDataForSelector(
    b"OC_NullDelimitedResult",
    b"ulonglongs",
    {
        "retval": {
            "type": objc._C_PTR + objc._C_ULNG_LNG,
            "c_array_delimited_by_null": True,
        }
    },
)


class TestNullDelimitedResult(TestCase):
    def test_metadata(self):
        for selector in (
            "chars",
            "chars2",
            "intchars",
            "voids",
            "chars",
            "uchars",
            "shorts",
            "ushorts",
            "ints",
            "uints",
            "longs",
            "ulongs",
            "longlongs",
            "ulonglongs",
            "floats",
            "objects",
            "newrefsOfClass_",
            "files",
        ):
            with self.subTest(selector):
                self.assertResultIsNullTerminated(
                    getattr(OC_NullDelimitedResult, selector)
                )

        self.assertResultHasType(OC_NullDelimitedResult.chars, objc._C_CHARPTR)
        self.assertResultHasType(
            OC_NullDelimitedResult.chars2, objc._C_PTR + objc._C_CHR
        )

        self.assertResultHasType(OC_NullDelimitedResult.uchars, objc._C_CHARPTR)
        self.assertResultHasType(
            OC_NullDelimitedResult.uchars2, objc._C_PTR + objc._C_UCHR
        )

        self.assertResultHasType(
            OC_NullDelimitedResult.longs, objc._C_PTR + objc._C_LNG
        )
        self.assertResultHasType(
            OC_NullDelimitedResult.ulongs, objc._C_PTR + objc._C_ULNG
        )

        self.assertResultHasType(
            OC_NullDelimitedResult.longlongs, objc._C_PTR + objc._C_LNG_LNG
        )
        self.assertResultHasType(
            OC_NullDelimitedResult.ulonglongs, objc._C_PTR + objc._C_ULNG_LNG
        )

    def test_values(self):
        for selector in (
            "intchars",
            "shorts",
            "ushorts",
            "ints",
            "uints",
            "longs",
            "ulongs",
            "longlongs",
            "ulonglongs",
        ):
            with self.subTest(selector):
                result = getattr(OC_NullDelimitedResult, selector)()
                self.assertIsInstance(result, tuple)
                self.assertEqual(len(result), 4)
                self.assertEqual(result, (1, 2, 3, 4))

        for selector in ("voids", "chars", "chars2", "uchars", "uchars2"):
            with self.subTest(selector):
                result = getattr(OC_NullDelimitedResult, selector)()
                self.assertIsInstance(result, bytes)
                self.assertEqual(len(result), 4)
                self.assertEqual(result, b"\x01\x02\x03\x04")

        with self.subTest("objects"):
            result = OC_NullDelimitedResult.objects()
            self.assertIsInstance(result, tuple)
            self.assertEqual(len(result), 4)
            self.assertEqual(result, ("one", "two", "three", "four"))

        with self.subTest("files"):
            result = OC_NullDelimitedResult.files()
            self.assertIsInstance(result, tuple)
            self.assertEqual(len(result), 2)
            self.assertIsInstance(result[0], objc.FILE)

        with self.subTest("floats"):
            with self.assertRaisesRegex(
                TypeError, "Cannot deal with NULL-terminated array of f"
            ):
                OC_NullDelimitedResult.floats()
