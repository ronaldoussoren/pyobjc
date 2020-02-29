import CFOpenDirectory
from PyObjCTools.TestSupport import *


class TestCFODContext(TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODContextGetTypeID(), (int, long))


if __name__ == "__main__":
    main()
