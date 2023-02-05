import dispatch
from PyObjCTools.TestSupport import TestCase


class TestBase(TestCase):
    def test_constants(self):
        self.assertFalse(hasattr(dispatch, "DISPATCH_SWIFT3_OVERLAY"))
