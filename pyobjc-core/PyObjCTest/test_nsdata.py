import objc
import sys
from objc import super  # noqa: A004
from PyObjCTools.TestSupport import TestCase, min_python_release
from PyObjCTest.helpernsdata import OC_MutableDataHelper

NSData = objc.lookUpClass("NSData")
NSMutableData = objc.lookUpClass("NSMutableData")


class TestNSDataSupport(TestCase):
    # XXX: migrate test cases from Cocoa bindings!
    def testyRoBuffer(self):
        buf = NSData.alloc().init()
        self.assertEqual(len(buf), 0)

        self.assertEqual(buf.bytes(), b"")
        self.assertIsInstance(buf.bytes(), bytes)

        buf = NSData.dataWithData_(b"hello")
        self.assertIsInstance(buf, NSData)
        self.assertEqual(buf[0:1], b"h")
        self.assertEqual(buf[0:2], b"he")

        self.assertEqual(buf.bytes(), b"hello")
        self.assertIsInstance(buf.bytes(), memoryview)

        with self.assertRaises(TypeError):
            buf.bytes(1)

        view = memoryview(buf)
        self.assertEqual(bytes(view), buf.bytes())
        self.assertTrue(view.readonly)

    def testyRwBuffer(self):
        buf = NSMutableData.alloc().init()
        self.assertEqual(len(buf), 0)
        self.assertIsInstance(buf.mutableBytes(), memoryview)

        buf = NSMutableData.dataWithData_(b"hello")
        self.assertIsInstance(buf, NSMutableData)

        self.assertEqual(buf[0], ord("h"))

        buf[0] = ord("H")
        self.assertEqual(buf[0], ord("H"))

        self.assertEqual(buf.bytes(), b"Hello")
        self.assertIsInstance(buf.bytes(), memoryview)

        self.assertEqual(buf[0:2], b"He")
        buf[0:2] = b"hE"
        self.assertEqual(buf[0:2], b"hE")

        with self.assertRaises(TypeError):
            buf.bytes(1)

        with self.assertRaises(TypeError):
            buf.mutableBytes(1)

        vw = buf.mutableBytes()
        self.assertIsInstance(vw, memoryview)
        vw[0:1] = b"Y"
        self.assertEqual(buf.bytes(), b"YEllo")

        view = memoryview(buf)
        self.assertEqual(bytes(view), buf.bytes())
        self.assertFalse(view.readonly)

    def testNullHandling(self):
        nullBuffer = OC_MutableDataHelper.alloc().initWithScenario_(0)
        self.assertEqual(nullBuffer.bytes(), b"")
        self.assertIsInstance(nullBuffer.bytes(), bytes)

        self.assertEqual(nullBuffer.mutableBytes(), b"")
        self.assertIsInstance(nullBuffer.mutableBytes(), memoryview)

    def testExceptions(self):
        raisingBuffer = OC_MutableDataHelper.alloc().initWithScenario_(1)

        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            raisingBuffer.bytes()

        with self.assertRaisesRegex(objc.error, "SomeException - Some Reason"):
            raisingBuffer.mutableBytes()


class DataSubClass(NSData):
    def init(self):
        self = super().init()
        self._value = b"hello world"
        return self

    def length(self):
        if self._value is None:
            return 0
        return len(self._value)

    def bytes(self):  # noqa: A003
        return self._value


class MutableDataSubClass(NSMutableData):
    def init(self):
        self = super().init()
        self._value = bytearray(b"hello world")
        return self

    def length(self):
        if self._value is None:
            return 0
        return len(self._value)

    def bytes(self):  # noqa: A003
        return self._value

    def mutableBytes(self):
        return self._value


