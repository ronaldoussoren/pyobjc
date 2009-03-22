from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSSpeechRecognizer (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSpeechRecognizer.listensInForegroundOnly)
        self.failUnlessResultIsBOOL(NSSpeechRecognizer.blocksOtherRecognizers)
        self.failUnlessArgIsBOOL(NSSpeechRecognizer.setListensInForegroundOnly_, 0)
        self.failUnlessArgIsBOOL(NSSpeechRecognizer.setBlocksOtherRecognizers_, 0)

if __name__ == "__main__":
    main()
