from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSecureTextFieldCell (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(NSSecureTextFieldCell.echosBullets)
        self.failUnlessArgIsBOOL(NSSecureTextFieldCell.setEchosBullets_, 0)

if __name__ == "__main__":
    main()
