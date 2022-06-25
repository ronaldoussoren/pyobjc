from PyObjCTools.TestSupport import TestCase, min_os_level
import objc
import NotificationCenter


class TestNCWidgetSearchViewDelegateHelper(NotificationCenter.NSObject):
    def widgetSearch_searchForTerm_maxResults_(self, a, b, c):
        pass


class TestNCWidgetSearchViewControlle(TestCase):
    @min_os_level("10.10")
    def testClasses10_10(self):
        self.assertProtocolExists("NCWidgetSearchViewDelegate")

    def test_protocol_methods(self):
        self.assertArgHasType(
            TestNCWidgetSearchViewDelegateHelper.widgetSearch_searchForTerm_maxResults_,
            2,
            objc._C_NSUInteger,
        )
