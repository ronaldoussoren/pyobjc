
from PyObjCTools.TestSupport import *
from Automator import *

class TestAutomatorErrors (TestCase):
    def testConstants(self):
        self.failUnlessEqual(AMAutomatorErrorDomain, u"com.apple.Automator")
        self.failUnlessEqual(AMActionErrorKey, u"AMActionErrorKey")

	self.failUnlessEqual(AMWorkflowNewerVersionError, -100)
	self.failUnlessEqual(AMWorkflowPropertyListInvalidError, -101)
	self.failUnlessEqual(AMWorkflowNewerActionVersionError, -111)
	self.failUnlessEqual(AMWorkflowOlderActionVersionError, -112)
	self.failUnlessEqual(AMUserCanceledError, -128)
	self.failUnlessEqual(AMNoSuchActionError, -200)
	self.failUnlessEqual(AMActionNotLoadableError, -201)
	self.failUnlessEqual(AMActionArchitectureMismatchError, -202)
	self.failUnlessEqual(AMActionRuntimeMismatchError, -203)
	self.failUnlessEqual(AMActionLoadError, -204)
	self.failUnlessEqual(AMActionLinkError, -205)
	self.failUnlessEqual(AMActionApplicationResourceError, -206)
	self.failUnlessEqual(AMActionApplicationVersionResourceError, -207)
	self.failUnlessEqual(AMActionFileResourceError, -208)
	self.failUnlessEqual(AMActionLicenseResourceError, -209)
	self.failUnlessEqual(AMActionRequiredActionResourceError, -210)
	self.failUnlessEqual(AMActionInitializationError, -211)
	self.failUnlessEqual(AMActionExecutionError, -212)
	self.failUnlessEqual(AMActionExceptionError, -213)
	self.failUnlessEqual(AMActionPropertyListInvalidError, -214)
	self.failUnlessEqual(AMActionInsufficientDataError, -215)
	self.failUnlessEqual(AMActionIsDeprecatedError, -216)
	self.failUnlessEqual(AMConversionNotPossibleError, -300)
	self.failUnlessEqual(AMConversionNoDataError, -301)
	self.failUnlessEqual(AMConversionFailedError, -302)


if __name__ == "__main__":
    main()
