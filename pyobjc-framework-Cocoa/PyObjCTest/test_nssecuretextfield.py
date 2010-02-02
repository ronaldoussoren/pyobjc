from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSecureTextFieldCell (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(NSSecureTextFieldCell.echosBullets)
        self.assertArgIsBOOL(NSSecureTextFieldCell.setEchosBullets_, 0)

if __name__ == "__main__":
    main()
