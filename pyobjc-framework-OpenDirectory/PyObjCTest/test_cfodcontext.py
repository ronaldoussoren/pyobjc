from PyObjCTools.TestSupport import *
import CFOpenDirectory

try:
    long
except NameError:
    long = int

class TestCFODContext (TestCase):
    def testMethods(self):
        self.assertIsInstance(CFOpenDirectory.ODContextGetTypeID(), (int, long))

if __name__ == "__main__":
    main()
