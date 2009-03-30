from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSNotification (TestCase):
    def testMethods(self):
        self.failUnlessArgIsSEL(NSNotificationCenter.addObserver_selector_name_object_, 1, 'v@:@')

if __name__ == "__main__":
    main()
