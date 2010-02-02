from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSSpeechRecognizer (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSSpeechRecognizer.listensInForegroundOnly)
        self.assertResultIsBOOL(NSSpeechRecognizer.blocksOtherRecognizers)
        self.assertArgIsBOOL(NSSpeechRecognizer.setListensInForegroundOnly_, 0)
        self.assertArgIsBOOL(NSSpeechRecognizer.setBlocksOtherRecognizers_, 0)

if __name__ == "__main__":
    main()
