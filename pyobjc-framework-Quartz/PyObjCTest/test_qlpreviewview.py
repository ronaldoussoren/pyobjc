import Quartz
from PyObjCTools.TestSupport import TestCase, min_os_level


class TestQLPreviewView(TestCase):
    def test_enum_types(self):
        self.assertIsEnumType(Quartz.QLPreviewViewStyle)

    @min_os_level("10.7")
    def testConstants10_7(self):
        self.assertEqual(Quartz.QLPreviewViewStyleNormal, 0)
        self.assertEqual(Quartz.QLPreviewViewStyleCompact, 1)

    @min_os_level("10.6")
    def testMethods10_6(self):
        self.assertResultIsBOOL(Quartz.QLPreviewView.shouldCloseWithWindow)
        self.assertResultIsBOOL(Quartz.QLPreviewView.autostarts)

        self.assertArgIsBOOL(Quartz.QLPreviewView.setShouldCloseWithWindow_, 0)
        self.assertArgIsBOOL(Quartz.QLPreviewView.setAutostarts_, 0)
