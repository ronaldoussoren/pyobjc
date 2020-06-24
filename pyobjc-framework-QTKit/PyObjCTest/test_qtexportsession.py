from PyObjCTools.TestSupport import TestCase, min_os_level
import QTKit
import objc


class TestQTExportSessionHelper(QTKit.NSObject):
    def exportSession_didReachProgess_(self, e, p):
        pass


class TestQTExportSession(TestCase):
    @min_os_level("10.7")
    def testMethods(self):
        self.assertResultIsBOOL(QTKit.QTExportSession.isRunning)
        self.assertResultIsBOOL(QTKit.QTExportSession.isFinished)
        self.assertResultIsBOOL(QTKit.QTExportSession.isCancelled)

        self.assertArgIsOut(
            QTKit.QTExportSession.initWithMovie_exportOptions_outputURL_error_, 3
        )

        self.assertResultIsBOOL(QTKit.QTExportSession.waitUntilFinished_)
        self.assertArgIsOut(QTKit.QTExportSession.waitUntilFinished_, 0)

    @min_os_level("10.7")
    def testProtocols(self):
        objc.protocolNamed("QTExportSessionDelegate")

        self.assertArgHasType(
            TestQTExportSessionHelper.exportSession_didReachProgess_, 1, objc._C_DBL
        )
