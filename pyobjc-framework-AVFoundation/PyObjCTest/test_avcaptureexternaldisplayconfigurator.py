import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAVCaptureExternalDisplayConfigurator(TestCase):
    @min_os_level("26.0")
    def test_methods(self):
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureExternalDisplayConfiguration.bypassColorSpaceConversion
        )
        self.assertArgIsBOOL(
            AVFoundation.AVCaptureExternalDisplayConfiguration.setBypassColorSpaceConversion_,
            0,
        )

        self.assertResultIsBOOL(
            AVFoundation.AVCaptureExternalDisplayConfigurator.isActive
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureExternalDisplayConfigurator.isMatchingFrameRateSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureExternalDisplayConfigurator.isBypassingColorSpaceConversionSupported
        )
        self.assertResultIsBOOL(
            AVFoundation.AVCaptureExternalDisplayConfigurator.isPreferredResolutionSupported
        )
