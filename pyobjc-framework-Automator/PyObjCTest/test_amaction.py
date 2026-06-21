import Automator
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestAMAction(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Automator.AMLogLevel)

    @min_os_level("10.7")
    def test_methods10_7(self):
        self.assertArgIsPrintf(Automator.AMAction.logMessageWithLevel_format_, 1)
        self.assertArgIsOut(Automator.AMAction.runWithInput_error_, 1)

    @min_os_level("10.5")
    def test_methods10_5(self):
        self.assertArgIsOut(Automator.AMAction.initWithContentsOfURL_error_, 1)
        self.assertArgIsBOOL(Automator.AMAction.initWithDefinition_fromArchive_, 1)
        self.assertResultIsBOOL(Automator.AMAction.ignoresInput)

    def test_methods(self):
        self.assertArgIsOut(Automator.AMAction.runWithInput_fromAction_error_, 2)

    @min_os_level("10.6")
    def test_methods10_6(self):
        self.assertResultIsBOOL(Automator.AMAction.isStopped)

    def test_constants(self):
        self.assertEqual(Automator.AMLogLevelDebug, 0)
        self.assertEqual(Automator.AMLogLevelInfo, 1)
        self.assertEqual(Automator.AMLogLevelWarn, 2)
        self.assertEqual(Automator.AMLogLevelError, 3)
