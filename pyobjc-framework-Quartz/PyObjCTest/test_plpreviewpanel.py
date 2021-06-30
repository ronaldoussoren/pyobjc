import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import Quartz


class TestQLPreviewPanelHelper(Quartz.NSObject):
    def previewPanel_handleEvent_(self, a, b):
        return 1

    def previewPanel_sourceFrameOnScreenForPreviewItem_(self, a, b):
        return 1

    def previewPanel_transitionImageForPreviewItem_contentRect_(self, a, b):
        return 1


class TestQLPreviewPanel(TestCase):
    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.isInFullScreenMode)

    @min_sdk_level("12.0")
    def test_protocols(self):
        objc.protocolNamed("QLPreviewPanelDataSource")

    def test_methods(self):
        self.assertResultIsBOOL(TestQLPreviewPanelHelper.previewPanel_handleEvent_)

        self.assertResultHasType(
            TestQLPreviewPanelHelper.previewPanel_sourceFrameOnScreenForPreviewItem_,
            Quartz.NSRect.__typestr__,
        )

        self.assertArgHasType(
            TestQLPreviewPanelHelper.previewPanel_transitionImageForPreviewItem_contentRect_,
            2,
            Quartz.NSRect.__typestr__,
        )
