import AppKit
from PyObjCTools.TestSupport import TestCase, min_sdk_level


class TestNSSpeechRecognizer(TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(AppKit.NSSpeechRecognizer.listensInForegroundOnly)
        self.assertResultIsBOOL(AppKit.NSSpeechRecognizer.blocksOtherRecognizers)
        self.assertArgIsBOOL(AppKit.NSSpeechRecognizer.setListensInForegroundOnly_, 0)
        self.assertArgIsBOOL(AppKit.NSSpeechRecognizer.setBlocksOtherRecognizers_, 0)

    @min_sdk_level("10.10")
    def testProtocols(self):
        self.assertProtocolExists("NSSpeechRecognizerDelegate")
