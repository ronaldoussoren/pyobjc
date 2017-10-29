
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTError (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertIsInstance(QTKitErrorDomain, unicode)
        self.assertIsInstance(QTErrorCaptureInputKey, unicode)
        self.assertIsInstance(QTErrorCaptureOutputKey, unicode)
        self.assertIsInstance(QTErrorDeviceKey, unicode)
        self.assertIsInstance(QTErrorExcludingDeviceKey, unicode)
        self.assertIsInstance(QTErrorRecordingSuccesfullyFinishedKey, unicode)

        self.assertEqual(QTErrorUnknown, -1)
        self.assertEqual(QTErrorIncompatibleInput, 1002)
        self.assertEqual(QTErrorIncompatibleOutput, 1003)
        self.assertEqual(QTErrorInvalidInputsOrOutputs, 1100)
        self.assertEqual(QTErrorDeviceAlreadyUsedbyAnotherSession, 1101)
        self.assertEqual(QTErrorNoDataCaptured, 1200)
        self.assertEqual(QTErrorSessionConfigurationChanged, 1201)
        self.assertEqual(QTErrorDiskFull, 1202)
        self.assertEqual(QTErrorDeviceWasDisconnected, 1203)
        self.assertEqual(QTErrorMediaChanged, 1204)
        self.assertEqual(QTErrorMaximumDurationReached, 1205)
        self.assertEqual(QTErrorMaximumFileSizeReached, 1206)
        self.assertEqual(QTErrorMediaDiscontinuity, 1207)
        self.assertEqual(QTErrorMaximumNumberOfSamplesForFileFormatReached, 1208)
        self.assertEqual(QTErrorDeviceNotConnected, 1300)
        self.assertEqual(QTErrorDeviceInUseByAnotherApplication, 1301)
        self.assertEqual(QTErrorDeviceExcludedByAnotherDevice, 1302)
        self.assertEqual(QTErrorInvalidDestinationFileTypeForExport, 1501)
        self.assertEqual(QTErrorInvalidSourceFileTypeForExport, 1502)
        self.assertEqual(QTErrorExportExecutionFailed, 1503)
        self.assertEqual(QTErrorExportInsufficientSpaceOnDevice, 1504)
        self.assertEqual(QTErrorExportNoSuchDirectoryOrFile, 1505)
        self.assertEqual(QTErrorExportIOError, 1506)

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(QTErrorTimeKey, unicode)
        self.assertIsInstance(QTErrorFileSizeKey, unicode)

    @expectedFailureIf(os_level_key(os_release()) >= os_level_key('10.6'))
    @min_os_level('10.6')
    def testConstants10_6_fail(self):
        try:
            self.assertIsInstance(QTErrorRecordingSuccessfullyFinishedKey, unicode)
        except NameError:
            self.fail("QTErrorRecordingSuccessfullyFinishedKey not defined")

if __name__ == "__main__":
    main()
