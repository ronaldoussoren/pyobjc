from PyObjCTools.TestSupport import *
import AppKit

class TestNSAnimationContext (TestCase):
    @min_os_level('10.7')
    def testMethods10_7(self):
        self.assertResultIsBlock(AppKit.NSAnimationContext.completionHandler, b'v')
        self.assertArgIsBlock(AppKit.NSAnimationContext.setCompletionHandler_, 0, b'v')

        self.assertArgIsBlock(AppKit.NSAnimationContext.runAnimationGroup_completionHandler_, 0, b'v@')
        self.assertArgIsBlock(AppKit.NSAnimationContext.runAnimationGroup_completionHandler_, 1, b'v')


    @min_os_level('10.8')
    def testMethods10_8(self):
        self.assertResultIsBOOL(AppKit.NSAnimationContext.allowsImplicitAnimation)
        self.assertArgIsBOOL(AppKit.NSAnimationContext.setAllowsImplicitAnimation_, 0)

if __name__ == "__main__":
    main()
