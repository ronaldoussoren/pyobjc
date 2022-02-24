from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyFlow(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEEvaluateConnectionRuleAction)
        self.assertIsEnumType(NetworkExtension.NEOnDemandRuleAction)
        self.assertIsEnumType(NetworkExtension.NEOnDemandRuleInterfaceType)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionConnect, 1)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionDisconnect, 2)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionEvaluateConnection, 3)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionIgnore, 4)

        self.assertEqual(NetworkExtension.NEOnDemandRuleInterfaceTypeAny, 0)
        self.assertEqual(NetworkExtension.NEOnDemandRuleInterfaceTypeEthernet, 1)
        self.assertEqual(NetworkExtension.NEOnDemandRuleInterfaceTypeWiFi, 2)

        self.assertEqual(
            NetworkExtension.NEEvaluateConnectionRuleActionConnectIfNeeded, 1
        )
        self.assertEqual(NetworkExtension.NEEvaluateConnectionRuleActionNeverConnect, 2)
