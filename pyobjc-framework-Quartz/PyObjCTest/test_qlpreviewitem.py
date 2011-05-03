
from PyObjCTools.TestSupport import *
import objc

try:
    from Quartz.QuickLookUI import *

except ImportError:
    pass

class TestQLPreviewItem (TestCase):
    @min_os_level('10.6')
    def testClasses(self):
        v = objc.protocolNamed('QLPreviewItem')
        self.assertIsInstance(v, objc.formal_protocol)

if __name__ == "__main__":
    main()