class TestSubclassing(TestCase):
    def testNSData(self):
        buf = DataSubClass.alloc().init()

        self.assertEqual(NSData.dataWithData_(buf), b"hello world")

        buf._value = None
        b = OC_MutableDataHelper.fetchBytesOf_(buf)
        self.assertIs(b, None)

        buf._value = 42
        with self.assertRaises(TypeError):
            OC_MutableDataHelper.fetchBytesOf_(buf)

    def testNSMutableData(self):
        buf = MutableDataSubClass.alloc().init()

        self.assertEqual(NSData.dataWithData_(buf), b"hello world")

        b = OC_MutableDataHelper.fetchMutableBytesOf_(buf)
        self.assertEqual(b, b"hello world")
        self.assertIsInstance(b, NSData)

        buf._value = None
        b = OC_MutableDataHelper.fetchMutableBytesOf_(buf)
        self.assertIs(b, None)

        b = OC_MutableDataHelper.fetchBytesOf_(buf)
        self.assertIs(b, None)

        buf._value = 42
        with self.assertRaises(TypeError):
            OC_MutableDataHelper.fetchBytesOf_(buf)

        with self.assertRaises(TypeError):
            OC_MutableDataHelper.fetchMutableBytesOf_(buf)

    def testCopyRO(self):
        orig = DataSubClass.alloc().init()
        copy = orig.copy()
        self.assertEqual(copy.bytes(), orig.bytes())
        self.assertIsInstance(copy, NSData)

    def testCopyRW(self):
        orig = MutableDataSubClass.alloc().init()
        copy = orig.copy()
        self.assertEqual(copy.bytes(), orig.bytes())
        self.assertIsInstance(copy, NSData)

        copy = orig.mutableCopy()
        self.assertEqual(copy.bytes(), orig.bytes())
        self.assertIsInstance(copy, NSMutableData)


