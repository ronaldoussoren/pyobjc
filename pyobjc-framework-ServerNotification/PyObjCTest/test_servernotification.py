'''
Some simple tests to check that the framework is properly wrapped.
'''
from PyObjCTools.TestSupport import *
from ServerNotification import *

class TestServerNotification (TestCase):
    def testClasses(self):
        self.assertArgIsSEL(NSServerNotificationCenter.addObserver_selector_name_object_, 1, b'v@:@')


if __name__ == "__main__":
    unittest.main()

