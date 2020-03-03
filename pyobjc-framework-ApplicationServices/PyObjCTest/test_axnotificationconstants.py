import HIServices
from PyObjCTools.TestSupport import TestCase


class TestAXNotificationConstants(TestCase):
    def testConstants(self):
        self.assertEqual(
            HIServices.kAXFocusedWindowChangedNotification, "AXFocusedWindowChanged"
        )
        self.assertEqual(
            HIServices.kAXFocusedUIElementChangedNotification,
            "AXFocusedUIElementChanged",
        )
        self.assertEqual(
            HIServices.kAXApplicationActivatedNotification, "AXApplicationActivated"
        )
        self.assertEqual(
            HIServices.kAXApplicationDeactivatedNotification, "AXApplicationDeactivated"
        )
        self.assertEqual(
            HIServices.kAXApplicationHiddenNotification, "AXApplicationHidden"
        )
        self.assertEqual(
            HIServices.kAXApplicationShownNotification, "AXApplicationShown"
        )
        self.assertEqual(HIServices.kAXWindowCreatedNotification, "AXWindowCreated")
        self.assertEqual(HIServices.kAXWindowMovedNotification, "AXWindowMoved")
        self.assertEqual(HIServices.kAXWindowResizedNotification, "AXWindowResized")
        self.assertEqual(
            HIServices.kAXWindowMiniaturizedNotification, "AXWindowMiniaturized"
        )
        self.assertEqual(
            HIServices.kAXWindowDeminiaturizedNotification, "AXWindowDeminiaturized"
        )
        self.assertEqual(HIServices.kAXDrawerCreatedNotification, "AXDrawerCreated")
        self.assertEqual(HIServices.kAXSheetCreatedNotification, "AXSheetCreated")
        self.assertEqual(HIServices.kAXHelpTagCreatedNotification, "AXHelpTagCreated")
        self.assertEqual(HIServices.kAXValueChangedNotification, "AXValueChanged")
        self.assertEqual(
            HIServices.kAXUIElementDestroyedNotification, "AXUIElementDestroyed"
        )
        self.assertEqual(
            HIServices.kAXElementBusyChangedNotification, "AXElementBusyChanged"
        )
        self.assertEqual(HIServices.kAXMenuOpenedNotification, "AXMenuOpened")
        self.assertEqual(HIServices.kAXMenuClosedNotification, "AXMenuClosed")
        self.assertEqual(
            HIServices.kAXMenuItemSelectedNotification, "AXMenuItemSelected"
        )
        self.assertEqual(HIServices.kAXRowCountChangedNotification, "AXRowCountChanged")
        self.assertEqual(HIServices.kAXRowExpandedNotification, "AXRowExpanded")
        self.assertEqual(HIServices.kAXRowCollapsedNotification, "AXRowCollapsed")
        self.assertEqual(
            HIServices.kAXSelectedCellsChangedNotification, "AXSelectedCellsChanged"
        )
        self.assertEqual(HIServices.kAXUnitsChangedNotification, "AXUnitsChanged")
        self.assertEqual(
            HIServices.kAXSelectedChildrenMovedNotification, "AXSelectedChildrenMoved"
        )
        self.assertEqual(
            HIServices.kAXSelectedChildrenChangedNotification,
            "AXSelectedChildrenChanged",
        )
        self.assertEqual(HIServices.kAXResizedNotification, "AXResized")
        self.assertEqual(HIServices.kAXMovedNotification, "AXMoved")
        self.assertEqual(HIServices.kAXCreatedNotification, "AXCreated")
        self.assertEqual(
            HIServices.kAXSelectedRowsChangedNotification, "AXSelectedRowsChanged"
        )
        self.assertEqual(
            HIServices.kAXSelectedColumnsChangedNotification, "AXSelectedColumnsChanged"
        )
        self.assertEqual(
            HIServices.kAXSelectedTextChangedNotification, "AXSelectedTextChanged"
        )
        self.assertEqual(HIServices.kAXTitleChangedNotification, "AXTitleChanged")
        self.assertEqual(HIServices.kAXLayoutChangedNotification, "AXLayoutChanged")
        self.assertEqual(
            HIServices.kAXAnnouncementRequestedNotification, "AXAnnouncementRequested"
        )
        self.assertEqual(HIServices.kAXUIElementsKey, "AXUIElementsKey")
        self.assertEqual(HIServices.kAXPriorityKey, "AXPriorityKey")
        self.assertEqual(HIServices.kAXAnnouncementKey, "AXAnnouncementKey")
        self.assertEqual(HIServices.kAXUIElementTitleKey, "AXUIElementTitleKey")

        self.assertEqual(HIServices.kAXPriorityLow, 10)
        self.assertEqual(HIServices.kAXPriorityMedium, 50)
        self.assertEqual(HIServices.kAXPriorityHigh, 90)
