from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCATextLayer(TestCase):
    def test_typed_enum(self):
        self.assertIsTypedEnum(Quartz.CATextLayerAlignmentMode, str)
        self.assertIsTypedEnum(Quartz.CATextLayerTruncationMode, str)

    @min_os_level("10.5")
    def test_constants(self):
        self.assertIsInstance(Quartz.kCATruncationNone, str)
        self.assertIsInstance(Quartz.kCATruncationStart, str)
        self.assertIsInstance(Quartz.kCATruncationEnd, str)
        self.assertIsInstance(Quartz.kCATruncationMiddle, str)
        self.assertIsInstance(Quartz.kCAAlignmentNatural, str)
        self.assertIsInstance(Quartz.kCAAlignmentLeft, str)
        self.assertIsInstance(Quartz.kCAAlignmentRight, str)
        self.assertIsInstance(Quartz.kCAAlignmentCenter, str)
        self.assertIsInstance(Quartz.kCAAlignmentJustified, str)

    @min_os_level("10.5")
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CATextLayer.isWrapped)
        self.assertArgIsBOOL(Quartz.CATextLayer.setWrapped_, 0)

    @min_os_level("10.11")
    def test_methods10_11(self):
        self.assertResultIsBOOL(Quartz.CATextLayer.allowsFontSubpixelQuantization)
        self.assertArgIsBOOL(Quartz.CATextLayer.setAllowsFontSubpixelQuantization_, 0)
