
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncSessionDriverHelper (NSObject):
    def sessionDriver_didNegotiateAndReturnError_(self, d, e): return 1
    def sessionDriver_willNegotiateAndReturnError_(self, d, e): return 1
    def sessionDriver_didReceiveSyncAlertAndReturnError_(self, d, e): return 1

    def recordsForEntityName_moreComing_error_(self, e, m, o):
        return (None, True, None)
    def applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_(self, c, e, i, r, err):
        return (0, None, None, None)

    def sessionPullChangesTimeout(self):
        return 1.0

    def changedRecordsForEntityName_moreComing_error_(self, n, m, e):
        return (None, False, None)

    def changesForEntityName_moreComing_error_(self, n, m, e):
        return (None, False, None)

    def identifiersForRecordsToDeleteForEntityName_moreComing_error_(self, n, m, e):
        return (None, False, None)

    def sessionDriver_didRegisterClientAndReturnError_(self, d, e):
        return (True, None)
    def sessionDriver_willPushAndReturnError_(self, d, e):
        return (True, None)
    def sessionDriver_didPushAndReturnError_(self, d, e):
        return (True, None)
    def sessionDriver_willPullAndReturnError_(self, d, e):
        return (True, None)
    def sessionDriver_didPullAndReturnError_(self, d, e):
        return (True, None)
    def sessionDriver_willFinishSessionAndReturnError_(self, d, e):
        return (True, None)

    def deleteAllRecordsForEntityName_error_(self, nm, e):
        return (True, None)
                      

class TestISyncSessionDriver (TestCase):
    @min_os_level('10.5')
    def testConstants(self):
        self.assertEqual(ISyncSessionDriverModeFast, 1)
        self.assertEqual(ISyncSessionDriverModeSlow, 2)
        self.assertEqual(ISyncSessionDriverModeRefresh, 3)

        self.assertEqual(ISyncSessionDriverChangeRefused, 0)
        self.assertEqual(ISyncSessionDriverChangeAccepted, 1)
        self.assertEqual(ISyncSessionDriverChangeIgnored, 2)
        self.assertEqual(ISyncSessionDriverChangeError, 3)

    @min_os_level('10.5')
    def testMethods(self):
        self.assertResultIsBOOL(ISyncSessionDriver.sync)
        self.assertResultIsBOOL(ISyncSessionDriver.startAsynchronousSync_)
        self.assertArgIsOut(ISyncSessionDriver.startAsynchronousSync_, 0)
        self.assertResultIsBOOL(ISyncSessionDriver.handlesSyncAlerts)


    @min_os_level('10.5')
    def testProtocols(self):
        self.assertIsInstance(protocols.ISyncSessionDriverDataSourceOptionalMethods, objc.informal_protocol)
        self.assertArgHasType(TestISyncSessionDriverHelper.recordsForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.assertArgHasType(TestISyncSessionDriverHelper.recordsForEntityName_moreComing_error_, 2, objc._C_OUT + objc._C_PTR + objc._C_ID)

        self.assertResultHasType(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, objc._C_INT)
        self.assertArgIsOut(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, 2)
        self.assertArgIsOut(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, 3)
        self.assertArgIsOut(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, 4)

        self.assertResultIsBOOL(TestISyncSessionDriverHelper.deleteAllRecordsForEntityName_error_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.deleteAllRecordsForEntityName_error_, 1)

        self.assertResultHasType(TestISyncSessionDriverHelper.sessionPullChangesTimeout, objc._C_DBL)
        self.assertArgHasType(TestISyncSessionDriverHelper.changedRecordsForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.assertArgIsOut(TestISyncSessionDriverHelper.changedRecordsForEntityName_moreComing_error_, 2)
        self.assertArgHasType(TestISyncSessionDriverHelper.changesForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.assertArgIsOut(TestISyncSessionDriverHelper.changesForEntityName_moreComing_error_, 2)
        self.assertArgHasType(TestISyncSessionDriverHelper.identifiersForRecordsToDeleteForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.assertArgIsOut(TestISyncSessionDriverHelper.identifiersForRecordsToDeleteForEntityName_moreComing_error_, 2)

        self.assertIsInstance(protocols.ISyncSessionDriverDelegate, objc.informal_protocol)


        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didRegisterClientAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didRegisterClientAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willPushAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willPushAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didPushAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didPushAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willPullAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willPullAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didPullAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didPullAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willFinishSessionAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willFinishSessionAndReturnError_, 1)

        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didNegotiateAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didNegotiateAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willNegotiateAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willNegotiateAndReturnError_, 1)
        self.assertResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didReceiveSyncAlertAndReturnError_)
        self.assertArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didReceiveSyncAlertAndReturnError_, 1)


if __name__ == "__main__":
    main()
