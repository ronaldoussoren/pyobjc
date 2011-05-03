#
#  ToDosDocument.py
#  ToDos
#
#  Converted by u.fiedler on 09.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from AppKit import *

from Category import Category
from PriorityToColourTransformer import PriorityToColourTransformer
from OverdueTransformer import OverdueTransformer

class ToDosDocument(NSDocument):
    nix = objc.IBOutlet()
    toDos = objc.ivar()

    def init(self):
        self = super(ToDosDocument, self).init()
        if self is None:
            return None
        self.toDos = NSMutableArray.array()
        return self # if this line is missing you will get the 
                    # simple message: "Can't create new document"

    def categories(self):
        return Category.allCategories()

    def windowNibName(self):
        return u"ToDosDocument"

    def dataRepresentationOfType_(self, aType):
        return NSKeyedArchiver.archivedDataWithRootObject_(self.toDos)

    def loadDataRepresentation_ofType_(self, data, aType):
        self.toDos = NSKeyedUnarchiver.unarchiveObjectWithData_(data)
        return True

priorityTransformer = PriorityToColourTransformer.alloc().init()
NSValueTransformer.setValueTransformer_forName_(
    priorityTransformer, u"PriorityToColourTransformer")

overdueTransformer = OverdueTransformer.alloc().init()
NSValueTransformer.setValueTransformer_forName_(
    overdueTransformer, u"OverdueTransformer")
