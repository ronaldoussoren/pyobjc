import InputMethodKit
from PyObjCTools.TestSupport import TestCase, min_os_level, expectedFailure


class TestIMKServer(TestCase):
    @expectedFailure
    def testBrokenConstants(self):
        # The definitions below are defined on 10.5, but not actually
        # exported by the framework.
        #
        # See also: Radar #6783035
        self.assertIsInstance(InputMethodKit.IMKModeDictionary, str)
        self.assertIsInstance(InputMethodKit.IMKDelegateClass, str)
        self.assertIsInstance(InputMethodKit.IMKControllerClass, str)

    @min_os_level("10.7")
    def testMethods10_7(self):
        self.assertResultIsBOOL(InputMethodKit.IMKServer.paletteWillTerminate)
        self.assertResultIsBOOL(InputMethodKit.IMKServer.lastKeyEventWasDeadKey)
