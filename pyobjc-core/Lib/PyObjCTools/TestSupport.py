"""
Helper code for implementing unittests.

This module is unsupported and is primairily used in the PyObjC
testsuite.
"""

import contextlib
import gc as _gc
import os as _os
import re as _re
import struct as _struct
import sys as _sys
import unittest as _unittest
import subprocess as _subprocess
import pickle as _pickle
from distutils.sysconfig import get_config_var as _get_config_var

import objc


# Ensure that methods in this module get filtered in the tracebacks
# from unittest
__unittest = False

# Have a way to disable the autorelease pool behaviour
_usepool = not _os.environ.get("PYOBJC_NO_AUTORELEASE")

# XXX: Python 2 Compatibility for the PyObjC Test Suite
try:
    unicode
except NameError:
    unicode = str

try:
    long
except NameError:
    long = int

try:
    basestring
except NameError:
    basestring = str

try:
    unichr
except NameError:
    unichr = chr


def _typemap(tp):
    if tp is None:
        return None
    return (
        tp.replace(b"_NSRect", b"CGRect")
        .replace(b"_NSPoint", b"CGPoint")
        .replace(b"_NSSize", b"CGSize")
    )


@contextlib.contextmanager
def pyobjc_options(**kwds):
    orig = {}
    try:
        for k in kwds:
            orig[k] = getattr(objc.options, k)
            setattr(objc.options, k, kwds[k])

        yield

    finally:
        for k in orig:
            setattr(objc.options, k, orig[k])


def sdkForPython(_cache=[]):  # noqa: B006, M511
    """
    Return the SDK version used to compile Python itself,
    or None if no framework was used
    """
    if not _cache:

        cflags = _get_config_var("CFLAGS")
        m = _re.search(r"-isysroot\s+([^ ]*)(\s|$)", cflags)
        if m is None:
            _cache.append(None)
            return None

        path = m.group(1)
        if path == "/":
            result = tuple(map(int, os_release().split(".")))
            _cache.append(result)
            return result

        bn = _os.path.basename(path)
        version = bn[6:-4]
        if version.endswith("u"):
            version = version[:-1]

        result = tuple(map(int, version.split(".")))
        _cache.append(result)
        return result

    return _cache[0]


def fourcc(v):
    """
    Decode four-character-code integer definition

    (e.g. 'abcd')
    """
    return _struct.unpack(">i", v)[0]


def cast_int(value):
    """
    Cast value to 32bit integer

    Usage:
        cast_int(1 << 31) == -1

    (where as: 1 << 31 == 2147483648)
    """
    value = value & 0xFFFFFFFF
    if value & 0x80000000:
        value = ~value + 1 & 0xFFFFFFFF
        return -value
    else:
        return value


def cast_longlong(value):
    """
    Cast value to 64bit integer

    Usage:
        cast_longlong(1 << 63) == -1
    """
    value = value & 0xFFFFFFFFFFFFFFFF
    if value & 0x8000000000000000:
        value = ~value + 1 & 0xFFFFFFFFFFFFFFFF
        return -value
    else:
        return value


def cast_uint(value):
    """
    Cast value to 32bit integer

    Usage:
        cast_int(1 << 31) == 2147483648

    """
    value = value & 0xFFFFFFFF
    return value


def cast_ulonglong(value):
    """
    Cast value to 64bit integer
    """
    value = value & 0xFFFFFFFFFFFFFFFF
    return value


_os_release = None


def os_release():
    """
    Returns the release of macOS (for example 10.5.1).
    """
    global _os_release
    if _os_release is not None:
        return _os_release

    _os_release = (
        _subprocess.check_output(["sw_vers", "-productVersion"]).decode().strip()
    )

    return _os_release


def arch_only(arch):
    """
    Usage::
        class Tests (unittest.TestCase):

            @arch_only("arm64")
            def testArm64(self):
                pass

    The test runs only when the specified architecture matches
    """

    def decorator(function):
        return _unittest.skipUnless(objc.arch == arch, f"{arch} only")(function)

    return decorator


