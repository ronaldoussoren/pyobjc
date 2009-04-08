#
#  BookmarksDocument.py
#  Bookmarks
#
#  Converted by u.fiedler on 10.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

import objc
from Cocoa import *

# BookmarksDocument defines this as it may be used for copy and paste
# in addition to just drag and drop
CopiedRowsType = u"COPIED_ROWS_TYPE"

class BookmarksDocument (NSDocument):
    bookmarksArray = objc.ivar('bookmarksArray')

    def init(self):
        self = super(BookmarksDocument, self).init()
        if self is None:
            return None
        self.bookmarksArray = NSMutableArray.array()
        return self

    def windowNibName(self):
        return u"BookmarksDocument"

    # Straightforward, standard document class
    # Allows content array to be saved, and file opened
    # Provides accessor methods for bookmarksArray

    # open and save -- very simple, just (un)archive bookmarksArray
    def dataRepresentationOfType_(self, aType):
        return NSKeyedArchiver.archivedDataWithRootObject_(self.bookmarksArray)
        
    def loadDataRepresentation_ofType_(self, data, aType):
        self.bookmarksArray = NSKeyedUnarchiver.unarchiveObjectWithData_(data)
        return True
