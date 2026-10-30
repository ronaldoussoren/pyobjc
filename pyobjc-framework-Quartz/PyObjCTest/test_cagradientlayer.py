from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCAGradientLayer(TestCase):
    def test_typed_enums(self):
        self.assertIsTypedEnum(Quartz.CAGradientLayerType, str)

    def test_constants(self):
        self.assertIsInstance(Quartz.kCAGradientLayerAxial, str)
        self.assertIsInstance(Quartz.kCAGradientLayerRadial, str)

    @min_os_level("10.14")
    def test_constants10_14(self):
        self.assertIsInstance(Quartz.kCAGradientLayerConic, str)

    def test_methods(self):
        self.assertResultHasType(
            Quartz.CAGradientLayer.startPoint, Quartz.CGPoint.__typestr__
        )
        self.assertResultHasType(
            Quartz.CAGradientLayer.endPoint, Quartz.CGPoint.__typestr__
        )

        self.assertArgHasType(
            Quartz.CAGradientLayer.setStartPoint_, 0, Quartz.CGPoint.__typestr__
        )
        self.assertArgHasType(
            Quartz.CAGradientLayer.setEndPoint_, 0, Quartz.CGPoint.__typestr__
        )
