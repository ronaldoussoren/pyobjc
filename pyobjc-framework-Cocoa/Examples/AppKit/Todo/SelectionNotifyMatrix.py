from objc import super
import Cocoa

RowSelectedNotification = "RowSelectedNotification"

class  SelectionNotifyMatrix (Cocoa.NSMatrix):
    def mouseDown_(self, theEvent):
        super(SelectionNotifyMatrix, self).mouseDown_(theEvent)

        row = self.selectedRow()
        if row != -1:
            Cocoa.NSNotificationCenter.defaultCenter(
                ).postNotificationName_object_userInfo_(
                    RowSelectedNotification,
                    self,
                    None)

    def selectCellAtRow_column_(self, row, col):
        super(SelectionNotifyMatrix, self).selectCellAtRow_column_(row, col)

        Cocoa.NSNotificationCenter.defaultCenter(
            ).postNotificationName_object_userInfo_(
                RowSelectedNotification,
                self,
                None)
