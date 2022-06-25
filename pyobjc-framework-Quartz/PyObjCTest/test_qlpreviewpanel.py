import objc
from Foundation import NSObject, NSRect
from PyObjCTools.TestSupport import TestCase, min_os_level

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
    @min_os_level("10.6")
    def testClasses(self):
        self.assertIsInstance(Quartz.QLPreviewPanel, objc.objc_class)

    @min_os_level("10.6")
    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.sharedPreviewPanelExists)
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.enterFullScreenMode_withOptions_)
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.isInFullScreenMode)

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

    @min_os_level("10.6")
    def testProtocols(self):
        self.assertProtocolExists("QLPreviewPanelDataSource")

    @min_os_level("10.7")
    def testProtocols10_7(self):
        self.assertProtocolExists("QLPreviewPanelDelegate")
