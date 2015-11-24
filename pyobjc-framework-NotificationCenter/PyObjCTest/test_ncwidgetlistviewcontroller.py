from PyObjCTools.TestSupport import *
import objc
import sys

if sys.maxsize > 2 ** 32:
    import NotificationCenter

    class TestNCWidgetListViewDelegateHelper (NotificationCenter.NSObject):
        def widgetList_viewControllerForRow_(self, wl, r): return 1
        def widgetList_shouldReorderRow_(self, wl, r): return 1
        def widgetList_didReorderRow_toRow_(self, wl, r, r2): pass
        def widgetList_shouldRemoveRow_(self, wl, r): return 1
        def widgetList_didRemoveRow_(self, wl, r): return 1


    class TestNCWidgetListViewController (TestCase):
        @min_os_level('10.10')
        def testClasses10_10(self):
            self.assertIsInstance(NotificationCenter.NCWidgetListViewController, objc.objc_class)

            self.assertResultIsBOOL(NotificationCenter.NCWidgetListViewController.hasDividerLines)
            self.assertArgIsBOOL(NotificationCenter.NCWidgetListViewController.setHasDividerLines_, 0)

            self.assertResultIsBOOL(NotificationCenter.NCWidgetListViewController.editing)
            self.assertArgIsBOOL(NotificationCenter.NCWidgetListViewController.setEditing_, 0)

            self.assertResultIsBOOL(NotificationCenter.NCWidgetListViewController.showsAddButtonWhenEditing)
            self.assertArgIsBOOL(NotificationCenter.NCWidgetListViewController.setShowsAddButtonWhenEditing_, 0)

            self.assertArgIsBOOL(NotificationCenter.NCWidgetListViewController.viewControllerAtRow_makeIfNecessary_, 1)

        @min_os_level('10.11')
        def testProtocols(self):
            objc.protocolNamed('NCWidgetListViewDelegate')

            self.assertArgHasType(TestNCWidgetListViewDelegateHelper.widgetList_viewControllerForRow_, 1, objc._C_NSUInteger)

            self.assertResultIsBOOL(TestNCWidgetListViewDelegateHelper.widgetList_shouldReorderRow_)
            self.assertArgHasType(TestNCWidgetListViewDelegateHelper.widgetList_shouldReorderRow_, 1, objc._C_NSUInteger)

            self.assertArgHasType(TestNCWidgetListViewDelegateHelper.widgetList_didReorderRow_toRow_, 1, objc._C_NSUInteger)
            self.assertArgHasType(TestNCWidgetListViewDelegateHelper.widgetList_didReorderRow_toRow_, 2, objc._C_NSUInteger)

            self.assertArgHasType(TestNCWidgetListViewDelegateHelper.widgetList_shouldRemoveRow_, 1, objc._C_NSUInteger)
            self.assertArgHasType(TestNCWidgetListViewDelegateHelper.widgetList_didRemoveRow_, 1, objc._C_NSUInteger)


if __name__ == "__main__":
    main()
