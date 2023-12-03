#
# Tests for NSArchiver/NSKeyedArchiver interop with pure ObjC code.
# That is, when a Python script uses an archiver to write out
# a data structure with basic python types (list, tuple, unicode,
# str, int, float) a pure ObjC program should be able to read
# that archive as a datastructure with the corresponding Cocoa
# classes.
import os
import datetime
import platform
import subprocess
import tempfile
from plistlib import loads

import objc
from PyObjCTools.TestSupport import (
    TestCase,
    os_release,
    os_level_key,
    cast_ulonglong,
    min_os_level,
)


MYDIR = os.path.dirname(os.path.abspath(__file__))


NSArray = objc.lookUpClass("NSArray")
NSArchiver = objc.lookUpClass("NSArchiver")
NSKeyedArchiver = objc.lookUpClass("NSKeyedArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")
NSKeyedUnarchiver = objc.lookUpClass("NSKeyedUnarchiver")
NSSet = objc.lookUpClass("NSSet")
NSString = objc.lookUpClass("NSString")


class TestNSKeyedArchivingInterop(TestCase):
    @classmethod
    def setUpClass(cls):
        src = os.path.join(MYDIR, "dump-nsarchive.m")
        dst = cls.progpath = os.path.join(MYDIR, "dump-nsarchive")

        subprocess.check_call(
            [
                "cc",
                "-o",
                dst,
                src,
                "-framework",
                "Foundation",
                "-DPyObjC_BUILD_RELEASE=%02d%02d"
                % (tuple(map(int, platform.mac_ver()[0].split(".")[:2]))),
            ]
        )

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.progpath):
            os.unlink(cls.progpath)

    def test_interop_date(self):
        testval = datetime.date.today()

        v = NSArray.arrayWithObject_(testval)
        data = NSKeyedArchiver.archivedDataWithRootObject_(v)
        if data is None:
            self.fail("Cannot create archive")

        with tempfile.NamedTemporaryFile() as fp:
            fp.write(data.bytes())
            fp.flush()

            converted = subprocess.check_output([self.progpath, "keyed", fp.name])

        converted = loads(converted)
        value = converted[0]
        self.assertIsInstance(value, datetime.datetime)
        # XXX: Checking the value itself is problematic because
        #      the datetime parser in plistlib is not timezone aware.
        # self.assertEqual(value.year, testval.year)
        # self.assertEqual(value.month, testval.month)
        # self.assertEqual(value.day, testval.day)

    def test_interop_datetime(self):
        testval = datetime.datetime.now()

        v = NSArray.arrayWithObject_(testval)
        data = NSKeyedArchiver.archivedDataWithRootObject_(v)
        if data is None:
            self.fail("Cannot create archive")

        with tempfile.NamedTemporaryFile() as fp:
            fp.write(data.bytes())
            fp.flush()

            converted = subprocess.check_output([self.progpath, "keyed", fp.name])

        converted = loads(converted)
        value = converted[0]
        self.assertIsInstance(value, datetime.datetime)

        # XXX: Checking the value itself is problematic because
        #      the datetime parser in plistlib is not timezone aware.
        # self.assertEqual(value, testval)

    def test_interop_float(self):
        for testval in (-4.5, 0, 5.5e10):
            v = NSArray.arrayWithObject_(testval)
            data = NSKeyedArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "keyed", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, [testval])

    def test_interop_int(self):
        for testval in (-42, 0, 42, -(2**62), 2**62, 2**63 + 10):
            with self.subTest(testval):
                v = NSArray.arrayWithObject_(testval)
                data = NSKeyedArchiver.archivedDataWithRootObject_(v)

                out = NSKeyedUnarchiver.unarchiveObjectWithData_(data)
                if testval > 2**63 and os_level_key(os_release()) < os_level_key(
                    "10.15"
                ):
                    # Bug in NSNumber
                    self.assertEqual(cast_ulonglong(out[0]), testval)
                else:
                    self.assertEqual(out[0], testval)

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output(
                        [self.progpath, "keyed", fp.name]
                    )

                converted = loads(converted)
                if testval > 2**63 and os_level_key(os_release()) < os_level_key(
                    "10.15"
                ):
                    self.assertEqual(cast_ulonglong(converted[0]), testval)
                else:
                    self.assertEqual(converted[0], testval)

    @min_os_level("10.12")
    def test_interop_int_overflow(self):
        # Known error on macOS 10.11
        testval = 2**64
        v = NSArray.arrayWithObject_(testval)
        data = NSKeyedArchiver.archivedDataWithRootObject_(v)

        with tempfile.NamedTemporaryFile() as fp:
            fp.write(data.bytes())
            fp.flush()

            with self.assertRaises(subprocess.CalledProcessError):
                subprocess.check_output([self.progpath, "keyed", fp.name])

    def test_interop_data(self):
        for testval in (b"hello world",):
            v = NSArray.arrayWithObject_(testval)
            data = NSKeyedArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "keyed", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, [testval])

    def test_interop_seq(self):
        for testval in (["a", "b", 3], ("a", "b", 3)):
            data = NSKeyedArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "keyed", fp.name])

            converted = loads(converted)
            self.assertIs(type(converted), list)
            self.assertEqual(converted, list(testval))

    def test_interop_set(self):
        for testval in ({"a", "b", 3}, frozenset({"a", "b", 3})):
            data = NSKeyedArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "keyed", fp.name])

            self.assertTrue(converted.startswith(b"{("))
            self.assertTrue(converted.endswith(b")}\n"))
            converted = b"{" + converted[2:-3] + b"}"
            converted = eval(converted.decode("utf-8"), {"a": "a", "b": "b"})
            self.assertEqual(converted, set(testval))

    def test_interop_dict(self):
        for testval in ({"a": "b", "c": 42},):
            data = NSKeyedArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "keyed", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, testval)


