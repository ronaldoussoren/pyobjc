from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestCGEXRToneMappingGamma(TestCase):
    @min_os_level("26.0")
    def test_functions26_0(self):
        Quartz.CGEXRToneMappingGammaGetDefaultOptions

        self.assertResultIsCFRetained(Quartz.CGGradientCreateWithContentHeadroom)
        self.assertArgIsIn(Quartz.CGGradientCreateWithContentHeadroom, 2)
        self.assertArgIsVariableSize(Quartz.CGGradientCreateWithContentHeadroom, 2)
        self.assertArgIsIn(Quartz.CGGradientCreateWithContentHeadroom, 3)
        self.assertArgSizeInArg(Quartz.CGGradientCreateWithContentHeadroom, 3, 4)

        Quartz.CGGradientGetContentHeadroom
