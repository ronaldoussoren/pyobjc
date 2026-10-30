from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure
import Quartz


class TestQuartzFilterManager(TestCase):
    def test_constants(self):
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

    @min_os_level("10.15")
    def test_constants10_15(self):
        self.assertIsInstance(Quartz.kQuartzFilterApplicationDomain, str)
        self.assertIsInstance(Quartz.kQuartzFilterPDFWorkflowDomain, str)
        self.assertIsInstance(Quartz.kQuartzFilterPrintingDomain, str)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QuartzFilterManager.selectFilter_)

    @expectedFailure
    def test_global_update_ok(self):
        self.fail("Not yet supported")
