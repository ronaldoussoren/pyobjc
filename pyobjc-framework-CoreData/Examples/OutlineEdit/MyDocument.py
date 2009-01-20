from CoreData import *
from AppKit import *

prioritySortDescriptions = NSArray.arrayWithObject_(
        NSSortDescriptor.alloc().initWithKey_ascending_("value", True))

class MyDocument (NSPersistentDocument):
    outlineTreeController = objc.IBOutlet()

    def initWithType_error_(self, tp, error):
        self, error = super(MyDocument, self).initWithType_error_(tp, error)
        if self is None:
            return (None, error)

        managedObjectContext = self.managedObjectContext()
    
        for aPriorityValue in range(5):
            aPriority = NSEntityDescription.insertNewObjectForEntityForName_inManagedObjectContext_("Priority", managedObjectContext)
            aPriority.setValue_forKey_(aPriorityValue+1, "value")

        NSEntityDescription.insertNewObjectForEntityForName_inManagedObjectContext_("Note", managedObjectContext)

        managedObjectContext.processPendingChanges()
        managedObjectContext.undoManager().removeAllActions()
        self.updateChangeCount_(NSChangeCleared)

        return (self, None)


    def windowNibName(self):
        return "MyDocument"


    def prioritySortDescriptions(self):
        return prioritySortDescriptions
        
    def createNote_(self, sender):
        self.outlineTreeController.add_(sender)

    def createChildNote_(self, sender):
        self.outlineTreeController.addChild_(sender)

    def indentNote_(self, sender):
        selectionPath = self.outlineTreeController.selectionIndexPath()
        if not selectionPath:
            NSBeep()
            return

        selection = self.outlineTreeController.selection()

        parentNote = selection.valueForKeyPath_("parent")
        if parentNote is None:
            children = self.outlineTreeController.content()
        else:
            children  = parentNote.valueForKeyPath_("children").allObjects()

        children = children.sortedArrayUsingDescriptors_(self.outlineTreeController.sortDescriptors())

        index = selectionPath.indexAtPosition_(selectionPath.length() - 1)
        if index == 0:
            NSBeep()
        else:
            sibling = children.objectAtIndex_(index - 1)
            selection.setValue_forKeyPath_(sibling, "parent")
    
    def dedentNote_(self, sender):
        selection = self.outlineTreeController.selection()
        parent = selection.valueForKeyPath_("parent")
    
        if parent is None or parent is NSMultipleValuesMarker or parent is NSNoSelectionMarker or parent is NSNotApplicableMarker:
            NSBeep();
            return;
        
        parent = parent.valueForKeyPath_("parent")
        selection.setValue_forKeyPath_(parent, "parent")
