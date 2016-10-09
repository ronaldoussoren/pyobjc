from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSLayoutGuide (TestCase):
    @min_os_level('10.12')
    def testMethods(self):
        self.assertResultIsBOOL(NSLayoutGuide.hasAmbiguousLayout)

if __name__ == "__main__":
    main()
