import AVFoundation
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level


class TestAVAssetReaderOutput(TestCase):
    @min_sdk_level("12.0")
    def test_protocols12_0(self):
        self.assertProtocolExists(
            "AVAssetReaderCaptionValidationHandling", AVFoundation
        )

    def test_methods(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetReaderOutput.alwaysCopiesSampleData)
        self.assertArgIsBOOL(
            AVFoundation.AVAssetReaderOutput.setAlwaysCopiesSampleData_, 0
        )

    @min_os_level("10.10")
    def test_methods10_10(self):
        self.assertResultIsBOOL(AVFoundation.AVAssetReaderOutput.supportsRandomAccess)
        self.assertArgIsBOOL(
            AVFoundation.AVAssetReaderOutput.setSupportsRandomAccess_, 0
        )
