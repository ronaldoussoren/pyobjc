
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSInterfaceStyle (TestCase):
    def testConstants(self):
        self.failUnlessEqual(NSNoInterfaceStyle, 0)
        self.failUnlessEqual(NSNextStepInterfaceStyle, 1)
        self.failUnlessEqual(NSWindows95InterfaceStyle, 2)
        self.failUnlessEqual(NSMacintoshInterfaceStyle, 3)

        self.failUnlessIsInstance(NSInterfaceStyleDefault, unicode)

    def testFunctions(self):
        v = NSInterfaceStyleForKey("button", None)
        self.failUnlessIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
