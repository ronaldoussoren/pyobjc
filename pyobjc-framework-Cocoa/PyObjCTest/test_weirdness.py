# This is not a real test, but more documentation of a strange feature of
# the Cocoa runtime.
#
# A number of classes in Cocoa grow new methods if you instantiate them. We
# work around this feature by rescanning the method table after calling a
# class-method.
#
# We need to do this to reliably detect calls to the superclass implementation
# of a method. Without the workaround, calls to NSButtonCell.isEnabled_ (one
# of the magical classes) would be interpreted as calls to
# NSActionCell.isEnabled_, which is wrong.
#

from PyObjCTools.TestSupport import (
    TestCase,
    max_sdk_level,
    os_release,
    os_level_key,
    skipUnless,
)
import objc

import AppKit  # noqa: F401


class TestWeirdness(TestCase):
    def doWeirdness(self, className, methodToTest):
        c = objc.lookUpClass(className)
        before = getattr(c, methodToTest)  # noqa: F841
        b = c.alloc().init()  # noqa: F841
        after = getattr(c, methodToTest)

        self.assertEqual(after.definingClass, c)

    @skipUnless(
        not (
            os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.14")
        ),
        "crash on 10.13",
    )
    @max_sdk_level("10.14")
    def testWeirdness1(self):
        self.doWeirdness("NSButtonCell", "setEnabled_")

    @skipUnless(
        not (
            os_level_key("10.13") <= os_level_key(os_release()) < os_level_key("10.14")
        ),
        "crash on 10.13",
    )
    @max_sdk_level("10.14")
    @max_sdk_level("10.14")
    def testWeirdness2(self):
        self.doWeirdness("NSTextView", "setEditable_")
