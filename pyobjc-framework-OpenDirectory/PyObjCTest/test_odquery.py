import OpenDirectory
from PyObjCTools.TestSupport import TestCase


class TestODQuery(TestCase):
    def testMethods(self):
        self.assertArgIsOut(
            OpenDirectory.ODQuery.queryWithNode_forRecordTypes_attribute_matchType_queryValues_returnAttributes_maximumResults_error_,  # noqa: B950
            7,
        )
        self.assertArgIsOut(
            OpenDirectory.ODQuery.initWithNode_forRecordTypes_attribute_matchType_queryValues_returnAttributes_maximumResults_error_,  # noqa: B950
            7,
        )

        self.assertArgIsBOOL(OpenDirectory.ODQuery.resultsAllowingPartial_error_, 0)
        self.assertArgIsOut(OpenDirectory.ODQuery.resultsAllowingPartial_error_, 1)

    def testProtocols(self):
        self.assertProtocolExists("ODQueryDelegate")
