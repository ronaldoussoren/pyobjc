import ImageCaptureCore
from PyObjCTools.TestSupport import TestCase


class TestICScannerDevice(TestCase):
    def test_constants(self):
        self.assertIsInstance(ImageCaptureCore.ICScannerStatusWarmingUp, str)
        self.assertIsInstance(ImageCaptureCore.ICScannerStatusWarmUpDone, str)
        self.assertIsInstance(ImageCaptureCore.ICScannerStatusRequestsOverviewScan, str)

        self.assertEqual(ImageCaptureCore.ICScannerTransferModeFileBased, 0)
        self.assertEqual(ImageCaptureCore.ICScannerTransferModeMemoryBased, 1)

    def test_protocols(self):
        self.assertProtocolExists("ICScannerDeviceDelegate", ImageCaptureCore)
