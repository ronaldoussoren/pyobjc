from AppKit import *
from Quartz import *
import objc

from PyObjCTools import NibClassBuilder

class MyPDFDocument (NibClassBuilder.AutoBaseClass):
    _outline        = objc.ivar()
    _searchResults  = objc.ivar()


    def dealloc(self):
        NSNotificationCenter.defaultCenter().removeObserver_(self)
        self._searchResults = None
        super(MyPDFDocument, self).dealloc()

    def windowNibName(self):
        return "MyDocument"

    def windowControllerDidLoadNib_(self, controller):
        super(MyPDFDocument, self).windowControllerDidLoadNib_(controller)

        if self.fileName():
            pdfDoc = PDFDocument.alloc().initWithURL_(
                    NSURL.fileURLWithPath_(self.fileName()))
            self._pdfView.setDocument_(pdfDoc)

        # Page changed notification.
        NSNotificationCenter.defaultCenter().addObserver_selector_name_object_(
                self, "pageChanged:", PDFViewPageChangedNotification, self._pdfView)

        # Find notifications.
        center = NSNotificationCenter.defaultCenter()
        center.addObserver_selector_name_object_(
                self, 'startFind:', PDFDocumentDidBeginFindNotification,
                self._pdfView.document())
        center.addObserver_selector_name_object_(
                self, 'findProgress:', PDFDocumentDidEndPageFindNotification,
                self._pdfView.document())
        center.addObserver_selector_name_object_(
                self, 'endFind:', PDFDocumentDidEndFindNotification,
                self._pdfView.document())

        # Set self to be delegate (find).
        self._pdfView.document().setDelegate_(self)

        # Get outline.
        self._outline = self._pdfView.document().outlineRoot()
        if self._outline is not None:
            # Remove text that says, "No outline."
            self._noOutlineText.removeFromSuperview()
            self._noOutlineText = None

            # Force it to load up.
            self._outlineView.reloadData()

        else:
            # Remove outline view (leaving instead text that says,
            # "No outline.").
            self._outlineView.enclosingScrollView().removeFromSuperview()
            self._outlineView = None

        # Open drawer.
        self._drawer.open()

        # Size the window.
        windowSize = self._pdfView.rowSizeForPage_(
                self._pdfView.currentPage())

        if (self._pdfView.displayMode() & 0x01) and (
                    self._pdfView.document().pageCount() > 1):
            windowSize.width +=  NSScroller.scrollerWidth()
        controller.window().setContentSize_(windowSize)

    def dataRepresentationOfType_(self, aType):
        return None

    def loadDataRepresentation_ofType_(self, data, aType):
        return True

    @objc.IBAction
    def toggleDrawer_(self, sender):
        self._drawer.toggle_(self)

    @objc.IBAction
    def takeDestinationFromOutline_(self, sender):
        # Get the destination associated with the search result list.
        # Tell the PDFView to go there.
        self._pdfView.goToDestination_(
                sender.itemAtRow_(sender.selectedRow()).destination())

    @objc.IBAction
    def displaySinglePage_(self, sender):
        # Display single page mode.
        if self._pdfView.displayMode() > kPDFDisplaySinglePageContinuous:
            self._pdfView.setDisplayMode_(self._pdfView.displayMode() - 2)

    @objc.IBAction
    def displayTwoUp_(self, sender):
        #  Display two-up.
        if self._pdfView.displayMode() < kPDFDisplayTwoUp:
            self._pdfView.setDisplayMode_(self._pdfView.displayMode() + 2)

    def pageChanged_(self, notification):
        # Skip out if there is no outline.
        if selfl_pdfView.document().outlineRoot() is None:
            return

        # What is the new page number (zero-based).
        newPageIndex = self._pdfView.document().indexForPage_(
                self._pdfView.currentPage())

        # Walk outline view looking for best firstpage number match.
        newlySelectedRow = -1;
        numRows = self._outlineView.numberOfRows()
        for i in range(numRows):
            outlineItem = self._outlineView.itemAtRow_(i)

            if self._pdfView.document().indexForPage_(
                    outlineItem.destination().page()) == newPageIndex:

                newlySelectedRow = i
                self._outlineView.selectRow_byExtendingSelection_(
                        newlySelectedRow, False)
                break

            elif self._pdfView.document().indexForPage_(outlineItem.destionation().page()) > newPageIndex:
                newlySelectedRow = i - 1
                self._outlineView.selectRow_byExtendingSelection_(
                        newlySelectedRow, False)
                break

        # Auto-scroll.
        if newlySelectedRow != -1:
            self._outlineView.scrollRowToVisible_(newlySelectedRow)


    def doFind_(self, sender):
        if self._pdfView.document().isFinding():
            self._pdfView.document().cancelFindString()


        # Lazily allocate _searchResults.
        if self._searchResults is None:
            self._searchResults = NSMutableArray.arrayWithCapacity_(10)

        self._pdfView.document().beginFindString_withOptions_(
                sender.stringValue(), NSCaseInsensitiveSearch)

    def startFind_(self, notification):
        # Empty arrays.
        self._searchResults.removeAllObjects()
        self._searchTable.reloadData()
        self._searchProgress.startAnimation_(self)

    def findProgress_(self, notification):
        pageIndex = notification.userInfo().objectForKey_(
                "PDFDocumentPageIndex") #.doubleValue()
        self._searchProgress.setDoubleValue_(
                pageIndex / self._pdfView.document().pageCount())

    def didMatchString_(self, instance):
        # Add page label to our array.
        self._searchResults.addObject_(instance.copy())
        self._searchTable.reloadData()

    def endFind_(self, notification):
        self._searchProgress.stopAnimation_(self)
        self._searchProgress.setDoubleValue_(0)

    #  The table view is used to hold search results.  Column 1 lists the
    # page number for the search result,  column two the section in the PDF
    # (x-ref with the PDF outline) where the result appears.

    def numberOfRowsInTableView_(self, aTableView):
        if self._searchResults is None:
            return 0
        return self._searchResults.count()

    def tableView_objectValueForTableColumn_row_(
            self, aTableView, theColumn, rowIndex):

        if theColumn.identifier() == "page":
            return  self._searchResults.objectAtIndex_(rowIndex).pages().objectAtIndex_(0).label()

        elif theColumn.identifier() == 'section':
            value = self._pdfView.document().outlineItemForSelection_(
                    self._searchResults.objectAtIndex_(rowIndex))

            if value is None:
                return None

            return value.label()

        else:
            return None

    def tableViewSelectionDidChange_(self, notification):
        # What was selected.  Skip out if the row has not changed.
        rowIndex = notification.object().selectedRow()
        if rowIndex >= 0:
            self._pdfView.setCurrentSelection_(
                    self._searchResults.objectAtIndex_(rowIndex))
            self._pdfView.centerSelectionInVisibleArea_(self)


    # The outline view is for the PDF outline.  Not all PDF's have an outline.
    def outlineView_numberOfChildrenOfItem_(self, outlineView, item):
        if item is None:
            if self._outline is not None:
                return self._outline.numberOfChildren()
            else:
                return 0

        else:
            return item.numberOfChildren()

    def outlineView_child_ofItem_(self, outlineView, index, item):
        if item is None:
            if self._outline is not None:
                return self._outline.childAtIndex_(index).retain()
            else:
                return None

        else:
            return item.childAtIndex_(index).retain()

    def outlineView_isItemExpandable_(self, outlineView, item):
        if item is None:
            if self._outline:
                return self._outline.numberOfChildren() > 0

            else:
                return False

        else:
            return item.numberOfChildren() > 0

    def outlineView_objectValueForTableColumn_byItem_(
            self, outlineView, tableColumn, item):
        return item.label()
