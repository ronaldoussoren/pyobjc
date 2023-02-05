import dispatch
from PyObjCTools.TestSupport import TestCase


class TestDispatch(TestCase):
    def test_constants(self):
        self.assertNotHasAttr(dispatch, "DISPATCH_API_VERSION")
