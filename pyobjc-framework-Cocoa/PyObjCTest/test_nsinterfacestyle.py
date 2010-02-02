
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSInterfaceStyle (TestCase):
    def testConstants(self):
        self.assertEqual(NSNoInterfaceStyle, 0)
        self.assertEqual(NSNextStepInterfaceStyle, 1)
        self.assertEqual(NSWindows95InterfaceStyle, 2)
        self.assertEqual(NSMacintoshInterfaceStyle, 3)

        self.assertIsInstance(NSInterfaceStyleDefault, unicode)

    def testFunctions(self):
        v = NSInterfaceStyleForKey("button", None)
        self.assertIsInstance(v, (int, long))


if __name__ == "__main__":
    main()
