"""
Instances of WSTConnectionWindowController are the controlling object
for the document windows for the Web Services Tool application.

Implements a standard toolbar.
"""

import string
import types

import Cocoa

# Note about multi-threading.
# Although WST does its network stuff in a background thread, with Python 2.2
# there are still moments where the app appears to hang briefly. This should
# only be noticeable when your DNS is slow-ish. The hang is caused by the
# socket.getaddrinfo() function, which is used (indirectly) when connecting
# to a server, which is a frequent operation when using xmlrpclib (it makes
# a new connection for each request). Up to (and including) version 2.3b1,
# Python would not grant time to other threads while blocking inside
# getaddrinfo(). This has been fixed *after* 2.3b1 was released. (jvr)
import objc
from twisted.internet import defer
from twisted.web.xmlrpc import Proxy

kWSTReloadContentsToolbarItemIdentifier = "WST: Reload Contents Toolbar Identifier"
"""Identifier for 'reload contents' toolbar item."""

kWSTPreferencesToolbarItemIdentifier = "WST: Preferences Toolbar Identifier"
"""Identifier for 'preferences' toolbar item."""

kWSTUrlTextFieldToolbarItemIdentifier = "WST: URL Textfield Toolbar Identifier"
"""Idnetifier for URL text field toolbar item."""


def addToolbarItem(
    aController,
    anIdentifier,
    aLabel,
    aPaletteLabel,
    aToolTip,
    aTarget,
    anAction,
    anItemContent,
    aMenu,
):
    """
    Adds an freshly created item to the toolbar defined by
    aController.  Makes a number of assumptions about the
    implementation of aController.  It should be refactored into a
    generically useful toolbar management utility.
    """
    toolbarItem = Cocoa.NSToolbarItem.alloc().initWithItemIdentifier_(anIdentifier)

    toolbarItem.setLabel_(aLabel)
    toolbarItem.setPaletteLabel_(aPaletteLabel)
    toolbarItem.setToolTip_(aToolTip)
    toolbarItem.setTarget_(aTarget)
    if anAction:
        toolbarItem.setAction_(anAction)

    if isinstance(anItemContent, Cocoa.NSImage):
        toolbarItem.setImage_(anItemContent)
    else:
        toolbarItem.setView_(anItemContent)
        bounds = anItemContent.bounds()
        minSize = (100, bounds[1][1])
        maxSize = (1000, bounds[1][1])
        toolbarItem.setMinSize_(minSize)
        toolbarItem.setMaxSize_(maxSize)

    if aMenu:
        menuItem = Cocoa.NSMenuItem.alloc().init()
        menuItem.setSubmenu_(aMenu)
        menuItem.setTitle_(aMenu.title())
        toolbarItem.setMenuFormRepresentation_(menuItem)

    aController._toolbarItems[anIdentifier] = toolbarItem


