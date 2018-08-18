from PyObjCTools.TestSupport import *
import AppKit

class TestNSAccessibilityCustomAction (TestCase):
    @min_os_level('10.13')
    def testMethods(self):
        self.assertArgIsBlock(AppKit.NSAccessibilityCustomAction.initWithName_handler_, 1, b'Z')
        self.assertArgIsSEL(AppKit.NSAccessibilityCustomAction.initWithName_target_selector_, 2, b'Z@:')

        self.assertResultIsBlock(AppKit.NSAccessibilityCustomAction.handler, b'Z')
        self.assertArgIsBlock(AppKit.NSAccessibilityCustomAction.setHandler_, 0, b'Z')

        # XXX: Cannot describe this properly:
        # self.assertResultIsBlock(AppKit.NSAccessibilityCustomAction.selector, b'...')
        # self.assertArgIsBlock(AppKit.NSAccessibilityCustomAction.setSelector_, 0, b'...')

if __name__ == "__main__":
    main()
