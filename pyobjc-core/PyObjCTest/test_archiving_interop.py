#
# Tests for NSArchiver/NSKeyedArchiver interop with pure ObjC code.
# That is, when a Python script uses an archiver to write out
# a data structure with basic python types (list, tuple, unicode,
# str, int, float) a pure ObjC program should be able to read
# that archive as a datastructure with the corresponding Cocoa
# classes.
from PyObjCTools.TestSupport import *

import objc
import subprocess
import tempfile
from distutils.sysconfig import get_config_var
import os
import sys

if sys.version_info[0] == 2:
    from plistlib import readPlistFromString as readPlistFromBytes, Data

else:
    from plistlib import readPlistFromBytes, Data


MYDIR = os.path.dirname(os.path.abspath(__file__))


NSArray = objc.lookUpClass('NSArray')
NSArchiver = objc.lookUpClass('NSArchiver')
NSKeyedArchiver = objc.lookUpClass('NSKeyedArchiver')
NSSet = objc.lookUpClass('NSSet')

class TestNSKeyedArchivingInterop (TestCase):
    @classmethod
    def setUpClass(cls):
        src = os.path.join(MYDIR, 'dump-nsarchive.m')
        dst = cls.progpath = os.path.join(MYDIR, 'dump-nsarchive')

        subprocess.check_call([
            'cc', '-o', dst, src, '-framework', 'Foundation'])

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.progpath):
            os.unlink(cls.progpath)

    def test_interop_string(self):
        for testval in (
                    b'hello world'.decode('utf-8'),
                    'goodbye moon',
                ):
            v = NSArray.arrayWithObject_(testval)
            data = NSKeyedArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [testval])

    def test_interop_float(self):
        for testval in (
                    -4.5,
                    0,
                    5.5e10,
                ):
            v = NSArray.arrayWithObject_(testval)
            data = NSKeyedArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [testval])

    def test_interop_int(self):
        for testval in (
                    -42,
                    0,
                    42,
                    -2**62,
                    2**62
                ):
            v = NSArray.arrayWithObject_(testval)
            data = NSKeyedArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [testval])

        testval = 2**64
        v = NSArray.arrayWithObject_(testval)
        data = NSKeyedArchiver.archivedDataWithRootObject_(v)

        with tempfile.NamedTemporaryFile() as fp:
            fp.write(data.bytes())
            fp.flush()

            self.assertRaises(subprocess.CalledProcessError, subprocess.check_output, [self.progpath, 'keyed', fp.name])

    @onlyPython3
    def test_interop_data(self):
        for testval in (
                    b'hello world',
                ):
            if sys.version_info[0] == 2:
                testval = buffer(testval)

            v = NSArray.arrayWithObject_(testval)
            data = NSKeyedArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [Data(testval)])

    def test_interop_seq(self):
        for testval in (
                    ["a", "b", 3],
                    ("a", "b", 3),
                ):

            data = NSKeyedArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertIs(type(converted), list)
            self.assertEqual(converted, list(testval))

    def test_interop_set(self):
        for testval in (
                    {"a", "b", 3},
                    frozenset({"a", "b", 3}),
                ):

            data = NSKeyedArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                subprocess.call([self.progpath, 'keyed', fp.name])
                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = eval(converted.decode('utf-8'), dict(a='a', b='b'))
            self.assertEqual(converted, set(testval))

    def test_interop_dict(self):
        for testval in (
                    {'a': 'b', 'c': 42 },
                ):

            data = NSKeyedArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, testval)

class TestNSArchivingInterop (TestCase):
    @classmethod
    def setUpClass(cls):
        src = os.path.join(MYDIR, 'dump-nsarchive.m')
        dst = cls.progpath = os.path.join(MYDIR, 'dump-nsarchive')

        subprocess.check_call([
            'cc', '-o', dst, src, '-framework', 'Foundation'])

    @classmethod
    def tearDownClass(cls):
        if os.path.exists(cls.progpath):
            os.unlink(cls.progpath)

    def test_interop_string(self):
        for testval in (
                    b'hello world'.decode('utf-8'),
                    'goodbye moon',
                ):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [testval])

    def test_interop_float(self):
        for testval in (
                    -4.5,
                    0,
                    5.5e10,
                ):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [testval])

    def test_interop_int(self):
        for testval in (
                    -42,
                    0,
                    42,
                    -2**62,
                    2**62
                ):
            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [testval])

        testval = 2**64
        v = NSArray.arrayWithObject_(testval)
        data = NSArchiver.archivedDataWithRootObject_(v)

        with tempfile.NamedTemporaryFile() as fp:
            fp.write(data.bytes())
            fp.flush()

            self.assertRaises(subprocess.CalledProcessError, subprocess.check_output, [self.progpath, 'plain', fp.name])

    @onlyPython3
    def test_interop_data(self):
        for testval in (
                    b'hello world',
                ):
            if sys.version_info[0] == 2:
                testval = buffer(testval)

            v = NSArray.arrayWithObject_(testval)
            data = NSArchiver.archivedDataWithRootObject_(v)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, [Data(testval)])

    def test_interop_seq(self):
        for testval in (
                    ["a", "b", 3],
                    ("a", "b", 3),
                ):

            data = NSArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertIs(type(converted), list)
            self.assertEqual(converted, list(testval))

    def test_interop_set(self):
        for testval in (
                    {"a", "b", 3},
                    frozenset({"a", "b", 3}),
                ):

            data = NSArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                subprocess.call([self.progpath, 'plain', fp.name])
                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = eval(converted.decode('utf-8'), dict(a='a', b='b'))
            self.assertEqual(converted, set(testval))

    def test_interop_dict(self):
        for testval in (
                    {'a': 'b', 'c': 42 },
                ):

            data = NSArchiver.archivedDataWithRootObject_(testval)

            with tempfile.NamedTemporaryFile() as fp:
                fp.write(data.bytes())
                fp.flush()

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            converted = readPlistFromBytes(converted)
            self.assertEqual(converted, testval)

if __name__ == "__main__":
    main()
