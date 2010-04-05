
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
        self.assertEqual(QTErrorDeviceNotConnected, 1300)
        self.assertEqual(QTErrorDeviceInUseByAnotherApplication, 1301)
        self.assertEqual(QTErrorDeviceExcludedByAnotherDevice, 1302)

if __name__ == "__main__":
    main()
