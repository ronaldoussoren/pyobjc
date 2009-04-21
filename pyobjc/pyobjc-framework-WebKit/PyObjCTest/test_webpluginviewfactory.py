
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPluginViewFactory (TestCase):
    def testConstants(self):
        self.failUnlessIsInstance(WebPlugInBaseURLKey, unicode)
        self.failUnlessIsInstance(WebPlugInAttributesKey, unicode)
        self.failUnlessIsInstance(WebPlugInContainerKey, unicode)
        self.failUnlessIsInstance(WebPlugInContainingElementKey, unicode)

if __name__ == "__main__":
    main()
