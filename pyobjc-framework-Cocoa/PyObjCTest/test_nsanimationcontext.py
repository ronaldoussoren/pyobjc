from PyObjCTools.TestSupport import *
import AppKit

class TestNSAnimationContext (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBlock(AppKit.NSAnimationContext.completionHandler, b'v')
        self.assertArgIsBlock(AppKit.NSAnimationContext.setCompletionHandler_, 0, b'v')

if __name__ == "__main__":
    main()
