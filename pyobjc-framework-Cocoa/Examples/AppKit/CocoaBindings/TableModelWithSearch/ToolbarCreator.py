#
#  ToolbarCreator.py
#  TableModelWithSearch
#
#  Created by Bill Bumgarner on Sun Apr 04 2004.
#  Copyright (c) 2004 __MyCompanyName__. All rights reserved.
#

from objc import YES, NO
from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder

NibClassBuilder.extractClasses("MainMenu")

kToolbarIdentifier = "TableModel Toolbar Identifier"
kSearchFieldItemIdentifier = "TableModel Search Field Identifier"

from FilteringArrayController import kLiteralSearch, kRegularExpressionSearch

class ToolbarCreator(NibClassBuilder.AutoBaseClass):
    def awakeFromNib(self):
        self.toolbarItemCache = {}

        # create toolbar containing search field
        toolbar = NSToolbar.alloc().initWithIdentifier_(kToolbarIdentifier)
        toolbar.setDelegate_(self)
        toolbar.setAllowsUserCustomization_(YES)
        toolbar.setAutosavesConfiguration_(YES)

        searchFieldItem = NSToolbarItem.alloc().initWithItemIdentifier_(kSearchFieldItemIdentifier)
        self.searchFieldItem = searchFieldItem
        searchFieldItem.setLabel_("Search")
        searchFieldItem.setPaletteLabel_("Search Field")
        searchFieldItem.setToolTip_("Search")
        searchFieldItem.setView_(self.searchField)
        searchFieldItem.setMinSize_(self.searchField.bounds().size)
        maxSize = self.searchField.bounds().size
        maxSize.width = maxSize.width + 150
        searchFieldItem.setMaxSize_(maxSize)

        self.toolbarItemCache[kSearchFieldItemIdentifier] = searchFieldItem

        self.window.setToolbar_(toolbar)

        cellMenu = NSMenu.alloc().initWithTitle_(u'Search Menu')
        # note, bottom up!
        for v in [kRegularExpressionSearch, kLiteralSearch]:
            item = NSMenuItem.alloc().initWithTitle_action_keyEquivalent_(v, 'changeSearchType:', u'')
            item.setRepresentedObject_(v)
            item.setTarget_(self)
            cellMenu.insertItem_atIndex_(item, 0)
        self.searchField.cell().setSearchMenuTemplate_(cellMenu)
        # this better be the kLiteralSearch menu item
        self.changeSearchType_(item)

    def changeSearchType_(self, sender):
        obj = sender.representedObject()
        self.searchField.cell().setPlaceholderString_(obj)
        self.searchField.setStringValue_(u'')
        self.filteringArrayController.changeSearchType_(obj)

    def toolbarDefaultItemIdentifiers_(self, aToolbar):
        return [
            kSearchFieldItemIdentifier,
            NSToolbarFlexibleSpaceItemIdentifier,
            NSToolbarSeparatorItemIdentifier,
            NSToolbarCustomizeToolbarItemIdentifier,
        ]

    def toolbarAllowedItemIdentifiers_(self, aToolbar):
        return [
            kSearchFieldItemIdentifier,
            NSToolbarFlexibleSpaceItemIdentifier,
            NSToolbarSpaceItemIdentifier,
            NSToolbarSeparatorItemIdentifier,
            NSToolbarPrintItemIdentifier,
            NSToolbarCustomizeToolbarItemIdentifier,
        ]

    def toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_(self, toolbar, itemIdentifier, flag):
        newItem = NSToolbarItem.alloc().initWithItemIdentifier_(itemIdentifier)
        item = self.toolbarItemCache[itemIdentifier]

        newItem.setLabel_( item.label() )
        newItem.setPaletteLabel_( item.paletteLabel() )
        if item.view():
            newItem.setView_( item.view() )
        else:
            newItem.setImage_( item.image() )

        newItem.setToolTip_( item.toolTip() )
        newItem.setTarget_( item.target() )
        newItem.setAction_( item.action() )
        newItem.setMenuFormRepresentation_( item.menuFormRepresentation() )

        if newItem.view():
            newItem.setMinSize_( item.minSize() )
            newItem.setMaxSize_( item.maxSize() )

        return newItem
