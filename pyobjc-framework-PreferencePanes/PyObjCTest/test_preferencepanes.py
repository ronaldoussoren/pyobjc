import objc
import PreferencePanes
from PyObjCTools.TestSupport import *


class TestPreferencePanes(TestCase):
    def testClasses(self):
        self.assertTrue(hasattr(PreferencePanes, "NSPreferencePane"))
        self.assertTrue(isinstance(PreferencePanes.NSPreferencePane, objc.objc_class))


if __name__ == "__main__":
    main()
