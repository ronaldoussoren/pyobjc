# THIS FILE IS GENERATED. DO NOT EDIT!!!
# Interface classes for using NIB files

from objc import IBOutlet
from Foundation import NSObject

class ClassesDataSourceBase (NSObject):
	"Base class for class 'ClassesDataSource'"
	classLabel = IBOutlet("classLabel")
	classTable = IBOutlet("classTable")
	searchBox = IBOutlet("searchBox")
	frameworkLabel = IBOutlet("frameworkLabel")
	methodTable = IBOutlet("methodTable")
	window = IBOutlet("window")

	def selectClass_(self, sender): pass

	def searchClass_(self, sender): pass


