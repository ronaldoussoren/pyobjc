from PyObjCTools.TestSupport import *
import unittest
import objc
import sys
import ctypes

from PyObjCTools import TestSupport

try:
    long
except NameError:
    long = int

try:
    unicode
except NameError:
    unicode = str

class Method(object):
    def __init__(self, argno, meta, selector=False):
        self._selector = selector
        if argno is None:
            self._meta = {'retval': meta}
        else:
            self._meta = {'arguments': { argno: meta }}

    @property
    def __class__(self):
        if self._selector:
            return objc.selector

        else:
            return Method


    def __metadata__(self):
        return self._meta.copy()


class TestTestSupport (TestCase):
    def test_sdkForPython(self):
        orig_get_config_var = TestSupport._get_config_var
        try:
            config_result = ''
            def get_config_var(value):
                if value != 'CFLAGS':
                    raise KeyError(value)

                return config_result

            TestSupport._get_config_var = get_config_var
            cache = sdkForPython.func_defaults[0] if sys.version_info[0] == 2 else sdkForPython.__defaults__[0]

            config_result = ''
            self.assertEqual(sdkForPython(), None)
            self.assertEqual(cache, [None])
            self.assertEqual(sdkForPython(), None)
            self.assertEqual(cache, [None])

            cache[:] = []

            config_result = '-isysroot /Developer/SDKs/MacOSX10.6.sdk'
            self.assertEqual(sdkForPython(), (10, 6))
            self.assertEqual(cache, [(10,6)])
            self.assertEqual(sdkForPython(), (10, 6))
            self.assertEqual(cache, [(10,6)])

            cache[:] = []

            config_result = '-isysroot /'
            os_rel = tuple(map(int, os_release().split('.')))
            self.assertEqual(sdkForPython(), os_rel)
            self.assertEqual(cache, [os_rel])
            self.assertEqual(sdkForPython(), os_rel)
            self.assertEqual(cache, [os_rel])

            cache[:] = []

            config_result = '-dynamic -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.4u.sdk -arch i386 -arch x86_64'
            self.assertEqual(sdkForPython(), (10,4))
            self.assertEqual(cache, [(10,4)])
            self.assertEqual(sdkForPython(), (10,4))
            self.assertEqual(cache, [(10,4)])

            cache[:] = []

            config_result = '-dynamic -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -arch i386 -arch x86_64'
            self.assertEqual(sdkForPython(), (10,10))
            self.assertEqual(cache, [(10,10)])
            self.assertEqual(sdkForPython(), (10,10))
            self.assertEqual(cache, [(10,10)])

            cache[:] = []

        finally:
            TestSupport._get_config_var = orig_get_config_var

    def test_os_release(self):
        import platform
        TestSupport._os_release = '10.10'
        self.assertEqual(os_release(), '10.10')
        TestSupport._os_release = None

        self.assertEqual(TestSupport.os_release(), '.'.join(platform.mac_ver()[0].split('.')[:2]))

    def test_fourcc(self):
        import struct
        self.assertEqual(fourcc(b'abcd'), struct.unpack('>i', b'abcd')[0])

    def test_cast(self):
        c_int = ctypes.c_int()
        c_uint = ctypes.c_uint()

        for v in (0, 1, sys.maxsize, sys.maxsize+2, 1<<31, -1, -10):
            c_int.value = v
            c_uint.value = v
            self.assertEqual(c_int.value, TestSupport.cast_int(v))
            self.assertEqual(c_uint.value, TestSupport.cast_uint(v))

        c_longlong = ctypes.c_longlong()
        c_ulonglong = ctypes.c_ulonglong()
        for v in (0, 1, sys.maxsize, sys.maxsize+2, 1<<63, -1, -10):
            c_longlong.value = v
            c_ulonglong.value = v
            self.assertEqual(c_longlong.value, TestSupport.cast_longlong(v))
            self.assertEqual(c_ulonglong.value, TestSupport.cast_ulonglong(v))

    def testOnlyIf(self):

        def func_false():
            pass
        dec_false = onlyIf(1==2, "message")(func_false)

        def func_true():
            pass
        dec_true = onlyIf(1==1, "message")(func_true)

        self.assertIs(func_true, dec_true)
        self.assertIsNot(func_false, dec_false)

        if sys.version_info[:2] >= (2, 7):
            try:
                dec_false()
            except TestSupport._unittest.SkipTest:
                # OK
                pass

            else:
                self.fail("Not skipped?")

    def testOnlyPython(self):
        orig_version = sys.version_info

        try:
            sys.version_info = (2, 7, 3, '-')

            @onlyPython2
            def func_true():
                pass

            @onlyPython3
            def func_false():
                pass

            try:
                func_true()
            except TestSupport._unittest.SkipTest:
                self.fail("Unexpected skip for python 2")

            try:
                func_false()
            except TestSupport._unittest.SkipTest:
                pass

            else:
                self.fail("Unexpected non-skip for python 2")

            sys.version_info = (3, 3, 1, '-')

            @onlyPython2
            def func_false():
                pass

            @onlyPython3
            def func_true():
                pass

            try:
                func_true()
            except TestSupport._unittest.SkipTest:
                self.fail("Unexpected skip for python 2")

            try:
                func_false()
            except TestSupport._unittest.SkipTest:
                pass

            else:
                self.fail("Unexpected non-skip for python 2")

        finally:
            sys.version_info = orig_version

    def testOnlyBits(self):
        orig_size = sys.maxsize

        try:
            sys.maxsize = 2**30

            @onlyOn32Bit
            def func_true(): pass

            @onlyOn64Bit
            def func_false(): pass

            try:
                func_true()
            except TestSupport._unittest.SkipTest:
                self.fail("Unexpected skip for python 2")

            try:
                func_false()
            except TestSupport._unittest.SkipTest:
                pass

            else:
                self.fail("Unexpected non-skip for python 2")

            sys.maxsize = 2**60

            @onlyOn32Bit
            def func_false(): pass

            @onlyOn64Bit
            def func_true(): pass

            try:
                func_true()
            except TestSupport._unittest.SkipTest:
                self.fail("Unexpected skip for python 2")

            try:
                func_false()
            except TestSupport._unittest.SkipTest:
                pass

            else:
                self.fail("Unexpected non-skip for python 2")

        finally:
            sys.maxsize = orig_size

    def test_mxx_os_level(self):
        orig_os_release = TestSupport.os_release

        try:
            TestSupport.os_release = lambda: '10.5'

            @min_os_level('10.4')
            def func_true_1(): pass

            @min_os_level('10.5')
            def func_true_2(): pass

            @min_os_level('10.6')
            def func_false_1(): pass

            @max_os_level('10.5')
            def func_true_3(): pass

            @max_os_level('10.6')
            def func_true_4(): pass

            @max_os_level('10.4')
            def func_false_2(): pass



            for func_true in (func_true_1, func_true_2, func_true_3, func_true_4):
                try:
                    func_true()
                except TestSupport._unittest.SkipTest:
                    self.fail("Unexpected skip for python 2")

            for func_false in (func_false_1, func_false_2):
                try:
                    func_false()
                except TestSupport._unittest.SkipTest:
                    pass

                else:
                    self.fail("Unexpected non-skip for python 2")




        finally:
            TestSupport.os_release = orig_os_release


    def testIs32Bit(self):
        orig = sys.maxsize
        try:
            sys.maxsize = 2 ** 31 -1
            self.assertTrue(is32Bit())

            sys.maxsize = 2 ** 63 -1
            self.assertFalse(is32Bit())

        finally:
            sys.maxsize = orig


    def test_assert_cftype(self):
        self.assertRaises(AssertionError, self.assertIsCFType, long)
        self.assertRaises(AssertionError, self.assertIsCFType, objc.lookUpClass('NSObject'))
        self.assertRaises(AssertionError, self.assertIsCFType, objc.lookUpClass('NSCFType'))

        class OC_OPAQUE_TEST_1 (objc.lookUpClass('NSCFType')): pass
        try:
            self.assertIsCFType(OC_OPAQUE_TEST_1)
        except AssertionError:
            self.fail("CFType subclass not recognized as CFType")



    def test_assert_opaque(self):
        self.assertRaises(AssertionError, self.assertIsOpaquePointer, long)

        class N (object):
            @property
            def __pointer__(self):
                pass

        self.assertRaises(AssertionError, self.assertIsOpaquePointer, N)

        class N (object):
            __typestr__  = b"^q"

        self.assertRaises(AssertionError, self.assertIsOpaquePointer, N)

        class N (object):
            __typestr__  = b"^q"

            @property
            def __pointer__(self):
                pass

        try:
            self.assertIsOpaquePointer(N)

        except AssertionError:
            self.fail("assertIsOpaque fails on opaque pointer type")


    def test_assert_result_nullterminated(self):
        m = Method(None, {"c_array_delimited_by_null": True })
        self.assertResultIsNullTerminated(m)

        m = Method(None, {"c_array_delimited_by_null": False })
        self.assertRaises(AssertionError, self.assertResultIsNullTerminated, m)

        m = Method(None, {})
        self.assertRaises(AssertionError, self.assertResultIsNullTerminated, m)

    def test_assert_arg_nullterminated(self):
        m = Method(3, {"c_array_delimited_by_null": True }, selector=True)
        self.assertArgIsNullTerminated(m, 1)

        m = Method(3, {"c_array_delimited_by_null": False }, selector=True)
        self.assertRaises(AssertionError, self.assertArgIsNullTerminated, m, 1)

        m = Method(3, {}, selector=True)
        self.assertRaises(AssertionError, self.assertArgIsNullTerminated, m, 1)

        m = Method(3, {"c_array_delimited_by_null": True }, selector=False)
        self.assertArgIsNullTerminated(m, 3)

        m = Method(3, {"c_array_delimited_by_null": False }, selector=False)
        self.assertRaises(AssertionError, self.assertArgIsNullTerminated, m, 3)

        m = Method(3, {}, selector=False)
        self.assertRaises(AssertionError, self.assertArgIsNullTerminated, m, 3)



    def test_assert_arg_IN(self):
        m = Method(3, { "type": b"n^@" })
        try:
            self.assertArgIsIn(m, 3)
        except AssertionError:
            raise
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"n^@" }, selector=True)
        try:
            self.assertArgIsIn(m, 1)
        except AssertionError:
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"^@" })
        try:
            self.assertArgIsIn(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, { "type": b"^@" }, selector=True)
        try:
            self.assertArgIsIn(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_assert_arg_OUT(self):
        m = Method(3, { "type": b"o^@" })
        try:
            self.assertArgIsOut(m, 3)
        except AssertionError:
            raise
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"o^@" }, selector=True)
        try:
            self.assertArgIsOut(m, 1)
        except AssertionError:
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"^@" })
        try:
            self.assertArgIsOut(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, { "type": b"^@" }, selector=True)
        try:
            self.assertArgIsOut(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_assert_arg_INOUT(self):
        m = Method(3, { "type": b"N^@" })
        try:
            self.assertArgIsInOut(m, 3)
        except AssertionError:
            raise
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"N^@" }, selector=True)
        try:
            self.assertArgIsInOut(m, 1)
        except AssertionError:
            self.fail("test failure for input argument")

        m = Method(3, { "type": b"^@" })
        try:
            self.assertArgIsInOut(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, { "type": b"^@" }, selector=True)
        try:
            self.assertArgIsInOut(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_arg_bool(self):
        m = Method(3, { "type": objc._C_NSBOOL })
        try:
            self.assertArgIsBOOL(m, 3)
        except AssertionError:
            raise
            self.fail("unexpected test failure")

        m = Method(3, { "type": objc._C_NSBOOL }, selector=True)
        try:
            self.assertArgIsBOOL(m, 1)
        except AssertionError:
            self.fail("unexpected test failure")

        m = Method(3, { "type": b"@" })
        try:
            self.assertArgIsBOOL(m, 3)
        except AssertionError:
            pass
        else:
            self.fail("unexpected test pass")

        m = Method(3, { "type": b"@" }, selector=True)
        try:
            self.assertArgIsBOOL(m, 1)
        except AssertionError:
            pass

        else:
            self.fail("unexpected test pass")

    def test_result_bool(self):
        m = Method(None, { "type": objc._C_NSBOOL })
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            raise
            self.fail("unexpected test failure")

        m = Method(None, { "type": objc._C_NSBOOL }, selector=True)
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            self.fail("unexpected test failure")

        m = Method(None, { "type": b"@" })
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            pass
        else:
            self.fail("unexpected test pass")

        m = Method(None, { "type": b"@" }, selector=True)
        try:
            self.assertResultIsBOOL(m)
        except AssertionError:
            pass

        else:
            self.fail("unexpected test pass")


    def run(self, *args, **kwds):
        unittest.TestCase.run(self, *args, **kwds)


if __name__ == "__main__":
    main()
