
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCView (TestCase):
    def testConstants(self):
        self.assertIsInstance(QCViewDidStartRenderingNotification, unicode)
        self.assertIsInstance(QCViewDidStopRenderingNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(QCView.loadCompositionFromFile_)

        self.assertArgIsBOOL(QCView.setAutostartsRendering_, 0)
        self.assertResultIsBOOL(QCView.autostartsRendering)

        self.assertResultIsBOOL(QCView.startRendering)
        self.assertResultIsBOOL(QCView.isRendering)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.assertResultIsBOOL(QCView.loadComposition_)
        self.assertResultIsBOOL(QCView.renderAtTime_arguments_)
        self.assertResultIsBOOL(QCView.isPausedRendering)

if __name__ == "__main__":
    main()
