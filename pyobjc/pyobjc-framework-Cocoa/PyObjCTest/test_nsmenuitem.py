
from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSMenuItem (TestCase):
    def testMethods(self):
        self.fail("- (id)initWithTitle:(NSString *)aString action:(SEL)aSelector keyEquivalent:(NSString *)charCode;")


if __name__ == "__main__":
    main()
