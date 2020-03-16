import libdispatch
from PyObjCTools.TestSupport import TestCase


class TestBase(TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(libdispatch, "DISPATCH_SWIFT3_OVERLAY"))
