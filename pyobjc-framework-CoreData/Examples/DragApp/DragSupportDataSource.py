"""
Abstract: Custom that handles Drag and Drop for table views by acting as a datasource.
"""
from Cocoa import *
import objc

class DragSupportDataSource (NSObject):
    # all the table views for which self is the datasource
    registeredTableViews = objc.ivar()

    def init(self):
        self = super(DragSupportDataSource, self).init()
        if self is None:
            return None

        self.registeredTableViews = NSMutableSet.alloc().init()
        return self;

    # ******** table view data source necessities *********

    # We use this method as a way of registering for drag types for all
    # the table views that will depend on us to implement D&D. Instead of
    # setting up innumerable outlets, simply depend on the fact that every
    # table view will ask its datasource for number of rows.
    def numberOfRowsInTableView_(self, aTableView):
        # this is potentially slow if there are lots of table views
        if not self.registeredTableViews.containsObject_(aTableView):
            aTableView.registerForDraggedTypes_([NSStringPboardType])
            #Cache the table views that have "registered" with us.
            self.registeredTableViews.addObject_(aTableView)

        # return 0 so the table view will fall back to getting data from
        # its binding
        return 0

    def tableView_objectValueForTableColumn_row_(self, aView, aColumn, rowIdx):
        # return None so the table view will fall back to getting data from
        # its binding
        return None

    # put the managedobject's ID on the pasteboard as an URL
    def tableView_writeRowsWithIndexes_toPasteboard_(self, tv, rowIndexes, pboard):
        success = False

        infoForBinding = tv.infoForBinding_(NSContentBinding)
        if infoForBinding is not None:
            arrayController = infoForBinding.objectForKey_(NSObservedObjectKey)
            objects = arrayController.arrangedObjects().objectsAtIndexes_(
                    rowIndexes)

            objectIDs = NSMutableArray.array()
            for i in xrange(objects.count()):
                item = objects[i]
                objectID = item.objectID()
                representedURL = objectID.URIRepresentation()
                objectIDs.append(representedURL)

            pboard.declareTypes_owner_([NSStringPboardType], None)
            pboard.addTypes_owner_([NSStringPboardType], None)
            success = pboard.setString_forType_(
                    objectIDs.componentsJoinedByString_(', '), NSStringPboardType)

        return success

    # *************** actual drag and drop work *****************
    def tableView_validateDrop_proposedRow_proposedDropOperation_(
            self, tableView, info, row, operation):

        # Avoid drag&drop on self. This might be interersting to enable in
        # light of ordered relationships
        if info.draggingSource() is not tableView:
            return NSDragOperationCopy
        else:
            return NSDragOperationNone

    def tableView_acceptDrop_row_dropOperation_(
            self, tableView, info, row, operation):

        success = False
        urlStrings = info.draggingPasteboard().stringForType_(NSStringPboardType)

        # get to the arraycontroller feeding the destination table view
        destinationContentBindingInfo = tableView.infoForBinding_(NSContentBinding)
        if destinationContentBindingInfo is not None:

            destinationArrayController = destinationContentBindingInfo.objectForKey_(NSObservedObjectKey)
            sourceArrayController = None

            # check for the arraycontroller feeding the source table view
            contentSetBindingInfo = destinationArrayController.infoForBinding_(NSContentSetBinding)
            if contentSetBindingInfo is not None:
                sourceArrayController = contentSetBindingInfo.objectForKey_(NSObservedObjectKey)

            # there should be exactly one item selected in the source controller, otherwise the destination controller won't be able to manipulate the relationship when we do addObject:
            if (sourceArrayController is not None) and (sourceArrayController.selectedObjects().count() == 1):
                context = destinationArrayController.managedObjectContext()
                destinationControllerEntity = NSEntityDescription.entityForName_inManagedObjectContext_(destinationArrayController.entityName(), context)

                items = urlStrings.split(', ')
                itemsToAdd = []

                for i in xrange(len(items)):
                    urlString = items[i]

                    # take the URL and get the managed object - assume
                    # all controllers using the same context
                    url = NSURL.URLWithString_(urlString)
                    objectID = context.persistentStoreCoordinator().managedObjectIDForURIRepresentation_(url)
                    if objectID is not None:
                        object = context.objectRegisteredForID_(objectID)

                        # make sure objects match the entity expected by
                        # the destination controller, and not already there
                        if object is not None and (object.entity() is destinationControllerEntity) and not (destinationArrayController.arrangedObjects().containsObject_(object)):
                            itemsToAdd.append(object)

                if len(itemsToAdd) > 0:
                    destinationArrayController.addObjects_(itemsToAdd)
                    success = True

        return success
