
from PyObjCTools.TestSupport import *
from Automator import *

class TestAMAction (TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsPrintf(AMAction.logMessageWithLevel_format_, 1)
        self.assertArgIsOut(AMAction.runWithInput_error_, 1)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsOut(AMAction.initWithContentsOfURL_error_, 1)
        self.assertArgIsBOOL(AMAction.initWithDefinition_fromArchive_, 1)
        self.assertResultIsBOOL(AMAction.ignoresInput)

    def testMethods(self):
        self.assertArgIsOut(AMAction.runWithInput_fromAction_error_, 2)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(AMAction.isStopped)

    def testConstants(self):
        self.assertEqual(AMLogLevelDebug, 0)
        self.assertEqual(AMLogLevelInfo, 1)
        self.assertEqual(AMLogLevelWarn, 2)
        self.assertEqual(AMLogLevelError, 3)

if __name__ == "__main__":
    main()
