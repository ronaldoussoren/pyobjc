from PyObjCTools.TestSupport import (
    TestCase,
    min_os_level,
    os_release,
    os_level_key,
    expectedFailureIf,
)
import QTKit


class TestQTError(TestCase):
    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(QTKit.QTKitErrorDomain, str)
        self.assertIsInstance(QTKit.QTErrorCaptureInputKey, str)
        self.assertIsInstance(QTKit.QTErrorCaptureOutputKey, str)
        self.assertIsInstance(QTKit.QTErrorDeviceKey, str)
        self.assertIsInstance(QTKit.QTErrorExcludingDeviceKey, str)
        self.assertIsInstance(QTKit.QTErrorRecordingSuccesfullyFinishedKey, str)

        self.assertEqual(QTKit.QTErrorUnknown, -1)
        self.assertEqual(QTKit.QTErrorIncompatibleInput, 1002)
        self.assertEqual(QTKit.QTErrorIncompatibleOutput, 1003)
        self.assertEqual(QTKit.QTErrorInvalidInputsOrOutputs, 1100)
        self.assertEqual(QTKit.QTErrorDeviceAlreadyUsedbyAnotherSession, 1101)
        self.assertEqual(QTKit.QTErrorNoDataCaptured, 1200)
        self.assertEqual(QTKit.QTErrorSessionConfigurationChanged, 1201)
        self.assertEqual(QTKit.QTErrorDiskFull, 1202)
        self.assertEqual(QTKit.QTErrorDeviceWasDisconnected, 1203)
        self.assertEqual(QTKit.QTErrorMediaChanged, 1204)
        self.assertEqual(QTKit.QTErrorMaximumDurationReached, 1205)
        self.assertEqual(QTKit.QTErrorMaximumFileSizeReached, 1206)
        self.assertEqual(QTKit.QTErrorMediaDiscontinuity, 1207)
        self.assertEqual(QTKit.QTErrorMaximumNumberOfSamplesForFileFormatReached, 1208)
        self.assertEqual(QTKit.QTErrorDeviceNotConnected, 1300)
        self.assertEqual(QTKit.QTErrorDeviceInUseByAnotherApplication, 1301)
        self.assertEqual(QTKit.QTErrorDeviceExcludedByAnotherDevice, 1302)
        self.assertEqual(QTKit.QTErrorInvalidDestinationFileTypeForExport, 1501)
        self.assertEqual(QTKit.QTErrorInvalidSourceFileTypeForExport, 1502)
        self.assertEqual(QTKit.QTErrorExportExecutionFailed, 1503)
        self.assertEqual(QTKit.QTErrorExportInsufficientSpaceOnDevice, 1504)
        self.assertEqual(QTKit.QTErrorExportNoSuchDirectoryOrFile, 1505)
        self.assertEqual(QTKit.QTErrorExportIOError, 1506)

    @min_os_level("10.6")
    def testConstants10_6(self):
        self.assertIsInstance(QTKit.QTErrorTimeKey, str)
        self.assertIsInstance(QTKit.QTErrorFileSizeKey, str)

    @expectedFailureIf(os_level_key(os_release()) >= os_level_key("10.6"))
    @min_os_level("10.6")
    def testConstants10_6_fail(self):
        try:
            self.assertIsInstance(QTKit.QTErrorRecordingSuccessfullyFinishedKey, str)
        except NameError:
            self.fail("QTErrorRecordingSuccessfullyFinishedKey not defined")
