import CoreServices
from PyObjCTools.TestSupport import TestCase


class TestLSConstants(TestCase):
    def test_constants(self):
        # self.assertIsEnumType(CoreServices.OSStatus)
        self.assertEqual(CoreServices.kLSNo32BitEnvironmentErr, -10386)
        self.assertEqual(CoreServices.kLSMalformedLocErr, -10400)
        self.assertEqual(CoreServices.kLSAppInTrashErr, -10660)
        self.assertEqual(CoreServices.kLSExecutableIncorrectFormat, -10661)
        self.assertEqual(CoreServices.kLSAttributeNotFoundErr, -10662)
        self.assertEqual(CoreServices.kLSAttributeNotSettableErr, -10663)
        self.assertEqual(CoreServices.kLSIncompatibleApplicationVersionErr, -10664)
        self.assertEqual(CoreServices.kLSNoRosettaEnvironmentErr, -10665)
        self.assertEqual(CoreServices.kLSGarbageCollectionUnsupportedErr, -10666)
        self.assertEqual(CoreServices.kLSUnknownErr, -10810)
        self.assertEqual(CoreServices.kLSNotAnApplicationErr, -10811)
        self.assertEqual(CoreServices.kLSNotInitializedErr, -10812)
        self.assertEqual(CoreServices.kLSDataUnavailableErr, -10813)
        self.assertEqual(CoreServices.kLSApplicationNotFoundErr, -10814)
        self.assertEqual(CoreServices.kLSUnknownTypeErr, -10815)
        self.assertEqual(CoreServices.kLSDataTooOldErr, -10816)
        self.assertEqual(CoreServices.kLSDataErr, -10817)
        self.assertEqual(CoreServices.kLSLaunchInProgressErr, -10818)
        self.assertEqual(CoreServices.kLSNotRegisteredErr, -10819)
        self.assertEqual(CoreServices.kLSAppDoesNotClaimTypeErr, -10820)
        self.assertEqual(CoreServices.kLSAppDoesNotSupportSchemeWarning, -10821)
        self.assertEqual(CoreServices.kLSServerCommunicationErr, -10822)
        self.assertEqual(CoreServices.kLSCannotSetInfoErr, -10823)
        self.assertEqual(CoreServices.kLSNoRegistrationInfoErr, -10824)
        self.assertEqual(CoreServices.kLSIncompatibleSystemVersionErr, -10825)
        self.assertEqual(CoreServices.kLSNoLaunchPermissionErr, -10826)
        self.assertEqual(CoreServices.kLSNoExecutableErr, -10827)
        self.assertEqual(CoreServices.kLSNoClassicEnvironmentErr, -10828)
        self.assertEqual(CoreServices.kLSMultipleSessionsNotSupportedErr, -10829)
        self.assertEqual(
            CoreServices.kLSLaunchFailedBecauseLaunchConstraintsWereViolatedErr, -10350
        )
        self.assertEqual(CoreServices.kLSTemplateApplicationIsCorruptErr, -10401)
        self.assertEqual(
            CoreServices.kLSTemplateApplicationDataVaultIsCorruptErr, -10402
        )
        self.assertEqual(
            CoreServices.kLSTemplateApplicationDataVaultInformationIsCorruptErr, -10403
        )
        self.assertEqual(
            CoreServices.kLSTemplateApplicationTeamIdentifierMismatchErr, -10404
        )
        self.assertEqual(CoreServices.kLSTemplateApplicationSignatureFailureErr, -10410)
        self.assertEqual(
            CoreServices.kLSTemplateApplicationSignatureNotFoundErr, -10411
        )
        self.assertEqual(
            CoreServices.kLSTemplateApplicationUnableToContactServerErr, -10420
        )
        self.assertEqual(CoreServices.kLSTemplateApplicationUnknownErr, -10421)
        self.assertEqual(
            CoreServices.kLSTemplateApplicationOperationRequiresEntitlementErr, -10422
        )

        self.assertIsEnumType(CoreServices.LSRolesMask)
        self.assertEqual(CoreServices.kLSRolesNone, 0x00000001)
        self.assertEqual(CoreServices.kLSRolesViewer, 0x00000002)
        self.assertEqual(CoreServices.kLSRolesEditor, 0x00000004)
        self.assertEqual(CoreServices.kLSRolesShell, 0x00000008)
        self.assertEqual(CoreServices.kLSRolesAll, 0xFFFFFFFF)

        # self.assertIsEnumType(CoreServices.OSType)
        self.assertEqual(CoreServices.kLSUnknownType, 0)
        self.assertEqual(CoreServices.kLSUnknownCreator, 0)