def min_python_release(version):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_python_release('3.2')
            def test_python_3_2(self):
                pass
    """
    parts = tuple(map(int, version.split(".")))
    return _unittest.skipUnless(
        _sys.version_info[:2] >= parts, f"Requires Python {version} or later"
    )


def _sort_key(version):
    parts = version.split(".")
    if len(parts) == 2:
        parts.append("0")

    if len(parts) != 3:
        raise ValueError(f"Invalid version: {version!r}")

    return tuple(int(x) for x in parts)


def os_level_key(release):
    """
    Return an object that can be used to compare two releases.
    """
    return _sort_key(release)


def min_sdk_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):
            @min_sdk_level('10.6')
            def testSnowLeopardSDK(self):
                pass
    """
    v = (objc.PyObjC_BUILD_RELEASE // 100, objc.PyObjC_BUILD_RELEASE % 100, 0)
    return _unittest.skipUnless(
        v >= os_level_key(release), f"Requires build with SDK {release} or later"
    )


def max_sdk_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):
            @max_sdk_level('10.5')
            def testUntilLeopardSDK(self):
                pass
    """
    v = (objc.PyObjC_BUILD_RELEASE // 100, objc.PyObjC_BUILD_RELEASE % 100, 0)
    return _unittest.skipUnless(
        v <= os_level_key(release), f"Requires build with SDK {release} or later"
    )


def min_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_os_level('10.6')
            def testSnowLeopardCode(self):
                pass
    """
    return _unittest.skipUnless(
        os_level_key(os_release()) >= os_level_key(release),
        f"Requires OSX {release} or later",
    )


def max_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @max_os_level('10.5')
            def testUntilLeopard(self):
                pass
    """
    return _unittest.skipUnless(
        os_level_key(os_release()) <= os_level_key(release),
        f"Requires OSX up to {release}",
    )


def os_level_between(min_release, max_release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @os_level_between('10.5', '10.8')
            def testUntilLeopard(self):
                pass
    """
    return _unittest.skipUnless(
        os_level_key(min_release)
        <= os_level_key(os_release())
        <= os_level_key(max_release),
        f"Requires OSX {min_release} up to {max_release}",
    )


_poolclass = objc.lookUpClass("NSAutoreleasePool")

# NOTE: On at least OSX 10.8 there are multiple proxy classes for CFTypeRef...
_nscftype = tuple(cls for cls in objc.getClassList() if "NSCFType" in cls.__name__)

_typealias = {}

_typealias[objc._C_LNG_LNG] = objc._C_LNG
_typealias[objc._C_ULNG_LNG] = objc._C_ULNG


