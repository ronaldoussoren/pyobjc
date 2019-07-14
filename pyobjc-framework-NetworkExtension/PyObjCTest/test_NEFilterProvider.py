from PyObjCTools.TestSupport import *
import sys

if sys.maxsize >= 2 ** 32:

    import NetworkExtension

    class TestNEFilterProvider (TestCase):
        @min_os_level('10.15')
        def testMethods10_15(self):
            self.assertArgIsBlock(NetworkExtension.NEFilterProvider.startFilterWithCompletionHandler_, 0, b'v@')
            self.assertArgIsBlock(NetworkExtension.NEFilterProvider.stopFilterWithReason_completionHandler_, 1, b'v')

            self.assertArgIsBOOL(NetworkExtension.NEFilterNewFlowVerdict.filterDataVerdictWithFilterInbound_peekInboundBytes_filterOutbound_peekOutboundBytes_, 0)
            self.assertArgIsBOOL(NetworkExtension.NEFilterNewFlowVerdict.filterDataVerdictWithFilterInbound_peekInboundBytes_filterOutbound_peekOutboundBytes_, 2)

        def test_constants(self):
            self.asserEqual(NetworkExtension.NEFilterActionInvalid, 0)
            self.asserEqual(NetworkExtension.NEFilterActionAllow, 1)
            self.asserEqual(NetworkExtension.NEFilterActionDrop, 2)
            self.asserEqual(NetworkExtension.NEFilterActionRemediate, 3)
            self.asserEqual(NetworkExtension.NEFilterActionFilterData, 4)

            self.assertEqual(NetworkExtension.NEFilterReportEventNewFlow, 1)
            self.assertEqual(NetworkExtension.NEFilterReportEventDataDecision, 2)
            self.assertEqual(NetworkExtension.NEFilterReportEventFlowClosed, 3)



if __name__ == "__main__":
    main()
