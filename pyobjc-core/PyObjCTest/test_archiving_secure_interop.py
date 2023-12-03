#
# Tests that validate that writing objects using
# secureCoding workings and can be read back in
# Objetive-C.
#
# SecureCoding is only supported for a number of
# builtin Python types (str, unicode, list, tuple,
# set, frozenset, dict) all of them excluding
# subclasses.
import os
import platform
import subprocess
import tempfile
import datetime

import objc
from PyObjCTools.TestSupport import TestCase, os_release, os_level_key, cast_ulonglong

from plistlib import loads


MYDIR = os.path.dirname(os.path.abspath(__file__))


NSArray = objc.lookUpClass("NSArray")
NSKeyedArchiver = objc.lookUpClass("NSKeyedArchiver")
NSUnarchiver = objc.lookUpClass("NSUnarchiver")
NSKeyedUnarchiver = objc.lookUpClass("NSKeyedUnarchiver")
NSSet = objc.lookUpClass("NSSet")

objc.registerMetaDataForSelector(
    b"NSKeyedArchiver",
    b"archivedDataWithRootObject:requiringSecureCoding:error:",
    {
        "arguments": {
            2 + 1: {"type": objc._C_NSBOOL},
            2 + 2: {"type_modifier": objc._C_OUT},
        }
    },
)

if os_level_key(os_release()) >= os_level_key("10.13"):
    # Secure coding was introduced in 10.13.

    class TestNSKeyedArchivingInterop(TestCase):
        @classmethod
        def setUpClass(cls):
            src = os.path.join(MYDIR, "dump-nsarchive-securecoding.m")
            dst = cls.progpath = os.path.join(MYDIR, "dump-nsarchive-securecoding")

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
            (
                data,
                error,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                v, True, None
            )

            if data is None:
                self.fail(f"Cannot create archive: {error}")

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, fp.name])

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
            (
                data,
                error,
            ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                v, True, None
            )

            if data is None:
                self.fail(f"Cannot create archive: {error}")

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, fp.name])

            converted = loads(converted)
            value = converted[0]
            self.assertIsInstance(value, datetime.datetime)

            # XXX: Checking the value itself is problematic because
            #      the datetime parser in plistlib is not timezone aware.
            # self.assertEqual(value, testval)

        def test_interop_string(self):
            for testval in ("hello world", "goodbye moon"):
                v = NSArray.arrayWithObject_(testval)
                (
                    data,
                    error,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    v, True, None
                )

                if data is None:
                    self.fail(f"Cannot create archive: {error}")

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output([self.progpath, fp.name])

                converted = loads(converted)
                self.assertEqual(converted, [testval])

        def test_interop_float(self):
            for testval in (-4.5, 0, 5.5e10):
                v = NSArray.arrayWithObject_(testval)
                (
                    data,
                    error,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    v, True, None
                )

                if data is None:
                    self.fail(f"Cannot create archive: {error}")

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output([self.progpath, fp.name])

                converted = loads(converted)
                self.assertEqual(converted, [testval])

        def test_interop_int(self):
            for testval in (-42, 0, 42, -(2**62), 2**62, 2**63 + 10):
                with self.subTest(testval):
                    v = NSArray.arrayWithObject_(testval)
                    (
                        data,
                        error,
                    ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                        v, True, None
                    )

                    if data is None:
                        self.fail(f"Cannot create archive: {error}")

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

                        converted = subprocess.check_output([self.progpath, fp.name])

                    converted = loads(converted)
                    if testval > 2**63 and os_level_key(os_release()) < os_level_key(
                        "10.15"
                    ):
                        # Bug in NSNumber
                        self.assertEqual(cast_ulonglong(converted[0]), testval)
                    else:
                        self.assertEqual(converted[0], testval)

            with self.subTest("overflow"):
                testval = 2**64
                v = NSArray.arrayWithObject_(testval)
                data = NSKeyedArchiver.archivedDataWithRootObject_(v)

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    with self.assertRaises(subprocess.CalledProcessError):
                        subprocess.check_output([self.progpath, fp.name])

        def test_interop_data(self):
            for testval in (b"hello world",):
                v = NSArray.arrayWithObject_(testval)
                (
                    data,
                    error,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    v, True, None
                )

                if data is None:
                    self.fail(f"Cannot create archive: {error}")

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output([self.progpath, fp.name])

                converted = loads(converted)
                self.assertEqual(converted, [testval])

        def test_interop_seq(self):
            for testval in (["a", "b", 3], ("a", "b", 3)):
                (
                    data,
                    error,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    testval, True, None
                )

                if data is None:
                    self.fail(f"Cannot create archive: {error}")

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output([self.progpath, fp.name])

                converted = loads(converted)
                self.assertIs(type(converted), list)
                self.assertEqual(converted, list(testval))

        def test_interop_set(self):
            for testval in ({"a", "b", 3}, frozenset({"a", "b", 3})):
                (
                    data,
                    error,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    testval, True, None
                )

                if data is None:
                    self.fail(f"Cannot create archive: {error}")

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output([self.progpath, fp.name])

                self.assertTrue(converted.startswith(b"{("))
                self.assertTrue(converted.endswith(b")}\n"))
                converted = b"{" + converted[2:-3] + b"}"
                converted = eval(converted.decode("utf-8"), {"a": "a", "b": "b"})

                self.assertEqual(converted, set(testval))

        def test_interop_dict(self):
            for testval in ({"a": "b", "c": 42},):
                (
                    data,
                    error,
                ) = NSKeyedArchiver.archivedDataWithRootObject_requiringSecureCoding_error_(
                    testval, True, None
                )

                if data is None:
                    self.fail(f"Cannot create archive: {error}")

                with tempfile.NamedTemporaryFile() as fp:
                    fp.write(data.bytes())
                    fp.flush()

                    converted = subprocess.check_output([self.progpath, fp.name])

                converted = loads(converted)
                self.assertEqual(converted, testval)
