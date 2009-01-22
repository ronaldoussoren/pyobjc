
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGActionMonitor (TestCase):
    def testConstants(self):
        self.failUnlessEqual(XGResourceActionNone, 0)
        self.failUnlessEqual(XGResourceActionStop, 1)
        self.failUnlessEqual(XGResourceActionRestart, 2)
        self.failUnlessEqual(XGResourceActionSuspend, 3)
        self.failUnlessEqual(XGResourceActionResume, 4)
        self.failUnlessEqual(XGResourceActionDelete, 5)
        self.failUnlessEqual(XGResourceActionRename, 6)
        self.failUnlessEqual(XGResourceActionMakeDefault, 7)
        self.failUnlessEqual(XGResourceActionSubmitJob, 8)
        self.failUnlessEqual(XGResourceActionGetOutputStreams, 9)
        self.failUnlessEqual(XGResourceActionGetOutputFiles, 10)
        self.failUnlessEqual(XGResourceActionGetSpecification, 11)

        self.failUnlessEqual(XGActionMonitorOutcomeNone, 0)
        self.failUnlessEqual(XGActionMonitorOutcomeSuccess, 1)
        self.failUnlessEqual(XGActionMonitorOutcomeFailure, 2)

        self.failUnlessIsInstance(XGActionMonitorResultsOutputStreamsKey, unicode)
        self.failUnlessIsInstance(XGActionMonitorResultsOutputFilesKey, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(XGActionMonitor.actionDidSucceed)
        self.failUnlessResultIsBOOL(XGActionMonitor.actionDidFail)


if __name__ == "__main__":
    main()
