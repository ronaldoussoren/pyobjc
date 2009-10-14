
from PyObjCTools.TestSupport import *
from Quartz import *

class TestIKFilterBrowserView (TestCase):
    @min_os_level('10.5')
    def testMethods(self):
        self.failUnlessArgIsBOOL(IKFilterBrowserView.setPreviewState_, 0)

if __name__ == "__main__":
    main()
