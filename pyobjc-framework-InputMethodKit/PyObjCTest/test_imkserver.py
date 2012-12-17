
from PyObjCTools.TestSupport import *
from InputMethodKit import *

try:
    unicode
except NameError:
    unicode = str

class TestIMKServer (TestCase):
    @expectedFailure
    def testBrokenConstants(self):
        # The definitions below are defined on 10.5, but not actually
        # exported by the framework.
        #
        # See also: Radar #6783035
        self.assertIsInstance(IMKDelegateClass, unicode)
        self.assertIsInstance(IMKControllerClass, unicode)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBOOL(IMKServer.paletteWillTerminate)
        self.assertResultIsBOOL(IMKServer.lastKeyEventWasDeadKey)


if __name__ == "__main__":
    main()
