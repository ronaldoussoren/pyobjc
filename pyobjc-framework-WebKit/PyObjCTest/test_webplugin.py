
from PyObjCTools.TestSupport import *
from WebKit import *

class TestWebPluginHelper (NSObject):
    def webPlugInSetIsSelected_(self, v): pass

class TestWebPlugin (TestCase):
    def testMethods(self):
        self.assertArgIsBOOL(TestWebPluginHelper.webPlugInSetIsSelected_, 0)

if __name__ == "__main__":
    main()
