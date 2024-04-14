"""
This is the runner for the tests defined in Modules/objc/unittest.m. Those tests
check a number lowlevel features of the bridge.

This file provides a nice unittest wrapper around the functions in that file,
the code in this file defines a class CTests that has the functions in the
unitest.m file as its methods.
"""

import platform
import sys
import warnings
import objc
from PyObjCTools.TestSupport import TestCase, pyobjc_options

ctests = objc._ctests

names = list(ctests.keys())
methods = {}


def do_exec(value, locals_dict, globals_dict):
    exec(value, locals_dict, globals_dict)


def make_test(name):
    """
    Create a method for use in a unittest, the exec is needed to get the
    proper function name
    """
    result = {"meth": ctests[name]}

    if (
        sys.platform == "darwin"
        and name == "CheckNSInvoke"
        and platform.machine() == "Power Macintosh"
        and tuple(map(int, platform.mac_ver()[0].split("."))) < (10, 5)
    ):
        # There is a bug in Apple's implementation of NSInvocation
        # surpress the test failure until Apple fixes the class.
        # Don't change the C-code, the same function is used to disable
        # parts of the unittests that trigger the bug.
        def test_CheckNSInvoke(self):
            try:
                ctests["CheckNSInvoke"]()
            except AssertionError:
                return

            self.fail("NSInvocation works!")

        return test_CheckNSInvoke

    elif name == "InvalidObjCPointer":

        def test_InvalidObjCPointer(self):
            with warnings.catch_warnings():
                warnings.filterwarnings("ignore", category=objc.ObjCPointerWarning)

                with pyobjc_options(unknown_pointer_raises=False):
                    ctests["InvalidObjCPointer"]()

        return test_InvalidObjCPointer

    do_exec(
        """\
def test_%s(self):
    meth()
"""
        % (name,),
        result,
        result,
    )

    return result[f"test_{name}"]


def test_AlwaysFails(self):
    with self.assertRaisesRegex(AssertionError, r"Modules/objc/ctests.m:\d+ 0 == 1"):
        ctests["AlwaysFails"]()


for n in names:
    if n == "AlwaysFails":
        methods[f"test_{n}"] = test_AlwaysFails
    else:
        methods[f"test_{n}"] = make_test(n)

CTests = type(TestCase)("CTests", (TestCase,), methods)
