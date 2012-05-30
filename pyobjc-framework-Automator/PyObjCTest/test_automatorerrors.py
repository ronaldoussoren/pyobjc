
from PyObjCTools.TestSupport import *
from Automator import *

try:
    unicode
except NameError:
    unicode = str

class TestAutomatorErrors (TestCase):
    def testConstants(self):
        self.assertEqual(AMAutomatorErrorDomain, "com.apple.Automator")
        self.assertEqual(AMActionErrorKey, "AMActionErrorKey")
        self.assertIsInstance(AMAutomatorErrorDomain, (str, unicode))
        self.assertIsInstance(AMActionErrorKey, (str, unicode))

        self.assertEqual(AMWorkflowNewerVersionError, -100)
        self.assertEqual(AMWorkflowPropertyListInvalidError, -101)
        self.assertEqual(AMWorkflowNewerActionVersionError, -111)
        self.assertEqual(AMWorkflowOlderActionVersionError, -112)
        self.assertEqual(AMUserCanceledError, -128)
        self.assertEqual(AMNoSuchActionError, -200)
        self.assertEqual(AMActionNotLoadableError, -201)
        self.assertEqual(AMActionArchitectureMismatchError, -202)
        self.assertEqual(AMActionRuntimeMismatchError, -203)
        self.assertEqual(AMActionLoadError, -204)
        self.assertEqual(AMActionLinkError, -205)
        self.assertEqual(AMActionApplicationResourceError, -206)
        self.assertEqual(AMActionApplicationVersionResourceError, -207)
        self.assertEqual(AMActionFileResourceError, -208)
        self.assertEqual(AMActionLicenseResourceError, -209)
        self.assertEqual(AMActionRequiredActionResourceError, -210)
        self.assertEqual(AMActionInitializationError, -211)
        self.assertEqual(AMActionExecutionError, -212)
        self.assertEqual(AMActionExceptionError, -213)
        self.assertEqual(AMActionPropertyListInvalidError, -214)
        self.assertEqual(AMActionInsufficientDataError, -215)
        self.assertEqual(AMActionIsDeprecatedError, -216)
        self.assertEqual(AMConversionNotPossibleError, -300)
        self.assertEqual(AMConversionNoDataError, -301)
        self.assertEqual(AMConversionFailedError, -302)


if __name__ == "__main__":
    main()
