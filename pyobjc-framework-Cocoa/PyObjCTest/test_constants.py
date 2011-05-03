from PyObjCTools.TestSupport import *
import AppKit
import objc

class ContantTest (TestCase):

    def testNSFloatingWindowLevel(self):
        # NSFloatingWindowLevel is a define in Objective-C, up-to 1.0rc1
        # we didn't correctly pick up this define due to a bug in the code.
        self.assert_(hasattr(AppKit, 'NSFloatingWindowLevel'))
        self.assert_(isinstance(AppKit.NSFloatingWindowLevel, int))

    def testNSAnyEventMask(self):
        self.assertEqual(AppKit.NSAnyEventMask, -1)

    def testNSViewFrameDidChangeNotification(self):
        self.assert_(hasattr(AppKit, 'NSViewFrameDidChangeNotification'))
        self.assert_(isinstance(AppKit.NSViewFrameDidChangeNotification, unicode))

    def testNSUpArrowFunctionKey(self):
        self.assert_(hasattr(AppKit, 'NSUpArrowFunctionKey'))
        self.assert_(isinstance(AppKit.NSUpArrowFunctionKey, unicode))

if __name__ == "__main__":
    main()
