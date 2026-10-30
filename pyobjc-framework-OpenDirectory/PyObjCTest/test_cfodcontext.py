import CFOpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestCFODContext(TestCase):
    def test_methods(self):
        self.assertIsInstance(CFOpenDirectory.ODContextGetTypeID(), int)
