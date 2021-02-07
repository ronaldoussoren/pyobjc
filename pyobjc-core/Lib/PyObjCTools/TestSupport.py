"""
Helper code for implementing unittests.

This module is unsupported and is primairily used in the PyObjC
testsuite.
"""
from __future__ import print_function

import contextlib
import gc as _gc
import os as _os
import plistlib as _pl
import re as _re
import struct as _struct
import sys as _sys
import unittest as _unittest
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

    if hasattr(_pl, "load"):
        with open("/System/Library/CoreServices/SystemVersion.plist", "rb") as fp:
            pl = _pl.load(fp)
    else:
        pl = _pl.readPlist("/System/Library/CoreServices/SystemVersion.plist")
    v = pl["ProductVersion"]
    return ".".join(v.split("."))


def is32Bit():
    """
    Return True if we're running in 32-bit mode
    """
    if _sys.maxsize > 2 ** 32:
        return False
    return True


def onlyIf(expr, message=None):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyIf(1 == 2)
            def testUnlikely(self):
                pass

    The test only runs when the argument expression is true
    """

    def callback(function):
        if not expr:
            if hasattr(_unittest, "skip"):
                return _unittest.skip(message)(function)
            return lambda self: None  # pragma: no cover (py2.6)
        else:
            return function

    return callback


def onlyPython2(function):
    """
    Usage:
        class Tests (unittest.TestCase):

            @onlyPython2
            def testPython2(self):
                pass

    The test is only executed for Python 2.x
    """
    return onlyIf(_sys.version_info[0] == 2, "python2.x only")(function)


def onlyPython3(function):
    """
    Usage:
        class Tests (unittest.TestCase):

            @onlyPython3
            def testPython3(self):
                pass

    The test is only executed for Python 3.x
    """
    return onlyIf(_sys.version_info[0] == 3, "python3.x only")(function)


def onlyOn32Bit(function):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyOn32Bit
            def test32BitOnly(self):
                pass

    The test runs only on 32-bit systems
    """
    return onlyIf(is32Bit(), "32-bit only")(function)


def onlyOn64Bit(function):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyOn64Bit
            def test64BitOnly(self):
                pass

    The test runs only on 64-bit systems
    """
    return onlyIf(not is32Bit(), "64-bit only")(function)


def min_python_release(version):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_python_release('3.2')
            def test_python_3_2(self):
                pass
    """
    parts = tuple(map(int, version.split(".")))
    return onlyIf(
        _sys.version_info[:2] >= parts, "Requires Python %s or later" % (version,)
    )


