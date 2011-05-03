import objc
import PreferencePanes
from PyObjCTools.TestSupport import *

class TestPreferencePanes (TestCase):
    def testClasses(self):
        self.assert_( hasattr(PreferencePanes, 'NSPreferencePane') )
        self.assert_( isinstance(PreferencePanes.NSPreferencePane, objc.objc_class) )

if __name__ == "__main__":
    main()
