import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestICScannerBandData(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(ImageCaptureCore.ICScannerBandData.isBigEndian)
