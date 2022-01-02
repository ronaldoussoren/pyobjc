"""
XXX: Move at least part of the NSCoder tests from
pyobjc-framework-Cocoa to here.
"""
import objc
from PyObjCTools.TestSupport import TestCase


class TestNSCoder(TestCase):
    def test_encodeValuesOfObjCTypes_unsupported(self):

        coder = (
            objc.lookUpClass("NSKeyedArchiver")
            .alloc()
            .initRequiringSecureCoding_(False)
        )
        with self.assertRaisesRegex(
            TypeError, r"Cannot call 'encodeValuesOfObjCTypes:' on '<.*>' from Python"
        ):
            coder.encodeValuesOfObjCTypes_("ii", 1, 2)
        coder.finishEncoding()
