from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCView(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.QCViewDidStartRenderingNotification, str)
        self.assertIsInstance(Quartz.QCViewDidStopRenderingNotification, str)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QCView.loadCompositionFromFile_)

        self.assertArgIsBOOL(Quartz.QCView.setAutostartsRendering_, 0)
        self.assertResultIsBOOL(Quartz.QCView.autostartsRendering)

        self.assertResultIsBOOL(Quartz.QCView.startRendering)
        self.assertResultIsBOOL(Quartz.QCView.isRendering)

        self.assertResultIsBOOL(Quartz.QCView.loadComposition_)
        self.assertResultIsBOOL(Quartz.QCView.renderAtTime_arguments_)
        self.assertResultIsBOOL(Quartz.QCView.isPausedRendering)
