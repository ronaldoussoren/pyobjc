
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMImplementation (TestCase):
    def testMethods(self):
        self.assertResultIsBOOL(DOMImplementation.hasFeature_version_)
        self.assertResultIsBOOL(DOMImplementation.hasFeature__)

if __name__ == "__main__":
    main()
