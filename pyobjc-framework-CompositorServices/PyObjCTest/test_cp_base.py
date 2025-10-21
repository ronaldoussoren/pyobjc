from PyObjCTools.TestSupport import TestCase

import CompositorServices


class TestCPBase(TestCase):
    def test_functions(self):
        self.assertNotHasAttr(CompositorServices, "cp_retain")
        self.assertNotHasAttr(CompositorServices, "cp_release")
