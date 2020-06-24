from PyObjCTools.TestSupport import TestCase, min_os_level
import Quartz


class TestQCView(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.QCViewDidStartRenderingNotification, str)
        self.assertIsInstance(Quartz.QCViewDidStopRenderingNotification, str)

    def testMethods(self):
        self.assertResultIsBOOL(Quartz.QCView.loadCompositionFromFile_)

        self.assertArgIsBOOL(Quartz.QCView.setAutostartsRendering_, 0)
        self.assertResultIsBOOL(Quartz.QCView.autostartsRendering)

        self.assertResultIsBOOL(Quartz.QCView.startRendering)
        self.assertResultIsBOOL(Quartz.QCView.isRendering)

    @min_os_level("10.5")
    def testMethods10_5(self):
        self.assertResultIsBOOL(Quartz.QCView.loadComposition_)
        self.assertResultIsBOOL(Quartz.QCView.renderAtTime_arguments_)
        self.assertResultIsBOOL(Quartz.QCView.isPausedRendering)
