import Cocoa
import CoreData
import objc
from objc import super

prioritySortDescriptions = Cocoa.NSArray.arrayWithObject_(
    Cocoa.NSSortDescriptor.alloc().initWithKey_ascending_("value", True)
)


class MyDocument(CoreData.NSPersistentDocument):
    outlineTreeController = objc.IBOutlet()

    def initWithType_error_(self, tp, error):
        self, error = super(MyDocument, self).initWithType_error_(tp, error)
        if self is None:
            return (None, error)

        managedObjectContext = self.managedObjectContext()

        for aPriorityValue in range(5):
            aPriority = CoreData.NSEntityDescription.insertNewObjectForEntityForName_inManagedObjectContext_(  # noqa:  B950
                "Priority", managedObjectContext
            )
            aPriority.setValue_forKey_(aPriorityValue + 1, "value")

        CoreData.NSEntityDescription.insertNewObjectForEntityForName_inManagedObjectContext_(
            "Note", managedObjectContext
        )

        managedObjectContext.processPendingChanges()
        managedObjectContext.undoManager().removeAllActions()
        self.updateChangeCount_(Cocoa.NSChangeCleared)

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
            Cocoa.NSBeep()
            return

        selection = self.outlineTreeController.selection()

        parentNote = selection.valueForKeyPath_("parent")
        if parentNote is None:
            children = self.outlineTreeController.content()
        else:
            children = parentNote.valueForKeyPath_("children").allObjects()

        children = children.sortedArrayUsingDescriptors_(
            self.outlineTreeController.sortDescriptors()
        )

        index = selectionPath.indexAtPosition_(selectionPath.length() - 1)
        if index == 0:
            Cocoa.NSBeep()
        else:
            sibling = children.objectAtIndex_(index - 1)
            selection.setValue_forKeyPath_(sibling, "parent")

    def dedentNote_(self, sender):
        selection = self.outlineTreeController.selection()
        parent = selection.valueForKeyPath_("parent")

        if parent in (
            None,
            Cocoa.NSMultipleValuesMarker,
            Cocoa.NSNoSelectionMarker,
            Cocoa.NSNotApplicableMarker,
        ):
            Cocoa.NSBeep()
            return

        parent = parent.valueForKeyPath_("parent")
        selection.setValue_forKeyPath_(parent, "parent")
