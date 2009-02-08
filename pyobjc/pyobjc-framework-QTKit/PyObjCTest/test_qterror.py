
from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTError (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.failUnlessIsInstance(QTKitErrorDomain, unicode)
        self.failUnlessIsInstance(QTErrorCaptureInputKey, unicode)
        self.failUnlessIsInstance(QTErrorCaptureOutputKey, unicode)
        self.failUnlessIsInstance(QTErrorDeviceKey, unicode)
        self.failUnlessIsInstance(QTErrorExcludingDeviceKey, unicode)
        self.failUnlessIsInstance(QTErrorRecordingSuccesfullyFinishedKey, unicode)

        self.failUnlessEqual(QTErrorUnknown, -1)
        self.failUnlessEqual(QTErrorIncompatibleInput, 1002)
        self.failUnlessEqual(QTErrorIncompatibleOutput, 1003)
        self.failUnlessEqual(QTErrorInvalidInputsOrOutputs, 1100)
        self.failUnlessEqual(QTErrorDeviceAlreadyUsedbyAnotherSession, 1101)
        self.failUnlessEqual(QTErrorNoDataCaptured, 1200)
        self.failUnlessEqual(QTErrorSessionConfigurationChanged, 1201)
        self.failUnlessEqual(QTErrorDiskFull, 1202)
        self.failUnlessEqual(QTErrorDeviceWasDisconnected, 1203)
        self.failUnlessEqual(QTErrorMediaChanged, 1204)
        self.failUnlessEqual(QTErrorMaximumDurationReached, 1205)
        self.failUnlessEqual(QTErrorMaximumFileSizeReached, 1206)
        self.failUnlessEqual(QTErrorMediaDiscontinuity, 1207)
        self.failUnlessEqual(QTErrorDeviceNotConnected, 1300)
        self.failUnlessEqual(QTErrorDeviceInUseByAnotherApplication, 1301)
        self.failUnlessEqual(QTErrorDeviceExcludedByAnotherDevice, 1302)

if __name__ == "__main__":
    main()
