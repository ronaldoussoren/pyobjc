from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEFilterProvider(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEFilterAction)
        self.assertIsEnumType(NetworkExtension.NEFilterReportEvent)
        self.assertIsEnumType(NetworkExtension.NEFilterReportFrequency)

    @min_os_level("10.15")
    def testMethods10_15(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterProvider.startFilterWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEFilterProvider.stopFilterWithReason_completionHandler_,
            1,
            b"v",
        )

        self.assertArgIsBOOL(
            NetworkExtension.NEFilterNewFlowVerdict.filterDataVerdictWithFilterInbound_peekInboundBytes_filterOutbound_peekOutboundBytes_,  # noqa: B950
            0,
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEFilterNewFlowVerdict.filterDataVerdictWithFilterInbound_peekInboundBytes_filterOutbound_peekOutboundBytes_,  # noqa: B950
            2,
        )

        self.assertResultIsBOOL(NetworkExtension.NEFilterVerdict.shouldReport)
        self.assertArgIsBOOL(NetworkExtension.NEFilterVerdict.setShouldReport_, 0)

    def test_constants(self):
        self.assertEqual(NetworkExtension.NEFilterActionInvalid, 0)
        self.assertEqual(NetworkExtension.NEFilterActionAllow, 1)
        self.assertEqual(NetworkExtension.NEFilterActionDrop, 2)
        self.assertEqual(NetworkExtension.NEFilterActionRemediate, 3)
        self.assertEqual(NetworkExtension.NEFilterActionFilterData, 4)

        self.assertEqual(NetworkExtension.NEFilterReportEventNewFlow, 1)
        self.assertEqual(NetworkExtension.NEFilterReportEventDataDecision, 2)
        self.assertEqual(NetworkExtension.NEFilterReportEventFlowClosed, 3)
        self.assertEqual(NetworkExtension.NEFilterReportEventStatistics, 4)

        self.assertEqual(NetworkExtension.NEFilterReportFrequencyNone, 0)
        self.assertEqual(NetworkExtension.NEFilterReportFrequencyLow, 1)
        self.assertEqual(NetworkExtension.NEFilterReportFrequencyMedium, 2)
        self.assertEqual(NetworkExtension.NEFilterReportFrequencyHigh, 3)
