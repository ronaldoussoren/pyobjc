import Quartz
from PyObjCTools.TestSupport import TestCase


class TestQLPreviewView(TestCase):
    def test_enums(self):
        self.assertIsEnumType(Quartz.QLPreviewViewStyle)
        self.assertEqual(Quartz.QLPreviewViewStyleNormal, 0)
        self.assertEqual(Quartz.QLPreviewViewStyleCompact, 1)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QLPreviewView.shouldCloseWithWindow)
        self.assertResultIsBOOL(Quartz.QLPreviewView.autostarts)

        self.assertArgIsBOOL(Quartz.QLPreviewView.setShouldCloseWithWindow_, 0)
        self.assertArgIsBOOL(Quartz.QLPreviewView.setAutostarts_, 0)