class TestCase(_unittest.TestCase):
    """
    A version of TestCase that wraps every test into its own
    autorelease pool.

    This also adds a number of useful assertion methods
    """

    # New API for testing function/method signatures, with one assert for
    # the callable and one assert each for every return value and argument.
    #
    # Primary reason for the new API is to ensure that all metadata overrides
    # are explicitly tested.

    def assertManualBinding(self, func):
        if hasattr(func, "__metadata__"):
            self.fail(f"{func} has automatic bindings")

    def assertCallable(self, func, *, argcount, variadic=None, deprecated=None):
        """
        Assert basic information about a method or function
        """

        results = []
        if not hasattr(func, "__metadata__"):
            self.fail("{func} has manual bindings")

        info = func.__metadata__()

        if isinstance(func, objc.selector):
            cnt = info["arguments"] - 2
        else:
            cnt = info["arguments"]

        if cnt != argcount:
            results.append(f"{cnt} argument, expected {argcount}")

        if variadic is not None:
            if func.get("variadic") is not variadic:
                results.append(f"variadic {info['variadic']!r} is not {variadic!r}")

        else:
            if info.get("variadic") is True:
                results.append("variadic is True, not tested")

        if deprecated is not None:
            if info.get("deprecated") != deprecated:
                results.append(f"variadic {info['deprecated']!r} != {deprecated!r}")

        else:
            if info.get("deprecated") is not None:
                results.append("deprecated is set, not tested")

        if results:
            self.fail(f"{func}: " + ", ".join(results))

    def assertReturns(
        self,
        func,
        *,
        type_encoding=None,
        null_accepted=None,
        already_retained=None,
        already_cfretained=None,
        callable=None,  # noqa: A002
        c_array_of_variable_length=None,
        c_array_delimited_by_null=None,
    ):
        """
        Assert information about a return value
        """

        results = []
        info = func.__metadata__()["retval"]

        if type_encoding is not None:
            if info["type"] != type_encoding:
                results.append(f"encoding {info['type']!r} != {type_encoding!r}")

        if null_accepted is not None:
            if info["null_accepted"] is not null_accepted:
                results.append(
                    f"null_accepted {info['null_accepted']!r} is not {null_accepted!r}"
                )

        else:
            if info["null_accepted"] is False:
                results.append("null_accepted is False, not tested")

        if already_retained is not None:
            if info["already_retained"] is not already_retained:
                results.append(
                    f"already_retained {info['already_retained']!r} is not {already_retained!r}"
                )

        else:
            if info["already_retained"] is True:
                results.append("already_retained is True, not tested")

        if already_cfretained is not None:
            if info["already_cfretained"] is not already_cfretained:
                results.append(
                    f"already_cfretained {info['already_cfretained']!r} is not {already_cfretained!r}"
                )

        else:
            if info["already_cfretained"] is True:
                results.append("already_cfretained is True, not tested")

        if c_array_of_variable_length is not None:
            if info["c_array_of_variable_length"] is not c_array_of_variable_length:
                results.append(
                    f"c_array_of_variable_length {info['c_array_of_variable_length']!r} is not {c_array_of_variable_length!r}"
                )

        else:
            if info["c_array_of_variable_length"] is True:
                results.append("c_array_of_variable_length is True, not tested")

        if c_array_delimited_by_null is not None:
            if info["c_array_delimited_by_null"] is not c_array_delimited_by_null:
                results.append(
                    f"c_array_delimited_by_null {info['c_array_delimited_by_null']!r} is not {c_array_delimited_by_null!r}"
                )

        else:
            if info["c_array_delimited_by_null"] is True:
                results.append("c_array_delimited_by_null is True, not tested")

        if callable is not None:
            raise RuntimeError("Need to design API for this")

        if results:
            self.fail(f"{func} return-value: " + ", ".join(results))

    def assertArgument(
        self,
        func,
        argno,
        *,
        type_encoding=None,
        type_modifier=None,
        null_accepted=None,
        printf_format=None,
        already_retained=None,
        already_cfretained=None,
        callable=None,  # noqa: A002
        callable_retaind=None,
        c_array_length_in_arg=None,
        c_array_length_in_result=None,
        c_array_of_variable_length=None,
        c_array_delimited_by_null=None,
    ):
        """
        Assert information about an argument
        """
        try:
            if isinstance(func, objc.selector):
                info = func.__metadata__()["arguments"][argno + 2]
            else:
                info = func.__metadata__()["arguments"][argno]
        except IndexError:
            self.fail(f"{func.__name__!r} does not have argument {argno}")

        results = []
        have_modifier = False
        have_array = False

        if type_encoding is not None:
            if type_modifier is not None:
                expected_type = type_modifier + type_encoding

            else:
                expected_type = type_encoding

            if info["type"] != expected_type:
                results.append(f"encoding {info['type']!r} != {expected_type!r}")

        elif type_modifier is not None:
            if not info["type"].startswith(type_modifier + b"^") and not info[
                "type"
            ].startswith(type_modifier + b"*"):
                results.append(
                    f"modifier {type_modifier!r} not set or set for non-pointer {info['type']!r}"
                )
            else:
                have_modifier = True

        else:
            if info["type"][0] in (objc._C_IN, objc._C_OUT, objc._C_INOUT):
                results.append("modifier is set, not tested")
                have_modifier = True

        if null_accepted is not None:
            if info["null_accepted"] is not null_accepted:
                results.append(
                    f"null_accepted {info['null_accepted']!r} is not {null_accepted!r}"
                )

        else:
            if info["null_accepted"] is False:
                results.append("null_accepted is False, not tested")

        if printf_format is not None:
            if info["printf_format"] is not null_accepted:
                results.append(
                    f"printf_format {info['printf_format']!r} is not {printf_format!r}"
                )

        else:
            if info["printf_format"] is True:
                results.append("printf_format is True, not tested")

        if already_retained is not None:
            if info["already_retained"] is not already_retained:
                results.append(
                    f"already_retained {info['already_retained']!r} is not {already_retained!r}"
                )

        else:
            if info["already_retained"] is True:
                results.append("already_retained is True, not tested")

        if already_cfretained is not None:
            if info["already_cfretained"] is not already_cfretained:
                results.append(
                    f"already_cfretained {info['already_cfretained']!r} is not {already_cfretained!r}"
                )

        else:
            if info["already_cfretained"] is True:
                results.append("already_cfretained is True, not tested")

        if c_array_of_variable_length is not None:
            have_array = True
            if info["c_array_of_variable_length"] is not c_array_of_variable_length:
                results.append(
                    f"c_array_of_variable_length {info['c_array_of_variable_length']!r} is not {c_array_of_variable_length!r}"
                )

        if c_array_length_in_arg is not None:
            have_array = True
            if info["c_array_length_in_arg"] != c_array_length_in_arg:
                results.append(
                    f"c_array_length_in_arg {info['c_array_length_in_arg']!r} != {c_array_length_in_arg!r}"
                )

        else:
            if info["c_array_length_in_arg"] is not None:
                results.append("c_array_length_in_arg is set, not tested")

        if c_array_length_in_result is not None:
            have_array = True
            if info["c_array_length_in_result"] is not c_array_length_in_result:
                results.append(
                    f"c_array_length_in_result {info['c_array_length_in_result']!r} is not {c_array_length_in_result!r}"
                )

        else:
            if info["c_array_length_in_result"] is True:
                results.append("c_array_length_in_arg is True, not tested")

        if c_array_delimited_by_null is not None:
            have_array = True
            if info["c_array_delimited_by_null"] is not c_array_delimited_by_null:
                results.append(
                    f"c_array_delimited_by_null {info['c_array_delimited_by_null']!r} is not {c_array_delimited_by_null!r}"
                )

        else:
            if info["c_array_delimited_by_null"] is True:
                results.append("c_array_delimited_by_null is True, not tested")

        if have_array and not have_modifier:
            results.append("array, not no modifier specified")

        if callable is not None:
            raise RuntimeError("Need to design API for this")

        if results:
            self.fail(f"{func} arg {argno}: " + ", ".join(results))

    # ----

    def assertIsCFType(self, tp, message=None):
        if not isinstance(tp, objc.objc_class):
            self.fail(message or f"{tp!r} is not a CFTypeRef type")

        if any(x is tp for x in _nscftype):
            self.fail(message or f"{tp!r} is not a unique CFTypeRef type")

        for cls in tp.__bases__:
            if "NSCFType" in cls.__name__:
                return

        self.fail(message or f"{tp!r} is not a CFTypeRef type")

        # NOTE: Don't test if this is a subclass of one of the known
        #       CF roots, this tests is mostly used to ensure that the
        #       type is distinct from one of those roots.
        # NOTE: With the next two lines enabled there are spurious test
        #       failures when a CF type is toll-free bridged to an
        #       (undocumented) Cocoa class. It might be worthwhile to
        #       look for these, but not in the test suite.
        # if not issubclass(tp, _nscftype):
        #    self.fail(message or "%r is not a CFTypeRef subclass"%(tp,))

    def assertIsOpaquePointer(self, tp, message=None):
        if not hasattr(tp, "__pointer__"):
            self.fail(message or f"{tp!r} is not an opaque-pointer")

        if not hasattr(tp, "__typestr__"):
            self.fail(message or f"{tp!r} is not an opaque-pointer")

    def assertResultIsNullTerminated(self, method, message=None):
        info = method.__metadata__()
        if not info.get("retval", {}).get("c_array_delimited_by_null"):
            self.fail(message or f"result of {method!r} is not a null-terminated array")

    def assertIsNullTerminated(self, method, message=None):
        info = method.__metadata__()
        if not info.get("c_array_delimited_by_null") or not info.get("variadic"):
            self.fail(
                message
                or "%s is not a variadic function with a "
                "null-terminated list of arguments" % (method,)
            )

    def assertArgIsNullTerminated(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if not info["arguments"][argno + offset].get("c_array_delimited_by_null"):
                self.fail(
                    message
                    or "argument %d of %r is not a null-terminated array"
                    % (argno, method)
                )
        except (KeyError, IndexError):
            self.fail(
                message
                or "argument %d of %r is not a null-terminated array" % (argno, method)
            )

    def assertArgIsVariableSize(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if not info["arguments"][argno + offset].get("c_array_of_variable_length"):
                self.fail(
                    message
                    or "argument %d of %r is not a variable sized array"
                    % (argno, method)
                )
        except (KeyError, IndexError):
            self.fail(
                message
                or "argument %d of %r is not a variable sized array" % (argno, method)
            )

    def assertResultIsVariableSize(self, method, message=None):
        info = method.__metadata__()
        if not info.get("retval", {}).get("c_array_of_variable_length", False):
            self.fail(message or f"result of {method!r} is not a variable sized array")

    def assertArgSizeInResult(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if not info["arguments"][argno + offset].get("c_array_length_in_result"):
                self.fail(
                    message
                    or "argument %d of %r does not have size in result"
                    % (argno, method)
                )
        except (KeyError, IndexError):
            self.fail(
                message
                or "argument %d of %r does not have size in result" % (argno, method)
            )

    def assertArgIsPrintf(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info.get("variadic"):
            self.fail(message or f"{method!r} is not a variadic function")

        try:
            if not info["arguments"][argno + offset].get("printf_format"):
                self.fail(
                    message
                    or "%r argument %d is not a printf format string" % (method, argno)
                )
        except (KeyError, IndexError):
            self.fail(
                message
                or "%r argument %d is not a printf format string" % (method, argno)
            )

    def assertArgIsCFRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()

        try:
            if not info["arguments"][argno + offset]["already_cfretained"]:
                self.fail(message or f"{method!r} is not cfretained")
        except (KeyError, IndexError):
            self.fail(message or f"{method!r} is not cfretained")

    def assertArgIsNotCFRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if info["arguments"][argno + offset]["already_cfretained"]:
                self.fail(message or f"{method!r} is cfretained")
        except (KeyError, IndexError):
            pass

    def assertResultIsCFRetained(self, method, message=None):
        info = method.__metadata__()

        if not info.get("retval", {}).get("already_cfretained", False):
            self.fail(message or f"{method!r} is not cfretained")

    def assertResultIsNotCFRetained(self, method, message=None):
        info = method.__metadata__()
        if info.get("retval", {}).get("already_cfretained", False):
            self.fail(message or f"{method!r} is cfretained")

    def assertArgIsRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()

        try:
            if not info["arguments"][argno + offset]["already_retained"]:
                self.fail(message or f"{method!r} is not retained")
        except (KeyError, IndexError):
            self.fail(message or f"{method!r} is not retained")

    def assertArgIsNotRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if info["arguments"][argno + offset]["already_retained"]:
                self.fail(message or f"{method!r} is retained")
        except (KeyError, IndexError):
            pass

    def assertResultIsRetained(self, method, message=None):
        info = method.__metadata__()
        if not info.get("retval", {}).get("already_retained", False):
            self.fail(message or f"{method!r} is not retained")

    def assertResultIsNotRetained(self, method, message=None):
        info = method.__metadata__()
        if info.get("retval", {}).get("already_retained", False):
            self.fail(message or f"{method!r} is retained")

    def assertResultHasType(self, method, tp, message=None):
        info = method.__metadata__()
        typestr = info.get("retval").get("type", b"v")
        if (
            typestr != tp
            and _typemap(typestr) != _typemap(tp)
            and _typealias.get(typestr, typestr) != _typealias.get(tp, tp)
        ):
            self.fail(
                message
                or f"result of {method!r} is not of type {tp!r}, but {typestr!r}"
            )

    def assertArgHasType(self, method, argno, tp, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            i = info["arguments"][argno + offset]

        except (KeyError, IndexError):
            self.fail(
                message
                or "arg %d of %s has no metadata (or doesn't exist)" % (argno, method)
            )

        else:
            typestr = i.get("type", b"@")

        if (
            typestr != tp
            and _typemap(typestr) != _typemap(tp)
            and _typealias.get(typestr, typestr) != _typealias.get(tp, tp)
        ):
            self.fail(
                message
                or "arg %d of %s is not of type %r, but %r"
                % (argno, method, tp, typestr)
            )

    def assertArgIsFunction(self, method, argno, sel_type, retained, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()

        try:
            i = info["arguments"][argno + offset]
        except (KeyError, IndexError):
            self.fail(
                message
                or "arg %d of %s has no metadata (or doesn't exist)" % (argno, method)
            )

        else:
            typestr = i.get("type", b"@")

        if typestr != b"^?":
            self.fail(
                message
                or "arg %d of %s is not of type function_pointer" % (argno, method)
            )

        st = i.get("callable")
        if st is None:
            self.fail(
                message
                or "arg %d of %s is not of type function_pointer" % (argno, method)
            )

        try:
            iface = st["retval"]["type"]
            for a in st["arguments"]:
                iface += a["type"]
        except KeyError:
            self.fail(
                message
                or "arg %d of %s is a function pointer with incomplete type information"
                % (argno, method)
            )

        if iface != sel_type:
            self.fail(
                message
                or "arg %d of %s is not a function_pointer with type %r, but %r"
                % (argno, method, sel_type, iface)
            )

        st = info["arguments"][argno + offset].get("callable_retained", False)
        if bool(st) != bool(retained):
            self.fail(
                message
                or "arg %d of %s; retained: %r, expected: %r"
                % (argno, method, st, retained)
            )

    def assertResultIsFunction(self, method, sel_type, message=None):
        info = method.__metadata__()

        try:
            i = info["retval"]
        except (KeyError, IndexError):
            self.fail(
                message or f"result of {method} has no metadata (or doesn't exist)"
            )

        else:
            typestr = i.get("type", b"@")

        if typestr != b"^?":
            self.fail(message or f"result of {method} is not of type function_pointer")

        st = i.get("callable")
        if st is None:
            self.fail(message or f"result of {method} is not of type function_pointer")

        try:
            iface = st["retval"]["type"]
            for a in st["arguments"]:
                iface += a["type"]
        except KeyError:
            self.fail(
                message
                or "result of %s is a function pointer with incomplete type information"
                % (method,)
            )

        if iface != sel_type:
            self.fail(
                message
                or "result of %s is not a function_pointer with type %r, but %r"
                % (method, sel_type, iface)
            )

    def assertArgIsBlock(self, method, argno, sel_type, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            typestr = info["arguments"][argno + offset]["type"]
        except (IndexError, KeyError):
            self.fail("arg %d of %s does not exist" % (argno, method))

        if typestr != b"@?":
            self.fail(
                message
                or "arg %d of %s is not of type block: %s" % (argno, method, typestr)
            )

        st = info["arguments"][argno + offset].get("callable")
        if st is None:
            self.fail(
                message
                or "arg %d of %s is not of type block: no callable" % (argno, method)
            )

        try:
            iface = st["retval"]["type"]
            if st["arguments"][0]["type"] != b"^v":
                self.fail(
                    message
                    or "arg %d of %s has an invalid block signature %r for argument 0"
                    % (argno, method, st["arguments"][0]["type"])
                )
            for a in st["arguments"][1:]:
                iface += a["type"]
        except KeyError:
            self.fail(
                message
                or "result of %s is a block pointer with incomplete type information"
                % (method,)
            )

        if iface != sel_type:
            self.fail(
                message
                or "arg %d of %s is not a block with type %r, but %r"
                % (argno, method, sel_type, iface)
            )

    def assertResultIsBlock(self, method, sel_type, message=None):
        info = method.__metadata__()

        try:
            typestr = info["retval"]["type"]
            if typestr != b"@?":
                self.fail(
                    message or f"result of {method} is not of type block: {typestr}"
                )
        except KeyError:
            self.fail(
                message or "result of {} is not of type block: {}".format(method, b"v")
            )

        st = info["retval"].get("callable")
        if st is None:
            self.fail(
                message
                or "result of %s is not of type block: no callable specified" % (method)
            )

        try:
            iface = st["retval"]["type"]
            if st["arguments"][0]["type"] != b"^v":
                self.fail(
                    message
                    or "result %s has an invalid block signature %r for argument 0"
                    % (method, st["arguments"][0]["type"])
                )
            for a in st["arguments"][1:]:
                iface += a["type"]
        except KeyError:
            self.fail(
                message
                or "result of %s is a block pointer with incomplete type information"
                % (method,)
            )

        if iface != sel_type:
            self.fail(
                message
                or "result of %s is not a block with type %r, but %r"
                % (method, sel_type, iface)
            )

    def assertResultIsSEL(self, method, sel_type, message=None):
        info = method.__metadata__()
        try:
            i = info["retval"]
        except (KeyError, IndexError):
            self.fail(
                message or f"result of {method} has no metadata (or doesn't exist)"
            )

        typestr = i.get("type", b"@")
        if typestr != objc._C_SEL:
            self.fail(message or f"result of {method} is not of type SEL")

        st = i.get("sel_of_type")
        if st != sel_type and _typemap(st) != _typemap(sel_type):
            self.fail(
                message
                or "result of %s doesn't have sel_type %r but %r"
                % (method, sel_type, st)
            )

    def assertArgIsSEL(self, method, argno, sel_type, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            i = info["arguments"][argno + offset]
        except (KeyError, IndexError):
            self.fail(
                message
                or "arg %d of %s has no metadata (or doesn't exist)" % (argno, method)
            )

        typestr = i.get("type", b"@")
        if typestr != objc._C_SEL:
            self.fail(message or "arg %d of %s is not of type SEL" % (argno, method))

        st = i.get("sel_of_type")
        if st != sel_type and _typemap(st) != _typemap(sel_type):
            self.fail(
                message
                or "arg %d of %s doesn't have sel_type %r but %r"
                % (argno, method, sel_type, st)
            )

    def assertResultIsBOOL(self, method, message=None):
        info = method.__metadata__()
        typestr = info["retval"]["type"]
        if typestr != objc._C_NSBOOL:
            self.fail(
                message or f"result of {method} is not of type BOOL, but {typestr!r}"
            )

    def assertArgIsBOOL(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        typestr = info["arguments"][argno + offset]["type"]
        if typestr != objc._C_NSBOOL:
            self.fail(
                message
                or "arg %d of %s is not of type BOOL, but %r" % (argno, method, typestr)
            )

    def assertArgIsFixedSize(self, method, argno, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            cnt = info["arguments"][argno + offset]["c_array_of_fixed_length"]
            if cnt != count:
                self.fail(
                    message
                    or "arg %d of %s is not a C-array of length %d"
                    % (argno, method, count)
                )
        except (KeyError, IndexError):
            self.fail(
                message
                or "arg %d of %s is not a C-array of length %d" % (argno, method, count)
            )

    def assertResultIsFixedSize(self, method, count, message=None):
        info = method.__metadata__()
        try:
            cnt = info["retval"]["c_array_of_fixed_length"]
            if cnt != count:
                self.fail(
                    message
                    or "result of %s is not a C-array of length %d" % (method, count)
                )
        except (KeyError, IndexError):
            self.fail(
                message
                or "result of %s is not a C-array of length %d" % (method, count)
            )

    def assertArgSizeInArg(self, method, argno, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            cnt = info["arguments"][argno + offset]["c_array_length_in_arg"]
        except (KeyError, IndexError):
            self.fail(
                message
                or "arg %d of %s is not a C-array of with length in arg %s"
                % (argno, method, count)
            )

        if isinstance(count, (list, tuple)):
            count2 = tuple(x + offset for x in count)
        else:
            count2 = count + offset
        if cnt != count2:
            self.fail(
                message
                or "arg %d of %s is not a C-array of with length in arg %s"
                % (argno, method, count)
            )

    def assertResultSizeInArg(self, method, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info["retval"]["c_array_length_in_arg"]
        if cnt != count + offset:
            self.fail(
                message
                or "result %s is not a C-array of with length in arg %d"
                % (method, count)
            )

    def assertArgIsOut(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        typestr = info["arguments"][argno + offset]["type"]
        if not typestr.startswith(b"o^") and not typestr.startswith(b"o*"):
            self.fail(
                message or "arg %d of %s is not an 'out' argument" % (argno, method)
            )

    def assertArgIsInOut(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        typestr = info["arguments"][argno + offset]["type"]
        if not typestr.startswith(b"N^") and not typestr.startswith(b"N*"):
            self.fail(
                message or "arg %d of %s is not an 'inout' argument" % (argno, method)
            )

    def assertArgIsIn(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        typestr = info["arguments"][argno + offset]["type"]
        if not typestr.startswith(b"n^") and not typestr.startswith(b"n*"):
            self.fail(
                message or "arg %d of %s is not an 'in' argument" % (argno, method)
            )

    def assertStartswith(self, value, test, message=None):  # pragma: no cover
        if not value.startswith(test):
            self.fail(message or f"{value!r} does not start with {test!r}")

    def assertHasAttr(self, value, key, message=None):
        if not hasattr(value, key):
            self.fail(message or f"{key} is not an attribute of {value!r}")

    def assertNotHasAttr(self, value, key, message=None):
        if hasattr(value, key):
            self.fail(message or f"{key} is an attribute of {value!r}")

    def assertIsSubclass(self, value, types, message=None):
        if not issubclass(value, types):
            self.fail(message or f"{value} is not a subclass of {types!r}")

    def assertIsNotSubclass(self, value, types, message=None):
        if issubclass(value, types):
            self.fail(message or f"{value} is a subclass of {types!r}")

    def assertClassIsFinal(self, cls):
        if not isinstance(cls, objc.objc_class):
            self.fail(f"{cls} is not an Objective-C class")
        elif not cls.__objc_final__:
            self.fail(f"{cls} is not an final class")

    def assertProtocolExists(self, name):
        ok = True
        try:
            proto = objc.protocolNamed(name)

        except objc.ProtocolError:
            ok = False

        if not ok:
            self.fail(f"Protocol {name!r} does not exist")

        if not isinstance(proto, objc.formal_protocol):
            # Should never happen
            self.fail(f"Protocol {name!r} is not a protocol, but {type(proto)}")

    def assertPickleRoundTrips(self, value):
        buf = _pickle.dumps(value)
        clone = _pickle.loads(buf)

        self.assertEqual(clone, value)
        self.assertIsInstance(clone, type(value))

    def run(self, *args):
        """
        Run the test, same as unittest.TestCase.run, but every test is
        run with a fresh autorelease pool.
        """
        if _usepool:
            p = _poolclass.alloc().init()
        else:
            p = 1

        try:
            _unittest.TestCase.run(self, *args)
        finally:
            _gc.collect()
            del p
            _gc.collect()


main = _unittest.main
expectedFailure = _unittest.expectedFailure
skipUnless = _unittest.skipUnless


def expectedFailureIf(condition):
    if condition:
        return expectedFailure
    else:
        return lambda func: func
