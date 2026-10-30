import InputMethodKit
from PyObjCTools.TestSupport import TestCase


class TestIMKServer(TestCase):
    def test_constants(self):
        self.assertIsInstance(InputMethodKit.IMKModeDictionary, str)
        self.assertIsInstance(InputMethodKit.IMKDelegateClass, str)
        self.assertIsInstance(InputMethodKit.IMKControllerClass, str)

    def test_methods(self):
        self.assertResultIsBOOL(InputMethodKit.IMKServer.new().paletteWillTerminate)
        self.assertResultIsBOOL(InputMethodKit.IMKServer.new().lastKeyEventWasDeadKey)
