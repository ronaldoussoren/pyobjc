import Automator
from PyObjCTools.TestSupport import TestCase


class TestAutomatorErrors(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Automator.AMErrorCode)

    def testConstants(self):
        self.assertEqual(Automator.AMAutomatorErrorDomain, "com.apple.Automator")
        self.assertEqual(Automator.AMActionErrorKey, "AMActionErrorKey")
        self.assertIsInstance(Automator.AMAutomatorErrorDomain, str)
        self.assertIsInstance(Automator.AMActionErrorKey, str)

        self.assertEqual(Automator.AMWorkflowNewerVersionError, -100)
        self.assertEqual(Automator.AMWorkflowPropertyListInvalidError, -101)
        self.assertEqual(Automator.AMWorkflowNewerActionVersionError, -111)
        self.assertEqual(Automator.AMWorkflowOlderActionVersionError, -112)
        self.assertEqual(Automator.AMWorkflowActionsNotLoadedError, -113)
        self.assertEqual(Automator.AMWorkflowNoEnabledActionsError, -114)
        self.assertEqual(Automator.AMUserCanceledError, -128)
        self.assertEqual(Automator.AMNoSuchActionError, -200)
        self.assertEqual(Automator.AMActionNotLoadableError, -201)
        self.assertEqual(Automator.AMActionArchitectureMismatchError, -202)
        self.assertEqual(Automator.AMActionRuntimeMismatchError, -203)
        self.assertEqual(Automator.AMActionLoadError, -204)
        self.assertEqual(Automator.AMActionLinkError, -205)
        self.assertEqual(Automator.AMActionApplicationResourceError, -206)
        self.assertEqual(Automator.AMActionApplicationVersionResourceError, -207)
        self.assertEqual(Automator.AMActionFileResourceError, -208)
        self.assertEqual(Automator.AMActionLicenseResourceError, -209)
        self.assertEqual(Automator.AMActionRequiredActionResourceError, -210)
        self.assertEqual(Automator.AMActionInitializationError, -211)
        self.assertEqual(Automator.AMActionExecutionError, -212)
        self.assertEqual(Automator.AMActionExceptionError, -213)
        self.assertEqual(Automator.AMActionPropertyListInvalidError, -214)
        self.assertEqual(Automator.AMActionInsufficientDataError, -215)
        self.assertEqual(Automator.AMActionIsDeprecatedError, -216)
        self.assertEqual(Automator.AMActionFailedGatekeeperError, -217)
        self.assertEqual(Automator.AMActionSignatureCorruptError, -218)
        self.assertEqual(Automator.AMActionQuarantineError, -219)
        self.assertEqual(Automator.AMActionXProtectError, -220)
        self.assertEqual(Automator.AMActionMalwareError, -221)
        self.assertEqual(Automator.AMActionThirdPartyActionsNotAllowedError, -222)
        self.assertEqual(Automator.AMActionXPCError, -223)
        self.assertEqual(Automator.AMConversionNotPossibleError, -300)
        self.assertEqual(Automator.AMConversionNoDataError, -301)
        self.assertEqual(Automator.AMConversionFailedError, -302)
