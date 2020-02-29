from ImageCaptureCore import *
from PyObjCTools.TestSupport import *


class TestICScannerDevice(TestCase):
    def testConstants(self):
        self.assertIsInstance(ICScannerStatusWarmingUp, unicode)
        self.assertIsInstance(ICScannerStatusWarmUpDone, unicode)
        self.assertIsInstance(ICScannerStatusRequestsOverviewScan, unicode)

        self.assertEqual(ICScannerTransferModeFileBased, 0)
        self.assertEqual(ICScannerTransferModeMemoryBased, 1)

    def testProtocolObjects(self):
        objc.protocolNamed("ICScannerDeviceDelegate")


if __name__ == "__main__":
    main()
