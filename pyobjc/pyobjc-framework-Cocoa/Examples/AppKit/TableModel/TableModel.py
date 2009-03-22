"""TableModel.py -- Minimal example showing how to use an NSTableView.

To build the demo program, run this line in Terminal.app:

    $ python setup.py py2app -A

This creates a directory "dist" containing TableModel.app. (The
-A option causes the files to be symlinked to the .app bundle instead
of copied. This means you don't have to rebuild the app if you edit the
sources or nibs.)
"""

# Or rather, this app shows how to create an object conforming to the
# NSTableDataSource protocol.  The model object is connected to the table view
# in the nib, both as the delegate and the data source.  The table view will
# ask our object for data; it controls us, not the other way around.

from PyObjCTools import AppHelper
from Cocoa import *
import pkg_resources

ROWCOUNT = 200

# class defined in MainMenu.nib
class TableModel(NSObject):
    label = objc.IBOutlet()
    tableView = objc.IBOutlet()

    # An instance of this class is connected to the 'datasource' and
    # the 'delegate' outlet of the table view in the nib.

    def awakeFromNib(self):
        self.editedFields = {}
        self.rowcount = ROWCOUNT
        # tableView is an outlet set in Interface Builder
        self.tableView.setAutosaveName_("TableView")
        self.tableView.setAutosaveTableColumns_(1)
        self.tableView.setTarget_(self)
        self.tableView.setDoubleAction_("doubleClick:")
        self.tableView.window().setDelegate_(self)

    def init(self):
        self.rowcount = ROWCOUNT
        return self

    @objc.IBAction
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

    def tableViewSelectionDidChange_(self, notification):
        # Always use this delegate method instead of using the action to do something
        # when the selection changed: the action method is only called when the selection
        # changed by means of a mouse click; this method is also called when the
        # user uses the arrow keys.
        if self.tableView.numberOfSelectedRows() == 0:
            if self.tableView.numberOfSelectedColumns() == 0:
                self.label.setStringValue_("")
            else:
                items = list(self.tableView.selectedColumnEnumerator())
                word = "Column"
        else:
            items = list(self.tableView.selectedRowEnumerator())
            word = "Row"
        label = "%s%s: %s" % (word, ("s", "")[len(items) == 1], ", ".join([str(x) for x in items]))
        self.label.setStringValue_(label)

    @objc.IBAction
    def windowShouldClose_(self, sender):
        print "Should Close?"
        return 0


AppHelper.runEventLoop()
