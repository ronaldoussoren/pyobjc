import Quartz
from PyObjCTools.TestSupport import TestCase


class TestCAEmitterCell(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.CAEmitterCell.shouldArchiveValueForKey_)
        self.assertResultIsBOOL(Quartz.CAEmitterCell.isEnabled)
        self.assertArgIsBOOL(Quartz.CAEmitterCell.setEnabled_, 0)
