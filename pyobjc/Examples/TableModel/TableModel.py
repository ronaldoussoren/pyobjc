from Foundation import NSObject
from AppKit import NSApplicationMain, NSTableDataSource
from AppKit.NibClassBuilder import extractClasses, AutoBaseClass
from objc import selector
import sys

extractClasses("MainMenu")


ROWCOUNT = 200


class PyModel(AutoBaseClass, NSTableDataSource):

	def awakeFromNib(self):
		self.rowcount = ROWCOUNT
		return self

	def init(self):
		self.rowcount = ROWCOUNT
		return self

	def numberOfRowsInTableView_(self, aTableView):
		#print "numerOfRowsInTableView: called"
		return self.rowcount


	def tableView_objectValueForTableColumn_row_(self, 
			aTableView, aTableColumn, rowIndex):
		#print "tableView:objectValueForTableColumn:row: called"
		return "{%s, %d}" % (aTableColumn.identifier(), rowIndex)



sys.exit(NSApplicationMain(sys.argv))
