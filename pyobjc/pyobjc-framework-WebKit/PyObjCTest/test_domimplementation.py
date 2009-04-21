
from PyObjCTools.TestSupport import *
from WebKit import *

class TestDOMImplementation (TestCase):
    def testMethods(self):
        self.failUnlessResultIsBOOL(DOMImplementation.hasFeature_version_)
        self.failUnlessResultIsBOOL(DOMImplementation.hasFeature__)

if __name__ == "__main__":
    main()
