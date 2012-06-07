from Quartz import *
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

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

if __name__ == "__main__":
    main()