class TestBytesInterface(TestCase):
    oc_cls = NSData
    py_cls = bytes

    def test_interface_methods(self):
        data = self.oc_cls.dataWithData_(b"hello world")
        meth_type = type(self.test_interface_methods)

        names = [nm for nm in dir(self.py_cls) if not nm.startswith("_")]
        for nm in names:
            if nm == "copy":
                continue
            with self.subTest(nm):
                m = getattr(data, nm)
                self.assertIsInstance(m, meth_type)

    def test_new(self):
        value = self.oc_cls(b"hello")
        self.assertIsInstance(value, self.oc_cls)
        self.assertEqual(value.bytes(), b"hello")

        value = self.oc_cls()
        self.assertIsInstance(value, self.oc_cls)
        self.assertEqual(value.bytes(), b"")

        value = self.oc_cls([1, 2, 3])
        self.assertIsInstance(value, self.oc_cls)
        self.assertEqual(value.bytes(), b"\x01\x02\x03")

    def test_capitalize(self):
        for val in (b"hello", b"HELLO", b"hELLO"):
            with self.subTest(val):
                oc = self.oc_cls.dataWithData_(val)
                py = self.py_cls(val)

                self.assertEqual(oc.capitalize(), py.capitalize())
                self.assertIsNot(oc.capitalize(), oc)

    def test_lower(self):
        for val in (b"hello", b"HELLO", b"hELLO"):
            with self.subTest(val):
                oc = self.oc_cls.dataWithData_(val)
                py = self.py_cls(val)

                self.assertEqual(oc.lower(), py.lower())
                self.assertIsNot(oc.lower(), oc)

    def test_upper(self):
        for val in (b"hello", b"HELLO", b"hELLO"):
            with self.subTest(val):
                oc = self.oc_cls.dataWithData_(val)
                py = self.py_cls(val)

                self.assertEqual(oc.upper(), py.upper())
                self.assertIsNot(oc.upper(), oc)

    def test_swapcase(self):
        for val in (b"hello", b"HELLO", b"hELLO"):
            with self.subTest(val):
                oc = self.oc_cls.dataWithData_(val)
                py = self.py_cls(val)

                self.assertEqual(oc.swapcase(), py.swapcase())
                self.assertIsNot(oc.swapcase(), oc)

    def test_center(self):
        val = b"hello"
        oc = self.oc_cls(val)
        py = self.py_cls(val)

        with self.subTest("too few arguments"):
            with self.assertRaises(TypeError):
                oc.center()

            with self.assertRaises(TypeError):
                py.center()

        with self.subTest("too many arguments"):
            with self.assertRaises(TypeError):
                oc.center(10, b" ", 9)

            with self.assertRaises(TypeError):
                py.center(10, b" ", 9)

        with self.subTest("bad argument types"):
            with self.assertRaises(TypeError):
                oc.center("10", b" ")

            with self.assertRaises(TypeError):
                py.center("10", b" ")

            with self.assertRaises(TypeError):
                oc.center(10, " ")

            with self.assertRaises(TypeError):
                py.center(10, " ")

        for i in (1, len(val), len(val) + 3, len(val) * 2):
            with self.subTest(f"center in {i}"):
                self.assertEqual(py.center(i), oc.center(i))

            with self.subTest(f"center in {i} with dashes"):
                self.assertEqual(py.center(i, b"-"), oc.center(i, b"-"))

    def test_count(self):
        val = b"aaabbccccd"
        needles = [b"a", b"b", b"c", b"d", b"e"]

        oc = self.oc_cls.dataWithData_(val)
        py = self.py_cls(val)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertEqual(oc.count(oc_needle), py.count(py_needle))
            self.assertEqual(oc.count(oc_needle), oc.count(py_needle))
            self.assertEqual(oc.count(oc_needle), py.count(oc_needle))

    def test_index(self):
        val = b"aaabbccccdd"
        needles = [b"a", b"b", b"c", b"d"]

        oc = self.oc_cls.dataWithData_(val)
        py = self.py_cls(val)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertEqual(oc.index(oc_needle), py.index(py_needle))
            self.assertEqual(oc.index(oc_needle), oc.index(py_needle))
            self.assertEqual(oc.index(oc_needle), py.index(oc_needle))

            self.assertEqual(oc.index(oc_needle, 1), py.index(oc_needle, 1))
            self.assertEqual(oc.index(oc_needle, 1, 20), py.index(oc_needle, 1, 20))

        with self.assertRaises(ValueError):
            oc.index(oc_needle, 1, 9)

        oc_needle = self.oc_cls.dataWithData_(b"e")
        py_needle = self.py_cls(b"e")

        with self.assertRaises(ValueError):
            oc.index(oc_needle)

        with self.assertRaises(ValueError):
            oc.index(py_needle)

        with self.assertRaises(ValueError):
            py.index(oc_needle)

        with self.assertRaises(ValueError):
            py.index(py_needle)

    def test_rindex(self):
        val = b"aaabbccccdd"
        needles = [b"a", b"b", b"c", b"d"]

        oc = self.oc_cls.dataWithData_(val)
        py = self.py_cls(val)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertEqual(oc.rindex(oc_needle), py.rindex(py_needle))
            self.assertEqual(oc.rindex(oc_needle), oc.rindex(py_needle))
            self.assertEqual(oc.rindex(oc_needle), py.rindex(oc_needle))

            self.assertEqual(oc.rindex(oc_needle, 1), py.rindex(oc_needle, 1))
            self.assertEqual(oc.rindex(oc_needle, 1, 20), py.rindex(oc_needle, 1, 20))

        with self.assertRaises(ValueError):
            oc.rindex(oc_needle, 1, 9)

        oc_needle = self.oc_cls.dataWithData_(b"e")
        py_needle = self.py_cls(b"e")

        with self.assertRaises(ValueError):
            oc.rindex(oc_needle)

        with self.assertRaises(ValueError):
            oc.rindex(py_needle)

        with self.assertRaises(ValueError):
            py.rindex(oc_needle)

        with self.assertRaises(ValueError):
            py.rindex(py_needle)

    def test_find(self):
        val = b"aaabbccccd"
        needles = [b"a", b"b", b"c", b"d", b"e"]

        oc = self.oc_cls.dataWithData_(val)
        py = self.py_cls(val)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertEqual(oc.find(oc_needle), py.find(py_needle))
            self.assertEqual(oc.find(oc_needle), oc.find(py_needle))
            self.assertEqual(oc.find(oc_needle), py.find(oc_needle))

            self.assertEqual(oc.find(oc_needle, 1), py.find(oc_needle, 1))
            self.assertEqual(oc.find(oc_needle, 1, 9), py.find(oc_needle, 1, 9))

    def test_rfind(self):
        val = b"aaabbccccd"
        needles = [b"a", b"b", b"c", b"d", b"e"]

        oc = self.oc_cls.dataWithData_(val)
        py = self.py_cls(val)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertEqual(oc.rfind(oc_needle), py.rfind(py_needle))
            self.assertEqual(oc.rfind(oc_needle), oc.rfind(py_needle))
            self.assertEqual(oc.rfind(oc_needle), py.rfind(oc_needle))

            self.assertEqual(oc.rfind(oc_needle, 1), py.rfind(py_needle, 1))
            self.assertEqual(oc.rfind(oc_needle, 1, 9), py.rfind(py_needle, 1, 9))
            self.assertEqual(oc.rfind(oc_needle, 5, 7), py.rfind(py_needle, 5, 7))

    def test_len(self):
        for value in (b"", b"hello"):
            oc = self.oc_cls.dataWithData_(value)
            py = self.py_cls(value)

            self.assertEqual(len(oc), len(py))
            self.assertEqual(len(oc), len(value))

    def test_as_bytes(self):
        value = b"hello wolrd"

        oc = self.oc_cls.dataWithData_(value)
        self.assertIsInstance(oc, self.oc_cls)

        py = self.py_cls(oc)
        self.assertEqual(py, value)
        self.assertIsInstance(py, self.py_cls)

    def test_str(self):
        for value in (b"", b"hello"):
            oc = self.oc_cls.dataWithData_(value)
            self.assertEqual(str(oc), str(value))

    def getitem(self):
        value = b"hello"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc[0], py[0])
        self.assertEqual(oc[1:3], py[1:3])

        self.assertEqual(oc[:3], py[:3])
        self.assertEqual(oc[3:], py[3:])

        self.assertEqual(oc[-8:], py[-8:])
        self.assertEqual(oc[2:9], py[2:9])

    def test_decode(self):
        value = b"hello"
        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.decode(), py.decode())
        self.assertEqual(oc.decode("latin1"), py.decode("latin1"))

        value = b"hello\xff"
        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        with self.assertRaises(UnicodeDecodeError):
            oc.decode("utf-8")

        with self.assertRaises(UnicodeDecodeError):
            py.decode("utf-8")

    def test_startswith(self):
        value = b"hello world"
        needles = [b"hello", b"world"]

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertIs(oc.startswith(py_needle), py.startswith(py_needle))
            self.assertIs(oc.startswith(py_needle), oc.startswith(oc_needle))
            self.assertIs(py.startswith(py_needle), oc.startswith(oc_needle))

        offset = 1
        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle[offset:])
            py_needle = self.py_cls(needle[offset:])

            self.assertIs(oc.startswith(py_needle, 1), py.startswith(py_needle, 1))
            self.assertIs(oc.startswith(py_needle, 1), oc.startswith(oc_needle, 1))
            self.assertIs(py.startswith(py_needle, 1), oc.startswith(oc_needle, 1))

            self.assertIs(
                oc.startswith(py_needle, 1, 3), py.startswith(py_needle, 1, 3)
            )
            self.assertIs(
                oc.startswith(py_needle, 1, 3), oc.startswith(oc_needle, 1, 3)
            )
            self.assertIs(
                py.startswith(py_needle, 1, 3), oc.startswith(oc_needle, 1, 3)
            )

    def test_endswith(self):
        value = b"hello world"
        needles = [b"hello", b"world"]

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle)
            py_needle = self.py_cls(needle)

            self.assertIs(oc.endswith(py_needle), py.endswith(py_needle))
            self.assertIs(oc.endswith(py_needle), oc.endswith(oc_needle))
            self.assertIs(py.endswith(py_needle), oc.endswith(oc_needle))

        offset = 1
        for needle in needles:
            oc_needle = self.oc_cls.dataWithData_(needle[:-offset])
            py_needle = self.py_cls(needle[:-offset])

            self.assertIs(
                oc.endswith(py_needle, 0, len(value) - 1),
                py.endswith(py_needle, 0, len(value) - 1),
            )
            self.assertIs(
                oc.endswith(py_needle, 0, len(value) - 1),
                oc.endswith(oc_needle, 0, len(value) - 1),
            )
            self.assertIs(
                py.endswith(py_needle, 0, len(value) - 1),
                oc.endswith(oc_needle, 0, len(value) - 1),
            )

    def test_char_types(self):
        values = [
            b"abc",
            b"123",
            b" ",
            b"a 3",
            b"a \xff",
            b"HELLO",
            b"Hello",
            b"Hello World",
            b"a42",
        ]
        methods = [
            "isalnum",
            "isalpha",
            "isdigit",
            "islower",
            "isspace",
            "istitle",
            "isupper",
        ]
        if sys.version_info[:2] >= (3, 7):
            methods.append("isascii")

        for meth in methods:
            for value in values:
                with self.subTest(method=meth, value=value):
                    oc = self.oc_cls.dataWithData_(value)
                    py = self.py_cls(value)

                    self.assertIs(getattr(oc, meth)(), getattr(py, meth)())

    def test_titlecase(self):
        values = [b"abc", b"hello world"]
        values += [n.upper() for n in values]

        for value in values:
            oc = self.oc_cls.dataWithData_(value)
            py = self.py_cls(value)

            self.assertEqual(oc.title(), py.title())

    @min_python_release("3.9")
    def test_removefx(self):
        value = b"hello world"
        needles = [b"he", b"rld"]

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for meth in ("removesuffix", "removeprefix"):
            for needle in needles:
                oc_needle = self.oc_cls.dataWithData_(needle)
                py_needle = self.py_cls(needle)

                self.assertEqual(
                    getattr(oc, meth)(py_needle), getattr(py, meth)(py_needle)
                )
                self.assertEqual(
                    getattr(oc, meth)(oc_needle), getattr(py, meth)(py_needle)
                )
                self.assertEqual(
                    getattr(oc, meth)(oc_needle), getattr(py, meth)(oc_needle)
                )

    def test_just(self):
        methods = ["ljust", "rjust"]
        value = b"hello"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for meth in methods:
            for width in (0, 5, 10):
                with self.subTest(meth=meth, width=width):
                    self.assertEqual(getattr(oc, meth)(width), getattr(py, meth)(width))
                    self.assertEqual(
                        getattr(oc, meth)(width, b"*"), getattr(py, meth)(width, b"*")
                    )

    def test_zfill(self):
        value = b"hello"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for width in (0, 5, 10):
            with self.subTest(width=width):
                self.assertEqual(oc.zfill(width), py.zfill(width))

    def test_strip(self):
        methods = ["strip", "lstrip", "rstrip"]
        value = b" hello "

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for meth in methods:
            with self.subTest(meth=meth):
                self.assertEqual(getattr(oc, meth)(), getattr(py, meth)())

        value = b"acabaac"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for meth in methods:
            with self.subTest(meth=meth):
                self.assertEqual(getattr(oc, meth)(b"ac"), getattr(py, meth)(b"ac"))

    def test_mul(self):
        value = b"hello "

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for idx in (0, 1, 8):
            self.assertEqual(oc * idx, py * idx)
            self.assertEqual(idx * oc, idx * py)

    def test_add(self):
        value = b"hello "

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc + b"world", py + b"world")
        self.assertEqual(b"world" + oc, b"world" + py)

    def test_expandtabs(self):
        value = b"a b\tc\td"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.expandtabs(), py.expandtabs())

        for size in (4, 8, 7):
            self.assertEqual(oc.expandtabs(size), py.expandtabs(size))
            self.assertEqual(oc.expandtabs(tabsize=size), py.expandtabs(tabsize=size))

    def test_fromhex(self):
        source = b"hello world".hex()

        oc = self.oc_cls.fromhex(source)
        py = self.py_cls.fromhex(source)

        self.assertEqual(oc, py)

        source = source[:4] + " " + source[4:]
        oc = self.oc_cls.fromhex(source)
        py = self.py_cls.fromhex(source)

    def test_hex(self):
        value = b"hello "

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.hex(), py.hex())

    def test_join(self):
        value = b", "
        lst = [b"a", b"b", b"c"]

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.join(lst), py.join(lst))

    def test_partition(self):
        methods = ["partition", "rpartition"]
        value = b"a=b=c"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for meth in methods:
            self.assertEqual(getattr(oc, meth)(b"="), getattr(py, meth)(b"="))

    def test_split(self):
        methods = ["split", "rsplit"]
        value = b"abc abc abc"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        for meth in methods:
            self.assertEqual(getattr(oc, meth)(), getattr(py, meth)())
            self.assertEqual(getattr(oc, meth)(None), getattr(py, meth)(None))
            self.assertEqual(getattr(oc, meth)(None, 1), getattr(py, meth)(None, 1))
            self.assertEqual(getattr(oc, meth)(b"b", 1), getattr(py, meth)(b"b", 1))

    def test_replace(self):
        value = b"abcabcabc"
        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.replace(b"ab", b"A"), py.replace(b"ab", b"A"))
        self.assertEqual(oc.replace(b"ab", b"A", 1), py.replace(b"ab", b"A", 1))

    def test_splitlines(self):
        value = b"a\nb\nc\r\nd"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.splitlines(), py.splitlines())

    def test_maketrans(self):
        self.assertEqual(
            self.oc_cls.maketrans(b"abc", b"DEF"), self.py_cls.maketrans(b"abc", b"DEF")
        )

    def test_translate(self):
        trans = bytes.maketrans(b"ab", b"DE")

        value = b"labrador"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        self.assertEqual(oc.translate(trans), py.translate(trans))
        self.assertEqual(oc.translate(trans, b"r"), py.translate(trans, b"r"))


