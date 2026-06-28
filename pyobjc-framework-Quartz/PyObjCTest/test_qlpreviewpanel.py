import objc
from Foundation import NSObject, NSRect
from PyObjCTools.TestSupport import TestCase

import Quartz


class TestQLPreviewPanelHelper(NSObject):
    def acceptsPreviewPanelControl_(self, panel):
        return 1

    def previewPanel_handleEvent_(self, panel, event):
        return 1

    def previewPanel_sourceFrameOnScreenForPreviewItem_(self, panel, item):
        return 1

    def previewPanel_transitionImageForPreviewItem_contentRect_(
        self, panel, item, rect
    ):
        return 1


class TestQLPreviewPanel(TestCase):
    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.sharedPreviewPanelExists)
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.enterFullScreenMode_withOptions_)
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.isInFullScreenMode)

    def test_protocols(self):
        self.assertProtocolExists("QLPreviewPanelDataSource", Quartz)
        self.assertProtocolExists("QLPreviewPanelDelegate", Quartz)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestQLPreviewPanelHelper.acceptsPreviewPanelControl_)
        self.assertResultIsBOOL(TestQLPreviewPanelHelper.previewPanel_handleEvent_)

        self.assertResultHasType(
            TestQLPreviewPanelHelper.previewPanel_sourceFrameOnScreenForPreviewItem_,
            NSRect.__typestr__,
        )
        self.assertArgHasType(
            TestQLPreviewPanelHelper.previewPanel_transitionImageForPreviewItem_contentRect_,
            2,
            objc._C_IN + objc._C_PTR + NSRect.__typestr__,
        )
