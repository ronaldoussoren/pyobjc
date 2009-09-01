'''
Some simple tests to check that the framework is properly wrapped.
'''
from PyObjCTools.TestSupport import *
from ServerNotification import *

class TestServerNotification (TestCase):
    def testClasses(self):
        self.failUnlessArgIsSEL(NSServerNotificationCenter.addObserver_selector_name_object_, 1, 'v@:@')


if __name__ == "__main__":
    unittest.main()

