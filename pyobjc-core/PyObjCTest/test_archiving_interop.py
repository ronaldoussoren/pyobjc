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
import platform

if sys.version_info[0] == 2:
    from plistlib import readPlistFromString as readPlistFromBytes, Data

else:
    from plistlib import readPlistFromBytes, Data


MYDIR = os.path.dirname(os.path.abspath(__file__))


NSArray = objc.lookUpClass('NSArray')
NSArchiver = objc.lookUpClass('NSArchiver')
NSKeyedArchiver = objc.lookUpClass('NSKeyedArchiver')
NSUnarchiver = objc.lookUpClass('NSUnarchiver')
NSKeyedUnarchiver = objc.lookUpClass('NSKeyedUnarchiver')
NSSet = objc.lookUpClass('NSSet')

class TestNSKeyedArchivingInterop (TestCase):
    @classmethod
    def setUpClass(cls):
        src = os.path.join(MYDIR, 'dump-nsarchive.m')
        dst = cls.progpath = os.path.join(MYDIR, 'dump-nsarchive')

        subprocess.check_call([
            'cc', '-o', dst, src, '-framework', 'Foundation',
            '-DPyObjC_BUILD_RELEASE=%02d%02d'%(tuple(map(int, platform.mac_ver()[0].split('.')[:2]))),
        ])

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

                converted = subprocess.check_output([self.progpath, 'keyed', fp.name])

            self.assertTrue(converted.startswith(b'{('))
            self.assertTrue(converted.endswith(b')}\n'))
            converted = b'{' + converted[2:-3] + b'}'
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
            'cc', '-o', dst, src, '-framework', 'Foundation',
            '-DPyObjC_BUILD_RELEASE=%02d%02d'%(tuple(map(int, platform.mac_ver()[0].split('.')[:2]))),
        ])

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

                converted = subprocess.check_output([self.progpath, 'plain', fp.name])

            self.assertTrue(converted.startswith(b'{('))
            self.assertTrue(converted.endswith(b')}\n'))
            converted = b'{' + converted[2:-3] + b'}'
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


class Class1:
    pass

class Class2 (object):
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
        return {'a': self.a, 'b': self.b, NSString.stringWithString_('c'): self.c}


class TestLoadingOlderVersions (TestCase):
    def do_verify(self, path):
        import __main__

        # Ensure that class definitions are present:
        __main__.Class1 = Class1
        __main__.Class2 = Class2
        __main__.Class3 = Class3
        __main__.Class4 = Class4

        if path.endswith('keyed'):
            archiver = NSKeyedUnarchiver
        else:
            archiver = NSUnarchiver

        data = archiver.unarchiveObjectWithFile_(path)
        self.assertIsInstance(data, Class2)
        self.assertEqual(data.lst, [1,2,3])
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
        self.assertEqual(o.a, 'A')
        self.assertEqual(o.b, 'B')


    for fname in os.listdir(os.path.join(MYDIR, 'archives')):
        def test(self, fname=fname):
            self.do_verify(os.path.join(MYDIR, 'archives', fname))
        locals()['test_%s'%(fname.replace('.', '_').replace('-', '_'))] = test
        del test


if __name__ == "__main__":
    main()
