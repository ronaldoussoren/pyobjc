#
#  DNDArrayController.py
#  Bookmarks
#
#  Converted by u.fiedler on 10.02.05.
#
#  The original version was written in Objective-C by Malcolm Crawford
#  at http://homepage.mac.com/mmalc/CocoaExamples/controllers.html
#
#  See "Dragging Files" for a conceptual introduction:
#  file:///Developer/ADC%20Reference%20Library/documentation/Cocoa/Conceptual/DragandDrop/index.html#//apple_ref/doc/uid/10000069i
#  or http://developer.apple.com/documentation/Cocoa/Conceptual/DragandDrop/Tasks/DraggingFiles.html


from Foundation import *
from AppKit import *
from BookmarksDocument import CopiedRowsType

MovedRowsType = u"MOVED_ROWS_TYPE"

class DNDArrayController (NSArrayController):
    # DNDArrayController is delegate and dataSource of tableView
    tableView = objc.IBOutlet()

    def awakeFromNib(self):
        "register for drag and drop"
        self.tableView.registerForDraggedTypes_(
            [CopiedRowsType, MovedRowsType, NSURLPboardType])
        self.tableView.setAllowsMultipleSelection_(True)


    def tableView_writeRows_toPasteboard_(self, tv, rows, pboard):
        # declare our own pasteboard types
        typesArray = [CopiedRowsType, MovedRowsType]

        # If the number of rows is not 1, then we only support our own types.
        # If there is just one row, then try to create an NSURL from the url
        # value in that row.  If that's possible, add NSURLPboardType to the
        # list of supported types, and add the NSURL to the pasteboard.
        if len(rows) != 1:
            pboard.declareTypes_owner_(typesArray, self)
        else:
            # Try to create an URL
            # If we can, add NSURLPboardType to the declared types and write
            # the URL to the pasteboard; otherwise declare existing types
            row = rows[0]
            urlString = self.arrangedObjects()[row].valueForKey_(u'url')
            url = None
            if urlString:
                url = NSURL.URLWithString_(urlString)
            if urlString and url:
                typesArray.append(NSURLPboardType)
                pboard.declareTypes_owner_(typesArray, self)
                url.writeToPasteboard_(pboard)
            else:
                pboard.declareTypes_owner_(typesArray, self)

        # add rows array for local move
        pboard.setPropertyList_forType_(rows, MovedRowsType)

        # create new array of selected rows for remote drop
        # could do deferred provision, but keep it direct for clarity
        rowCopies = self.arrangedObjects()[:]

        # setPropertyList works here because we're using dictionaries, strings,
        # and dates; otherwise, archive collection to NSData...
        pboard.setPropertyList_forType_(rowCopies, CopiedRowsType)
        return True

    def tableView_validateDrop_proposedRow_proposedDropOperation_(self, tv, info, row, op):
        dragOp = NSDragOperationCopy
        # if drag source is self, it's a move
        if info.draggingSource() == self.tableView:
            dragOp =  NSDragOperationMove
        # we want to put the object at, not over,
        # the current row (contrast NSTableViewDropOn)
        tv.setDropRow_dropOperation_(row, NSTableViewDropAbove)
        return dragOp

    def tableView_acceptDrop_row_dropOperation_(self, tv, info, row, op):
        if row < 0:
            row = 0
        if info.draggingSource() == self.tableView:
            rows = info.draggingPasteboard().propertyListForType_(MovedRowsType)
            indexSet = self.indexSetFromRows_(rows)
            self.moveObjectsInArrangedObjectsFromIndexes_toIndex_(indexSet, row)
            # set selected rows to those that were just moved
            # Need to work out what moved where to determine proper selection...
            rowsAbove = self.rowsAboveRow_inIndexSet_(row, indexSet)
            aRange = NSMakeRange(row - rowsAbove, indexSet.count())
            indexSet = NSIndexSet.indexSetWithIndexesInRange_(aRange)
            # set selected rows to those that were just copied
            self.setSelectionIndexes_(indexSet)
            return True

        # Can we get rows from another document?  If so, add them, then return.
        newRows = info.draggingPasteboard().propertyListForType_(CopiedRowsType)
        if newRows:
            aRange = NSMakeRange(row, newRows.count())
            indexSet = NSIndexSet.indexSetWithIndexesInRange_(aRange)
            self.insertObjects_atArrangedObjectIndexes_(newRows, indexSet)
            self.setSelectionIndexes_(indexSet)
            return True

        # Can we get an URL?  If so, add a new row, configure it, then return.
        url = NSURL.URLFromPasteboard_(info.draggingPasteboard())
        if url:
            newObject = self.newObject()
            self.insertObject_atArrangedObjectIndex_(newObject, row)
            newObject.setValue_forKey_(url.absoluteString(), u"url")
            newObject.setValue_forKey_(NSCalendarDate.date(), u"date")
            # set selected rows to those that were just copied
            self.setSelectionIndex_(row)
            return True
        return False

    def moveObjectsInArrangedObjectsFromIndexes_toIndex_(self, indexSet, insertIndex):
        objects = self.arrangedObjects()
        index = indexSet.lastIndex()
        aboveInsertIndexCount = 0
        removeIndex = 0

        while index != NSNotFound:
            if index >= insertIndex:
                removeIndex = index + aboveInsertIndexCount
                aboveInsertIndexCount += 1
            else:
                removeIndex = index
                insertIndex -= 1
            obj = objects.objectAtIndex_(removeIndex)
            self.removeObjectAtArrangedObjectIndex_(removeIndex)
            self.insertObject_atArrangedObjectIndex_(obj, insertIndex)
            index = indexSet.indexLessThanIndex_(index)

    def indexSetFromRows_(self, rows):
        indexSet = NSMutableIndexSet.indexSet()
        for row in rows:
            indexSet.addIndex_(row)
        return indexSet

    def rowsAboveRow_inIndexSet_(self, row, indexSet):
        currentIndex = indexSet.firstIndex()
        i = 0
        while currentIndex != NSNotFound:
            if currentIndex < row:
                i += 1
            currentIndex = indexSet.indexGreaterThanIndex_(currentIndex)
        return i
