
from PyObjCTools.TestSupport import *
from Quartz.ImageKit import *

class TestIKFilterBrowserView (TestCase):
    def testMethods(self):
        self.failUnlessArgIsBOOL(IKFilterBrowserView.setPreviewState_, 0)

if __name__ == "__main__":
    main()