class TestNSArchivingInterop(TestCase):
    @classmethod
    def setUpClass(cls):
        src = os.path.join(MYDIR, "dump-nsarchive.m")
        dst = cls.progpath = os.path.join(MYDIR, "dump-nsarchive")

        subprocess.check_call(
            [
                "cc",
                "-o",
                dst,
                src,
                "-framework",
                "Foundation",
                "-DPyObjC_BUILD_RELEASE=%02d%02d"
                % (tuple(map(int, platform.mac_ver()[0].split(".")[:2]))),
            ]
        )

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.progpath):
            os.unlink(cls.progpath)

    def test_interop_string(self):
        for testval in ("hello world", "goodbye moon"):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, [testval])

    def test_interop_float(self):
        for testval in (-4.5, 0, 5.5e10):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, [testval])

    def test_interop_int(self):
        for testval in (-42, 0, 42, -(2**62), 2**62):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, [testval])

        testval = 2**64
        v = NSArray.arrayWithObject_(testval)
        data = NSArchiver.archivedDataWithRootObject_(v)

        with tempfile.NamedTemporaryFile() as fp:
            fp.write(data.bytes())
            fp.flush()

            with self.assertRaises(subprocess.CalledProcessError):
                subprocess.check_output([self.progpath, "plain", fp.name])

    def test_interop_data(self):
        for testval in (b"hello world",):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, [testval])

    def test_interop_seq(self):
        for testval in (["a", "b", 3], ("a", "b", 3)):
            data = NSArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            converted = loads(converted)
            self.assertIs(type(converted), list)
            self.assertEqual(converted, list(testval))

    def test_interop_set(self):
        for testval in ({"a", "b", 3}, frozenset({"a", "b", 3})):
            data = NSArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            self.assertTrue(converted.startswith(b"{("))
            self.assertTrue(converted.endswith(b")}\n"))
            converted = b"{" + converted[2:-3] + b"}"
            converted = eval(converted.decode("utf-8"), {"a": "a", "b": "b"})
            self.assertEqual(converted, set(testval))

    def test_interop_dict(self):
        for testval in ({"a": "b", "c": 42},):
            data = NSArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, "plain", fp.name])

            converted = loads(converted)
            self.assertEqual(converted, testval)


class Class1:
    pass


class Class2:
    pass


class Class3:
    def __init__(self):
        self.a = None
        self.b = None

    def __getstate__(self):
        return (self.a, self.b)

    def __setstate__(self, state):
        self.a, self.b = state


class Class4:
    def __init__(self):
        self.a = None
        self.b = None

    def __getstate__(self):
        return {"a": self.a, "b": self.b, NSString.stringWithString_("c"): self.c}


class TestLoadingOlderVersions(TestCase):
    def do_verify(self, path):
        import __main__

        # Ensure that class definitions are present:
        __main__.Class1 = Class1
        __main__.Class2 = Class2
        __main__.Class3 = Class3
        __main__.Class4 = Class4

        if path.endswith("keyed"):
            archiver = NSKeyedUnarchiver
        else:
            archiver = NSUnarchiver

        data = archiver.unarchiveObjectWithFile_(path)
        self.assertIsInstance(data, Class2)
        self.assertEqual(data.lst, [1, 2, 3])
        self.assertEqual(data.string, "hello world")
        self.assertIsInstance(data.obj, Class1)
        o = data.obj
        self.assertEqual(o.a, 42)
        self.assertEqual(o.b, 2.5)
        self.assertIsInstance(data.o3, Class3)
        self.assertIsInstance(data.o4, Class4)
        o = data.o3
        self.assertEqual(o.a, 42)
        self.assertEqual(o.b, 21)
        o = data.o4
        self.assertEqual(o.a, "A")
        self.assertEqual(o.b, "B")

    for fname in os.listdir(os.path.join(MYDIR, "archives")):

        def test(self, fname=fname):
            self.do_verify(os.path.join(MYDIR, "archives", fname))

        locals()["test_%s" % (fname.replace(".", "_").replace("-", "_"))] = test
        del test
