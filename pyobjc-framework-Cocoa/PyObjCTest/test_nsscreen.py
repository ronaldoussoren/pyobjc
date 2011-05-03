
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScreen (TestCase):
    def testMethods(self):
        m = NSScreen.supportedWindowDepths.__metadata__()
        self.assertTrue(m['retval']['c_array_delimited_by_null'])

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSScreenColorSpaceDidChangeNotification, unicode)

if __name__ == "__main__":
    main()
