
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSScreen (TestCase):
    def testMethods(self):
        m = NSScreen.supportedWindowDepths.__metadata__()
        self.assertTrue(m['retval']['c_array_delimited_by_null'])

    @min_os_level('10.6')
    def testConstants10_6(self):
        self.assertIsInstance(NSScreenColorSpaceDidChangeNotification, unicode)

    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultHasType(NSScreen.convertRectToBacking_, NSRect.__typestr__)
        self.assertArgHasType(NSScreen.convertRectToBacking_, 0, NSRect.__typestr__)
        self.assertResultHasType(NSScreen.convertRectFromBacking_, NSRect.__typestr__)
        self.assertArgHasType(NSScreen.convertRectFromBacking_, 0, NSRect.__typestr__)
        self.assertResultHasType(NSScreen.backingAlignedRect_options_, NSRect.__typestr__)
        self.assertArgHasType(NSScreen.backingAlignedRect_options_, 0, NSRect.__typestr__)

    @min_os_level('10.9')
    def testMethods10_9(self):
        self.assertResultIsBOOL(NSScreen.screensHaveSeparateSpaces)

    @min_os_level('10.12')
    def testMethods10_12(self):
        self.assertResultIsBOOL(NSScreen.canRepresentDisplayGamut_)

if __name__ == "__main__":
    main()
