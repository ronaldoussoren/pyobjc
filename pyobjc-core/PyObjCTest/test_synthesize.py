"""
Tests for objc.synthesize
"""

import objc
from PyObjCTest.fnd import NSObject
from PyObjCTools.TestSupport import TestCase


class TestSynthesizeCopier(NSObject):
    def copy(self):
        return 42


class TestSynthesizeHelper(NSObject):
    objc.synthesize("someTitle", copy=True)
    objc.synthesize("stringValue", copy=False)
    objc.synthesize("read", readwrite=False)
    objc.synthesize("write", ivarName="_do_write")


class TestSynthesize(TestCase):
    def testNames(self):
        self.assertHasAttr(TestSynthesizeHelper, "someTitle")
        self.assertHasAttr(TestSynthesizeHelper, "setSomeTitle_")

        self.assertHasAttr(TestSynthesizeHelper, "stringValue")
        self.assertHasAttr(TestSynthesizeHelper, "setStringValue_")

        self.assertHasAttr(TestSynthesizeHelper, "read")
        self.assertNotHasAttr(TestSynthesizeHelper, "setRead_")

        self.assertHasAttr(TestSynthesizeHelper, "write")
        self.assertHasAttr(TestSynthesizeHelper, "setWrite_")

    def testAttributes(self):
        o = TestSynthesizeHelper.alloc().init()
        o.setWrite_("42")
        self.assertEqual(o._do_write, "42")
        self.assertEqual(o.write(), "42")

        o.setStringValue_("hello")
        self.assertEqual(o._stringValue, "hello")
        self.assertEqual(o.stringValue(), "hello")

        o._read = 1
        self.assertEqual(o.read(), 1)
        o._read = 2
        self.assertEqual(o.read(), 2)

    def testCopying(self):
        obj = TestSynthesizeHelper.alloc().init()

        v = TestSynthesizeCopier.alloc().init()

        obj.setStringValue_(v)
        self.assertIs(obj.stringValue(), v)

        obj.setSomeTitle_(v)
        self.assertEqual(obj.someTitle(), 42)

    def testFailures(self):
        with self.assertRaisesRegex(ValueError, "Empty property name"):
            objc.synthesize("")

        # The message is suboptimal, but good enough.
        with self.assertRaisesRegex(ValueError, "Empty property name"):
            objc.synthesize(None)
