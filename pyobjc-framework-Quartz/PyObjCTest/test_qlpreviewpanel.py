
from PyObjCTools.TestSupport import *
import objc
from Foundation import NSObject

try:
    from Quartz import *
except ImportError:
    pass

class TestQLPreviewPanelHelper (NSObject):
    def acceptsPreviewPanelControl_(self, panel): return 1
    def previewPanel_handleEvent_(self, panel, event): return 1
    def previewPanel_sourceFrameOnScreenForPreviewItem_(self, panel, item): return 1
    def previewPanel_transitionImageForPreviewItem_contentRect_(self, panel, item, rect): return 1


class TestQLPreviewPanel (TestCase):
    @min_os_level('10.6')
    def testClasses(self):
        self.assertIsInstance(QLPreviewPanel, objc.objc_class)

    @min_os_level('10.6')
    def testMethods(self):
        self.assertResultIsBOOL(QLPreviewPanel.sharedPreviewPanelExists)
        self.assertResultIsBOOL(QLPreviewPanel.enterFullScreenMode_withOptions_)
        self.assertResultIsBOOL(QLPreviewPanel.isInFullScreenMode)

        self.assertResultIsBOOL(TestQLPreviewPanelHelper.acceptsPreviewPanelControl_)
        self.assertResultIsBOOL(TestQLPreviewPanelHelper.previewPanel_handleEvent_)

        self.assertResultHasType(TestQLPreviewPanelHelper.previewPanel_sourceFrameOnScreenForPreviewItem_, NSRect.__typestr__)
        self.assertArgHasType(TestQLPreviewPanelHelper.previewPanel_transitionImageForPreviewItem_contentRect_, 2, NSRect.__typestr__)

if __name__ == "__main__":
    main()
