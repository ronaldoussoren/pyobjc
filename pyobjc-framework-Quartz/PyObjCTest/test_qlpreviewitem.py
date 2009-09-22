
from PyObjCTools.TestSupport import *
import objc

try:
    from Quartz.QuickLookUI import *

except ImportError:
    pass

class TestQLPreviewItem (TestCase):
    @min_os_level('10.6')
    def testClasses(self):
        self.failUnlessIsInstance(QLPreviewItem, objc.objc_class)

if __name__ == "__main__":
    main()
