import CFOpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestCFODContext(TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODContextGetTypeID(), int)
