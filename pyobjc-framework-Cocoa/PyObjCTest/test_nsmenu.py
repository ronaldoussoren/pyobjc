
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMenu (TestCase):
    def testMethods(self):
        self.fail("- (NSMenuItem *)insertItemWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode atIndex:(NSInteger)index;")
        self.fail("- (NSMenuItem *)addItemWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode;")

    def testConstants(self):
        self.failUnlessIsInstance(NSMenuWillSendActionNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidSendActionNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidAddItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidRemoveItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidChangeItemNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidBeginTrackingNotification, unicode)
        self.failUnlessIsInstance(NSMenuDidEndTrackingNotification, unicode)



if __name__ == "__main__":
    main()
