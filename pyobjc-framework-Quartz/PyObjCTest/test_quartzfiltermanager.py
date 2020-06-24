from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz


class TestQuartzFilterManager(TestCase):
    @min_os_level("10.5")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QuartzFilterManager.selectFilter_)

    @min_os_level("10.5")
    def testConstants(self):
        self.assertIsInstance(Quartz.kQuartzFilterManagerDidAddFilterNotification, str)
        self.assertIsInstance(
            Quartz.kQuartzFilterManagerDidRemoveFilterNotification, str
        )
        self.assertIsInstance(
            Quartz.kQuartzFilterManagerDidModifyFilterNotification, str
        )
        self.assertIsInstance(
            Quartz.kQuartzFilterManagerDidSelectFilterNotification, str
        )

    @min_os_level("10.6")
    @expectedFailure
    def testConstants10_6(self):
        # The following definitions are documented for 10.5, but aren't actually
        # exported from the framework:
        self.assertIsInstance(Quartz.kQuartzFilterApplicationDomain, str)
        self.assertIsInstance(Quartz.kQuartzFilterPDFWorkflowDomain, str)
        self.assertIsInstance(Quartz.kQuartzFilterPrintingDomain, str)

    @expectedFailure
    def testGlobalUpdateOK(self):
        self.fail("Not yet supported")
