from Cocoa import *

import math

searchIndex = 0

class MyWindowController (NSWindowController):
    query = objc.ivar()
    previousRowCount = objc.ivar(objc._C_INT)

    myTableView = objc.IBOutlet()
    mySearchResults = objc.IBOutlet()
    predicateEditor = objc.IBOutlet()
    progressView = objc.IBOutlet()        # the progress search view
    progressSearch = objc.IBOutlet()      # spinning gear
    progressSearchLabel = objc.IBOutlet() # search result #


    def dealloc(self):
        NSNotificationCenter.defaultCenter().removeObserver_(self)

    def awakeFromNib(self):
        # no vertical scrolling, we always want to show all rows
        self.predicateEditor.enclosingScrollView().setHasVerticalScroller_(False)

        self.previousRowCount = 3
        self.predicateEditor.addRow_(self)

        # put the focus in the first text field
        displayValue = self.predicateEditor.displayValuesForRow_(1).lastObject()
        if isinstance(displayValue,  NSControl):
            self.window().makeFirstResponder_(displayValue)

        # create and initalize our query
        self.query = NSMetadataQuery.alloc().init()

        # setup our Spotlight notifications
        nf = NSNotificationCenter.defaultCenter()
        nf.addObserver_selector_name_object_(self, 'queryNotification:', None, self.query)

        # initialize our Spotlight query, sort by contact name

        # XXX: this framework isn't wrapped yet!
        self.query.setSortDescriptors_([NSSortDescriptor.alloc().initWithKey_ascending_(
            'kMDItemContactKeywords', True)])
        self.query.setDelegate_(self)

        # start with our progress search label empty
        self.progressSearchLabel.setStringValue_("")

        return

    def applicationShouldTerminateAfterLastWindowClosed_(self, sender):
        return True

    def loadResultsFromQuery_(self, notif):
        results = notif.object().results()

        NSLog("search count = %d", len(results))
        foundResultsStr = "Results found: %d"%(len(results),)
        self.progressSearchLabel.setStringValue_(foundResultsStr)

        # iterate through the array of results, and match to the existing stores
        for item in results:
            cityStr = item.valueForAttribute_('kMDItemCity')
            nameStr = item.valueForAttribute_('kMDItemDisplayName')
            stateStr = item.valueForAttribute_('kMDItemStateOrProvince')
            phoneNumbers = item.valueForAttribute_('kMDItemPhoneNumbers')
            phoneStr = None
            if phoneNumbers:
                phoneStr = phoneNumbers[0]

            storePath = item.valueForAttribute_('kMDItemPath').stringByResolvingSymlinksInPath()

            # create a dictionary entry to be added to our search results array
            emptyStr = ""
            dict = {
                    'name': nameStr or "",
                    'phone': phoneStr or "",
                    'city': cityStr or "",
                    'state': stateStr or "",
                    'url': NSURL.fileURLWithPath_(storePath),
            }
            self.mySearchResults.append(dict)

    def queryNotification_(self, note):
        # the NSMetadataQuery will send back a note when updates are happening.
        # By looking at the [note name], we can tell what is happening
        if note.name() == NSMetadataQueryDidStartGatheringNotification:
            # the query has just started
            NSLog("search: started gathering")

            self.progressSearch.setHidden_(False)
            self.progressSearch.startAnimation_(self)
            self.progressSearch.animate_(self)
            self.progressSearchLabel.setStringValue_("Searching...")

        elif note.name() == NSMetadataQueryDidFinishGatheringNotification:
            # at this point, the query will be done. You may recieve an update
            # later on.
            NSLog("search: finished gathering");

            self.progressSearch.setHidden_(True)
            self.progressSearch.stopAnimation_(self)

            self.loadResultsFromQuery_(note)

        elif note.name() == NSMetadataQueryGatheringProgressNotification:
            # the query is still gathering results...
            NSLog("search: progressing...")

            self.progressSearch.animate_(self)

        elif note.name() == NSMetadataQueryDidUpdateNotification:
            # an update will happen when Spotlight notices that a file as
            # added, removed, or modified that affected the search results.
            NSLog("search: an update happened.")

    # -------------------------------------------------------------------------
    #   inspect:selectedObjects
    #
    #   This method obtains the selected object (in our case for single selection,
    #   it's the first item), and opens its URL.
    # -------------------------------------------------------------------------
    def inspect_(self, selectedObjects):
        objectDict = selectedObjects[0]
        if objectDict is not None:
            url = objectDict['url']
            NSWorkspace.sharedWorkspace().openURL_(url)

    # ------------------------------------------------------------------------
    #   spotlightFriendlyPredicate:predicate
    #
    #   This method will "clean up" an NSPredicate to make it ready for Spotlight, or return nil if the predicate can't be cleaned.
    #
    #   Foundation's Spotlight support in NSMetdataQuery places the following requirements on an NSPredicate:
    #           - Value-type (always YES or NO) predicates are not allowed
    #           - Any compound predicate (other than NOT) must have at least two subpredicates
    # -------------------------------------------------------------------------
    def spotlightFriendlyPredicate_(self, predicate):
        if predicate == NSPredicate.predicateWithValue_(True) or predicate == NSPredicate.predicateWithValue_(False):
            return False

        elif isinstance(predicate, NSCompoundPredicate):

            type = predicate.compoundPredicateType()
            cleanSubpredicates = []
            for dirtySubpredicate in predicate.subpredicates():
                cleanSubpredicate = self.spotlightFriendlyPredicate_(
                    dirtySubpredicate)
                if cleanSubpredicate:
                    cleanSubpredicates.append(cleanSubpredicate)

            if len(cleanSubpredicates) == 0:
                return None

            else:
                if len(cleanSubpredicates) == 1 and type != NSNotPredicateType:
                    return cleanSubpredicates[0]

                else:
                    return NSCompoundPredicate.alloc().initWithType_subpredicates_(type, cleanSubpredicates)

        else:
            return predicate

    # -------------------------------------------------------------------------
    #   createNewSearchForPredicate:predicate:withTitle
    #
    # -------------------------------------------------------------------------
    def createNewSearchForPredicate_withTitle_(self, predicate, title):
        if predicate is not None:
            self.mySearchResults.removeObjects_(
                self.mySearchResults.arrangedObjects());        # remove the old search results

            # always search for items in the Address Book
            addrBookPredicate = NSPredicate.predicateWithFormat_(
                "(kMDItemKind = 'Address Book Person Data')")
            predicate = NSCompoundPredicate.andPredicateWithSubpredicates_(
                [addrBookPredicate, predicate])

            self.query.setPredicate_(predicate)
            self.query.startQuery()

    # --------------------------------------------------------------------------
    #   predicateEditorChanged:sender
    #
    #  This method gets called whenever the predicate editor changes.
    #   It is the action of our predicate editor and the single plate for all our updates.
    #
    #   We need to do potentially three things:
    #           1) Fire off a search if the user hits enter.
    #           2) Add some rows if the user deleted all of them, so the user isn't left without any rows.
    #           3) Resize the window if the number of rows changed (the user hit + or -).
    # --------------------------------------------------------------------------
    @objc.IBAction
    def predicateEditorChanged_(self, sender):
        # check NSApp currentEvent for the return key
        event = NSApp.currentEvent()
        if event is None:
            return

        if event.type() == NSKeyDown:
            characters = event.characters()
            if len(characters) > 0 and characters[0] == u'\r':
                # get the predicat, which is the object value of our view
                predicate = self.predicateEditor.objectValue()

                # make it Spotlight friendly
                predicate = self.spotlightFriendlyPredicate_(predicate)
                if predicate is not None:
                    global searchIndex
                    title = NSLocalizedString("Search #%ld", "Search title");
                    self.createNewSearchForPredicate_withTitle_(
                            predicate, title % searchIndex)
                    searchIndex += 1

        # if the user deleted the first row, then add it again - no sense leaving the user with no rows
        if self.predicateEditor.numberOfRows() == 0:
            self.predicateEditor.addRow_(self)

        # resize the window vertically to accomodate our views:

        # get the new number of rows, which tells us the needed change in height,
        # note that we can't just get the view frame, because it's currently animating - this method is called before the animation is finished.
        newRowCount = self.predicateEditor.numberOfRows()

        # if there's no change in row count, there's no need to resize anything
        if newRowCount == self.previousRowCount:
            return

        # The autoresizing masks, by default, allows the NSTableView to grow and keeps the predicate editor fixed.
        # We need to temporarily grow the predicate editor, and keep the NSTableView fixed, so we have to change the autoresizing masks.
        # Save off the old ones; we'll restore them after changing the window frame.
        tableScrollView = self.myTableView.enclosingScrollView()
        oldOutlineViewMask = tableScrollView.autoresizingMask()

        predicateEditorScrollView = self.predicateEditor.enclosingScrollView()
        oldPredicateEditorViewMask = predicateEditorScrollView.autoresizingMask()

        tableScrollView.setAutoresizingMask_(
                NSViewWidthSizable | NSViewMaxYMargin)
        predicateEditorScrollView.setAutoresizingMask_(
                NSViewWidthSizable | NSViewHeightSizable)

        # determine if we need to grow or shrink the window
        growing = (newRowCount > self.previousRowCount)

        # if growing, figure out by how much.  Sizes must contain nonnegative values, which is why we avoid negative floats here.
        heightDifference = abs(self.predicateEditor.rowHeight() * (newRowCount - self.previousRowCount))

        # convert the size to window coordinates -
        # if we didn't do this, we would break under scale factors other than 1.
        # We don't care about the horizontal dimension, so leave that as 0.
        #
        sizeChange = self.predicateEditor.convertSize_toView_(
                NSMakeSize(0, heightDifference), None)

        # offset our status view
        frame = self.progressView.frame()
        self.progressView.setFrameOrigin_(NSMakePoint(
            frame.origin.x,
            frame.origin.y - self.predicateEditor.rowHeight() * (newRowCount - self.previousRowCount)))

        # change the window frame size:
        # - if we're growing, the height goes up and the origin goes down (corresponding to growing down).
        # - if we're shrinking, the height goes down and the origin goes up.
        windowFrame = self.window().frame()
        if growing:
            windowFrame.size.height += sizeChange.height
            windowFrame.origin.y -= sizeChange.height
        else:
            windowFrame.size.height -= sizeChange.height
            windowFrame.origin.y += sizeChange.height

        self.window().setFrame_display_animate_(windowFrame, True, True)

        # restore the autoresizing mask
        tableScrollView.setAutoresizingMask_(oldOutlineViewMask)
        predicateEditorScrollView.setAutoresizingMask_(oldPredicateEditorViewMask)

        self.previousRowCount = newRowCount     # save our new row count
