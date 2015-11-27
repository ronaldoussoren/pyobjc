from AppKit import *
from PyObjCTools.TestSupport import *

class TestNSUserActivity (TestCase):
    @min_os_level('10.10')
    def testConstants10_10(self):
        self.assertIsInstance(NSUserActivityDocumentURLKey, unicode)

if __name__ == "__main__":
    main()