def _sort_key(version):
    parts = version.split(".")
    if len(parts) == 2:
        parts.append("0")

    if len(parts) != 3:
        raise ValueError("Invalid version: %r" % (version,))

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
    return onlyIf(
        v >= os_level_key(release), "Requires build with SDK %s or later" % (release,)
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
    return onlyIf(
        v <= os_level_key(release), "Requires build with SDK %s or later" % (release,)
    )


def min_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_os_level('10.6')
            def testSnowLeopardCode(self):
                pass
    """
    return onlyIf(
        os_level_key(os_release()) >= os_level_key(release),
        "Requires OSX %s or later" % (release,),
    )


def max_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @max_os_level('10.5')
            def testUntilLeopard(self):
                pass
    """
    return onlyIf(
        os_level_key(os_release()) <= os_level_key(release),
        "Requires OSX upto %s" % (release,),
    )


def os_level_between(min_release, max_release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @os_level_between('10.5', '10.8')
            def testUntilLeopard(self):
                pass
    """
    return onlyIf(
        os_level_key(min_release)
        <= os_level_key(os_release())
        <= os_level_key(max_release),
        "Requires OSX %s upto %s" % (min_release, max_release),
    )


_poolclass = objc.lookUpClass("NSAutoreleasePool")

# NOTE: On at least OSX 10.8 there are multiple proxy classes for CFTypeRef...
_nscftype = tuple(cls for cls in objc.getClassList() if "NSCFType" in cls.__name__)

_typealias = {}

if not is32Bit():
    _typealias[objc._C_LNG_LNG] = objc._C_LNG
    _typealias[objc._C_ULNG_LNG] = objc._C_ULNG

else:  # pragma: no cover (32-bit)
    _typealias[objc._C_LNG] = objc._C_INT
    _typealias[objc._C_ULNG] = objc._C_UINT


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
                results.append(f"variadic is True, not tested")

        if deprecated is not None:
            if info.get("deprecated") != deprecated:
                results.append(f"variadic {info['deprecated']!r} != {deprecated!r}")

        else:
            if info.get("deprecated") is not None:
                results.append(f"deprecated is set, not tested")

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
                results.append(f"null_accepted is False, not tested")

        if already_retained is not None:
            if info["already_retained"] is not already_retained:
                results.append(
                    f"already_retained {info['already_retained']!r} is not {already_retained!r}"
                )

        else:
            if info["already_retained"] is True:
                results.append(f"already_retained is True, not tested")

        if already_cfretained is not None:
            if info["already_cfretained"] is not already_cfretained:
                results.append(
                    f"already_cfretained {info['already_cfretained']!r} is not {already_cfretained!r}"
                )

        else:
            if info["already_cfretained"] is True:
                results.append(f"already_cfretained is True, not tested")

        if c_array_of_variable_length is not None:
            if info["c_array_of_variable_length"] is not c_array_of_variable_length:
                results.append(
                    f"c_array_of_variable_length {info['c_array_of_variable_length']!r} is not {c_array_of_variable_length!r}"
                )

        else:
            if info["c_array_of_variable_length"] is True:
                results.append(f"c_array_of_variable_length is True, not tested")

        if c_array_delimited_by_null is not None:
            if info["c_array_delimited_by_null"] is not c_array_delimited_by_null:
                results.append(
                    f"c_array_delimited_by_null {info['c_array_delimited_by_null']!r} is not {c_array_delimited_by_null!r}"
                )

        else:
            if info["c_array_delimited_by_null"] is True:
                results.append(f"c_array_delimited_by_null is True, not tested")

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
                results.append(f"null_accepted is False, not tested")

        if printf_format is not None:
            if info["printf_format"] is not null_accepted:
                results.append(
                    f"printf_format {info['printf_format']!r} is not {printf_format!r}"
                )

        else:
            if info["printf_format"] is True:
                results.append(f"printf_format is True, not tested")

        if already_retained is not None:
            if info["already_retained"] is not already_retained:
                results.append(
                    f"already_retained {info['already_retained']!r} is not {already_retained!r}"
                )

        else:
            if info["already_retained"] is True:
                results.append(f"already_retained is True, not tested")

        if already_cfretained is not None:
            if info["already_cfretained"] is not already_cfretained:
                results.append(
                    f"already_cfretained {info['already_cfretained']!r} is not {already_cfretained!r}"
                )

        else:
            if info["already_cfretained"] is True:
                results.append(f"already_cfretained is True, not tested")

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
                results.append(f"c_array_length_in_arg is set, not tested")

        if c_array_length_in_result is not None:
            have_array = True
            if info["c_array_length_in_result"] is not c_array_length_in_result:
                results.append(
                    f"c_array_length_in_result {info['c_array_length_in_result']!r} is not {c_array_length_in_result!r}"
                )

        else:
            if info["c_array_length_in_result"] is True:
                results.append(f"c_array_length_in_arg is True, not tested")

        if c_array_delimited_by_null is not None:
            have_array = True
            if info["c_array_delimited_by_null"] is not c_array_delimited_by_null:
                results.append(
                    f"c_array_delimited_by_null {info['c_array_delimited_by_null']!r} is not {c_array_delimited_by_null!r}"
                )

        else:
            if info["c_array_delimited_by_null"] is True:
                results.append(f"c_array_delimited_by_null is True, not tested")

        if have_array and not have_modifier:
            results.append("array, not no modifier specified")

        if callable is not None:
            raise RuntimeError("Need to design API for this")

        if results:
            self.fail(f"{func} arg {argno}: " + ", ".join(results))

    # ----

    def assertIsCFType(self, tp, message=None):
        if not isinstance(tp, objc.objc_class):
            self.fail(message or "%r is not a CFTypeRef type" % (tp,))

        if any(x is tp for x in _nscftype):
            self.fail(message or "%r is not a unique CFTypeRef type" % (tp,))

        for cls in tp.__bases__:
            if "NSCFType" in cls.__name__:
                return

        self.fail(message or "%r is not a CFTypeRef type" % (tp,))

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
            self.fail(message or "%r is not an opaque-pointer" % (tp,))

        if not hasattr(tp, "__typestr__"):
            self.fail(message or "%r is not an opaque-pointer" % (tp,))

    def assertResultIsNullTerminated(self, method, message=None):
        info = method.__metadata__()
        if not info.get("retval", {}).get("c_array_delimited_by_null"):
            self.fail(
                message or "result of %r is not a null-terminated array" % (method,)
            )

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
            self.fail(
                message or "result of %r is not a variable sized array" % (method,)
            )

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
            self.fail(message or "%r is not a variadic function" % (method,))

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
                self.fail(message or "%r is not cfretained" % (method,))
        except (KeyError, IndexError):
            self.fail(message or "%r is not cfretained" % (method,))

    def assertArgIsNotCFRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if info["arguments"][argno + offset]["already_cfretained"]:
                self.fail(message or "%r is cfretained" % (method,))
        except (KeyError, IndexError):
            pass

    def assertResultIsCFRetained(self, method, message=None):
        info = method.__metadata__()

        if not info.get("retval", {}).get("already_cfretained", False):
            self.fail(message or "%r is not cfretained" % (method,))

    def assertResultIsNotCFRetained(self, method, message=None):
        info = method.__metadata__()
        if info.get("retval", {}).get("already_cfretained", False):
            self.fail(message or "%r is cfretained" % (method,))

    def assertArgIsRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()

        try:
            if not info["arguments"][argno + offset]["already_retained"]:
                self.fail(message or "%r is not retained" % (method,))
        except (KeyError, IndexError):
            self.fail(message or "%r is not retained" % (method,))

    def assertArgIsNotRetained(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        try:
            if info["arguments"][argno + offset]["already_retained"]:
                self.fail(message or "%r is retained" % (method,))
        except (KeyError, IndexError):
            pass

    def assertResultIsRetained(self, method, message=None):
        info = method.__metadata__()
        if not info.get("retval", {}).get("already_retained", False):
            self.fail(message or "%r is not retained" % (method,))

    def assertResultIsNotRetained(self, method, message=None):
        info = method.__metadata__()
        if info.get("retval", {}).get("already_retained", False):
            self.fail(message or "%r is retained" % (method,))

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
                or "result of %r is not of type %r, but %r" % (method, tp, typestr)
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
                message or "result of %s has no metadata (or doesn't exist)" % (method,)
            )

        else:
            typestr = i.get("type", b"@")

        if typestr != b"^?":
            self.fail(
                message or "result of %s is not of type function_pointer" % (method,)
            )

        st = i.get("callable")
        if st is None:
            self.fail(
                message or "result of %s is not of type function_pointer" % (method,)
            )

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
                    message
                    or "result of %s is not of type block: %s" % (method, typestr)
                )
        except KeyError:
            self.fail(
                message or "result of %s is not of type block: %s" % (method, b"v")
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
                message or "result of %s has no metadata (or doesn't exist)" % (method,)
            )

        typestr = i.get("type", b"@")
        if typestr != objc._C_SEL:
            self.fail(message or "result of %s is not of type SEL" % (method,))

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
                message
                or "result of %s is not of type BOOL, but %r" % (method, typestr)
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

    #
    # Addition assert methods, all of them should only be necessary for
    # python 2.7 or later
    #

    if not hasattr(_unittest.TestCase, "assertItemsEqual"):  # pragma: no cover

        def assertItemsEqual(self, seq1, seq2, message=None):
            # This is based on unittest.util._count_diff_all_purpose from
            # Python 2.7
            s, t = list(seq1), list(seq2)
            m, n = len(s), len(t)
            NULL = object()
            result = []
            for i, elem in enumerate(s):
                if elem is NULL:
                    continue

                cnt_s = cnt_t = 0
                for j in range(i, m):
                    if s[j] == elem:
                        cnt_s += 1
                        s[j] = NULL

                for j, other_elem in enumerate(t):
                    if other_elem == elem:
                        cnt_t += 1
                        t[j] = NULL

                if cnt_s != cnt_t:
                    result.append((cnt_s, cnt_t, elem))
            for i, elem in enumerate(t):
                if elem is NULL:
                    continue
                cnt_t = 0
                for j in range(i, n):
                    if t[j] == elem:
                        cnt_t += 1
                        t[j] = NULL

                result.append((0, cnt_t, elem))

            if result:
                for actual, expected, value in result:
                    print("Seq1 %d, Seq2: %d  value: %r" % (actual, expected, value))

                self.fail(
                    message
                    or (
                        "sequences do not contain the same items:"
                        + "\n".join(
                            ["Seq1 %d, Seq2: %d  value: %r" % (item) for item in result]
                        )
                    )
                )

    if not hasattr(_unittest.TestCase, "assertStartswith"):

        def assertStartswith(self, value, test, message=None):  # pragma: no cover
            if not value.startswith(test):
                self.fail(message or "%r does not start with %r" % (value, test))

    if not hasattr(_unittest.TestCase, "assertIs"):  # pragma: no cover

        def assertIs(self, value, test, message=None):
            if value is not test:
                self.fail(
                    message
                    or "%r (id=%r) is not %r (id=%r) "
                    % (value, id(value), test, id(test))
                )

    if not hasattr(_unittest.TestCase, "assertIsNot"):  # pragma: no cover

        def assertIsNot(self, value, test, message=None):
            if value is test:
                self.fail(message or "%r is %r" % (value, test))

    if not hasattr(_unittest.TestCase, "assertIsNone"):  # pragma: no cover

        def assertIsNone(self, value, message=None):
            self.assertIs(value, None)

    if not hasattr(_unittest.TestCase, "assertIsNotNone"):  # pragma: no cover

        def assertIsNotNone(self, value, message=None):
            if value is None:
                self.fail(message, "%r is not None" % (value,))

    if not hasattr(_unittest.TestCase, "assertHasAttr"):  # pragma: no cover

        def assertHasAttr(self, value, key, message=None):
            if not hasattr(value, key):
                self.fail(message or "%s is not an attribute of %r" % (key, value))

    if not hasattr(_unittest.TestCase, "assertNotHasAttr"):  # pragma: no cover

        def assertNotHasAttr(self, value, key, message=None):
            if hasattr(value, key):
                self.fail(message or "%s is an attribute of %r" % (key, value))

    def assertIsSubclass(self, value, types, message=None):
        if not issubclass(value, types):
            self.fail(message or "%s is not a subclass of %r" % (value, types))

    def assertIsNotSubclass(self, value, types, message=None):
        if issubclass(value, types):
            self.fail(message or "%s is a subclass of %r" % (value, types))

    if not hasattr(_unittest.TestCase, "assertIsInstance"):  # pragma: no cover

        def assertIsInstance(self, value, types, message=None):
            if not isinstance(value, types):
                self.fail(
                    message
                    or "%s is not an instance of %r but %s"
                    % (value, types, type(value))
                )

    if not hasattr(_unittest.TestCase, "assertIsNotInstance"):  # pragma: no cover

        def assertIsNotInstance(self, value, types, message=None):
            if isinstance(value, types):
                self.fail(message or "%s is an instance of %r" % (value, types))

    if not hasattr(_unittest.TestCase, "assertIn"):  # pragma: no cover

        def assertIn(self, value, seq, message=None):
            if value not in seq:
                self.fail(message or "%r is not in %r" % (value, seq))

    if not hasattr(_unittest.TestCase, "assertNotIn"):  # pragma: no cover

        def assertNotIn(self, value, seq, message=None):
            if value in seq:
                self.fail(message or "%r is in %r" % (value, seq))

    if not hasattr(_unittest.TestCase, "assertGreaterThan"):  # pragma: no cover

        def assertGreaterThan(self, val, test, message=None):
            if not (val > test):
                self.fail(message or "%r <= %r" % (val, test))

    if not hasattr(_unittest.TestCase, "assertGreaterEqual"):  # pragma: no cover

        def assertGreaterEqual(self, val, test, message=None):
            if not (val >= test):
                self.fail(message or "%r < %r" % (val, test))

    if not hasattr(_unittest.TestCase, "assertLessThan"):  # pragma: no cover

        def assertLessThan(self, val, test, message=None):
            if not (val < test):
                self.fail(message or "%r >= %r" % (val, test))

    if not hasattr(_unittest.TestCase, "assertLessEqual"):  # pragma: no cover

        def assertLessEqual(self, val, test, message=None):
            if not (val <= test):
                self.fail(message or "%r > %r" % (val, test))

    if not hasattr(_unittest.TestCase, "assertAlmostEquals"):  # pragma: no cover

        def assertAlmostEquals(self, val1, val2, message=None):
            self.failUnless(
                abs(val1 - val2) < 0.00001,
                message or "abs(%r - %r) >= 0.00001" % (val1, val2),
            )

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

if hasattr(_unittest, "expectedFailure"):
    expectedFailure = _unittest.expectedFailure

else:  # pragma: no cover (py2.6)

    def expectedFailure(func):
        def test(self):
            try:
                func(self)

            except AssertionError:
                return

            self.fail("test unexpectedly passed")

        test.__name__ == func.__name__

        return test


def expectedFailureIf(condition):
    if condition:
        return expectedFailure
    else:
        return lambda func: func
