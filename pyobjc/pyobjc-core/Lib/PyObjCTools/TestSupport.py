"""
Helper code for implementing unittests.

This module is unsupported and is primairily used in the PyObjC
testsuite.
"""
import plistlib as _pl
import unittest as _unittest
import objc
import os as _os
import gc as _gc
import subprocess as _subprocess
import sys as _sys
import struct as _struct
from distutils.sysconfig import get_config_var as _get_config_var
import re as _re

# Have a way to disable the autorelease pool behaviour
_usepool = not _os.environ.get('PYOBJC_NO_AUTORELEASE')
_useleaks = bool(_os.environ.get('PyOBJC_USE_LEAKS'))
_leaksVerbose = True

def sdkForPython(_cache=[]):
    """
    Return the SDK version used to compile Python itself,
    or None if no framework was used
    """
    if not _cache:

        cflags = _get_config_var('CFLAGS')
        m = _re.search('-isysroot ([^ ]*) ', cflags)
        if m is None:
            return None

        path = m.group(1)
        bn = _os.path.basename(path)
        version = bn[6:-4]
        if version.endswith('u'):
            version = version[:-1]

        return map(int, version.split('.'))

    return _cache[0]

def fourcc(v):
    """
    Decode four-character-code integer definition

    (e.g. 'abcd')
    """
    return _struct.unpack('>i', v)[0]

def cast_int(value):
    """
    Cast value to 32bit integer

    Usage:
        cast_int(1 << 31) == -1

    (where as: 1 << 31 == 2147483648)
    """
    value = value & 0xffffffff
    if value & 0x80000000:
        value =   ~value + 1 & 0xffffffff
        return -value
    else:
        return value

_os_release = None
def os_release():
    """
    Returns '10.5' on all releases of Leopard, simularly for other
    major releases.
    """
    global _os_release
    if _os_release is not None:
        return _os_release

    pl = _pl.readPlist('/System/Library/CoreServices/SystemVersion.plist')
    v = pl['ProductVersion']
    return '.'.join(v.split('.')[:2])

def onlyOn32Bit(function):
    """
    Usage::

        class Tests (unittest.TestCase):

            @onlyOn32Bit
            def test32BitOnly(self):
                pass

    The test runs only on 32-bit systems
    """
    if _sys.maxint > 2 ** 32:
        return None
    else:
        return function


def min_os_level(release):
    """
    Usage::

        class Tests (unittest.TestCase):

            @min_os_level('10.6')
            def testSnowLeopardCode(self):
                pass
    """
    if os_release() >= release:
        def decorator(function):
            return function

    else:
        def decorator(function):
            return None

    return decorator



def _leaks():
    data = _subprocess.Popen(
            ['/usr/bin/leaks', str(_os.getpid())], stdout=_subprocess.PIPE
        ).communicate()[0]
    return data.splitlines()


_poolclass = objc.lookUpClass('NSAutoreleasePool')
_nscftype = objc.lookUpClass('NSCFType')

