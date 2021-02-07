from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAValueFunction(TestCase):
    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(Quartz.kCAValueFunctionRotateX, str)
        self.assertIsInstance(Quartz.kCAValueFunctionRotateY, str)
        self.assertIsInstance(Quartz.kCAValueFunctionRotateZ, str)
        self.assertIsInstance(Quartz.kCAValueFunctionScale, str)
        self.assertIsInstance(Quartz.kCAValueFunctionScaleX, str)
        self.assertIsInstance(Quartz.kCAValueFunctionScaleY, str)
        self.assertIsInstance(Quartz.kCAValueFunctionScaleZ, str)
        self.assertIsInstance(Quartz.kCAValueFunctionTranslate, str)
        self.assertIsInstance(Quartz.kCAValueFunctionTranslateX, str)
        self.assertIsInstance(Quartz.kCAValueFunctionTranslateY, str)
        self.assertIsInstance(Quartz.kCAValueFunctionTranslateZ, str)
