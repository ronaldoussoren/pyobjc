from Foundation import NSObject
from AppKit import NSApplicationMain, NSTableDataSource, NSTableViewDelegate
from PyObjCTools import NibClassBuilder, AppHelper
from objc import selector
import sys

NibClassBuilder.extractClasses("MainMenu")

ROWCOUNT = 200

class PyModel(NibClassBuilder.AutoBaseClass, NSTableDataSource, NSTableViewDelegate):

    def awakeFromNib(self):
        self.stuff = {}
        self.rowcount = ROWCOUNT
        return self


    def init(self):
        self.rowcount = ROWCOUNT
        return self


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

    def tableView_shouldSelectRow_(self, aTableView, rowIndex):
        print "shouldSelectRow_", rowIndex
        return (rowIndex % 2)

AppHelper.runEventLoop()
