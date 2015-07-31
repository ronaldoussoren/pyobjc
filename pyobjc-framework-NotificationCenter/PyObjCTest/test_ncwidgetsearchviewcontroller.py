from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import NotificationCenter

    class TestNCWidgetSearchViewDelegateHelper (NotificationCenter.NSObject):
        def widgetSearch_searchForTerm_maxResults_(self, a, b, c): pass


    class TestNCWidgetSearchViewControlle (TestCase):
        @min_os_level('10.10')
        def testClasses10_10(self):
            objc.protocolNamed('NCWidgetSearchViewDelegate')

            self.assertArgHasType(TestNCWidgetSearchViewDelegateHelper.widgetSearch_searchForTerm_maxResults_,
                    2, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
