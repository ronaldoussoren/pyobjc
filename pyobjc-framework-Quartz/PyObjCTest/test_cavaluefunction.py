from Quartz import *
from PyObjCTools.TestSupport import *


class TestCAValueFunction (TestCase):
    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(kCAValueFunctionRotateX, unicode)
        self.assertIsInstance(kCAValueFunctionRotateY, unicode)
        self.assertIsInstance(kCAValueFunctionRotateZ, unicode)
        self.assertIsInstance(kCAValueFunctionScale, unicode)
        self.assertIsInstance(kCAValueFunctionScaleX, unicode)
        self.assertIsInstance(kCAValueFunctionScaleY, unicode)
        self.assertIsInstance(kCAValueFunctionScaleZ, unicode)
        self.assertIsInstance(kCAValueFunctionTranslate, unicode)
        self.assertIsInstance(kCAValueFunctionTranslateX, unicode)
        self.assertIsInstance(kCAValueFunctionTranslateY, unicode)
        self.assertIsInstance(kCAValueFunctionTranslateZ, unicode)

if __name__ == "__main__":
    main()
