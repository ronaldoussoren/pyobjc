from Cocoa import *

RowSelectedNotification = "RowSelectedNotification"

class  SelectionNotifyMatrix (NSMatrix):
    def mouseDown_(self, theEvent):
        super(SelectionNotifyMatrix, self).mouseDown_(theEvent)

        row = self.selectedRow()
        #print "mouseDown_", theEvent, row
        if row != -1:
            NSNotificationCenter.defaultCenter(
                ).postNotificationName_object_userInfo_(
                    RowSelectedNotification,
                    self,
                    None)

    def selectCellAtRow_column_(self, row, col):
        super(SelectionNotifyMatrix, self).selectCellAtRow_column_(row, col)

        NSNotificationCenter.defaultCenter(
            ).postNotificationName_object_userInfo_(
                RowSelectedNotification,
                self,
                None)
