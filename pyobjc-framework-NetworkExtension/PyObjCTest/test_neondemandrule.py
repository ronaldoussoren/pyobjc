from PyObjCTools.TestSupport import TestCase
import NetworkExtension


class TestNEAppProxyFlow(TestCase):
    def test_enums(self):
        self.assertIsEnumType(NetworkExtension.NEEvaluateConnectionRuleAction)
        self.assertEqual(
            NetworkExtension.NEEvaluateConnectionRuleActionConnectIfNeeded, 1
        )
        self.assertEqual(NetworkExtension.NEEvaluateConnectionRuleActionNeverConnect, 2)

        self.assertIsEnumType(NetworkExtension.NEOnDemandRuleAction)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionConnect, 1)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionDisconnect, 2)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionEvaluateConnection, 3)
        self.assertEqual(NetworkExtension.NEOnDemandRuleActionIgnore, 4)

        self.assertIsEnumType(NetworkExtension.NEOnDemandRuleInterfaceType)
        self.assertEqual(NetworkExtension.NEOnDemandRuleInterfaceTypeAny, 0)
        self.assertEqual(NetworkExtension.NEOnDemandRuleInterfaceTypeEthernet, 1)
        self.assertEqual(NetworkExtension.NEOnDemandRuleInterfaceTypeWiFi, 2)
