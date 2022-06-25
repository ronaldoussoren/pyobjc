from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCRendererHelper(Quartz.NSObject):
    def setValue_forInputKey_(self, v, k):
        return 1


class TestQCRenderer(TestCase):
    def testConstants(self):
        self.assertIsInstance(Quartz.QCRendererEventKey, str)
        self.assertIsInstance(Quartz.QCRendererMouseLocationKey, str)

    def testProtocols(self):
        self.assertProtocolExists("QCCompositionRenderer")

    def testMethods(self):
        self.assertResultIsBOOL(TestQCRendererHelper.setValue_forInputKey_)

        self.assertResultIsBOOL(Quartz.QCRenderer.renderAtTime_arguments_)
