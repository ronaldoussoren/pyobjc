import Automator
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAMAction(TestCase):
    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertArgIsPrintf(Automator.AMAction.logMessageWithLevel_format_, 1)
        self.assertArgIsOut(Automator.AMAction.runWithInput_error_, 1)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertArgIsOut(Automator.AMAction.initWithContentsOfURL_error_, 1)
        self.assertArgIsBOOL(Automator.AMAction.initWithDefinition_fromArchive_, 1)
        self.assertResultIsBOOL(Automator.AMAction.ignoresInput)

    def testMethods(self):
        self.assertArgIsOut(Automator.AMAction.runWithInput_fromAction_error_, 2)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Automator.AMAction.isStopped)

    def testConstants(self):
        self.assertEqual(Automator.AMLogLevelDebug, 0)
        self.assertEqual(Automator.AMLogLevelInfo, 1)
        self.assertEqual(Automator.AMLogLevelWarn, 2)
        self.assertEqual(Automator.AMLogLevelError, 3)
