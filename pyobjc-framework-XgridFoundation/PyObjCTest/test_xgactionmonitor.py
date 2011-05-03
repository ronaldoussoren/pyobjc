
from PyObjCTools.TestSupport import *
from XgridFoundation import *

class TestXGActionMonitor (TestCase):
    def testConstants(self):
        self.assertEqual(XGResourceActionNone, 0)
        self.assertEqual(XGResourceActionStop, 1)
        self.assertEqual(XGResourceActionRestart, 2)
        self.assertEqual(XGResourceActionSuspend, 3)
        self.assertEqual(XGResourceActionResume, 4)
        self.assertEqual(XGResourceActionDelete, 5)
        self.assertEqual(XGResourceActionRename, 6)
        self.assertEqual(XGResourceActionMakeDefault, 7)
        self.assertEqual(XGResourceActionSubmitJob, 8)
        self.assertEqual(XGResourceActionGetOutputStreams, 9)
        self.assertEqual(XGResourceActionGetOutputFiles, 10)
        self.assertEqual(XGResourceActionGetSpecification, 11)

        self.assertEqual(XGActionMonitorOutcomeNone, 0)
        self.assertEqual(XGActionMonitorOutcomeSuccess, 1)
        self.assertEqual(XGActionMonitorOutcomeFailure, 2)

        self.assertIsInstance(XGActionMonitorResultsOutputStreamsKey, unicode)
        self.assertIsInstance(XGActionMonitorResultsOutputFilesKey, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(XGActionMonitor.actionDidSucceed)
        self.assertResultIsBOOL(XGActionMonitor.actionDidFail)


if __name__ == "__main__":
    main()
