import unittest
import objc
import PreferencePanes

class TestPreferencePanes (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(PreferencePanes, 'NSPreferencePane') )
        self.assert_( isinstance(PreferencePanes.NSPreferencePane, objc.objc_class) )

    def testValues(self):
        self.assert_( hasattr(PreferencePanes, 'NSUnselectCancel') )
        self.assert_( isinstance(PreferencePanes.NSUnselectCancel, (int, long)) )
        self.assertEquals(PreferencePanes.NSUnselectCancel, 0)

        self.assert_( hasattr(PreferencePanes, 'kNSPrefPaneHelpMenuInfoPListKey') )
        self.assert_( isinstance(PreferencePanes.kNSPrefPaneHelpMenuInfoPListKey, (str, unicode)) )

        self.assertEquals(PreferencePanes.kNSPrefPaneHelpMenuInfoPListKey, u"NSPrefPaneHelpAnchors")


    def testVariables(self):
        self.assert_( hasattr(PreferencePanes, 'NSPreferencePaneDoUnselectNotification') )
        self.assert_( isinstance(PreferencePanes.NSPreferencePaneDoUnselectNotification, unicode) )

if __name__ == "__main__":
    unittest.main()
