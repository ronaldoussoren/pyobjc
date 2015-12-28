from PyObjCTools.TestSupport import *
from QTKit import *

class TestQTExportSessionHelper (NSObject):
    def exportSession_didReachProgess_(self, e, p): pass

class TestQTExportSession (TestCase):
    @min_os_level('10.7')
    def testMethods(self):
        self.assertResultIsBOOL(QTExportSession.isRunning)
        self.assertResultIsBOOL(QTExportSession.isFinished)
        self.assertResultIsBOOL(QTExportSession.isCancelled)

        self.assertArgIsOut(QTExportSession.initWithMovie_exportOptions_outputURL_error_, 3)

        self.assertResultIsBOOL(QTExportSession.waitUntilFinished_)
        self.assertArgIsOut(QTExportSession.waitUntilFinished_, 0)

    @min_os_level('10.7')
    def testProtocols(self):
        objc.protocolNamed('QTExportSessionDelegate')

        self.assertArgHasType(TestQTExportSessionHelper.exportSession_didReachProgess_, 1, objc._C_DBL)


if __name__ == "__main__":
    main()
