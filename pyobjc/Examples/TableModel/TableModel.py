from Foundation import NSObject
from AppKit import NSApplicationMain, NSTableDataSource, NSTableViewDelegate
from PyObjCTools import NibClassBuilder, AppHelper
from objc import selector
import sys

NibClassBuilder.extractClasses("MainMenu")

ROWCOUNT = 200

class PyModel(NibClassBuilder.AutoBaseClass):

    def awakeFromNib(self):
        self.stuff = {}
        self.rowcount = ROWCOUNT
        # tableView is an outlet set in Interface Builder
        self.tableView.setTarget_(self)
        self.tableView.setDoubleAction_("doubleClick:")
        # this also works, but you still need to set the target:
        #self.tableView.setDoubleAction_(self.doubleClick_)

    def init(self):
        self.rowcount = ROWCOUNT
        return self

    def doubleClick_(self, sender):
        # double-clicking a column header causes clickedRow() to return -1
        print "doubleClick!", sender.clickedColumn(), sender.clickedRow()

    # data source methods
    def numberOfRowsInTableView_(self, aTableView):
        return self.rowcount

    def tableView_objectValueForTableColumn_row_(
            self, aTableView, aTableColumn, rowIndex):
        col = aTableColumn.identifier()
        return self.stuff.get((aTableColumn, rowIndex),
            "{%s, %d}" % (col, rowIndex))

    def tableView_setObjectValue_forTableColumn_row_(
            self, aTableView, anObject, aTableColumn, rowIndex):
        col = aTableColumn.identifier()
        self.stuff[(aTableColumn, rowIndex)] = anObject

    # delegate methods
    def tableView_shouldSelectRow_(self, aTableView, rowIndex):
        print "shouldSelectRow_", rowIndex
        # only allow odd rows to be selected
        return rowIndex % 2

    def tableView_shouldEditTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        # only allow cells in the second column in odd rows to be edited
        return (rowIndex % 2) and aTableColumn.identifier() == "col_2"


AppHelper.runEventLoop()
