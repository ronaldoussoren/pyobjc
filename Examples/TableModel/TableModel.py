"""TableModel.py -- Minimal example showing how to use an NSTableView.

To build the demo program, run this line in Terminal.app:

    $ python buildapp.py --link build

This creates a directory "build" containing TableModel.app. (The --link option
causes the files to be symlinked to the .app bundle instead of copied. This
means you don't have to rebuild the app if you edit the sources or nibs.)
"""

# Or rather, this app shows how to create an object conforming to the
# NSTableDataSource protocol.  The model object is connected to the table view
# in the nib, both as the delegate and the data source.  The table view will
# ask our object for data; it controls us, not the other way around.

from PyObjCTools import NibClassBuilder, AppHelper

NibClassBuilder.extractClasses("MainMenu")

ROWCOUNT = 200

# class defined in MainMenu.nib
class PyModel(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSObject
    # The following outlets are added to the class:
    # tableView

    def awakeFromNib(self):
        self.editedFields = {}
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
        return self.editedFields.get((aTableColumn, rowIndex),
            "{%s, %d}" % (col, rowIndex))

    def tableView_setObjectValue_forTableColumn_row_(
            self, aTableView, anObject, aTableColumn, rowIndex):
        self.editedFields[(aTableColumn, rowIndex)] = anObject

    # delegate methods
    def tableView_shouldSelectRow_(self, aTableView, rowIndex):
        # only allow odd rows to be selected
        return rowIndex % 2

    def tableView_shouldEditTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        # only allow cells in the second column in odd rows to be edited
        return (rowIndex % 2) and aTableColumn.identifier() == "col_2"


AppHelper.runEventLoop()