class WSTConnectionWindowController(Cocoa.NSWindowController):
    """
    As per the definition in the NIB file,
    WSTConnectionWindowController is a subclass of
    NSWindowController.  It acts as a NSTableView data source and
    implements a standard toolbar.
    """

    methodDescriptionTextView = objc.IBOutlet()
    methodsTable = objc.IBOutlet()
    progressIndicator = objc.IBOutlet()
    statusTextField = objc.IBOutlet()
    urlTextField = objc.IBOutlet()

    __slots__ = (
        "_toolbarItems",
        "_toolbarDefaultItemIdentifiers",
        "_toolbarAllowedItemIdentifiers",
        "_methods",
        "_methodSignatures",
        "_methodDescriptions",
        "_server",
        "_methodPrefix",
    )

    @classmethod
    def connectionWindowController(self):
        """
        Create and return a default connection window instance.
        """
        return WSTConnectionWindowController.alloc().init()

    def init(self):
        """
        Designated initializer.

        Returns self (as per ObjC designated initializer definition,
        unlike Python's __init__() method).
        """
        self = self.initWithWindowNibName_("WSTConnection")

        self._toolbarItems = {}
        self._toolbarDefaultItemIdentifiers = []
        self._toolbarAllowedItemIdentifiers = []

        self._methods = []
        return self

    def awakeFromNib(self):
        """
        Invoked when the NIB file is loaded.  Initializes the various
        UI widgets.
        """
        self.retain()  # balanced by autorelease() in windowWillClose_

        self.statusTextField.setStringValue_("No host specified.")
        self.progressIndicator.setStyle_(Cocoa.NSProgressIndicatorSpinningStyle)
        self.progressIndicator.setDisplayedWhenStopped_(False)

        self.createToolbar()

    def windowWillClose_(self, aNotification):
        """
        Clean up when the document window is closed.
        """
        self.autorelease()

    def createToolbar(self):
        """
        Creates and configures the toolbar to be used by the window.
        """
        toolbar = Cocoa.NSToolbar.alloc().initWithIdentifier_("WST Connection Window")
        toolbar.setDelegate_(self)
        toolbar.setAllowsUserCustomization_(True)
        toolbar.setAutosavesConfiguration_(True)

        self.createToolbarItems()

        self.window().setToolbar_(toolbar)

        lastURL = Cocoa.NSUserDefaults.standardUserDefaults().stringForKey_("LastURL")
        if lastURL and len(lastURL):
            self.urlTextField.setStringValue_(lastURL)

    def createToolbarItems(self):
        """
        Creates all of the toolbar items that can be made available in
        the toolbar.  The actual set of available toolbar items is
        determined by other mechanisms (user defaults, for example).
        """
        addToolbarItem(
            self,
            kWSTReloadContentsToolbarItemIdentifier,
            "Reload",
            "Reload",
            "Reload Contents",
            None,
            "reloadVisibleData:",
            Cocoa.NSImage.imageNamed_("Reload"),
            None,
        )
        addToolbarItem(
            self,
            kWSTPreferencesToolbarItemIdentifier,
            "Preferences",
            "Preferences",
            "Show Preferences",
            None,
            "orderFrontPreferences:",
            Cocoa.NSImage.imageNamed_("Preferences"),
            None,
        )
        addToolbarItem(
            self,
            kWSTUrlTextFieldToolbarItemIdentifier,
            "URL",
            "URL",
            "Server URL",
            None,
            None,
            self.urlTextField,
            None,
        )

        self._toolbarDefaultItemIdentifiers = [
            kWSTReloadContentsToolbarItemIdentifier,
            kWSTUrlTextFieldToolbarItemIdentifier,
            Cocoa.NSToolbarSeparatorItemIdentifier,
            Cocoa.NSToolbarCustomizeToolbarItemIdentifier,
        ]

        self._toolbarAllowedItemIdentifiers = [
            kWSTReloadContentsToolbarItemIdentifier,
            kWSTUrlTextFieldToolbarItemIdentifier,
            Cocoa.NSToolbarSeparatorItemIdentifier,
            Cocoa.NSToolbarSpaceItemIdentifier,
            Cocoa.NSToolbarFlexibleSpaceItemIdentifier,
            Cocoa.NSToolbarPrintItemIdentifier,
            kWSTPreferencesToolbarItemIdentifier,
            Cocoa.NSToolbarCustomizeToolbarItemIdentifier,
        ]

    def toolbarDefaultItemIdentifiers_(self, anIdentifier):
        """
        Return an array of toolbar item identifiers that identify the
        set, in order, of items that should be displayed on the
        default toolbar.
        """
        return self._toolbarDefaultItemIdentifiers

    def toolbarAllowedItemIdentifiers_(self, anIdentifier):
        """
        Return an array of toolbar items that may be used in the toolbar.
        """
        return self._toolbarAllowedItemIdentifiers

    def toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_(
        self, toolbar, itemIdentifier, flag
    ):
        """
        Delegate method fired when the toolbar is about to insert an
        item into the toolbar.  Item is identified by itemIdentifier.

        Effectively makes a copy of the cached reference instance of
        the toolbar item identified by itemIdentifier.
        """
        newItem = Cocoa.NSToolbarItem.alloc().initWithItemIdentifier_(itemIdentifier)
        item = self._toolbarItems[itemIdentifier]

        newItem.setLabel_(item.label())
        newItem.setPaletteLabel_(item.paletteLabel())
        if item.view():
            newItem.setView_(item.view())
        else:
            newItem.setImage_(item.image())

        newItem.setToolTip_(item.toolTip())
        newItem.setTarget_(item.target())
        newItem.setAction_(item.action())
        newItem.setMenuFormRepresentation_(item.menuFormRepresentation())

        if newItem.view():
            newItem.setMinSize_(item.minSize())
            newItem.setMaxSize_(item.maxSize())

        return newItem

    def setStatusTextFieldMessage_(self, aMessage):
        """
        Sets the contents of the statusTextField to aMessage and
        forces the fileld's contents to be redisplayed.
        """
        if not aMessage:
            aMessage = "Displaying information about %d methods." % len(self._methods)
        # All UI calls should be directed to the main thread
        self.statusTextField.setStringValue_(aMessage)

    def reloadData(self):
        """Tell the main thread to update the table view."""
        self.methodsTable.reloadData()

    def startWorking(self):
        """Signal the UI there's work going on."""
        self.progressIndicator.startAnimation_(self)

    def stopWorking(self):
        """Signal the UI that the work is done."""
        self.progressIndicator.stopAnimation_(self)

    @objc.IBAction
    def reloadVisibleData_(self, sender):
        """
        Reloads the list of methods and their signatures from the
        XML-RPC server specified in the urlTextField.  Displays
        appropriate error messages, if necessary.
        """
        url = self.urlTextField.stringValue()
        self._methods = []
        self._methodSignatures = {}
        self._methodDescriptions = {}

        if not url:
            self.window().setTitle_("Untitled.")
            self.setStatusTextFieldMessage_("No URL specified.")
            return

        self.window().setTitle_(url)
        Cocoa.NSUserDefaults.standardUserDefaults().setObject_forKey_(url, "LastURL")

        self.setStatusTextFieldMessage_("Retrieving method list...")
        self.getMethods(url)

    @objc.python_method
    def getMethods(self, url):
        _server = self._server = Proxy(url.encode("utf8"))
        self.startWorking()
        return (
            _server.callRemote("listMethods")
            .addCallback(
                # call self.receivedMethods(result, _server, "") on success
                self.receivedMethods,
                _server,
                "",
            )
            .addErrback(
                # on error, call this lambda
                lambda e: _server.callRemote("system.listMethods").addCallback(
                    # call self.receievedMethods(result, _server, "system.")
                    self.receivedMethods,
                    _server,
                    "system.",
                )
            )
            .addErrback(
                # log the failure instance, with a method
                self.receivedMethodsFailure,
                "listMethods()",
            )
            .addBoth(
                # stop working nomatter what trap all errors (returns None)
                lambda n: self.stopWorking()
            )
        )

    @objc.python_method
    def receivedMethodsFailure(self, why, method):
        self._server = None
        self._methodPrefix = None
        self.setStatusTextFieldMessage_(
            ("Server failed to respond to %s.  See below for more information.")
            % (method,)
        )
        # log.err(why)
        self.methodDescriptionTextView.setString_(why.getTraceback())

    @objc.python_method
    def receivedMethods(self, _methods, _server, _methodPrefix):
        self._server = _server
        self._methods = _methods
        self._methodPrefix = _methodPrefix

        self._methods.sort()
        self.reloadData()
        self.setStatusTextFieldMessage_(
            "Retrieving information about %d methods." % (len(self._methods),)
        )

        # we could make all the requests at once :)
        # but the server might not like that so we will chain them
        d = defer.succeed(None)
        for index, aMethod in enumerate(self._methods):
            d.addCallback(self.fetchMethodSignature, index, aMethod).addCallbacks(
                callback=self.processSignatureForMethod,
                callbackArgs=(index, aMethod),
                errback=self.couldntProcessSignatureForMethod,
                errbackArgs=(index, aMethod),
            )
        return d.addCallback(
            lambda ig: self.setStatusTextFieldMessage_(None)
        ).addCallback(lambda ig: self.reloadData())

    @objc.python_method
    def fetchMethodSignature(self, ignore, index, aMethod):
        if (index % 5) == 0:
            self.reloadData()
        self.setStatusTextFieldMessage_(
            "Retrieving signature for method %s (%d of %d)."
            % (aMethod, index, len(self._methods))
        )
        return self._server.callRemote(self._methodPrefix + "methodSignature", aMethod)

    @objc.python_method
    def processSignatureForMethod(self, methodSignature, index, aMethod):
        signatures = None
        if not len(methodSignature):
            return
        for aSignature in methodSignature:
            if (type(aSignature) == types.ListType) and (  # noqa: E721
                len(aSignature) > 0
            ):
                signature = "{} {}({})".format(
                    aSignature[0],
                    aMethod,
                    string.join(aSignature[1:], ", "),
                )
            else:
                signature = aSignature
        if signatures:
            signatures = signatures + ", " + signature
        else:
            signatures = signature
        self._methodSignatures[aMethod] = signatures

    @objc.python_method
    def couldntProcessSignatureForMethod(self, why, index, aMethod):
        # log.err(why)
        self._methodSignatures[aMethod] = "<error> {} {}".format(
            aMethod,
            why.getBriefTraceback(),
        )

    def tableViewSelectionDidChange_(self, sender):
        """
        When the user selects a remote method, this method displays
        the documentation for that method as returned by the XML-RPC
        server.  If the method's documentation has been previously
        queried, the documentation will be retrieved from a cache.
        """
        selectedRow = self.methodsTable.selectedRow()
        selectedMethod = self._methods[selectedRow]

        def displayMethod(methodDescription):
            self.setStatusTextFieldMessage_(None)
            self.methodDescriptionTextView.setString_(methodDescription)

        self.fetchMethodDescription(selectedMethod).addCallback(displayMethod)

    @objc.python_method
    def fetchMethodDescription(self, aMethod):
        desc = self._methodDescriptions
        if aMethod in desc:
            return defer.succeed(desc[aMethod])

        def cacheDesc(v):
            v = v or "No description available."
            desc[aMethod] = v
            return v

        def _stopWorking(v):
            self.stopWorking()
            return v

        desc[aMethod] = "<description is being retrieved>"
        self.setStatusTextFieldMessage_(f"Retrieving signature for method {aMethod}...")
        self.startWorking()
        return (
            self._server.callRemote(self._methodPrefix + "methodHelp", aMethod)
            .addCallback(_stopWorking)
            .addCallback(cacheDesc)
        )

    def numberOfRowsInTableView_(self, aTableView):
        """
        Returns the number of methods found on the server.
        """
        return len(self._methods)

    def tableView_objectValueForTableColumn_row_(
        self, aTableView, aTableColumn, rowIndex
    ):
        """
        Returns either the raw method name or the method signature,
        depending on if a signature had been found on the server.
        """
        aMethod = self._methods[rowIndex]
        if aMethod in self._methodSignatures:
            return self._methodSignatures[aMethod]
        else:
            return aMethod

    def tableView_shouldEditTableColumn_row_(self, aTableView, aTableColumn, rowIndex):
        # don't allow editing of any cells
        return 0