class TestCase (_unittest.TestCase):
    """
    A version of TestCase that wraps every test into its own
    autorelease pool.

    This also adds a number of useful assertion methods
    """
    def failUnlessIsCFType(self, tp, message = None):
        if not isinstance(tp, objc.objc_class):
            self.fail(message or "%r is not a CFTypeRef type"%(tp,))

        if tp is _nscftype:
            self.fail(message or "%r is not a unique CFTypeRef type"%(tp,))

    def failUnlessIsOpaquePointer(self, tp, message = None):
        if not hasattr(tp, "__pointer__"):
            self.fail(message or "%r is not an opaque-pointer"%(tp,))

        if not hasattr(tp, "__typestr__"):
            self.fail(message or "%r is not an opaque-pointer"%(tp,))


    def failUnlessIsNone(self, value, message = None):
        if value is not None:
            sel.fail(message or "%r is not %r"%(value, test))

    def failIfIsNone(self, value,  message = None):
        if value is None:
            sel.fail(message, "%r is not %r"%(value, test))

    def failUnlessResultIsNullTerminated(self, method, message = None):
        info = method.__metadata__()
        if not info['retval'].get('c_array_delimited_by_null'):
            self.fail(message or "argument %d of %r is not a nul-terminated array"%(argno, method))

    def failUnlessIsNullTerminated(self, method, message = None):
        info = method.__metadata__()
        if not info.get('c_array_delimited_by_null') or not info.get('variadic'):
            self.fail(message or "%s is not a variadic function with a null-terminated list of arguments"%(method,))

    def failUnlessArgIsNullTerminated(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset].get('c_array_delimited_by_null'):
            self.fail(message or "argument %d of %r is not a nul-terminated array"%(argno, method))

    def failUnlessArgIsVariableSize(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset].get('c_array_of_variable_length'):
            self.fail(message or "argument %d of %r is not a variable sized array"%(argno, method))

    def failUnlessResultIsVariableSize(self, method, message = None):
        info = method.__metadata__()
        if not info['retval'].get('c_array_of_variable_length'):
            self.fail(message or "result of %r is not a variable sized array"%(argno, method))

    def failUnlessArgSizeInResult(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset].get('c_array_length_in_result'):
            self.fail(message or "argument %d of %r does not have size in result"%(argno, method))

    def failUnlessArgIsPrintf(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info.get('variadic'):
            self.fail(message or "%r is not a variadic function"%(method,))

        if not info['arguments'][argno+offset].get('printf_format'):
            self.fail(message or "%r argument %d is not a printf format string"%(method, argno))

    def failUnlessArgIsCFRetained(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if not info['arguments'][argno+offset]['already_cfretained']:
            self.fail(message or "%r is not cfretained"%(method,))

    def failIfArgIsCFRetained(self, method, argno, message = None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        if info['arguments'][argno+offset]['already_cfretained']:
            self.fail(message or "%r is cfretained"%(method,))

    def failUnlessResultIsCFRetained(self, method, message = None):
        info = method.__metadata__()
        if not info['retval']['already_cfretained']:
            self.fail(message or "%r is not cfretained"%(method,))

    def failIfResultIsCFRetained(self, method, message = None):
        info = method.__metadata__()
        if info['retval']['already_cfretained']:
            self.fail(message or "%r is cfretained"%(method,))

    def failUnlessResultIsRetained(self, method, message = None):
        info = method.__metadata__()
        if not info['retval']['already_retained']:
            self.fail(message or "%r is not retained"%(method,))

    def failIfResultIsRetained(self, method, message = None):
        info = method.__metadata__()
        if info['retval']['already_retained']:
            self.fail(message or "%r is retained"%(method,))

    def failUnlessResultHasType(self, method, tp, message=None):
        info = method.__metadata__()
        type = info['retval']['type']
        if type != tp:
            self.fail(message or "result of %r is not of type %r, but %r"%(
                method, tp, type))
        
    def failUnlessArgHasType(self, method, argno, tp, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != tp:
            self.fail(message or "arg %d of %s is not of type %r, but %r"%(
                argno, method, tp, type))

    def failUnlessArgIsFunction(self, method, argno, sel_type, retained, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != '^?':
            self.fail(message or "arg %d of %s is not of type function_pointer"%(
                argno, method))

        st = info['arguments'][argno+offset].get('callable')
        if st is None:
            self.fail(message or "arg %d of %s is not of type function_pointer"%(
                argno, method))

        iface = st['retval']['type']
        for a in st['arguments']:
            iface += a['type']

        if iface != sel_type:
            self.fail(message or "arg %d of %s is not a function_pointer with type %r, but %r"%(argno, method, sel_type, iface))


        st = info['arguments'][argno+offset]['callable_retained']
        if bool(st) != bool(retained):
            self.fail(message or "arg %d of %s; retained: %r, expected: %r"%(
                argno, method, st, retained))


    def failUnlessArgIsSEL(self, method, argno, sel_type, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != objc._C_SEL:
            self.fail(message or "arg %d of %s is not of type SEL"%(
                argno, method))

        st = info['arguments'][argno+offset].get('sel_of_type')
        if st != sel_type:
            self.fail(message or "arg %d of %s doesn't have sel_type %r but %r"%(
                argno, method, sel_type, st))

    def failUnlessResultIsBOOL(self, method, message=None):
        info = method.__metadata__()
        type = info['retval']['type']
        if type != objc._C_NSBOOL:
            self.fail(message or "result of %s is not of type BOOL"%(
                method))

    def failUnlessArgIsBOOL(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if type != objc._C_NSBOOL:
            self.fail(message or "arg %d of %s is not of type BOOL"%(
                argno, method))

    def failUnlessArgIsFixedSize(self, method, argno, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info['arguments'][argno+offset]['c_array_of_fixed_length']
        if cnt != count:
            self.fail(message or "arg %d of %s is not a C-array of length %d"%(
                argno, method, count))

    def failUnlessArgSizeInArg(self, method, argno, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info['arguments'][argno+offset]['c_array_length_in_arg']
        if isinstance(count, (list, tuple)):
            count2 = tuple(x + offset for x in count)
        else:
            count2 = count + offset
        if cnt != count2:
            self.fail(message or "arg %d of %s is not a C-array of with length in arg %d"%(
                argno, method, count))

    def failUnlessResultSizeInArg(self, method, count, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        cnt = info['retval']['c_array_length_in_arg']
        if cnt != count + offset:
            self.fail(message or "result %s is not a C-array of with length in arg %d"%(
                argno, method, count))


    def failUnlessArgIsOut(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if not type.startswith('o^'):
            self.fail(message or "arg %d of %s is not an 'out' argument"%(
                argno, method))

    def failUnlessArgIsInOut(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if not type.startswith('N^'):
            self.fail(message or "arg %d of %s is not an 'inout' argument"%(
                argno, method))

    def failUnlessArgIsIn(self, method, argno, message=None):
        if isinstance(method, objc.selector):
            offset = 2
        else:
            offset = 0
        info = method.__metadata__()
        type = info['arguments'][argno+offset]['type']
        if not type.startswith('n^'):
            self.fail(message or "arg %d of %s is not an 'in' argument"%(
                argno, method))


    def failUnlessStartswith(self, value, check, message=None):
        if not value.startswith(check):
            self.fail(message or "not %r.startswith(%r)"%(value, check))

    def failUnlessIsInstance(self, value, types, message=None):
        if not isinstance(value, types):
            self.fail(message or "%s is not an instance of %r"%(value, types))

    def failIfIsInstance(self, value, types, message=None):
        if isinstance(value, types):
            self.fail(message or "%s is an instance of %r"%(value, types))

    assertIsInstance = failUnlessIsInstance

    if not hasattr(_unittest.TestCase, "assertAlmostEquals"):
        def assertAlmostEquals(self, val1, val2, message=None):
            self.failUnless(abs (val1 - val2) < 0.00001, message)



    def run(self, *args):
        if _useleaks:
            leaksBefore = _leaks()
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
            
            if _useleaks:
                leaksAfter = _leaks()
                if len(leaksBefore) != len(leaksAfter):
                    print "\ntest %s is leaking [%d lines]"%(self, len(leaksAfter) - len(leaksBefore))
                    if _leaksVerbose:
                        # XXX: add a smartish filter the surpresses the leaks
                        # in leaksBefore.
                        for ln in leaksAfter:
                            print ln

main = _unittest.main

if hasattr(_unittest, 'expectedFailure'):
    expectedFailure = _unittest.expectedFailure
else:
    def expectedFailure(func):
        def test(self):
            try:
                func(self)
            
            except AssertionError:
                return

            self.fail("test unexpectedly passed")
        test.__name__ == func.__name__

        return test