class TestBytearrayInterface(TestBytesInterface):
    oc_cls = NSMutableData
    py_cls = bytearray

    def test_reverse(self):
        value = b"hello"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        oc.reverse()
        py.reverse()

        self.assertEqual(py, value[::-1])
        self.assertEqual(oc, value[::-1])

    def test_clear(self):
        value = b"hello"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        oc.clear()
        py.clear()

        self.assertEqual(py, b"")
        self.assertEqual(oc, b"")

    def test_remove(self):
        value = b"parser"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        oc.remove(ord(b"r"))
        py.remove(ord(b"r"))

        self.assertEqual(py, b"paser")
        self.assertEqual(oc, b"paser")

        with self.assertRaises(TypeError):
            oc.remove(b"r")
            py.remove(b"r")

        with self.assertRaises(ValueError):
            oc.remove(0)
            py.remove(0)

    def test_imul(self):
        value = b"parser"

        for idx in (0, 1, 10):
            oc = oc_orig = self.oc_cls.dataWithData_(value)
            py = py_orig = self.py_cls(value)

            oc *= idx
            py *= idx

            self.assertIs(oc, oc_orig)
            self.assertIs(py, py_orig)

            self.assertEqual(bytes(oc), value * idx)
            self.assertEqual(py, value * idx)

    def test_iadd(self):
        value = b"parser"

        oc = oc_orig = self.oc_cls.dataWithData_(value)
        py = py_orig = self.py_cls(value)

        oc += b" foo"
        py += b" foo"

        self.assertEqual(oc, py)
        self.assertIs(oc, oc_orig)
        self.assertIs(py, py_orig)

        with self.assertRaises(TypeError):
            oc += [1, 2, 3]

        with self.assertRaises(TypeError):
            py += [1, 2, 3]

    def test_extend(self):
        value = b"parser"

        oc = oc_orig = self.oc_cls.dataWithData_(value)
        py = py_orig = self.py_cls(value[:-1] + value[-1:])

        oc.extend(b" foo")
        py.extend(b" foo")

        self.assertEqual(py, oc)
        self.assertIs(oc, oc_orig)
        self.assertIs(py, py_orig)

        oc.extend([1, 2, 3])
        py.extend([1, 2, 3])

        self.assertEqual(oc, py)
        self.assertIs(oc, oc_orig)
        self.assertIs(py, py_orig)

    def test_setitem(self):
        value = b"parser"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        oc[0] = ord(b"P")
        py[0] = ord(b"P")

        self.assertEqual(oc, py)

        oc[1:3] = b"FL"
        py[1:3] = b"FL"

        self.assertEqual(oc, py)

        # XXX: The exceptions for OC and PY don't match
        # but that's ok for now
        with self.assertRaises((BufferError, ValueError)):
            oc[1:3] = b"X"

        with self.assertRaises((BufferError, ValueError)):
            py[1:3] = b"X"

    def test_delitem(self):
        value = b"parser" * 4

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        del oc[0]
        del py[0]

        self.assertEqual(py, oc)

        del oc[1:3]
        del py[1:3]

        self.assertEqual(py, oc)

        del oc[3::5]
        del py[3::5]

        self.assertEqual(oc, py)

        value = b"parser" * 4

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        del oc[20:0:-1]
        del py[20:0:-1]

        self.assertEqual(oc, py)

        value = b"parser" * 4

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        del oc[-2]
        del py[-2]

        self.assertEqual(oc, py)

        with self.assertRaisesRegex(IndexError, "index out of range"):
            del oc[-len(value)]

        with self.assertRaisesRegex(IndexError, "index out of range"):
            del py[-len(value)]

    def test_insert(self):
        value = b"abcdefg"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        oc.insert(3, 42)
        py.insert(3, 42)

        self.assertEqual(oc, py)

        with self.assertRaises(TypeError):
            oc.insert(3, b"a")

        with self.assertRaises(TypeError):
            py.insert(3, b"a")

    def test_append(self):
        value = b"abcdefg"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        oc.append(42)
        py.append(42)

        self.assertEqual(bytes(oc), py)

        with self.assertRaises(TypeError):
            oc.append(b"a")

        with self.assertRaises(TypeError):
            py.append(b"a")

    def test_pop(self):
        value = b"abcdefg"

        oc = self.oc_cls.dataWithData_(value)
        py = self.py_cls(value)

        o = oc.pop()
        p = py.pop()

        self.assertEqual(o, p)
        self.assertEqual(bytes(oc), py)

        o = oc.pop(3)
        p = py.pop(3)

        self.assertEqual(o, p)
        self.assertEqual(bytes(oc), py)

        o = oc.pop(-2)
        p = py.pop(-2)

        self.assertEqual(o, p)
        self.assertEqual(bytes(oc), py)

        with self.assertRaisesRegex(IndexError, "index out of range"):
            oc.pop(-2 * len(value))

        with self.assertRaisesRegex(IndexError, "index out of range"):
            py.pop(-22 * len(value))
