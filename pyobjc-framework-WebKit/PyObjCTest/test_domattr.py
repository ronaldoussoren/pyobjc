
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMAttr (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMAttr.specified)

if __name__ == "__main__":
    main()
