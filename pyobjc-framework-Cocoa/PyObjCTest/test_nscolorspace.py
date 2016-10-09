
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

        self.assertEqual(NSColorSpaceModelUnknown, -1)
        self.assertEqual(NSColorSpaceModelGray, 0)
        self.assertEqual(NSColorSpaceModelRGB, 1)
        self.assertEqual(NSColorSpaceModelCMYK, 2)
        self.assertEqual(NSColorSpaceModelLAB, 3)
        self.assertEqual(NSColorSpaceModelDeviceN, 4)
        self.assertEqual(NSColorSpaceModelIndexed, 5)
        self.assertEqual(NSColorSpaceModelPatterned, 6)


    def testMethods(self):
        self.assertArgHasType(NSColorSpace.initWithColorSyncProfile_, 0, b"^{OpaqueCMProfileRef=}")
        self.assertResultHasType(NSColorSpace.colorSyncProfile, b"^{OpaqueCMProfileRef=}")

if __name__ == "__main__":
    main()
