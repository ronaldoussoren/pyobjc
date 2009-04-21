
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPluginHelper (NSObject):
    def webPlugInSetIsSelected_(self, v): pass

class TestWebPlugin (TestCase):
    def testConstants(self):
        self.failUnlessArgIsBOOL(TestWebPluginHelper.webPlugInSetIsSelected_, 0)

if __name__ == "__main__":
    main()
