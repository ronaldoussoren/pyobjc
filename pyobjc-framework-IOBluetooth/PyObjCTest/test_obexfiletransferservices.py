from PyObjCTools.TestSupport import TestCase

import IOBluetooth


class TestOBEXFileTransferServices(TestCase):
    def test_constants(self):
        self.assertIsInstance(IOBluetooth.kFTSProgressBytesTransferredKey, str)
        self.assertIsInstance(IOBluetooth.kFTSProgressBytesTotalKey, str)
        self.assertIsInstance(IOBluetooth.kFTSProgressPercentageKey, str)
        self.assertIsInstance(IOBluetooth.kFTSProgressPrecentageKey, str)
        self.assertIsInstance(IOBluetooth.kFTSProgressEstimatedTimeKey, str)
        self.assertIsInstance(IOBluetooth.kFTSProgressTimeElapsedKey, str)
        self.assertIsInstance(IOBluetooth.kFTSProgressTransferRateKey, str)
        self.assertIsInstance(IOBluetooth.kFTSListingNameKey, str)
        self.assertIsInstance(IOBluetooth.kFTSListingTypeKey, str)
        self.assertIsInstance(IOBluetooth.kFTSListingSizeKey, str)

        self.assertIsEnumType(IOBluetooth.FTSFileType)
        self.assertEqual(IOBluetooth.kFTSFileTypeFolder, 1)
        self.assertEqual(IOBluetooth.kFTSFileTypeFile, 2)

    def test_methods(self):
        self.assertResultIsBOOL(IOBluetooth.OBEXFileTransferServices.isBusy)
        self.assertResultIsBOOL(IOBluetooth.OBEXFileTransferServices.isConnected)
