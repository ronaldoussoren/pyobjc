
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMStyleSheet (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMStyleSheet.disabled)
        self.failUnlessArgIsBOOL(DOMStyleSheet.setDisabled_, 0)

if __name__ == "__main__":
    main()
