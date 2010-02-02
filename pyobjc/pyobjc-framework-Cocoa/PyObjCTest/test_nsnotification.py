from Foundation import *
from PyObjCTools.TestSupport import *

class TestNSNotification (TestCase):
    def testMethods(self):
        self.assertArgIsSEL(NSNotificationCenter.addObserver_selector_name_object_, 1, 'v@:@')

    @min_os_level('10.6')
    def testMethods10_6(self):
        self.assertArgIsBlock(NSNotificationCenter.addObserverForName_object_queue_usingBlock_, 3, 'v@')

if __name__ == "__main__":
    main()
