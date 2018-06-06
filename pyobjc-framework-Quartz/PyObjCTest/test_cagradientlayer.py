from Quartz import *
from PyObjCTools.TestSupport import *

class TestCAGradientLayer (TestCase):
    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertResultHasType(CAGradientLayer.startPoint, CGPoint.__typestr__)
        self.assertResultHasType(CAGradientLayer.endPoint, CGPoint.__typestr__)

        self.assertArgHasType(CAGradientLayer.setStartPoint_, 0, CGPoint.__typestr__)
        self.assertArgHasType(CAGradientLayer.setEndPoint_, 0, CGPoint.__typestr__)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCAGradientLayerAxial, unicode)
        self.assertIsInstance(kCAGradientLayerRadial, unicode)

    @min_os_level('10.14')
    def testConstants10_14(self):
        self.assertIsInstance(kCAGradientLayerConic, unicode)

if __name__ == "__main__":
    main()
