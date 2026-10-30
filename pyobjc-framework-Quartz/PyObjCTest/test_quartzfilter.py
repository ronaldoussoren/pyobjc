from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQuartzFilter(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QuartzFilter.applyToContext_)
