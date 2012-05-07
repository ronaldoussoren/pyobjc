from PyObjCTools.TestSupport import *
import AppKit

class TestNSAnimationContext (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBlock(AppKit.NSAnimationContext.completionHandler, 'v')
        self.assertArgIsBlock(AppKit.NSAnimationContext.setCompletionHandler_, 0, 'v')

if __name__ == "__main__":
    main()
