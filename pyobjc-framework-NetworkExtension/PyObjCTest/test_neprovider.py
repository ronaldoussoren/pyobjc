from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class NEProvider(TestCase):
    def test_enums(self):
        self.assertIsEnumType(NetworkExtension.NEProviderStopReason)
        self.assertEqual(NetworkExtension.NEProviderStopReasonNone, 0)
        self.assertEqual(NetworkExtension.NEProviderStopReasonUserInitiated, 1)
        self.assertEqual(NetworkExtension.NEProviderStopReasonProviderFailed, 2)
        self.assertEqual(NetworkExtension.NEProviderStopReasonNoNetworkAvailable, 3)
        self.assertEqual(
            NetworkExtension.NEProviderStopReasonUnrecoverableNetworkChange, 4
        )
        self.assertEqual(NetworkExtension.NEProviderStopReasonProviderDisabled, 5)
        self.assertEqual(NetworkExtension.NEProviderStopReasonAuthenticationCanceled, 6)
        self.assertEqual(NetworkExtension.NEProviderStopReasonConfigurationFailed, 7)
        self.assertEqual(NetworkExtension.NEProviderStopReasonIdleTimeout, 8)
        self.assertEqual(NetworkExtension.NEProviderStopReasonConfigurationDisabled, 9)
        self.assertEqual(NetworkExtension.NEProviderStopReasonConfigurationRemoved, 10)
        self.assertEqual(NetworkExtension.NEProviderStopReasonSuperceded, 11)
        self.assertEqual(NetworkExtension.NEProviderStopReasonUserLogout, 12)
        self.assertEqual(NetworkExtension.NEProviderStopReasonUserSwitch, 13)
        self.assertEqual(NetworkExtension.NEProviderStopReasonConnectionFailed, 14)
        self.assertEqual(NetworkExtension.NEProviderStopReasonSleep, 15)
        self.assertEqual(NetworkExtension.NEProviderStopReasonAppUpdate, 16)
        self.assertEqual(NetworkExtension.NEProviderStopReasonInternalError, 17)

    @min_os_level("10.11")
    def test_methods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEProvider.sleepWithCompletionHandler_, 0, b"v"
        )
        self.assertArgIsBOOL(
            NetworkExtension.NEProvider.createTCPConnectionToEndpoint_enableTLS_TLSParameters_delegate_,
            1,
        )

    @min_os_level("10.12")
    def test_methods10_12(self):
        self.assertArgIsBlock(
            NetworkExtension.NEProvider.displayMessage_completionHandler_, 1, b"vZ"
        )
