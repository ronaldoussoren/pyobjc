
from PyObjCTools.TestSupport import *
from Quartz.QuartzComposer import *

class TestQCView (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(QCViewDidStartRenderingNotification, unicode)
        self.failUnlessIsInstance(QCViewDidStopRenderingNotification, unicode)

    def testMethods(self):
        self.failUnlessResultIsBOOL(QCView.loadCompositionFromFile_)

        self.failUnlessArgIsBOOL(QCView.setAutostartsRendering_, 0)
        self.failUnlessResultIsBOOL(QCView.autostartsRendering)

        self.failUnlessResultIsBOOL(QCView.startRendering)
        self.failUnlessResultIsBOOL(QCView.isRendering)

    @min_os_level('10.5')
    def testMethods10_5(self):
        self.failUnlessResultIsBOOL(QCView.loadComposition_)
        self.failUnlessResultIsBOOL(QCView.renderAtTime_arguments_)
        self.failUnlessResultIsBOOL(QCView.isPausedRendering)

if __name__ == "__main__":
    main()
