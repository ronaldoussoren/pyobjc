
from PyObjCTools.TestSupport import *
import objc
from Foundation import NSObject

try:
    from Quartz.QuickLookUI import *
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
        self.failUnlessIsInstance(QLPreviewPanel, objc.objc_class)

    @min_os_level('10.6')
    def testMethods(self):
        self.failUnlessResultIsBOOL(QLPreviewPanel.sharedPreviewPanelExists)
        self.failUnlessResultIsBOOL(QLPreviewPanel.enterFullScreenMode_withOptions_)
        self.failUnlessResultIsBOOL(QLPreviewPanel.isInFullScreenMode)

        self.failUnlessResultIsBOOL(TestQLPreviewPanelHelper.acceptsPreviewPanelControl_)
        self.failUnlessResultIsBOOL(TestQLPreviewPanelHelper.previewPanel_handleEvent_)

        #previewPanel_sourceFrameOnScreenForPreviewItem_
        #previewPanel_transitionImageForPreviewItem_contentRect_
        self.fail("finishme")

if __name__ == "__main__":
    main()
