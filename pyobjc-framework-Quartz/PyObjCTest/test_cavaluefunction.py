from PyObjCTools.TestSupport import TestCase
import Quartz


class TestCAValueFunction(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(Quartz.CAValueFunctionName, str)

    def test_constants(self):
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
