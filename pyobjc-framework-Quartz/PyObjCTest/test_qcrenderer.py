from PyObjCTools.TestSupport import TestCase
import Quartz


class TestQCRendererHelper(Quartz.NSObject):
    def setValue_forInputKey_(self, v, k):
        return 1


class TestQCRenderer(TestCase):
    def test_constants(self):
        self.assertIsInstance(Quartz.QCRendererEventKey, str)
        self.assertIsInstance(Quartz.QCRendererMouseLocationKey, str)

    def test_methods(self):
        self.assertResultIsBOOL(Quartz.QCRenderer.renderAtTime_arguments_)

    def test_protocols(self):
        self.assertProtocolExists("QCCompositionRenderer", Quartz)

    def test_protocol_methods(self):
        self.assertResultIsBOOL(TestQCRendererHelper.setValue_forInputKey_)
