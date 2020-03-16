from PyObjCTools.TestSupport import TestCase
import XgridFoundation


class TestXGActionMonitor(TestCase):
    def testConstants(self):
        self.assertEqual(XgridFoundation.XGResourceActionNone, 0)
        self.assertEqual(XgridFoundation.XGResourceActionStop, 1)
        self.assertEqual(XgridFoundation.XGResourceActionRestart, 2)
        self.assertEqual(XgridFoundation.XGResourceActionSuspend, 3)
        self.assertEqual(XgridFoundation.XGResourceActionResume, 4)
        self.assertEqual(XgridFoundation.XGResourceActionDelete, 5)
        self.assertEqual(XgridFoundation.XGResourceActionRename, 6)
        self.assertEqual(XgridFoundation.XGResourceActionMakeDefault, 7)
        self.assertEqual(XgridFoundation.XGResourceActionSubmitJob, 8)
        self.assertEqual(XgridFoundation.XGResourceActionGetOutputStreams, 9)
        self.assertEqual(XgridFoundation.XGResourceActionGetOutputFiles, 10)
        self.assertEqual(XgridFoundation.XGResourceActionGetSpecification, 11)

        self.assertEqual(XgridFoundation.XGActionMonitorOutcomeNone, 0)
        self.assertEqual(XgridFoundation.XGActionMonitorOutcomeSuccess, 1)
        self.assertEqual(XgridFoundation.XGActionMonitorOutcomeFailure, 2)

        self.assertIsInstance(XgridFoundation.XGActionMonitorResultsOutputStreamsKey, str)
        self.assertIsInstance(XgridFoundation.XGActionMonitorResultsOutputFilesKey, str)

    def testMethods(self):
        self.assertResultIsBOOL(XgridFoundation.XGActionMonitor.actionDidSucceed)
        self.assertResultIsBOOL(XgridFoundation.XGActionMonitor.actionDidFail)
