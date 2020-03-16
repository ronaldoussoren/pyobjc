import libdispatch
from PyObjCTools.TestSupport import TestCase


class TestDispatch(TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(libdispatch, "DISPATCH_API_VERSION"))
