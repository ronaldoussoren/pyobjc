import OpenDirectory
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestODSession(TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODSessionProxyAddress, str)
        self.assertIsInstance(OpenDirectory.ODSessionProxyPort, str)
        self.assertIsInstance(OpenDirectory.ODSessionProxyUsername, str)
        self.assertIsInstance(OpenDirectory.ODSessionProxyPassword, str)

    def testMethods(self):
        self.assertArgIsOut(OpenDirectory.ODSession.sessionWithOptions_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODSession.initWithOptions_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODSession.nodeNamesAndReturnError_, 0)

    @min_os_level("10.9")
    def testMethods10_9(self):
        self.assertArgIsBOOL(
            OpenDirectory.ODSession.configurationAuthorizationAllowingUserInteraction_error_,
            0,
        )
        self.assertArgIsOut(
            OpenDirectory.ODSession.configurationAuthorizationAllowingUserInteraction_error_,
            1,
        )

        self.assertResultIsBOOL(
            OpenDirectory.ODSession.addConfiguration_authorization_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODSession.addConfiguration_authorization_error_, 2
        )

        self.assertResultIsBOOL(
            OpenDirectory.ODSession.deleteConfiguration_authorization_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODSession.deleteConfiguration_authorization_error_, 2
        )

        self.assertResultIsBOOL(
            OpenDirectory.ODSession.deleteConfigurationWithNodename_authorization_error_
        )
        self.assertArgIsOut(
            OpenDirectory.ODSession.deleteConfigurationWithNodename_authorization_error_,
            2,
        )
