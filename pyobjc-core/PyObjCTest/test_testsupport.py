import sys
import unittest

try:
    import ctypes
except ImportError:
    ctypes = None

import objc
from PyObjCTools import TestSupport
from PyObjCTools.TestSupport import (
    TestCase,
    sdkForPython,
    os_release,
    onlyIf,
    onlyPython2,
    onlyPython3,
    max_os_level,
    is32Bit,
    min_os_level,
    fourcc,
)


class Method(object):
    def __init__(self, argno, meta, selector=False):
        self._selector = selector
        if argno is None:
            self._meta = {"retval": meta}
        else:
            self._meta = {"arguments": {argno: meta}}

    @property
    def __class__(self):
        if self._selector:
            return objc.selector

        else:
            return Method

    def __metadata__(self):
        return self._meta.copy()


class TestTestSupport(TestCase):
    def test_sdkForPython(self):
        orig_get_config_var = TestSupport._get_config_var
        try:
            config_result = ""

            def get_config_var(value):
                if value != "CFLAGS":
                    raise KeyError(value)

                return config_result

            TestSupport._get_config_var = get_config_var
            cache = sdkForPython.__defaults__[0]

            config_result = ""
            self.assertEqual(sdkForPython(), None)
            self.assertEqual(cache, [None])
            self.assertEqual(sdkForPython(), None)
            self.assertEqual(cache, [None])

            cache[:] = []

            config_result = "-isysroot /Developer/SDKs/MacOSX10.6.sdk"
            self.assertEqual(sdkForPython(), (10, 6))
            self.assertEqual(cache, [(10, 6)])
            self.assertEqual(sdkForPython(), (10, 6))
            self.assertEqual(cache, [(10, 6)])

            cache[:] = []

            config_result = "-isysroot /"
            os_rel = tuple(map(int, os_release().split(".")))
            self.assertEqual(sdkForPython(), os_rel)
            self.assertEqual(cache, [os_rel])
            self.assertEqual(sdkForPython(), os_rel)
            self.assertEqual(cache, [os_rel])

            cache[:] = []

            config_result = "-dynamic -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.4u.sdk -arch i386 -arch x86_64"  # noqa: B950
            self.assertEqual(sdkForPython(), (10, 4))
            self.assertEqual(cache, [(10, 4)])
            self.assertEqual(sdkForPython(), (10, 4))
            self.assertEqual(cache, [(10, 4)])

            cache[:] = []

            config_result = "-dynamic -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.10.sdk -arch i386 -arch x86_64"  # noqa: B950
            self.assertEqual(sdkForPython(), (10, 10))
            self.assertEqual(cache, [(10, 10)])
            self.assertEqual(sdkForPython(), (10, 10))
            self.assertEqual(cache, [(10, 10)])

            cache[:] = []

        finally:
            TestSupport._get_config_var = orig_get_config_var

    def test_os_release(self):
        import platform

        TestSupport._os_release = "10.10"
        self.assertEqual(os_release(), "10.10")
        TestSupport._os_release = None

        self.assertEqual(
            TestSupport.os_release(), ".".join(platform.mac_ver()[0].split("."))
        )

    def test_fourcc(self):
        import struct

        self.assertEqual(fourcc(b"abcd"), struct.unpack(">i", b"abcd")[0])

    @onlyIf(ctypes is not None, "test requires ctypes")
    def test_cast(self):
        c_int = ctypes.c_int()
        c_uint = ctypes.c_uint()

        for v in (0, 1, sys.maxsize, sys.maxsize + 2, 1 << 31, -1, -10):
            c_int.value = v
            c_uint.value = v
            self.assertEqual(c_int.value, TestSupport.cast_int(v))
            self.assertEqual(c_uint.value, TestSupport.cast_uint(v))

        c_longlong = ctypes.c_longlong()
        c_ulonglong = ctypes.c_ulonglong()
        for v in (0, 1, sys.maxsize, sys.maxsize + 2, 1 << 63, -1, -10):
            c_longlong.value = v
            c_ulonglong.value = v
            self.assertEqual(c_longlong.value, TestSupport.cast_longlong(v))
            self.assertEqual(c_ulonglong.value, TestSupport.cast_ulonglong(v))

    def testOnlyIf(self):
        def func_false():
            pass

        dec_false = onlyIf(1 == 2, "message")(func_false)

        def func_true():
            pass

        dec_true = onlyIf(1 == 1, "message")(func_true)

        self.assertIs(func_true, dec_true)
        self.assertIsNot(func_false, dec_false)

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
            sys.version_info = (2, 7, 3, "-")

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

            sys.version_info = (3, 3, 1, "-")

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

    def test_mxx_os_level(self):
        orig_os_release = TestSupport.os_release

        try:
            TestSupport.os_release = lambda: "10.5"

            @min_os_level("10.4")
            def func_true_1():
                pass

            @min_os_level("10.5")
            def func_true_2():
                pass

            @min_os_level("10.6")
            def func_false_1():
                pass

            @max_os_level("10.5")
            def func_true_3():
                pass

            @max_os_level("10.6")
            def func_true_4():
                pass

            @max_os_level("10.4")
            def func_false_2():
                pass

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
            sys.maxsize = 2 ** 31 - 1
            self.assertTrue(is32Bit())

            sys.maxsize = 2 ** 63 - 1
            self.assertFalse(is32Bit())

        finally:
            sys.maxsize = orig

    def testAssertIsSubclass(self):
        self.assertIsSubclass(int, object)
        self.assertIsSubclass(str, object)
        self.assertIsSubclass(objc.objc_class, type)
        self.assertRaises(
            self.failureException,
            self.assertIsSubclass,
            objc.objc_class,
            objc.objc_object,
        )

    def testAssertIsNotSubclass(self):
        self.assertIsNotSubclass(object, int)
        self.assertRaises(
            self.failureException, self.assertIsNotSubclass, objc.objc_object, object
        )

    def testAssertIsIstance(self):
        self.assertIsInstance(object(), object)
        self.assertIsInstance(42, object)
        self.assertIsInstance(42, (int, str))

        self.assertRaises(self.failureException, self.assertIsInstance, 42, str)

    def test_assert_cftype(self):
        self.assertRaises(self.failureException, self.assertIsCFType, int)
        self.assertRaises(
            self.failureException, self.assertIsCFType, objc.lookUpClass("NSCFType")
        )

        # 'assertIsCFType' primarily tests that a type is either tollfree bridged, or
        # has a distinct type that is different from the default NSCFType 'placeholder' type.
        # self.assertIsCFType(objc.lookUpClass('NSObject'))
        self.assertRaises(
            self.failureException, self.assertIsCFType, objc.lookUpClass("NSObject")
        )

        class OC_OPAQUE_TEST_1(objc.lookUpClass("NSCFType")):
            pass

        try:
            self.assertIsCFType(OC_OPAQUE_TEST_1)
        except self.failureException:
            self.fail("CFType subclass not recognized as CFType")

    def test_assert_opaque(self):
        self.assertRaises(self.failureException, self.assertIsOpaquePointer, int)

        class N(object):
            @property
            def __pointer__(self):
                pass

        self.assertRaises(self.failureException, self.assertIsOpaquePointer, N)

        class N(object):
            __typestr__ = b"^q"

        self.assertRaises(self.failureException, self.assertIsOpaquePointer, N)

        class N(object):
            __typestr__ = b"^q"

            @property
            def __pointer__(self):
                pass

        try:
            self.assertIsOpaquePointer(N)

        except self.failureException:
            self.fail("assertIsOpaque fails on opaque pointer type")

    def test_assert_result_nullterminated(self):
        m = Method(None, {"c_array_delimited_by_null": True})
        self.assertResultIsNullTerminated(m)

        m = Method(None, {"c_array_delimited_by_null": False})
        self.assertRaises(self.failureException, self.assertResultIsNullTerminated, m)

        m = Method(None, {})
        self.assertRaises(self.failureException, self.assertResultIsNullTerminated, m)

    def test_assert_arg_nullterminated(self):
        m = Method(3, {"c_array_delimited_by_null": True}, selector=True)
        self.assertArgIsNullTerminated(m, 1)
        self.assertRaises(self.failureException, self.assertArgIsNullTerminated, m, 0)

        m = Method(3, {"c_array_delimited_by_null": False}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsNullTerminated, m, 1)

        m = Method(3, {}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsNullTerminated, m, 1)

        m = Method(3, {"c_array_delimited_by_null": True}, selector=False)
        self.assertArgIsNullTerminated(m, 3)
        self.assertRaises(self.failureException, self.assertArgIsNullTerminated, m, 2)

        m = Method(3, {"c_array_delimited_by_null": False}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsNullTerminated, m, 3)

        m = Method(3, {}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsNullTerminated, m, 3)

    def test_function_nullterminated(self):
        m = Method(None, {}, selector=False)
        m._meta.update({"variadic": True, "c_array_delimited_by_null": True})
        self.assertIsNullTerminated(m)

        m._meta["variadic"] = False
        self.assertRaises(self.failureException, self.assertIsNullTerminated, m)

        m._meta["variadic"] = True
        m._meta["c_array_delimited_by_null"] = False
        self.assertRaises(self.failureException, self.assertIsNullTerminated, m)

        del m._meta["variadic"]
        m._meta["c_array_delimited_by_null"] = True
        self.assertRaises(self.failureException, self.assertIsNullTerminated, m)

        m = Method(None, {}, selector=True)
        m._meta.update({"variadic": True, "c_array_delimited_by_null": True})
        self.assertIsNullTerminated(m)

        m._meta["variadic"] = False
        self.assertRaises(self.failureException, self.assertIsNullTerminated, m)

        m._meta["variadic"] = True
        m._meta["c_array_delimited_by_null"] = False
        self.assertRaises(self.failureException, self.assertIsNullTerminated, m)

        del m._meta["variadic"]
        m._meta["c_array_delimited_by_null"] = True
        self.assertRaises(self.failureException, self.assertIsNullTerminated, m)

    def test_arg_varialbe_size(self):
        m = Method(3, {"c_array_of_variable_length": True}, selector=True)
        self.assertArgIsVariableSize(m, 1)
        self.assertRaises(self.failureException, self.assertArgIsVariableSize, m, 0)

        m = Method(3, {"c_array_of_variable_length": False}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsVariableSize, m, 1)

        m = Method(3, {"c_array_of_variable_length": True}, selector=False)
        self.assertArgIsVariableSize(m, 3)
        self.assertRaises(self.failureException, self.assertArgIsVariableSize, m, 1)

        m = Method(3, {"c_array_of_variable_length": False}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsVariableSize, m, 3)

    def test_result_varialbe_size(self):
        m = Method(None, {"c_array_of_variable_length": True}, selector=True)
        self.assertResultIsVariableSize(m, 1)

        m = Method(None, {"c_array_of_variable_length": False}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsVariableSize, m, 1)

        m = Method(None, {}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsVariableSize, m, 1)

    def test_argsize_in_result(self):
        m = Method(3, {"c_array_length_in_result": True}, selector=True)
        self.assertArgSizeInResult(m, 1)
        self.assertRaises(self.failureException, self.assertArgSizeInResult, m, 0)

        m = Method(3, {"c_array_length_in_result": False}, selector=True)
        self.assertRaises(self.failureException, self.assertArgSizeInResult, m, 1)

        m = Method(3, {}, selector=True)
        self.assertRaises(self.failureException, self.assertArgSizeInResult, m, 1)

        m = Method(3, {"c_array_length_in_result": True}, selector=False)
        self.assertArgSizeInResult(m, 3)
        self.assertRaises(self.failureException, self.assertArgSizeInResult, m, 2)

        m = Method(3, {"c_array_length_in_result": False}, selector=True)
        self.assertRaises(self.failureException, self.assertArgSizeInResult, m, 3)

        m = Method(3, {}, selector=True)
        self.assertRaises(self.failureException, self.assertArgSizeInResult, m, 3)

    def test_arg_printf(self):
        m = Method(3, {"printf_format": True}, selector=True)
        m._meta["variadic"] = True
        self.assertArgIsPrintf(m, 1)
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 0)

        m._meta["variadic"] = False
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 1)

        m._meta["variadic"] = True
        m._meta["arguments"][3]["printf_format"] = False
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 1)

        m._meta["variadic"] = True
        del m._meta["arguments"][3]["printf_format"]
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 1)

        m = Method(3, {"printf_format": True}, selector=False)
        m._meta["variadic"] = True
        self.assertArgIsPrintf(m, 3)
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 2)

        m._meta["variadic"] = False
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 3)

        m._meta["variadic"] = True
        m._meta["arguments"][3]["printf_format"] = False
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 3)

        m._meta["variadic"] = True
        del m._meta["arguments"][3]["printf_format"]
        self.assertRaises(self.failureException, self.assertArgIsPrintf, m, 3)

    def test_arg_cfretained(self):
        m = Method(3, {"already_cfretained": True}, selector=True)
        self.assertArgIsCFRetained(m, 1)
        self.assertRaises(self.failureException, self.assertArgIsCFRetained, m, 0)

        m = Method(3, {"already_cfretained": False}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsCFRetained, m, 1)

        m = Method(3, {}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsCFRetained, m, 1)

        m = Method(3, {"already_cfretained": True}, selector=False)
        self.assertArgIsCFRetained(m, 3)
        self.assertRaises(self.failureException, self.assertArgIsCFRetained, m, 2)

        m = Method(3, {"already_cfretained": False}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsCFRetained, m, 3)

        m = Method(3, {}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsCFRetained, m, 3)

    def test_arg_not_cfretained(self):
        m = Method(3, {"already_cfretained": True}, selector=True)
        self.assertArgIsNotCFRetained(m, 0)
        self.assertRaises(self.failureException, self.assertArgIsNotCFRetained, m, 1)

        m = Method(3, {"already_cfretained": False}, selector=True)
        self.assertArgIsNotCFRetained(m, 1)

        m = Method(3, {}, selector=True)
        self.assertArgIsNotCFRetained(m, 1)

        m = Method(3, {"already_cfretained": True}, selector=False)
        self.assertArgIsCFRetained(m, 3)
        self.assertArgIsNotCFRetained(m, 1)

        m = Method(3, {"already_cfretained": False}, selector=False)
        self.assertArgIsNotCFRetained(m, 1)

        m = Method(3, {}, selector=False)
        self.assertArgIsNotCFRetained(m, 1)

    def test_result_cfretained(self):
        m = Method(None, {"already_cfretained": True})
        self.assertResultIsCFRetained(m)

        m = Method(None, {"already_cfretained": False})
        self.assertRaises(self.failureException, self.assertResultIsCFRetained, m)

        m = Method(None, {})
        self.assertRaises(self.failureException, self.assertResultIsCFRetained, m)

    def test_result_not_cfretained(self):
        m = Method(None, {"already_cfretained": True})
        self.assertRaises(self.failureException, self.assertResultIsNotCFRetained, m)

        m = Method(None, {"already_cfretained": False})
        self.assertResultIsNotCFRetained(m)

        m = Method(None, {})
        self.assertResultIsNotCFRetained(m)

    def test_arg_type(self):
        m = Method(3, {"type": objc._C_DBL}, selector=True)
        self.assertArgHasType(m, 1, objc._C_DBL)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 2, objc._C_ID
        )
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 1, objc._C_ID
        )

        m = Method(3, {}, selector=True)
        self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {"type": objc._C_LNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_LNG)
        self.assertArgHasType(m, 1, objc._C_LNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 1, objc._C_ID
        )

        m = Method(3, {"type": objc._C_ULNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_ULNG)
        self.assertArgHasType(m, 1, objc._C_ULNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 1, objc._C_ID
        )

        m = Method(3, {"type": objc._C_LNG_LNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_LNG)
        self.assertArgHasType(m, 1, objc._C_LNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 1, objc._C_ID
        )

        m = Method(3, {"type": objc._C_ULNG_LNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_ULNG)
        self.assertArgHasType(m, 1, objc._C_ULNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 1, objc._C_ID
        )

        m = Method(3, {"type": objc._C_DBL}, selector=False)
        self.assertArgHasType(m, 3, objc._C_DBL)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 3, objc._C_ID
        )
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 2, objc._C_ID
        )

        m = Method(3, {}, selector=False)
        self.assertArgHasType(m, 3, objc._C_ID)

        m = Method(3, {"type": objc._C_LNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_LNG)
        self.assertArgHasType(m, 3, objc._C_LNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 3, objc._C_ID
        )

        m = Method(3, {"type": objc._C_ULNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_ULNG)
        self.assertArgHasType(m, 3, objc._C_ULNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 3, objc._C_ID
        )

        m = Method(3, {"type": objc._C_LNG_LNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_LNG)
        self.assertArgHasType(m, 3, objc._C_LNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 3, objc._C_ID
        )

        m = Method(3, {"type": objc._C_ULNG_LNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_ULNG)
        self.assertArgHasType(m, 3, objc._C_ULNG_LNG)
        self.assertRaises(
            self.failureException, self.assertArgHasType, m, 3, objc._C_ID
        )

    def test_result_type(self):
        m = Method(None, {})
        self.assertResultHasType(m, objc._C_VOID)
        self.assertRaises(
            self.failureException, self.assertResultHasType, m, objc._C_ID
        )

        m = Method(None, {"type": objc._C_DBL})
        self.assertResultHasType(m, objc._C_DBL)
        self.assertRaises(
            self.failureException, self.assertResultHasType, m, objc._C_ID
        )

        m = Method(None, {"type": objc._C_LNG}, selector=False)
        self.assertResultHasType(m, objc._C_LNG)
        self.assertResultHasType(m, objc._C_LNG_LNG)
        self.assertRaises(
            self.failureException, self.assertResultHasType, m, objc._C_ID
        )

        m = Method(None, {"type": objc._C_ULNG}, selector=False)
        self.assertResultHasType(m, objc._C_ULNG)
        self.assertResultHasType(m, objc._C_ULNG_LNG)
        self.assertRaises(
            self.failureException, self.assertResultHasType, m, objc._C_ID
        )

        m = Method(None, {"type": objc._C_LNG_LNG}, selector=False)
        self.assertResultHasType(m, objc._C_LNG)
        self.assertResultHasType(m, objc._C_LNG_LNG)
        self.assertRaises(
            self.failureException, self.assertResultHasType, m, objc._C_ID
        )

        m = Method(None, {"type": objc._C_ULNG_LNG}, selector=False)
        self.assertResultHasType(m, objc._C_ULNG)
        self.assertResultHasType(m, objc._C_ULNG_LNG)
        self.assertRaises(
            self.failureException, self.assertResultHasType, m, objc._C_ID
        )

    def test_arg_fixed_size(self):
        m = Method(3, {"c_array_of_fixed_length": 42}, selector=True)
        self.assertArgIsFixedSize(m, 1, 42)
        self.assertRaises(self.failureException, self.assertArgIsFixedSize, m, 0, 42)
        self.assertRaises(self.failureException, self.assertArgIsFixedSize, m, 1, 3)

        m = Method(3, {}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsFixedSize, m, 1, 3)

        m = Method(3, {"c_array_of_fixed_length": 42}, selector=False)
        self.assertArgIsFixedSize(m, 3, 42)
        self.assertRaises(self.failureException, self.assertArgIsFixedSize, m, 2, 42)
        self.assertRaises(self.failureException, self.assertArgIsFixedSize, m, 3, 3)

        m = Method(3, {}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsFixedSize, m, 3, 3)

    def test_result_fixed_size(self):
        m = Method(None, {"c_array_of_fixed_length": 42})
        self.assertResultIsFixedSize(m, 42)
        self.assertRaises(self.failureException, self.assertResultIsFixedSize, m, 3)

        m = Method(None, {}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsFixedSize, m, 3)

    def test_arg_size_in_arg(self):
        m = Method(3, {"c_array_length_in_arg": 4}, selector=True)
        self.assertArgSizeInArg(m, 1, 2)
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 1, 3)
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 0, 3)

        m = Method(3, {"c_array_length_in_arg": (2, 4)}, selector=True)
        self.assertArgSizeInArg(m, 1, (0, 2))
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 1, (0, 3))
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 0, (1, 2))

        m = Method(3, {"c_array_length_in_arg": 4}, selector=False)
        self.assertArgSizeInArg(m, 3, 4)
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 1, 3)
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 0, 3)

        m = Method(3, {"c_array_length_in_arg": (2, 4)}, selector=False)
        self.assertArgSizeInArg(m, 3, (2, 4))
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 1, (2, 3))
        self.assertRaises(self.failureException, self.assertArgSizeInArg, m, 0, (2, 3))

    def test_result_ize_in_arg(self):
        m = Method(None, {"c_array_length_in_arg": 4}, selector=True)
        self.assertResultSizeInArg(m, 2)
        self.assertRaises(self.failureException, self.assertResultSizeInArg, m, 3)
        self.assertRaises(self.failureException, self.assertResultSizeInArg, m, 3)

        m = Method(None, {"c_array_length_in_arg": 4}, selector=False)
        self.assertResultSizeInArg(m, 4)
        self.assertRaises(self.failureException, self.assertResultSizeInArg, m, 3)

    def test_arg_retained(self):
        m = Method(3, {"already_retained": True}, selector=True)
        self.assertArgIsRetained(m, 1)
        self.assertRaises(self.failureException, self.assertArgIsRetained, m, 0)

        m = Method(3, {"already_retained": False}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsRetained, m, 1)

        m = Method(3, {}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsRetained, m, 1)

        m = Method(3, {"already_retained": True}, selector=False)
        self.assertArgIsRetained(m, 3)
        self.assertRaises(self.failureException, self.assertArgIsRetained, m, 2)

        m = Method(3, {"already_retained": False}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsRetained, m, 3)

        m = Method(3, {}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsRetained, m, 3)

    def test_arg_not_retained(self):
        m = Method(3, {"already_retained": True}, selector=True)
        self.assertArgIsNotRetained(m, 0)
        self.assertRaises(self.failureException, self.assertArgIsNotRetained, m, 1)

        m = Method(3, {"already_retained": False}, selector=True)
        self.assertArgIsNotRetained(m, 1)

        m = Method(3, {}, selector=True)
        self.assertArgIsNotRetained(m, 1)

        m = Method(3, {"already_retained": True}, selector=False)
        self.assertArgIsRetained(m, 3)
        self.assertArgIsNotRetained(m, 1)

        m = Method(3, {"already_retained": False}, selector=False)
        self.assertArgIsNotRetained(m, 1)

        m = Method(3, {}, selector=False)
        self.assertArgIsNotRetained(m, 1)

    def test_result_retained(self):
        m = Method(None, {"already_retained": True})
        self.assertResultIsRetained(m)

        m = Method(None, {"already_retained": False})
        self.assertRaises(self.failureException, self.assertResultIsRetained, m)

        m = Method(None, {})
        self.assertRaises(self.failureException, self.assertResultIsRetained, m)

    def test_result_not_retained(self):
        m = Method(None, {"already_retained": True})
        self.assertRaises(self.failureException, self.assertResultIsNotRetained, m)

        m = Method(None, {"already_retained": False})
        self.assertResultIsNotRetained(m)

        m = Method(None, {})
        self.assertResultIsNotRetained(m)

    def test_assert_arg_IN(self):
        m = Method(3, {"type": b"n^@"})
        try:
            self.assertArgIsIn(m, 3)
        except self.failureException:
            raise
            self.fail("test failure for input argument")

        m = Method(3, {"type": b"n^@"}, selector=True)
        try:
            self.assertArgIsIn(m, 1)
        except self.failureException:
            self.fail("test failure for input argument")

        m = Method(3, {"type": b"^@"})
        try:
            self.assertArgIsIn(m, 3)
        except self.failureException:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, {"type": b"^@"}, selector=True)
        try:
            self.assertArgIsIn(m, 1)
        except self.failureException:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_assert_arg_OUT(self):
        m = Method(3, {"type": b"o^@"})
        try:
            self.assertArgIsOut(m, 3)
        except self.failureException:
            raise
            self.fail("test failure for input argument")

        m = Method(3, {"type": b"o^@"}, selector=True)
        try:
            self.assertArgIsOut(m, 1)
        except self.failureException:
            self.fail("test failure for input argument")

        m = Method(3, {"type": b"^@"})
        try:
            self.assertArgIsOut(m, 3)
        except self.failureException:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, {"type": b"^@"}, selector=True)
        try:
            self.assertArgIsOut(m, 1)
        except self.failureException:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_assert_arg_INOUT(self):
        m = Method(3, {"type": b"N^@"})
        try:
            self.assertArgIsInOut(m, 3)
        except self.failureException:
            raise
            self.fail("test failure for input argument")

        m = Method(3, {"type": b"N^@"}, selector=True)
        try:
            self.assertArgIsInOut(m, 1)
        except self.failureException:
            self.fail("test failure for input argument")

        m = Method(3, {"type": b"^@"})
        try:
            self.assertArgIsInOut(m, 3)
        except self.failureException:
            pass
        else:
            self.fail("test pass for not-input argument")

        m = Method(3, {"type": b"^@"}, selector=True)
        try:
            self.assertArgIsInOut(m, 1)
        except self.failureException:
            pass

        else:
            self.fail("test pass for not-input argument")

    def test_arg_bool(self):
        m = Method(3, {"type": objc._C_NSBOOL})
        try:
            self.assertArgIsBOOL(m, 3)
        except self.failureException:
            raise
            self.fail("unexpected test failure")

        m = Method(3, {"type": objc._C_NSBOOL}, selector=True)
        try:
            self.assertArgIsBOOL(m, 1)
        except self.failureException:
            self.fail("unexpected test failure")

        m = Method(3, {"type": b"@"})
        try:
            self.assertArgIsBOOL(m, 3)
        except self.failureException:
            pass
        else:
            self.fail("unexpected test pass")

        m = Method(3, {"type": b"@"}, selector=True)
        try:
            self.assertArgIsBOOL(m, 1)
        except self.failureException:
            pass

        else:
            self.fail("unexpected test pass")

    def test_arg_is_sel(self):
        m = Method(3, {"type": objc._C_SEL, "sel_of_type": b"v@:@"}, selector=True)
        self.assertArgIsSEL(m, 1, b"v@:@")

        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 2, b"v@:@")
        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 1, b"v@:")

        m = Method(3, {"type": objc._C_SEL}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 1, b"v@:")

        m = Method(3, {"type": objc._C_ID, "sel_of_type": b"v@:@"}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 1, b"v@:@")

        m = Method(3, {"type": objc._C_SEL, "sel_of_type": b"v@:@"}, selector=False)
        self.assertArgIsSEL(m, 3, b"v@:@")

        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 2, b"v@:@")
        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 3, b"v@:")

        m = Method(3, {"type": objc._C_SEL}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 3, b"v@:")

        m = Method(3, {"type": objc._C_ID, "sel_of_type": b"v@:@"}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsSEL, m, 3, b"v@:@")

    def test_arg_is_function(self):
        m = Method(
            3,
            {
                "type": b"^?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
            },
            selector=True,
        )
        self.assertArgIsFunction(m, 1, b"i@d", False)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 0, "v", False
        )
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, "i@b", False
        )
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, "i@d", True
        )
        m = Method(
            3,
            {
                "type": b"^?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
                "callable_retained": True,
            },
            selector=True,
        )
        self.assertArgIsFunction(m, 1, b"i@d", True)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, b"i@d", False
        )

        m = Method(3, {"type": b"?", "callable": {}}, selector=True)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, "v", False
        )

        m = Method(3, {"type": b"^?"}, selector=True)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, "v", False
        )
        m = Method(3, {"type": b"^?", "callable": {}}, selector=True)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, "v", False
        )
        m = Method(
            3,
            {"type": b"^?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 1, "v", False
        )

        m = Method(
            3,
            {
                "type": b"^?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
            },
            selector=False,
        )
        self.assertArgIsFunction(m, 3, b"i@d", False)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 2, "v", False
        )
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 3, "i@b", False
        )
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 3, "i@d", True
        )
        m = Method(
            3,
            {
                "type": b"^?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
                "callable_retained": True,
            },
            selector=False,
        )
        self.assertArgIsFunction(m, 3, b"i@d", True)

        m = Method(3, {"type": b"?", "callable": {}}, selector=False)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 3, "v", False
        )

        m = Method(3, {"type": b"^?"}, selector=True)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 3, "v", False
        )
        m = Method(3, {"type": b"^?", "callable": {}}, selector=False)
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 3, "v", False
        )
        m = Method(
            3,
            {"type": b"^?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=False,
        )
        self.assertRaises(
            self.failureException, self.assertArgIsFunction, m, 3, "v", False
        )

    def test_result_is_function(self):
        m = Method(
            None,
            {
                "type": b"^?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
            },
            selector=True,
        )
        self.assertResultIsFunction(m, b"i@d")
        self.assertRaises(self.failureException, self.assertResultIsFunction, m, "i@b")

        m = Method(1, {})
        self.assertRaises(self.failureException, self.assertResultIsFunction, m, "i@b")

        m = Method(None, {"type": b"?", "callable": {}}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsFunction, m, "v")

        m = Method(None, {"type": b"^?"}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsFunction, m, "v")
        m = Method(None, {"type": b"^?", "callable": {}}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsFunction, m, "v")
        m = Method(
            None,
            {"type": b"^?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        self.assertRaises(self.failureException, self.assertResultIsFunction, m, "v")

    def test_arg_is_block(self):
        m = Method(
            3,
            {
                "type": b"@?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [
                        {"type": b"^v"},
                        {"type": objc._C_ID},
                        {"type": objc._C_DBL},
                    ],
                },
            },
            selector=True,
        )
        self.assertArgIsBlock(m, 1, b"i@d")
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 0, "v")
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 1, "i@b")

        m = Method(
            3,
            {
                "type": b"@?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
                "callable_retained": True,
            },
            selector=True,
        )
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 1, "v")

        m = Method(3, {"type": b"?", "callable": {}}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 1, "v")

        m = Method(3, {"type": b"@?"}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 1, "v")
        m = Method(3, {"type": b"@?", "callable": {}}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 1, "v")
        m = Method(
            3,
            {"type": b"@?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 1, "v")

        m = Method(
            3,
            {
                "type": b"@?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [
                        {"type": b"^v"},
                        {"type": objc._C_ID},
                        {"type": objc._C_DBL},
                    ],
                },
            },
            selector=False,
        )
        self.assertArgIsBlock(m, 3, b"i@d")
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 2, "v")
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 3, "i@b")

        m = Method(
            3,
            {
                "type": b"@?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
                "callable_retained": True,
            },
            selector=False,
        )
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 3, "v")

        m = Method(3, {"type": b"?", "callable": {}}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 3, "v")

        m = Method(3, {"type": b"@?"}, selector=True)
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 3, "v")
        m = Method(3, {"type": b"@?", "callable": {}}, selector=False)
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 3, "v")
        m = Method(
            3,
            {"type": b"@?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=False,
        )
        self.assertRaises(self.failureException, self.assertArgIsBlock, m, 3, "v")

    def test_result_is_block(self):
        m = Method(
            None,
            {
                "type": b"@?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [
                        {"type": b"^v"},
                        {"type": objc._C_ID},
                        {"type": objc._C_DBL},
                    ],
                },
            },
            selector=True,
        )
        self.assertResultIsBlock(m, b"i@d")
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "i@b")

        m = Method(
            None,
            {
                "type": b"@?",
                "callable": {
                    "retval": {"type": objc._C_INT},
                    "arguments": [{"type": objc._C_ID}, {"type": objc._C_DBL}],
                },
                "callable_retained": True,
            },
            selector=True,
        )
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "v")

        m = Method(3, {})
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "v")

        m = Method(None, {"type": b"?", "callable": {}}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "v")

        m = Method(None, {"type": b"@?"}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "v")
        m = Method(None, {"type": b"@?", "callable": {}}, selector=True)
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "v")
        m = Method(
            None,
            {"type": b"@?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        self.assertRaises(self.failureException, self.assertResultIsBlock, m, "v")

    def test_result_bool(self):
        m = Method(None, {"type": objc._C_NSBOOL})
        try:
            self.assertResultIsBOOL(m)
        except self.failureException:
            raise
            self.fail("unexpected test failure")

        m = Method(None, {"type": objc._C_NSBOOL}, selector=True)
        try:
            self.assertResultIsBOOL(m)
        except self.failureException:
            self.fail("unexpected test failure")

        m = Method(None, {"type": b"@"})
        try:
            self.assertResultIsBOOL(m)
        except self.failureException:
            pass
        else:
            self.fail("unexpected test pass")

        m = Method(None, {"type": b"@"}, selector=True)
        try:
            self.assertResultIsBOOL(m)
        except self.failureException:
            pass

        else:
            self.fail("unexpected test pass")

    def test_running(self):
        orig_use = TestSupport._usepool
        orig_class = TestSupport._poolclass
        orig_run = TestSupport._unittest.TestCase.run

        allocs = [0]
        NSObject = objc.lookUpClass("NSObject")
        self.assertIsNot(NSObject, None)

        class PoolClass(object):
            def init(self):
                allocs[0] += 1

            @classmethod
            def alloc(cls):
                return cls()

        TestSupport._unittest.TestCase.run = lambda self: None

        try:
            TestSupport._poolclass = PoolClass

            TestSupport._usepool = True

            self.assertEqual(allocs, [0])
            TestCase.run(self)
            self.assertEqual(allocs, [1])

            TestSupport._usepool = False
            self.assertEqual(allocs, [1])
            TestCase.run(self)
            self.assertEqual(allocs, [1])

        finally:
            TestSupport._usepool = orig_use
            TestSupport._poolclass = orig_class
            TestSupport._unittest.TestCase.run = orig_run

    def run(self, *args, **kwds):
        unittest.TestCase.run(self, *args, **kwds)
