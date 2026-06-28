import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase


class TestICScannerBandData(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICScannerBandData.isBigEndian)
