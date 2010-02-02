
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSColorSpace (TestCase):
    def testConstants(self):
        self.assertEqual(NSUnknownColorSpaceModel, -1)
        self.assertEqual(NSGrayColorSpaceModel, 0)
        self.assertEqual(NSRGBColorSpaceModel, 1)
        self.assertEqual(NSCMYKColorSpaceModel, 2)
        self.assertEqual(NSLABColorSpaceModel, 3)
        self.assertEqual(NSDeviceNColorSpaceModel, 4)
        self.assertEqual(NSIndexedColorSpaceModel, 5)
        self.assertEqual(NSPatternColorSpaceModel, 6)



if __name__ == "__main__":
    main()
