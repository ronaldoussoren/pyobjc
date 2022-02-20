from PyObjCTools.TestSupport import TestCase, min_os_level
import NetworkExtension


class TestNEAppProxyFlow(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(NetworkExtension.NEFilterManagerError)
        self.assertIsEnumType(NetworkExtension.NEFilterManagerGrade)

    @min_os_level("10.11")
    def testConstants(self):
        self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationInvalid, 1)
        self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationDisabled, 2)
        self.assertEqual(NetworkExtension.NEFilterManagerErrorConfigurationStale, 3)
        self.assertEqual(
            NetworkExtension.NEFilterManagerErrorConfigurationCannotBeRemoved, 4
        )
        self.assertEqual(
            NetworkExtension.NEFilterManagerErrorConfigurationPermissionDenied, 5
        )
        self.assertEqual(
            NetworkExtension.NEFilterManagerErrorConfigurationInternalError, 6
        )

        self.assertEqual(NetworkExtension.NEFilterManagerGradeFirewall, 1)
        self.assertEqual(NetworkExtension.NEFilterManagerGradeInspector, 2)

        self.assertIsInstance(NetworkExtension.NEFilterErrorDomain, str)
        self.assertIsInstance(
            NetworkExtension.NEFilterConfigurationDidChangeNotification, str
        )

    @min_os_level("10.11")
    def testMethods(self):
        self.assertArgIsBlock(
            NetworkExtension.NEFilterManager.loadFromPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEFilterManager.removeFromPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertArgIsBlock(
            NetworkExtension.NEFilterManager.saveToPreferencesWithCompletionHandler_,
            0,
            b"v@",
        )
        self.assertResultIsBOOL(NetworkExtension.NEFilterManager.isEnabled)
        self.assertArgIsBOOL(NetworkExtension.NEFilterManager.setEnabled_, 0)
