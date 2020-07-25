import libdispatch
from PyObjCTools.TestSupport import TestCase


class TestDispatch(TestCase):
    def test_constants(self):
        self.assertNotHasAttr(libdispatch, "DISPATCH_API_VERSION")
