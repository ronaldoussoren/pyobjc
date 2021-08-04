import objc
from PyObjCTools.TestSupport import TestCase, min_os_level, min_sdk_level

import Quartz


# XXX: This test file needs to be merged with test_ql... !!!
class TestPLPreviewPanelHelper(Quartz.NSObject):
    def previewPanel_handleEvent_(self, a, b):
        return 1

    def previewPanel_sourceFrameOnScreenForPreviewItem_(self, a, b):
        return 1

    def previewPanel_transitionImageForPreviewItem_contentRect_(self, a, b, c):
        return 1


class TestQLPreviewPanel(TestCase):
    @min_os_level("12.0")
    def testMethods12_0(self):
        self.assertResultIsBOOL(Quartz.QLPreviewPanel.isInFullScreenMode)

    @min_sdk_level("12.0")
    def test_protocols(self):
        objc.protocolNamed("QLPreviewPanelDataSource")

    def test_methods(self):
        self.assertResultIsBOOL(TestPLPreviewPanelHelper.previewPanel_handleEvent_)

        self.assertResultHasType(
            TestPLPreviewPanelHelper.previewPanel_sourceFrameOnScreenForPreviewItem_,
            Quartz.NSRect.__typestr__,
        )

        self.assertArgHasType(
            TestPLPreviewPanelHelper.previewPanel_transitionImageForPreviewItem_contentRect_,
            2,
            b"n^" + Quartz.NSRect.__typestr__,
        )
