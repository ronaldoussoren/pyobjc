from PyObjCTools.TestSupport import TestCase

import Network


class TestNWObject(TestCase):
    def test_functions(self):
        self.assertFalse(hasattr(Network, "nw_retain"))
        self.assertFalse(hasattr(Network, "nw_release"))
