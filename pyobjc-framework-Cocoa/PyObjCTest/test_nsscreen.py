
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScreen (TestCase):
    def testMethods(self):
        m = NSScreen.supportedWindowDepths.__metadata__()
        self.failUnless(m['retval']['c_array_delimited_by_null'])

if __name__ == "__main__":
    main()
