import sys
import unittest

try:
    import ctypes
except ImportError:
    ctypes = None

import pickle
import typing
import enum

import objc
from PyObjCTools import TestSupport
from PyObjCTools.TestSupport import (
    no_autorelease_pool,
    pyobjc_options,
    expectedFailure,
    expectedFailureIf,
    TestCase,
    sdkForPython,
    os_release,
    skipUnless,
    os_level_between,
    max_os_level,
    min_os_level,
    min_sdk_level,
    max_sdk_level,
    min_python_release,
    fourcc,
    arch_only,
)
from unittest import SkipTest, mock


class Method:
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
    def test_pyobjc_options(self):
        class Options:
            pass

        orig_options = objc.options

        try:
            objc.options = Options()
            objc.options.opt1 = True
            objc.options.opt2 = 1

            self.assertIs(objc.options.opt1, True)
            self.assertEqual(objc.options.opt2, 1)

            with pyobjc_options(opt1=False):
                self.assertIs(objc.options.opt1, False)
                self.assertEqual(objc.options.opt2, 1)

            self.assertIs(objc.options.opt1, True)
            self.assertEqual(objc.options.opt2, 1)

            with pyobjc_options(opt1=False, opt2=42):
                self.assertIs(objc.options.opt1, False)
                self.assertEqual(objc.options.opt2, 42)

            self.assertIs(objc.options.opt1, True)
            self.assertEqual(objc.options.opt2, 1)

            with self.assertRaisesRegex(
                AttributeError, "'Options' object has no attribute 'opt3'"
            ):
                with pyobjc_options(opt1=False, opt2=42, opt3="a"):
                    pass

            self.assertIs(objc.options.opt1, True)
            self.assertEqual(objc.options.opt2, 1)

        finally:
            objc.options = orig_options

    def test_expectedFailureIf(self):
        def func(self):
            pass

        o = expectedFailureIf(True)
        self.assertIs(o, expectedFailure)

        o = expectedFailureIf(False)
        self.assertIsNot(o, expectedFailure)
        self.assertIs(func, o(func))

    def test_arch_only(self):
        @arch_only("foo")
        def wrapped_function(self):
            raise RuntimeError("test me")

        with self.assertRaisesRegex(unittest.SkipTest, "foo only"):
            wrapped_function()

        orig = objc.arch
        try:
            objc.arch = "foo"

            with self.assertRaisesRegex(RuntimeError, "test me"):
                wrapped_function()

        finally:
            objc.arch = orig

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
        import subprocess

        TestSupport._os_release = "10.10"
        self.assertEqual(os_release(), "10.10")
        TestSupport._os_release = None

        value = subprocess.check_output(["sw_vers", "-productVersion"]).strip().decode()

        self.assertEqual(TestSupport.os_release(), value)

    def test_fourcc(self):
        import struct

        self.assertEqual(fourcc(b"abcd"), struct.unpack(">i", b"abcd")[0])

    @skipUnless(ctypes is not None, "test requires ctypes")
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

    def test_os_level_between(self):
        orig_os_release = TestSupport.os_release

        try:
            TestSupport.os_release = lambda: "10.5"

            @os_level_between("10.3", "10.4")
            def func_false_1():
                pass

            @os_level_between("10.3", "10.5")
            def func_true_1():
                pass

            @os_level_between("10.3", "10.8")
            def func_true_2():
                pass

            @os_level_between("10.5", "10.3")
            def func_false_2():
                pass

            @os_level_between("10.5", "10.5")
            def func_true_3():
                pass

            @os_level_between("10.5", "10.8")
            def func_true_4():
                pass

            @os_level_between("10.8", "10.3")
            def func_false_3():
                pass

            @os_level_between("10.8", "10.5")
            def func_false_4():
                pass

            @os_level_between("10.8", "10.8")
            def func_false_5():
                pass

            with self.assertRaisesRegex(ValueError, "Invalid version"):

                @os_level_between("11", "12.9")
                def func_invalid1():
                    pass

            with self.assertRaisesRegex(ValueError, "Invalid version"):

                @os_level_between("10.0", "12")
                def func_invalid2():
                    pass

            for func_true in (func_true_1, func_true_2, func_true_3, func_true_4):
                with self.subTest(func_true):
                    try:
                        func_true()
                    except TestSupport._unittest.SkipTest:
                        self.fail("Unexpected skip")

            for func_false in (
                func_false_1,
                func_false_2,
                func_false_3,
                func_false_4,
                func_false_5,
            ):
                with self.subTest(func_false):
                    try:
                        func_false()
                    except TestSupport._unittest.SkipTest:
                        pass

                    else:
                        self.fail("Unexpected non-skip")

        finally:
            TestSupport.os_release = orig_os_release

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

            with self.assertRaisesRegex(ValueError, "Invalid version"):

                @max_os_level("11")
                def func_invalid():
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

    def test_mxx_sdklevel(self):
        orig_build_release = objc.PyObjC_BUILD_RELEASE

        try:
            objc.PyObjC_BUILD_RELEASE = 1005

            @min_sdk_level("10.4")
            def func_true_1():
                pass

            @min_sdk_level("10.5")
            def func_true_2():
                pass

            @min_sdk_level("10.6")
            def func_false_1():
                pass

            @max_sdk_level("10.5")
            def func_true_3():
                pass

            @max_sdk_level("10.6")
            def func_true_4():
                pass

            @max_sdk_level("10.4")
            def func_false_2():
                pass

            with self.assertRaisesRegex(ValueError, "Invalid version"):

                @max_os_level("11")
                def func_invalid():
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
            objc.PyObjC_BUILD_RELEASE = orig_build_release

    def test_min_python_release(self):
        @min_python_release("99.5")
        def func1():
            pass

        with self.assertRaisesRegex(SkipTest, "Requires Python 99.5 or later"):
            func1()

        @min_python_release("2")
        def func1():
            pass

        try:
            func1()
        except SkipTest:
            self.fail("Unexpected skip")

        @min_python_release("3.0")
        def func1():
            pass

        try:
            func1()
        except SkipTest:
            self.fail("Unexpected skip")

    def testAssertIsSubclass(self):
        self.assertIsSubclass(int, object)
        self.assertIsSubclass(str, object)
        self.assertIsSubclass(objc.objc_class, type)

        with self.assertRaisesRegex(
            self.failureException,
            "<class 'objc.objc_class'> is not a subclass of <class objc.objc_object",
        ):
            self.assertIsSubclass(
                objc.objc_class,
                objc.objc_object,
            )

    def testAssertIsNotSubclass(self):
        self.assertIsNotSubclass(object, int)
        with self.assertRaisesRegex(
            self.failureException,
            "<class objc.objc_object is a subclass of <class 'object'>",
        ):
            self.assertIsNotSubclass(objc.objc_object, object)

    def testAssertIsIstance(self):
        self.assertIsInstance(object(), object)
        self.assertIsInstance(42, object)
        self.assertIsInstance(42, (int, str))

        with self.assertRaisesRegex(
            self.failureException, "42 is not an instance of <class 'str'>"
        ):
            self.assertIsInstance(42, str)

    def test_assertStartswith(self):
        with self.assertRaisesRegex(
            self.failureException, "'foo' does not start with 'bar'"
        ):
            self.assertStartswith("foo", "bar")

        try:
            self.assertStartswith("foobar", "foo")
        except self.failureException:
            self.fail("Unexpected assertion failure")

    def test_assertManualBinding(self):
        with self.assertRaisesRegex(self.failureException, ".*has automatic bindings"):
            self.assertManualBinding(objc.lookUpClass("NSObject").alloc)

        try:
            self.assertManualBinding(dir)
        except self.failureException:
            self.fail("Unexpected assertion failure")

    def test_assert_cftype(self):
        with self.assertRaisesRegex(
            self.failureException, "<class 'int'> is not a CFTypeRef type"
        ):
            self.assertIsCFType(int)
        with self.assertRaisesRegex(
            self.failureException,
            "<core-foundation class NSCFType at 0x[0-9a-f]+> is not a unique CFTypeRef type",
        ):
            self.assertIsCFType(objc.lookUpClass("NSCFType"))

        # 'assertIsCFType' primarily tests that a type is either tollfree bridged, or
        # has a distinct type that is different from the default NSCFType 'placeholder' type.
        # self.assertIsCFType(objc.lookUpClass('NSObject'))
        with self.assertRaisesRegex(
            self.failureException,
            "<objective-c class NSObject at 0x[0-9a-f]+> is not a CFTypeRef type",
        ):
            self.assertIsCFType(objc.lookUpClass("NSObject"))

        class OC_OPAQUE_TEST_1(objc.lookUpClass("NSCFType")):
            pass

        try:
            self.assertIsCFType(OC_OPAQUE_TEST_1)
        except self.failureException:
            self.fail("CFType subclass not recognized as CFType")

    def test_assert_enumtype(self):
        with self.assertRaisesRegex(
            self.failureException, "<class 'int'> is not a typing.NewType"
        ):
            self.assertIsEnumType(int)

        with self.assertRaisesRegex(
            self.failureException, ".* is not a typing.NewType based on 'int'"
        ):
            self.assertIsEnumType(typing.NewType("SomeType", str))

        try:
            self.assertIsEnumType(typing.NewType("SomeType", int))
        except self.failureException:
            self.fail("assertIsEnumType unexpectedly failed")

    def test_assert_typed_enum(self):
        with self.assertRaisesRegex(
            self.failureException, "<class 'int'> is not a typing.NewType"
        ):
            self.assertIsTypedEnum(int, int)

        with self.assertRaisesRegex(
            self.failureException, ".* is not a typing.NewType based on 'int'"
        ):
            self.assertIsTypedEnum(typing.NewType("SomeType", str), int)

        with self.assertRaisesRegex(
            self.failureException, ".* is not a typing.NewType based on 'str'"
        ):
            self.assertIsTypedEnum(typing.NewType("SomeType", int), str)

        try:
            self.assertIsTypedEnum(typing.NewType("SomeType", str), str)
        except self.failureException:
            self.fail("assertIsEnumType unexpectedly failed")

        try:
            self.assertIsTypedEnum(typing.NewType("SomeType", float), float)
        except self.failureException:
            self.fail("assertIsEnumType unexpectedly failed")

    def test_assert_opaque(self):
        with self.assertRaisesRegex(
            self.failureException, "<class 'int'> is not an opaque-pointer"
        ):
            self.assertIsOpaquePointer(int)

        class N:
            @property
            def __pointer__(self):
                pass

        with self.assertRaisesRegex(
            self.failureException,
            "<class 'PyObjCTest.test_testsupport.TestTestSupport.test_assert_opaque.<locals>.N'> is not an opaque-pointer",
        ):
            self.assertIsOpaquePointer(N)

        class N:
            __typestr__ = b"^q"

        with self.assertRaisesRegex(
            self.failureException,
            "<class 'PyObjCTest.test_testsupport.TestTestSupport.test_assert_opaque.<locals>.N'> is not an opaque-pointer",
        ):
            self.assertIsOpaquePointer(N)

        class N:
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
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is not a null-terminated array",
        ):
            self.assertResultIsNullTerminated(m)

        m = Method(None, {})
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is not a null-terminated array",
        ):
            self.assertResultIsNullTerminated(m)

    def test_assert_arg_nullterminated(self):
        m = Method(3, {"c_array_delimited_by_null": True}, selector=True)
        self.assertArgIsNullTerminated(m, 1)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 0 of <.*> is not a null-terminated array",
        ):
            self.assertArgIsNullTerminated(m, 0)

        m = Method(3, {"c_array_delimited_by_null": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 1 of <.*> is not a null-terminated array",
        ):
            self.assertArgIsNullTerminated(m, 1)

        m = Method(3, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 1 of <.*> is not a null-terminated array",
        ):
            self.assertArgIsNullTerminated(m, 1)

        m = Method(3, {"c_array_delimited_by_null": True}, selector=False)
        self.assertArgIsNullTerminated(m, 3)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 2 of <.*> is not a null-terminated array",
        ):
            self.assertArgIsNullTerminated(m, 2)

        m = Method(3, {"c_array_delimited_by_null": False}, selector=False)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 3 of <.*> is not a null-terminated array",
        ):
            self.assertArgIsNullTerminated(m, 3)

        m = Method(3, {}, selector=False)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 3 of <.*> is not a null-terminated array",
        ):
            self.assertArgIsNullTerminated(m, 3)

    def test_function_nullterminated(self):
        m = Method(None, {}, selector=False)
        m._meta.update({"variadic": True, "c_array_delimited_by_null": True})
        self.assertIsNullTerminated(m)

        m._meta["variadic"] = False
        with self.assertRaisesRegex(
            self.failureException,
            "<.*> is not a variadic function with a null-terminated list of arguments",
        ):
            self.assertIsNullTerminated(m)

        m._meta["variadic"] = True
        m._meta["c_array_delimited_by_null"] = False
        with self.assertRaisesRegex(
            self.failureException,
            "<.*> is not a variadic function with a null-terminated list of arguments",
        ):
            self.assertIsNullTerminated(m)

        del m._meta["variadic"]
        m._meta["c_array_delimited_by_null"] = True
        with self.assertRaisesRegex(
            self.failureException,
            "<.*> is not a variadic function with a null-terminated list of arguments",
        ):
            self.assertIsNullTerminated(m)

        m = Method(None, {}, selector=True)
        m._meta.update({"variadic": True, "c_array_delimited_by_null": True})
        self.assertIsNullTerminated(m)

        m._meta["variadic"] = False
        with self.assertRaisesRegex(
            self.failureException,
            "<.*> is not a variadic function with a null-terminated list of arguments",
        ):
            self.assertIsNullTerminated(m)

        m._meta["variadic"] = True
        m._meta["c_array_delimited_by_null"] = False
        with self.assertRaisesRegex(
            self.failureException,
            "<.*> is not a variadic function with a null-terminated list of arguments",
        ):
            self.assertIsNullTerminated(m)

        del m._meta["variadic"]
        m._meta["c_array_delimited_by_null"] = True
        with self.assertRaisesRegex(
            self.failureException,
            "<.*> is not a variadic function with a null-terminated list of arguments",
        ):
            self.assertIsNullTerminated(m)

    def test_arg_variable_size(self):
        m = Method(3, {"c_array_of_variable_length": True}, selector=True)
        self.assertArgIsVariableSize(m, 1)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 0 of <.*> is not a variable sized array",
        ):
            self.assertArgIsVariableSize(m, 0)

        m = Method(3, {"c_array_of_variable_length": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 1 of <.*> is not a variable sized array",
        ):
            self.assertArgIsVariableSize(m, 1)

        m = Method(3, {"c_array_of_variable_length": True}, selector=False)
        self.assertArgIsVariableSize(m, 3)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 1 of <.*> is not a variable sized array",
        ):
            self.assertArgIsVariableSize(m, 1)

        m = Method(3, {"c_array_of_variable_length": False}, selector=False)
        with self.assertRaisesRegex(
            self.failureException,
            "argument 3 of <.*> is not a variable sized array",
        ):
            self.assertArgIsVariableSize(m, 3)

    def test_result_varialbe_size(self):
        m = Method(None, {"c_array_of_variable_length": True}, selector=True)
        self.assertResultIsVariableSize(m, 1)

        m = Method(None, {"c_array_of_variable_length": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is not a variable sized array",
        ):
            self.assertResultIsVariableSize(m)

        m = Method(None, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is not a variable sized array",
        ):
            self.assertResultIsVariableSize(m)

    def test_argsize_in_result(self):
        m = Method(3, {"c_array_length_in_result": True}, selector=True)
        self.assertArgSizeInResult(m, 1)
        with self.assertRaisesRegex(
            self.failureException, "argument 0 of .* does not have size in result"
        ):
            self.assertArgSizeInResult(m, 0)

        m = Method(3, {"c_array_length_in_result": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "argument 1 of .* does not have size in result"
        ):
            self.assertArgSizeInResult(m, 1)

        m = Method(3, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "argument 1 of .* does not have size in result"
        ):
            self.assertArgSizeInResult(m, 1)

        m = Method(3, {"c_array_length_in_result": True}, selector=False)
        self.assertArgSizeInResult(m, 3)
        with self.assertRaisesRegex(
            self.failureException, "argument 2 of .* does not have size in result"
        ):
            self.assertArgSizeInResult(m, 2)

        m = Method(3, {"c_array_length_in_result": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "argument 3 of .* does not have size in result"
        ):
            self.assertArgSizeInResult(m, 3)

        m = Method(3, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "argument 3 of .* does not have size in result"
        ):
            self.assertArgSizeInResult(m, 3)

    def test_arg_printf(self):
        m = Method(3, {"printf_format": True}, selector=True)
        m._meta["variadic"] = True
        self.assertArgIsPrintf(m, 1)
        with self.assertRaisesRegex(
            self.failureException, "<.*> argument 0 is not a printf format string"
        ):
            self.assertArgIsPrintf(m, 0)

        m._meta["variadic"] = False
        with self.assertRaisesRegex(
            self.failureException, "<.*> is not a variadic function"
        ):
            self.assertArgIsPrintf(m, 1)

        m._meta["variadic"] = True
        m._meta["arguments"][3]["printf_format"] = False
        with self.assertRaisesRegex(
            self.failureException, "<.*> argument 1 is not a printf format string"
        ):
            self.assertArgIsPrintf(m, 1)

        m._meta["variadic"] = True
        del m._meta["arguments"][3]["printf_format"]
        with self.assertRaisesRegex(
            self.failureException, "<.*> argument 1 is not a printf format string"
        ):
            self.assertArgIsPrintf(m, 1)

        m = Method(3, {"printf_format": True}, selector=False)
        m._meta["variadic"] = True
        self.assertArgIsPrintf(m, 3)
        with self.assertRaisesRegex(
            self.failureException, "<.*> argument 2 is not a printf format string"
        ):
            self.assertArgIsPrintf(m, 2)

        m._meta["variadic"] = False
        with self.assertRaisesRegex(
            self.failureException, "<.*> is not a variadic function"
        ):
            self.assertArgIsPrintf(m, 3)

        m._meta["variadic"] = True
        m._meta["arguments"][3]["printf_format"] = False
        with self.assertRaisesRegex(
            self.failureException, "<.*> argument 3 is not a printf format string"
        ):
            self.assertArgIsPrintf(m, 3)

        m._meta["variadic"] = True
        del m._meta["arguments"][3]["printf_format"]
        with self.assertRaisesRegex(
            self.failureException, "<.*> argument 3 is not a printf format string"
        ):
            self.assertArgIsPrintf(m, 3)

    def test_arg_cfretained(self):

        m = Method(3, {"already_cfretained": True}, selector=True)
        self.assertArgIsCFRetained(m, 1)
        with self.assertRaisesRegex(
            self.failureException, "Argument 0 of <.*> is not cfretained"
        ):
            self.assertArgIsCFRetained(m, 0)

        m = Method(3, {"already_cfretained": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "Argument 1 of <.*> is not cfretained"
        ):
            self.assertArgIsCFRetained(m, 1)

        m = Method(3, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "Argument 1 of <.*> is not cfretained"
        ):
            self.assertArgIsCFRetained(m, 1)

        m = Method(3, {"already_cfretained": True}, selector=False)
        self.assertArgIsCFRetained(m, 3)
        with self.assertRaisesRegex(
            self.failureException, "Argument 2 of <.*> is not cfretained"
        ):
            self.assertArgIsCFRetained(m, 2)

        m = Method(3, {"already_cfretained": False}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "Argument 3 of <.*> is not cfretained"
        ):
            self.assertArgIsCFRetained(m, 3)

        m = Method(3, {}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "Argument 3 of <.*> is not cfretained"
        ):
            self.assertArgIsCFRetained(m, 3)

    def test_arg_not_cfretained(self):
        m = Method(3, {"already_cfretained": True}, selector=True)
        self.assertArgIsNotCFRetained(m, 0)
        with self.assertRaisesRegex(
            self.failureException, "Argument 1 of <.*> is cfretained"
        ):
            self.assertArgIsNotCFRetained(m, 1)

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
        with self.assertRaisesRegex(self.failureException, "<.*> is not cfretained"):
            self.assertResultIsCFRetained(m)

        m = Method(None, {})
        with self.assertRaisesRegex(self.failureException, "<.*> is not cfretained"):
            self.assertResultIsCFRetained(m)

    def test_result_not_cfretained(self):
        m = Method(None, {"already_cfretained": True})
        with self.assertRaisesRegex(self.failureException, "<.*> is cfretained"):
            self.assertResultIsNotCFRetained(m)

        m = Method(None, {"already_cfretained": False})
        self.assertResultIsNotCFRetained(m)

        m = Method(None, {})
        self.assertResultIsNotCFRetained(m)

    def test_arg_type(self):
        m = Method(3, {"type": objc._C_DBL}, selector=True)
        self.assertArgHasType(m, 1, objc._C_DBL)
        with self.assertRaisesRegex(
            self.failureException, r"arg 2 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgHasType(m, 2, objc._C_ID)

        with self.assertRaisesRegex(
            self.failureException,
            f"arg 1 of <.*> is not of type {objc._C_ID}, but {objc._C_DBL}",
        ):
            self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {}, selector=True)
        self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {"type": objc._C_LNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_LNG)
        self.assertArgHasType(m, 1, objc._C_LNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 1 of <.*> is not of type {objc._C_ID}, but {objc._C_LNG}",
        ):
            self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {"type": objc._C_ULNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_ULNG)
        self.assertArgHasType(m, 1, objc._C_ULNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 1 of <.*> is not of type {objc._C_ID}, but {objc._C_ULNG}",
        ):
            self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {"type": objc._C_LNG_LNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_LNG)
        self.assertArgHasType(m, 1, objc._C_LNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 1 of <.*> is not of type {objc._C_ID}, but {objc._C_LNG_LNG}",
        ):
            self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {"type": objc._C_ULNG_LNG}, selector=True)
        self.assertArgHasType(m, 1, objc._C_ULNG)
        self.assertArgHasType(m, 1, objc._C_ULNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 1 of <.*> is not of type {objc._C_ID}, but {objc._C_ULNG_LNG}",
        ):
            self.assertArgHasType(m, 1, objc._C_ID)

        m = Method(3, {"type": objc._C_DBL}, selector=False)
        self.assertArgHasType(m, 3, objc._C_DBL)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 3 of <.*> is not of type {objc._C_ID}, but {objc._C_DBL}",
        ):
            self.assertArgHasType(m, 3, objc._C_ID)
        with self.assertRaisesRegex(
            self.failureException, r"arg 2 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgHasType(m, 2, objc._C_ID)

        m = Method(3, {}, selector=False)
        self.assertArgHasType(m, 3, objc._C_ID)

        m = Method(3, {"type": objc._C_LNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_LNG)
        self.assertArgHasType(m, 3, objc._C_LNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 3 of <.*> is not of type {objc._C_ID}, but {objc._C_LNG}",
        ):
            self.assertArgHasType(m, 3, objc._C_ID)

        m = Method(3, {"type": objc._C_ULNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_ULNG)
        self.assertArgHasType(m, 3, objc._C_ULNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 3 of <.*> is not of type {objc._C_ID}, but {objc._C_ULNG}",
        ):
            self.assertArgHasType(m, 3, objc._C_ID)

        m = Method(3, {"type": objc._C_LNG_LNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_LNG)
        self.assertArgHasType(m, 3, objc._C_LNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 3 of <.*> is not of type {objc._C_ID}, but {objc._C_LNG_LNG}",
        ):
            self.assertArgHasType(m, 3, objc._C_ID)

        m = Method(3, {"type": objc._C_ULNG_LNG}, selector=False)
        self.assertArgHasType(m, 3, objc._C_ULNG)
        self.assertArgHasType(m, 3, objc._C_ULNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"arg 3 of <.*> is not of type {objc._C_ID}, but {objc._C_ULNG_LNG}",
        ):
            self.assertArgHasType(m, 3, objc._C_ID)

    def test_result_type(self):
        m = Method(None, {})
        self.assertResultHasType(m, objc._C_VOID)
        with self.assertRaisesRegex(
            self.failureException,
            f"result of <.*> is not of type {objc._C_ID}, but {objc._C_VOID}",
        ):
            self.assertResultHasType(m, objc._C_ID)

        m = Method(None, {"type": objc._C_DBL})
        self.assertResultHasType(m, objc._C_DBL)
        with self.assertRaisesRegex(
            self.failureException,
            f"result of <.*> is not of type {objc._C_ID}, but {objc._C_DBL}",
        ):
            self.assertResultHasType(m, objc._C_ID)

        m = Method(None, {"type": objc._C_LNG}, selector=False)
        self.assertResultHasType(m, objc._C_LNG)
        self.assertResultHasType(m, objc._C_LNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"result of <.*> is not of type {objc._C_ID}, but {objc._C_LNG}",
        ):
            self.assertResultHasType(m, objc._C_ID)

        m = Method(None, {"type": objc._C_ULNG}, selector=False)
        self.assertResultHasType(m, objc._C_ULNG)
        self.assertResultHasType(m, objc._C_ULNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"result of <.*> is not of type {objc._C_ID}, but {objc._C_ULNG}",
        ):
            self.assertResultHasType(m, objc._C_ID)

        m = Method(None, {"type": objc._C_LNG_LNG}, selector=False)
        self.assertResultHasType(m, objc._C_LNG)
        self.assertResultHasType(m, objc._C_LNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"result of <.*> is not of type {objc._C_ID}, but {objc._C_LNG_LNG}",
        ):
            self.assertResultHasType(m, objc._C_ID)

        m = Method(None, {"type": objc._C_ULNG_LNG}, selector=False)
        self.assertResultHasType(m, objc._C_ULNG)
        self.assertResultHasType(m, objc._C_ULNG_LNG)
        with self.assertRaisesRegex(
            self.failureException,
            f"result of <.*> is not of type {objc._C_ID}, but {objc._C_ULNG_LNG}",
        ):
            self.assertResultHasType(m, objc._C_ID)

    def test_arg_fixed_size(self):
        m = Method(3, {"c_array_of_fixed_length": 42}, selector=True)
        self.assertArgIsFixedSize(m, 1, 42)
        with self.assertRaisesRegex(
            self.failureException, "arg 0 of <.*> is not a C-array of length 42"
        ):
            self.assertArgIsFixedSize(m, 0, 42)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> is not a C-array of length 3"
        ):
            self.assertArgIsFixedSize(m, 1, 3)

        m = Method(3, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> is not a C-array of length 3"
        ):
            self.assertArgIsFixedSize(m, 1, 3)

        m = Method(3, {"c_array_of_fixed_length": 42}, selector=False)
        self.assertArgIsFixedSize(m, 3, 42)
        with self.assertRaisesRegex(
            self.failureException, "arg 2 of <.*> is not a C-array of length 42"
        ):
            self.assertArgIsFixedSize(m, 2, 42)
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> is not a C-array of length 3"
        ):
            self.assertArgIsFixedSize(m, 3, 3)

        m = Method(3, {}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> is not a C-array of length 3"
        ):
            self.assertArgIsFixedSize(m, 3, 3)

    def test_result_fixed_size(self):
        m = Method(None, {"c_array_of_fixed_length": 42})
        self.assertResultIsFixedSize(m, 42)
        with self.assertRaisesRegex(
            self.failureException, "result of <.*> is not a C-array of length 3"
        ):
            self.assertResultIsFixedSize(m, 3)

        m = Method(None, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "result of <.*> is not a C-array of length 3"
        ):
            self.assertResultIsFixedSize(m, 3)

    def test_arg_size_in_arg(self):
        m = Method(3, {"c_array_length_in_arg": 4}, selector=True)
        self.assertArgSizeInArg(m, 1, 2)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is not a C-array of with length in arg 3",
        ):
            self.assertArgSizeInArg(m, 1, 3)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 0 of <.*> is not a C-array of with length in arg 3",
        ):
            self.assertArgSizeInArg(m, 0, 3)

        m = Method(3, {"c_array_length_in_arg": (2, 4)}, selector=True)
        self.assertArgSizeInArg(m, 1, (0, 2))
        with self.assertRaisesRegex(
            self.failureException,
            r"arg 1 of <.*> is not a C-array of with length in arg \(0, 3\)",
        ):
            self.assertArgSizeInArg(m, 1, (0, 3))
        with self.assertRaisesRegex(
            self.failureException,
            r"arg 0 of <.*> is not a C-array of with length in arg \(1, 2\)",
        ):
            self.assertArgSizeInArg(m, 0, (1, 2))

        m = Method(3, {"c_array_length_in_arg": 4}, selector=False)
        self.assertArgSizeInArg(m, 3, 4)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is not a C-array of with length in arg 3",
        ):
            self.assertArgSizeInArg(m, 1, 3)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 0 of <.*> is not a C-array of with length in arg 3",
        ):
            self.assertArgSizeInArg(m, 0, 3)

        m = Method(3, {"c_array_length_in_arg": (2, 4)}, selector=False)
        self.assertArgSizeInArg(m, 3, (2, 4))
        with self.assertRaisesRegex(
            self.failureException,
            r"arg 1 of <.*> is not a C-array of with length in arg \(2, 3\)",
        ):
            self.assertArgSizeInArg(m, 1, (2, 3))
        with self.assertRaisesRegex(
            self.failureException,
            r"arg 0 of <.*> is not a C-array of with length in arg \(2, 3\)",
        ):
            self.assertArgSizeInArg(m, 0, (2, 3))

    def test_result_ssize_in_arg(self):
        m = Method(None, {"c_array_length_in_arg": 4}, selector=True)
        self.assertResultSizeInArg(m, 2)
        with self.assertRaisesRegex(
            self.failureException,
            "result <.*> is not a C-array of with length in arg 3",
        ):
            self.assertResultSizeInArg(m, 3)

        m = Method(None, {"c_array_length_in_arg": 4}, selector=False)
        self.assertResultSizeInArg(m, 4)
        with self.assertRaisesRegex(
            self.failureException,
            "result <.*> is not a C-array of with length in arg 3",
        ):
            self.assertResultSizeInArg(m, 3)

    def test_arg_retained(self):
        m = Method(3, {"already_retained": True}, selector=True)
        self.assertArgIsRetained(m, 1)
        with self.assertRaisesRegex(
            self.failureException, "Argument 0 of <.*> is not retained"
        ):
            self.assertArgIsRetained(m, 0)

        m = Method(3, {"already_retained": False}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "Argument 1 of <.*> is not retained"
        ):
            self.assertArgIsRetained(m, 1)

        m = Method(3, {}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "Argument 1 of <.*> is not retained"
        ):
            self.assertArgIsRetained(m, 1)

        m = Method(3, {"already_retained": True}, selector=False)
        self.assertArgIsRetained(m, 3)
        with self.assertRaisesRegex(
            self.failureException, "Argument 2 of <.*> is not retained"
        ):
            self.assertArgIsRetained(m, 2)

        m = Method(3, {"already_retained": False}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "Argument 3 of <.*> is not retained"
        ):
            self.assertArgIsRetained(m, 3)

        m = Method(3, {}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "Argument 3 of <.*> is not retained"
        ):
            self.assertArgIsRetained(m, 3)

    def test_arg_not_retained(self):
        m = Method(3, {"already_retained": True}, selector=True)
        self.assertArgIsNotRetained(m, 0)
        with self.assertRaisesRegex(
            self.failureException, "Argument 1 of <.*> is retained"
        ):
            self.assertArgIsNotRetained(m, 1)

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
        with self.assertRaisesRegex(
            self.failureException, "Result of <.*> is not retained"
        ):
            self.assertResultIsRetained(m)

        m = Method(None, {})
        with self.assertRaisesRegex(
            self.failureException, "Result of <.*> is not retained"
        ):
            self.assertResultIsRetained(m)

    def test_result_not_retained(self):
        m = Method(None, {"already_retained": True})
        with self.assertRaisesRegex(
            self.failureException, "Result of <.*> is retained"
        ):
            self.assertResultIsNotRetained(m)

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
        for tp in (objc._C_NSBOOL, objc._C_BOOL):
            with self.subTest(encoding=tp):
                m = Method(3, {"type": tp})
                try:
                    self.assertArgIsBOOL(m, 3)
                except self.failureException:
                    raise
                    self.fail("unexpected test failure")

                m = Method(3, {"type": tp}, selector=True)
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

    def test_assertHasAttr(self):
        with self.assertRaisesRegex(self.failureException, "foo"):
            self.assertHasAttr(object, "foo")

        try:
            self.assertHasAttr(self, "assertHasAttr")
        except self.failureExeption:
            self.fail("Unexpected assertion failure")

    def test_assertNotHasAttr(self):
        with self.assertRaisesRegex(
            self.failureException, "assertHasAttr is an attribute of <.*>"
        ):
            self.assertNotHasAttr(self, "assertHasAttr")

        try:
            self.assertNotHasAttr(object, "foo")
        except self.failureExeption:
            self.fail("Unexpected assertion failure")

    def test_ClassIsFinal(self):
        class FinalTesetClass(objc.lookUpClass("NSObject"), final=True):
            __objc_final__ = True

        try:
            self.assertClassIsFinal(FinalTesetClass)
        except self.failureException:
            self.fail("Unexpected assertion failure")

        with self.assertRaisesRegex(self.failureException, ".*is not a final class"):
            self.assertClassIsFinal(objc.lookUpClass("NSObject"))

        with self.assertRaisesRegex(
            self.failureException, ".*is not an Objective-C class"
        ):
            self.assertClassIsFinal(type(self))

    def test_assertProtoclExists(self):
        objc.protocolNamed("NSObject")
        try:
            objc.protocolNamed("FooBar")
        except objc.error:
            pass
        else:
            self.fail("Have FooBar protocol")

        with self.assertRaisesRegex(
            self.failureException, "Protocol 'FooBar' does not exist"
        ):
            self.assertProtocolExists("FooBar")

        try:
            self.assertProtocolExists("NSObject")
        except self.failureException:
            self.fail("Unexpected test failure")

        orig = objc.protocolNamed
        try:
            objc.protocolNamed = lambda name: name

            with self.assertRaisesRegex(
                self.failureException, "Protocol 'FooBar' is not a protocol, but.*"
            ):
                self.assertProtocolExists("FooBar")
        finally:
            objc.protocolNamed = orig

        try:
            objc.protocolNamed("FooBar")
        except objc.error:
            pass
        else:
            self.fail("Have FooBar protocol")

    def test_assertPickleRoundTrips(self):
        try:
            self.assertPickleRoundTrips(42)
        except self.failureException:
            self.fail("Unexpected assertion error")

        class NoPickle:
            def __getstate__(self):
                raise RuntimeError("go away")

        with self.assertRaises((pickle.PickleError, RuntimeError)):
            pickle.dumps(NoPickle())

        with self.assertRaisesRegex(self.failureException, ".* cannot be pickled"):
            self.assertPickleRoundTrips(NoPickle())

        class UnpickledAsInt:
            def __reduce__(self):
                return (int, (42,))

        o = UnpickledAsInt()
        self.assertEqual(pickle.loads(pickle.dumps(o)), 42)

        with self.assertRaisesRegex(
            self.failureException, "42 != <PyObjCTest.test_testsupport.*>"
        ):
            self.assertPickleRoundTrips(o)

        class NotEqual:
            def __eq__(self, other):
                return False

        o = NotEqual()
        self.assertNotEqual(o, o)

        with self.assertRaisesRegex(self.failureException, "<.*> cannot be pickled"):
            self.assertPickleRoundTrips(o)

    def test_result_is_sel(self):
        for is_selector in (True, False):
            m = Method(
                None,
                {"type": objc._C_SEL, "sel_of_type": b"v@:@"},
                selector=is_selector,
            )
            self.assertResultIsSEL(m, b"v@:@")

            with self.assertRaisesRegex(
                self.failureException,
                "result of <.*> doesn't have sel_type b'v@:d' but b'v@:@'",
            ):
                self.assertResultIsSEL(m, b"v@:d")

            m = Method(None, {"type": objc._C_INT}, selector=is_selector)
            with self.assertRaisesRegex(
                self.failureException, "result of <.*> is not of type SEL"
            ):
                self.assertResultIsSEL(m, b"v@:@")

            m = Method(None, {"type": objc._C_SEL}, selector=is_selector)
            with self.assertRaisesRegex(
                self.failureException,
                "result of <.*> doesn't have sel_type b'v@:@' but None",
            ):
                self.assertResultIsSEL(m, b"v@:@")

            with self.assertRaisesRegex(
                self.failureException,
                "result of <.*> doesn't have sel_type b'v@:@' but None",
            ):
                self.assertResultIsSEL(m, b"v@:@")

            class M:
                def __metadata__(self):
                    return {}

            with self.assertRaisesRegex(
                self.failureException, r"result.*has no metadata \(or doesn't exist\)"
            ):
                self.assertResultIsSEL(M(), b"v@:@")

    def test_arg_is_sel(self):
        m = Method(3, {"type": objc._C_SEL, "sel_of_type": b"v@:@"}, selector=True)
        self.assertArgIsSEL(m, 1, b"v@:@")

        with self.assertRaisesRegex(
            self.failureException, r"arg 2 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgIsSEL(m, 2, b"v@:@")
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> doesn't have sel_type b'v@:' but b'v@:@'",
        ):
            self.assertArgIsSEL(m, 1, b"v@:")

        m = Method(3, {"type": objc._C_SEL}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> doesn't have sel_type b'v@:' but None"
        ):
            self.assertArgIsSEL(m, 1, b"v@:")

        m = Method(3, {"type": objc._C_ID, "sel_of_type": b"v@:@"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> is not of type SEL"
        ):
            self.assertArgIsSEL(m, 1, b"v@:@")

        m = Method(3, {"type": objc._C_SEL, "sel_of_type": b"v@:@"}, selector=False)
        self.assertArgIsSEL(m, 3, b"v@:@")

        with self.assertRaisesRegex(
            self.failureException, r"arg 2 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgIsSEL(m, 2, b"v@:@")
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> doesn't have sel_type b'v@:' but b'v@:@'",
        ):
            self.assertArgIsSEL(m, 3, b"v@:")

        m = Method(3, {"type": objc._C_SEL}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> doesn't have sel_type b'v@:' but None"
        ):
            self.assertArgIsSEL(m, 3, b"v@:")

        m = Method(3, {"type": objc._C_ID, "sel_of_type": b"v@:@"}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> is not of type SEL"
        ):
            self.assertArgIsSEL(m, 3, b"v@:@")

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
        with self.assertRaisesRegex(
            self.failureException, r"arg 0 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgIsFunction(m, 0, "v", False)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is not a function_pointer with type 'i@b', but b'i@d'",
        ):
            self.assertArgIsFunction(m, 1, "i@b", False)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is not a function_pointer with type 'i@d', but b'i@d'",
        ):
            self.assertArgIsFunction(m, 1, "i@d", True)
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
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*>; retained: True, expected: False"
        ):
            self.assertArgIsFunction(m, 1, b"i@d", False)

        m = Method(3, {"type": b"?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> is not of type function_pointer"
        ):
            self.assertArgIsFunction(m, 1, "v", False)

        m = Method(3, {"type": b"^?"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> is not of type function_pointer"
        ):
            self.assertArgIsFunction(m, 1, "v", False)
        m = Method(3, {"type": b"^?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is a function pointer with incomplete type information",
        ):
            self.assertArgIsFunction(m, 1, "v", False)
        m = Method(
            3,
            {"type": b"^?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is a function pointer with incomplete type information",
        ):
            self.assertArgIsFunction(m, 1, "v", False)

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
        with self.assertRaisesRegex(
            self.failureException, r"arg 2 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgIsFunction(m, 2, "v", False)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> is not a function_pointer with type b'i@b', but b'i@d'",
        ):
            self.assertArgIsFunction(m, 3, b"i@b", False)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> is not a function_pointer with type 'i@d', but b'i@d'",
        ):
            self.assertArgIsFunction(m, 3, "i@d", True)
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
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> is not of type function_pointer"
        ):
            self.assertArgIsFunction(m, 3, "v", False)

        m = Method(3, {"type": b"^?"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, r"arg 3 of <.*> has no metadata \(or doesn't exist\)"
        ):
            self.assertArgIsFunction(m, 3, "v", False)
        m = Method(3, {"type": b"^?", "callable": {}}, selector=False)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> is a function pointer with incomplete type information",
        ):
            self.assertArgIsFunction(m, 3, "v", False)
        m = Method(
            3,
            {"type": b"^?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=False,
        )
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> is a function pointer with incomplete type information",
        ):
            self.assertArgIsFunction(m, 3, "v", False)

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
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is not a function_pointer with type 'i@b', but b'i@d'",
        ):
            self.assertResultIsFunction(m, "i@b")

        m = Method(1, {})
        with self.assertRaisesRegex(
            self.failureException,
            r"result of <.*> has no metadata \(or doesn't exist\)",
        ):
            self.assertResultIsFunction(m, "i@b")

        m = Method(None, {"type": b"?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "result of <.*> is not of type function_pointer"
        ):
            self.assertResultIsFunction(m, "v")

        m = Method(None, {"type": b"^?"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "result of <.*> is not of type function_pointer"
        ):
            self.assertResultIsFunction(m, "v")
        m = Method(None, {"type": b"^?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a function pointer with incomplete type information",
        ):
            self.assertResultIsFunction(m, "v")
        m = Method(
            None,
            {"type": b"^?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        with self.assertRaisesRegex(
            self.failureException,
            r"result of <.*> is a function pointer with incomplete type information",
        ):
            self.assertResultIsFunction(m, "v")

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
        with self.assertRaisesRegex(
            self.failureException, "arg 0 of <.*> does not exist"
        ):
            self.assertArgIsBlock(m, 0, "v")
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> is not a block with type 'i@b', but b'i@d'",
        ):
            self.assertArgIsBlock(m, 1, "i@b")

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
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*> has an invalid block signature b'@' for argument 0",
        ):
            self.assertArgIsBlock(m, 1, "v")

        m = Method(3, {"type": b"?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 1 of <.*> is not of type block: b'?'"
        ):
            self.assertArgIsBlock(m, 1, "v")

        m = Method(3, {"type": b"@?"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "arg 1 of <.*>: no callable specified for the block signature",
        ):
            self.assertArgIsBlock(m, 1, "v")
        m = Method(3, {"type": b"@?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a block pointer with incomplete type information",
        ):
            self.assertArgIsBlock(m, 1, "v")
        m = Method(
            3,
            {"type": b"@?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a block pointer with incomplete type information",
        ):
            self.assertArgIsBlock(m, 1, "v")

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
        with self.assertRaisesRegex(
            self.failureException, "arg 2 of <.*> does not exist"
        ):
            self.assertArgIsBlock(m, 2, "v")
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> is not a block with type b'i@b', but b'i@d'",
        ):
            self.assertArgIsBlock(m, 3, b"i@b")

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
        with self.assertRaisesRegex(
            self.failureException,
            "arg 3 of <.*> has an invalid block signature b'@' for argument 0",
        ):
            self.assertArgIsBlock(m, 3, "v")

        m = Method(3, {"type": b"?", "callable": {}}, selector=False)
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> is not of type block: b'?'"
        ):
            self.assertArgIsBlock(m, 3, "v")

        m = Method(3, {"type": b"@?"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "arg 3 of <.*> does not exist"
        ):
            self.assertArgIsBlock(m, 3, "v")
        m = Method(3, {"type": b"@?", "callable": {}}, selector=False)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a block pointer with incomplete type information",
        ):
            self.assertArgIsBlock(m, 3, "v")
        m = Method(
            3,
            {"type": b"@?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=False,
        )
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a block pointer with incomplete type information",
        ):
            self.assertArgIsBlock(m, 3, "v")

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
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is not a block with type b'i@b', but b'i@d'",
        ):
            self.assertResultIsBlock(m, b"i@b")

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
        with self.assertRaisesRegex(
            self.failureException,
            "result <.*> has an invalid block signature b'@' for argument 0",
        ):
            self.assertResultIsBlock(m, "v")

        m = Method(3, {})
        with self.assertRaisesRegex(
            self.failureException, "result of <.*> is not of type block: b'v'"
        ):
            self.assertResultIsBlock(m, "v")

        m = Method(None, {"type": b"?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException, "result of <.*> is not of type block: b'?'"
        ):
            self.assertResultIsBlock(m, "v")

        m = Method(None, {"type": b"@?"}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*>: no callable specified for the block signature",
        ):
            self.assertResultIsBlock(m, "v")
        m = Method(None, {"type": b"@?", "callable": {}}, selector=True)
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a block pointer with incomplete type information",
        ):
            self.assertResultIsBlock(m, "v")
        m = Method(
            None,
            {"type": b"@?", "callable": {"retval": {"type": objc._C_VOID}}},
            selector=True,
        )
        with self.assertRaisesRegex(
            self.failureException,
            "result of <.*> is a block pointer with incomplete type information",
        ):
            self.assertResultIsBlock(m, "v")

    def test_result_bool(self):
        for tp in (objc._C_NSBOOL, objc._C_BOOL):
            with self.subTest(encoding=tp):
                m = Method(None, {"type": tp})
                self.assertResultIsBOOL(m)

                m = Method(None, {"type": tp}, selector=True)
                self.assertResultIsBOOL(m)

                m = Method(None, {"type": b"@"})
                with self.assertRaisesRegex(
                    self.failureException,
                    f"result of <.*> is not of type BOOL, but {objc._C_ID}",
                ):
                    self.assertResultIsBOOL(m)

                m = Method(None, {"type": b"@"}, selector=True)
                with self.assertRaisesRegex(
                    self.failureException,
                    f"result of <.*> is not of type BOOL, but {objc._C_ID}",
                ):
                    self.assertResultIsBOOL(m)

    def test_arg_idlike(self):
        for tp in (b"@", b"^@", b"n^@", b"o^@", b"N^@"):
            with self.subTest(encoding=tp):
                m = Method(3, {"type": tp})
                try:
                    self.assertArgIsIDLike(m, 3)
                except self.failureException:
                    self.fail("Unexpctedly tested as not id-like")

        for tp in (b"@", b"^@", b"n^@", b"o^@", b"N^@"):
            with self.subTest(encoding=tp):
                m = Method(3, {"type": tp}, selector=True)
                try:
                    self.assertArgIsIDLike(m, 1)
                except self.failureException:
                    self.fail("Unexpctedly tested as not id-like")

        for tp in (b"^{__CFPython=}",):
            with self.subTest(encoding=tp, registered=False):
                try:
                    m = Method(3, {"type": tp})
                    self.assertArgIsIDLike(m, 3)
                except self.failureException:
                    pass
                else:
                    self.fail("Unexpectedly tested as id-like")

                try:
                    m = Method(3, {"type": b"^" + tp})
                    self.assertArgIsIDLike(m, 3)
                except self.failureException:
                    pass
                else:
                    self.fail("Unexpectedly tested as id-like")

            for pfx in (b"", b"^", b"n^", b"N^", b"o^"):
                with self.subTest(encoding=tp, msg="mocked _idSignatures", pfx=pfx):
                    orig = objc._idSignatures
                    objc._idSignatures = lambda tp=tp: [tp]
                    try:
                        try:
                            m = Method(3, {"type": pfx + tp})
                            self.assertArgIsIDLike(m, 3)
                        except self.failureException:
                            self.fail("Unexpectedly tested as not id-like")

                        try:
                            m = Method(3, {"type": pfx + tp})
                            self.assertArgIsIDLike(m, 3)
                        except self.failureException:
                            self.fail("Unexpectedly tested as not id-like")

                    finally:
                        objc._idSignatures = orig
                        if tp in TestSupport._idlike_cache:
                            TestSupport._idlike_cache.remove(tp)

        try:
            m = Method(3, {"type": b"d"})
            self.assertArgIsIDLike(m, 3)
        except self.failureException:
            pass
        else:
            self.fail("Unexpectedly tested as id-like")

    def test_result_idlike(self):
        for tp in (b"@", b"^@", b"n^@", b"o^@", b"N^@"):
            with self.subTest(encoding=tp):
                m = Method(None, {"type": tp})
                try:
                    self.assertResultIsIDLike(m)
                except self.failureException:
                    self.fail("Unexpctedly tested as not id-like")

        for tp in (b"^{__CFPython=}",):
            with self.subTest(encoding=tp, registered=False):
                try:
                    m = Method(None, {"type": tp})
                    self.assertResultIsIDLike(m)
                except self.failureException:
                    pass
                else:
                    self.fail("Unexpectedly tested as id-like")

                try:
                    m = Method(None, {"type": b"^" + tp})
                    self.assertResultIsIDLike(m)
                except self.failureException:
                    pass
                else:
                    self.fail("Unexpectedly tested as id-like")

            for pfx in (b"", b"^", b"n^", b"N^", b"o^"):
                with self.subTest(encoding=tp, msg="mocked _idSignatures", pfx=pfx):
                    orig = objc._idSignatures
                    objc._idSignatures = lambda tp=tp: [tp]
                    try:
                        try:
                            m = Method(None, {"type": pfx + tp})
                            self.assertResultIsIDLike(m)
                        except self.failureException:
                            self.fail("Unexpectedly tested as not id-like")

                        try:
                            m = Method(None, {"type": pfx + tp})
                            self.assertResultIsIDLike(m)
                        except self.failureException:
                            self.fail("Unexpectedly tested as not id-like")

                    finally:
                        objc._idSignatures = orig
                        if tp in TestSupport._idlike_cache:
                            TestSupport._idlike_cache.remove(tp)

        try:
            m = Method(None, {"type": b"d"})
            self.assertResultIsIDLike(m)
        except self.failureException:
            pass
        else:
            self.fail("Unexpectedly tested as id-like")

    def test_validate_callable_metadata(self):
        class Function:
            def __init__(self, argno, metadata):
                self._meta = {
                    "retval": {"type": b"@"},
                    "arguments": [
                        {"type": b"@"},
                        {"type": b"@"},
                    ],
                }
                if metadata is not None:
                    if argno is None:
                        self._meta["retval"] = metadata
                    else:
                        self._meta["arguments"][argno] = metadata

            def __metadata__(self):
                return self._meta

        for idx in (None, 1):
            with self.subTest(f"{idx}: nothing special"):
                try:
                    func = Function(
                        idx,
                        None,
                    )
                    self._validateCallableMetadata(func)
                except self.failureException:
                    self.fail("Unexpected test failure")

            with self.subTest(f"{idx}: _C_CHARPTR"):
                with self.assertRaisesRegex(
                    self.failureException,
                    r"'char\*'",
                ):
                    func = Function(
                        idx,
                        {
                            "type": objc._C_CHARPTR,
                        },
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: _C_CHARPTR (skip check)"):
                try:
                    func = Function(
                        idx,
                        {
                            "type": objc._C_CHARPTR,
                        },
                    )
                    self._validateCallableMetadata(func, skip_simple_charptr_check=True)
                except self.failureException:
                    self.fail("Unexpected test failure")

            with self.subTest(f"{idx}: _C_PTR + _C_CHR"):
                with self.assertRaisesRegex(
                    self.failureException,
                    r"'char\*'",
                ):
                    func = Function(
                        idx,
                        {"type": objc._C_PTR + objc._C_CHR},
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: _C_PTR + _C_CHR (skip check)"):
                try:
                    func = Function(
                        idx,
                        {"type": objc._C_PTR + objc._C_CHR},
                    )
                    self._validateCallableMetadata(func, skip_simple_charptr_check=True)
                except self.failureException as exc:
                    if "pointer argument, but no by-ref annotation" not in str(exc):
                        self.fail("Unexpected test failure")

            with self.subTest(f"{idx}: null-delimited _C_CHARPTR"):
                with self.assertRaisesRegex(
                    self.failureException,
                    r"null-delimited 'char\*', use _C_CHAR_AS_TEXT instead",
                ):
                    func = Function(
                        idx,
                        {"type": objc._C_CHARPTR, "c_array_delimited_by_null": True},
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: null-delimited _C_PTR + _C_CHR"):
                with self.assertRaisesRegex(
                    self.failureException,
                    r"null-delimited 'char\*', use _C_CHAR_AS_TEXT instead",
                ):
                    func = Function(
                        idx,
                        {
                            "type": objc._C_PTR + objc._C_CHR,
                            "c_array_delimited_by_null": True,
                        },
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: null-delimited _C_IN + _C_PTR + _C_CHR"):
                with self.assertRaisesRegex(
                    self.failureException,
                    r"null-delimited 'char\*', use _C_CHAR_AS_TEXT instead",
                ):
                    func = Function(
                        idx,
                        {
                            "type": objc._C_IN + objc._C_PTR + objc._C_CHR,
                            "c_array_delimited_by_null": True,
                        },
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: size arg ok (int)"):
                try:
                    func = Function(
                        idx,
                        {
                            "type": objc._C_IN + objc._C_PTR + objc._C_INT,
                            "c_array_size_in_arg": 0,
                        },
                    )
                    self._validateCallableMetadata(func)
                except self.failureException:
                    self.fail("Unexpected failure")

            with self.subTest(f"{idx}: size arg out of range (int)"):
                with self.assertRaisesRegex(
                    self.failureException, r"c_array_size_in_arg out of range 10 "
                ):
                    func = Function(
                        idx,
                        {"type": objc._C_PTR + objc._C_INT, "c_array_size_in_arg": 10},
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: size arg tuple ok"):
                try:
                    func = Function(
                        idx,
                        {
                            "type": objc._C_IN + objc._C_PTR + objc._C_INT,
                            "c_array_size_in_arg": (0, 1),
                        },
                    )
                    self._validateCallableMetadata(func)
                except self.failureException:
                    self.fail("Unexpected failure")

            with self.subTest(f"{idx}: size arg out of range (tuple[0])"):
                with self.assertRaisesRegex(
                    self.failureException, r"c_array_size_in_arg out of range 10 "
                ):
                    func = Function(
                        idx,
                        {
                            "type": objc._C_PTR + objc._C_INT,
                            "c_array_size_in_arg": (10, 1),
                        },
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: size arg out of range (tuple[1])"):
                with self.assertRaisesRegex(
                    self.failureException, r"c_array_size_in_arg out of range 10 "
                ):
                    func = Function(
                        idx,
                        {
                            "type": objc._C_PTR + objc._C_INT,
                            "c_array_size_in_arg": (1, 10),
                        },
                    )
                    self._validateCallableMetadata(func)

            with self.subTest(f"{idx}: both retained and cfretaind"):
                with self.assertRaisesRegex(
                    self.failureException,
                    "both already_retained and already_cfretained",
                ):

                    func = Function(
                        idx, {"already_cfretained": True, "already_retained": True}
                    )
                    self._validateCallableMetadata(func)

            for pfx in (objc._C_IN, objc._C_OUT, objc._C_INOUT):
                with self.subTest(f"{idx}: by-ref specifier {pfx} on int"):
                    with self.assertRaisesRegex(
                        self.failureException, r"byref specifier on non-pointer"
                    ):
                        func = Function(idx, {"type": pfx + objc._C_INT})
                        self._validateCallableMetadata(func)

                with self.subTest(f"{idx}: by-ref specifier {pfx} on empty struct"):
                    with self.assertRaisesRegex(
                        self.failureException, r"byref to empty struct"
                    ):
                        func = Function(idx, {"type": pfx + b"^{_CFSomeThing=}"})
                        self._validateCallableMetadata(func)

                with self.subTest(f"{idx}: by-ref for int pointer"):
                    try:
                        func = Function(idx, {"type": pfx + objc._C_PTR + objc._C_INT})
                        self._validateCallableMetadata(func)
                    except self.failureException:
                        self.fail("Unexpected failure")

                with self.subTest(f"{idx}: by-ref for struct pointer"):
                    try:
                        func = Function(idx, {"type": pfx + objc._C_PTR + b"{size=dd}"})
                        self._validateCallableMetadata(func)
                    except self.failureException:
                        self.fail("Unexpected failure")

    def test_assert_callable_metadata(self):
        class Mod:
            pass

        try:
            m = Mod()
            m.Object = objc.lookUpClass("Object")
            m.EnumType = enum.Enum
        except objc.error:
            pass  # "Object" root class is no longer present
            self.fail("Missing object class")

        else:
            with self.subTest("Object is igored"):
                try:
                    self.assertCallableMetadataIsSane(m, exclude_cocoa=False)
                except self.failureException:
                    self.fail("Unexpected failure")

                self.assertEqual(m.Object.__name__, "Object")
                self.assertIsInstance(m.Object, objc.objc_class)

        with self.subTest("validate framework identifier"):
            m = Mod()
            m.__bundle__ = Mod()
            m.__bundle__.bundleIdentifier = lambda: "framework.id"
            m.__framework_identifier__ = "framework.id2"

            with self.assertRaisesRegex(
                self.failureException, "framework.id' != 'framework.id2"
            ):
                self._validateBundleIdentifier(m)

            try:
                m.__framework_identifier__ = "framework.id"
                self._validateBundleIdentifier(m)
            except self.failureException:
                self.fail("validation failed unexpectedly")

        with self.subTest("validate is called for class and instance methods"):
            NSObject = objc.lookUpClass("NSObject")

            with mock.patch(
                "PyObjCTools.TestSupport.TestCase._validateCallableMetadata"
            ) as fn:
                m = Mod()
                m.Constant = 42
                m.NSObject = NSObject

                try:
                    self.assertCallableMetadataIsSane(m, exclude_cocoa=False)
                except self.failureException:
                    self.fail("Unexpected failure")

            if 0:
                fn.assert_any_call(
                    NSObject.pyobjc_instanceMethods.description,
                    "NSObject",
                    skip_simple_charptr_check=True,
                )
            fn.assert_any_call(
                NSObject.pyobjc_classMethods.description,
                "NSObject",
                skip_simple_charptr_check=True,
            )

        with self.subTest("validate instance variables are not checked"):
            NSObject = objc.lookUpClass("NSObject")

            class MyClassForValidating(NSObject):
                someVar = objc.ivar()

                def mymethod(self):
                    pass

            self.assertIsInstance(
                MyClassForValidating.pyobjc_instanceMethods.mymethod, objc.selector
            )
            self.assertIn("mymethod", dir(MyClassForValidating.pyobjc_instanceMethods))

            # Also mock the Cocoa package to avoid classes ending up there as well
            # XXX: Need to check if the actual usage of the API is safe in this respect as well!
            Cocoa = Mod()
            Cocoa.NSObject = objc.lookUpClass("NSObject")
            Cocoa.NSArray = objc.lookUpClass("NSArray")

            if "Cocoa" in sys.modules:
                orig_Cocoa = sys.modules["Cocoa"]
            else:
                orig_Cocoa = None
            sys.modules["Cocoa"] = Cocoa
            try:
                with mock.patch(
                    "PyObjCTools.TestSupport.TestCase._validateCallableMetadata"
                ) as fn:
                    m = Mod()
                    m.Constant = 42
                    m.MyClassForValidating = MyClassForValidating
                    m.NSArray = objc.lookUpClass("NSArray")

                    try:
                        self.assertCallableMetadataIsSane(m, exclude_cocoa=True)
                    except self.failureException:
                        self.fail("Unexpected failure")

            finally:
                if orig_Cocoa is None:
                    del sys.modules["Cocoa"]
                else:
                    sys.modules["Cocoa"] = orig_Cocoa

            fn.assert_any_call(
                MyClassForValidating.mymethod,
                "MyClassForValidating",
                skip_simple_charptr_check=False,
            )

            for entry in fn.call_args_list:
                self.assertNotIsInstance(entry.args[0], objc.ivar)
                self.assertNotEqual(
                    entry.args[0],
                    objc.lookUpClass("NSArray").pyobjc_instanceMethods.initWithArray_,
                )

        with self.subTest("function"):

            class Function:
                pass

            aFunction = Function()

            orig_function = objc.function
            objc.function = Function
            try:
                with mock.patch(
                    "PyObjCTools.TestSupport.TestCase._validateCallableMetadata"
                ) as fn:
                    m = Mod()
                    m.function = aFunction

                    try:
                        self.assertCallableMetadataIsSane(m, exclude_cocoa=True)
                    except self.failureException:
                        self.fail("Unexpected failure")
            finally:
                objc.function = orig_function

            fn.assert_any_call(aFunction)

        with self.subTest("ignored entries"):

            class Function:
                pass

            aFunction = Function()

            orig_function = objc.function
            objc.function = Function
            try:
                with mock.patch(
                    "PyObjCTools.TestSupport.TestCase._validateCallableMetadata"
                ) as fn:
                    m = Mod()
                    m.function = aFunction
                    m.NSObject = NSObject

                    try:
                        self.assertCallableMetadataIsSane(
                            m,
                            exclude_cocoa=False,
                            exclude_attrs=[
                                "function",
                                ("NSObject", "description"),
                            ],
                        )
                    except self.failureException:
                        self.fail("Unexpected failure")
            finally:
                objc.function = orig_function

            fn.assert_any_call(
                NSObject.pyobjc_classMethods.new,
                "NSObject",
                skip_simple_charptr_check=True,
            )
            for entry in fn.call_args_list:
                self.assertIsNot(entry.args[0], aFunction)
                self.assertIsNot(
                    entry.args[0], NSObject.pyobjc_instanceMethods.description
                )
                self.assertIsNot(
                    entry.args[0], NSObject.pyobjc_classMethods.description
                )

    @no_autorelease_pool
    def test_without_pool(self):
        self.assertIs(self._skip_usepool, True)

    def test_with_pool(self):
        self.assertIs(self._skip_usepool, False)

    def test_running(self):
        orig_use = TestSupport._usepool
        orig_class = TestSupport._poolclass
        orig_run = TestSupport._unittest.TestCase.run

        allocs = [0]
        NSObject = objc.lookUpClass("NSObject")
        self.assertIsNot(NSObject, None)

        class PoolClass:
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
