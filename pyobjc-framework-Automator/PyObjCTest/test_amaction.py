import Automator
from PyObjCTools.TestSupport import TestCase


class TestAMAction(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Automator.AMLogLevel)
        self.assertEqual(Automator.AMLogLevelDebug, 0)
        self.assertEqual(Automator.AMLogLevelInfo, 1)
        self.assertEqual(Automator.AMLogLevelWarn, 2)
        self.assertEqual(Automator.AMLogLevelError, 3)

    def test_methods(self):
        self.assertArgIsOut(Automator.AMAction.runWithInput_fromAction_error_, 2)

        self.assertResultIsBOOL(Automator.AMAction.isStopped)

        self.assertArgIsOut(Automator.AMAction.initWithContentsOfURL_error_, 1)
        self.assertArgIsBOOL(Automator.AMAction.initWithDefinition_fromArchive_, 1)
        self.assertResultIsBOOL(Automator.AMAction.ignoresInput)

        self.assertArgIsPrintf(Automator.AMAction.logMessageWithLevel_format_, 1)
        self.assertArgIsOut(Automator.AMAction.runWithInput_error_, 1)
