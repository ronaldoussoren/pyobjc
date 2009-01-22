
from PyObjCTools.TestSupport import *
from SyncServices import *

class TestISyncSessionDriverHelper (NSObject):
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
        self.failUnlessEqual(ISyncSessionDriverModeFast, 1)
        self.failUnlessEqual(ISyncSessionDriverModeSlow, 2)
        self.failUnlessEqual(ISyncSessionDriverModeRefresh, 3)

        self.failUnlessEqual(ISyncSessionDriverChangeRefused, 0)
        self.failUnlessEqual(ISyncSessionDriverChangeAccepted, 1)
        self.failUnlessEqual(ISyncSessionDriverChangeIgnored, 2)
        self.failUnlessEqual(ISyncSessionDriverChangeError, 3)

    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessResultIsBOOL(ISyncSessionDriver.sync)
        self.failUnlessResultIsBOOL(ISyncSessionDriver.startAsynchronousSync_)
        self.failUnlessArgIsOut(ISyncSessionDriver.startAsynchronousSync_, 0)
        self.failUnlessResultIsBOOL(ISyncSessionDriver.handlesSyncAlerts)


    @min_os_level('10.5')
    def testProtocols(self):
        self.failUnlessIsInstance(protocols.ISyncSessionDriverDataSourceOptionalMethods, objc.informal_protocol)
        self.failUnlessArgHasType(TestISyncSessionDriverHelper.recordsForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.failUnlessArgHasType(TestISyncSessionDriverHelper.recordsForEntityName_moreComing_error_, 2, objc._C_OUT + objc._C_ID)

        self.failUnlessResultHasType(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, objc._C_INT)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, 2)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, 3)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.applyChange_forEntityName_remappedRecordIdentifier_formattedRecord_error_, 4)

        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.deleteAllRecordsForEntityName_error_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.deleteAllRecordsForEntityName_error_, 1)

        self.failUnlessResultHasType(TestISyncSessionDriverHelper.sessionPullChangesTimeout, objc._C_DBL)
        self.failUnlessArgHasType(TestISyncSessionDriverHelper.changedRecordsForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.changedRecordsForEntityName_moreComing_error_, 2)
        self.failUnlessArgHasType(TestISyncSessionDriverHelper.changesForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.changesForEntityName_moreComing_error_, 2)
        self.failUnlessArgHasType(TestISyncSessionDriverHelper.identifiersForRecordsToDeleteForEntityName_moreComing_error_, 1, objc._C_OUT + objc._C_PTR + objc._C_NSBOOL)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.identifiersForRecordsToDeleteForEntityName_moreComing_error_, 2)

        self.failUnlessIsInstance(protocols.ISyncSessionDriverDelegate, objc.informal_protocol)


        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didRegisterClientAndReturnError_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didRegisterClientAndReturnError_, 1)
        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willPushAndReturnError_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willPushAndReturnError_, 1)
        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didPushAndReturnError_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didPushAndReturnError_, 1)
        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willPullAndReturnError_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willPullAndReturnError_, 1)
        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_didPullAndReturnError_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.sessionDriver_didPullAndReturnError_, 1)
        self.failUnlessResultIsBOOL(TestISyncSessionDriverHelper.sessionDriver_willFinishSessionAndReturnError_)
        self.failUnlessArgIsOut(TestISyncSessionDriverHelper.sessionDriver_willFinishSessionAndReturnError_, 1)


if __name__ == "__main__":
    main()
