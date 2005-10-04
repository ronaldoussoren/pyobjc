"""
Instances of WSTConnectionWindowController are the controlling object
for the document windows for the Web Services Tool application.

Implements a standard toolbar.
"""

from AppKit import *
from Foundation import *
from PyObjCTools import NibClassBuilder
import objc

from twisted.internet import defer
from twisted.web.xmlrpc import Proxy

from RPCMethod import *

#from twisted.python import log
#import sys
#log.startLogging(sys.stdout)

# cheap dirty way to turn those messages off
# from twisted.python import log
# log.logerr = open('/dev/null','w')

# Identifier for 'reload contents' toolbar item.
kWSTReloadContentsToolbarItemIdentifier = u"WST: Reload Contents Toolbar Identifier"

# Identifier for 'preferences' toolbar item.
kWSTPreferencesToolbarItemIdentifier = u"WST: Preferences Toolbar Identifier"

# Identifier for URL text field toolbar item.
kWSTUrlTextFieldToolbarItemIdentifier = u"WST: URL Textfield Toolbar Identifier"

def addToolbarItem(aController, anIdentifier, aLabel, aPaletteLabel,
                   aToolTip, aTarget, anAction, anItemContent, aMenu):
    """
    Adds an freshly created item to the toolbar defined by
    aController.  Makes a number of assumptions about the
    implementation of aController.  It should be refactored into a
    generically useful toolbar management untility.
    """
    toolbarItem = NSToolbarItem.alloc().initWithItemIdentifier_(anIdentifier)

    toolbarItem.setLabel_(aLabel)
    toolbarItem.setPaletteLabel_(aPaletteLabel)
    toolbarItem.setToolTip_(aToolTip)
    toolbarItem.setTarget_(aTarget)
    if anAction:
        toolbarItem.setAction_(anAction)

    if isinstance(anItemContent, NSImage):
        toolbarItem.setImage_(anItemContent)
    else:
        toolbarItem.setView_(anItemContent)
        bounds = anItemContent.bounds()
        minSize = (100, bounds[1][1])
        maxSize = (1000, bounds[1][1])
        toolbarItem.setMinSize_( minSize )
        toolbarItem.setMaxSize_( maxSize )

    if aMenu:
        menuItem = NSMenuItem.alloc().init()
        menuItem.setSubmenu_(aMenu)
        menuItem.setTitle_( aMenu.title() )
        toolbarItem.setMenuFormRepresentation_(menuItem)

    aController.k_toolbarItems[anIdentifier] = toolbarItem

NibClassBuilder.extractClasses( "WSTConnection" )

class WSTConnectionWindowController(NibClassBuilder.AutoBaseClass):
    """
    As per the definition in the NIB file,
    WSTConnectionWindowController is a subclass of
    NSWindowController.
    """

    def connectionWindowController(self):
        """
        Create and return a default connection window instance.
        """
        return WSTConnectionWindowController.alloc().init()

    connectionWindowController = classmethod(connectionWindowController)

    def init(self):
        """
        Designated initializer.

        Returns self (as per ObjC designated initializer definition,
        unlike Python's __init__() method).
        """
        self = self.initWithWindowNibName_(u"WSTConnection")

        self.k_toolbarItems = {}
        self.k_toolbarDefaultItemIdentifiers = []
        self.k_toolbarAllowedItemIdentifiers = []

        self.k_methods = {}
        self.k_methodArray = []
        return self

    def awakeFromNib(self):
        """
        Invoked when the NIB file is loaded.  Initializes the various
        UI widgets.
        """
        self.retain() # balanced by autorelease() in windowWillClose_

        self.statusTextField.setStringValue_(u"No host specified.")
        self.progressIndicator.setStyle_(NSProgressIndicatorSpinningStyle)
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
        toolbar = NSToolbar.alloc().initWithIdentifier_(u"WST Connection Window")
        toolbar.setDelegate_(self)
        toolbar.setAllowsUserCustomization_(True)
        toolbar.setAutosavesConfiguration_(True)

        self.createToolbarItems()

        self.window().setToolbar_(toolbar)

        lastURL = NSUserDefaults.standardUserDefaults().stringForKey_(u"LastURL")
        if lastURL and len(lastURL):
            self.urlTextField.setStringValue_(lastURL)

    def createToolbarItems(self):
        """
        Creates all of the toolbar items that can be made available in
        the toolbar.  The actual set of available toolbar items is
        determined by other mechanisms (user defaults, for example).
        """
        addToolbarItem(
            self, kWSTReloadContentsToolbarItemIdentifier,
            u"Reload", u"Reload", u"Reload Contents", None,
            "reloadVisibleData:", NSImage.imageNamed_(u"Reload"), None)
        addToolbarItem(
            self, kWSTPreferencesToolbarItemIdentifier,
            u"Preferences", u"Preferences", u"Show Preferences", None,
            "orderFrontPreferences:", NSImage.imageNamed_(u"Preferences"), None)
        addToolbarItem(
            self, kWSTUrlTextFieldToolbarItemIdentifier,
            u"URL", u"URL", u"Server URL", None,
            None, self.urlTextField, None)

        self.k_toolbarDefaultItemIdentifiers = [
            kWSTReloadContentsToolbarItemIdentifier,
            kWSTUrlTextFieldToolbarItemIdentifier,
            NSToolbarSeparatorItemIdentifier,
            NSToolbarCustomizeToolbarItemIdentifier,
        ]

        self.k_toolbarAllowedItemIdentifiers = [
            kWSTReloadContentsToolbarItemIdentifier,
            kWSTUrlTextFieldToolbarItemIdentifier,
            NSToolbarSeparatorItemIdentifier,
            NSToolbarSpaceItemIdentifier,
            NSToolbarFlexibleSpaceItemIdentifier,
            NSToolbarPrintItemIdentifier,
            kWSTPreferencesToolbarItemIdentifier,
            NSToolbarCustomizeToolbarItemIdentifier,
        ]

    def toolbarDefaultItemIdentifiers_(self, anIdentifier):
        """
        Return an array of toolbar item identifiers that identify the
        set, in order, of items that should be displayed on the
        default toolbar.
        """
        return self.k_toolbarDefaultItemIdentifiers

    def toolbarAllowedItemIdentifiers_(self, anIdentifier):
        """
        Return an array of toolbar items that may be used in the toolbar.
        """
        return self.k_toolbarAllowedItemIdentifiers

    def toolbar_itemForItemIdentifier_willBeInsertedIntoToolbar_(self,
                                                                 toolbar,
                                                                 itemIdentifier, flag):
        """
        Delegate method fired when the toolbar is about to insert an
        item into the toolbar.  Item is identified by itemIdentifier.

        Effectively makes a copy of the cached reference instance of
        the toolbar item identified by itemIdentifier.
        """
        newItem = NSToolbarItem.alloc().initWithItemIdentifier_(itemIdentifier)
        item = self.k_toolbarItems[itemIdentifier]

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

    def setStatusTextFieldMessage_(self, aMessage):
        """
        Sets the contents of the statusTextField to aMessage and
        forces the fileld's contents to be redisplayed.
        """
        if not aMessage:
            aMessage = u"Displaying information about %d methods." % (len(self.k_methods),)
        self.statusTextField.setStringValue_(aMessage)
    setStatusTextFieldMessage_ = objc.accessor(setStatusTextFieldMessage_)

    def startWorking(self):
        """Signal the UI there's work goin on."""
        self.progressIndicator.startAnimation_(self)

    def stopWorking(self):
        """Signal the UI that the work is done."""
        self.progressIndicator.stopAnimation_(self)

    def reloadVisibleData_(self, sender):
        """
        Reloads the list of methods and their signatures from the
        XML-RPC server specified in the urlTextField.  Displays
        appropriate error messages, if necessary.
        """
        url = self.urlTextField.stringValue()
        self.k_methods = {}

        if not url:
            self.window().setTitle_(u"Untitled.")
            self.setStatusTextFieldMessage_(u"No URL specified.")
            return

        self.window().setTitle_(url)
        NSUserDefaults.standardUserDefaults().setObject_forKey_(url, u"LastURL")

        self.setStatusTextFieldMessage_(u"Retrieving method list...")
        self.getMethods(url)

    def getMethods(self, url):
        _server = self.k_server = Proxy(url.encode('utf8'))
        self.startWorking()
        return _server.callRemote('listMethods').addCallback(
            # call self.receivedMethods(result, _server, "") on success
            self.receivedMethods, _server, ""
        ).addErrback(
            # on error, call this lambda
            lambda e: _server.callRemote('system.listMethods').addCallback(
                # call self.receievedMethods(result, _server, "system.")
                self.receivedMethods, _server, 'system.'
            )
        ).addErrback(
            # log the failure instance, with a method
            self.receivedMethodsFailure, 'listMethods()'
        ).addBoth(
            # stop working nomatter what trap all errors (returns None)
            lambda n:self.stopWorking()
        )

    def receivedMethodsFailure(self, why, method):
        self.k_server = None
        self.k_methodPrefix = None
        self.setStatusTextFieldMessage_(
           (u"Server failed to respond to %s.  "
            u"See below for more information."       ) % (method,)
        )
        #log.err(why)
        self.methodDescriptionTextView.setString_(why.getTraceback())

    def receivedMethods(self, _methods, _server, _methodPrefix):
        self.k_server = _server
        self.k_methods = {}
        self.k_methodPrefix = _methodPrefix
        for aMethod in _methods:
            self.k_methods[aMethod] = RPCMethod.alloc().initWithDocument_name_(self, aMethod)
        self.setMethodArray_(self.k_methods.values())
        self.k_methodPrefix = _methodPrefix

        self.setStatusTextFieldMessage_(
            u"Retrieving information about %d methods." % (len(self.k_methods),)
        )

        # we could make all the requests at once :)
        # but the server might not like that so we will chain them
        d = defer.succeed(None)
        for index, aMethod in enumerate(self.k_methodArray):
            d.addCallback(
                self.fetchMethodSignature, index, aMethod
            ).addCallbacks(
                callback = self.processSignatureForMethod,
                callbackArgs = (index, aMethod),
                errback = self.couldntProcessSignatureForMethod,
                errbackArgs = (index, aMethod),
            )
        return d.addCallback(
            lambda ig: self.setStatusTextFieldMessage_(None)
        )

    def fetchMethodSignature(self, ignore, index, aMethod):
        self.setStatusTextFieldMessage_(
            u"Retrieving signature for method %s (%d of %d)."
            % (aMethod.methodName() , index, len(self.k_methods))
        )
        return self.k_server.callRemote(
            (self.k_methodPrefix + 'methodSignature').encode('utf-8'),
            aMethod.methodName().encode('utf-8')
        )

    def processSignatureForMethod(self, methodSignature, index, aMethod):
        signatures = None
        if not len(methodSignature):
            return
        for aSignature in methodSignature:
            if isinstance(aSignature, list) and len(aSignature) > 0:
                signature = u"%s %s(%s)" % (aSignature[0], aMethod.methodName(), u", ".join(aSignature[1:]))
            else:
                signature = aSignature
        if signatures:
            signatures = signatures + u", " + signature
        else:
            signatures = signature

        aMethod.setMethodSignature_(signatures)
        self.replaceObjectInMethodArrayAtIndex_withObject_(index, aMethod)

    def couldntProcessSignatureForMethod(self, why, index, aMethod):
        #log.err(why)
        aMethod.setMethodSignature_(u"<error> %s %s" % (aMethod.methodName(), why.getBriefTraceback()))
        self.replaceObjectInMethodArrayAtIndex_withObject_(index, aMethod)

    def fetchMethodDescription_(self, aMethod):
        def cacheDesc(v):
            aMethod.setMethodDescription_(v or u'No description available.')

        self.setStatusTextFieldMessage_(u"Retrieving documentation for method %s..." % (aMethod.methodName(),))
        self.startWorking()
        self.k_server.callRemote((self.k_methodPrefix + u'methodHelp').encode('utf-8'), aMethod.methodName().encode('utf-8')).addCallback(cacheDesc)

    def methodArray(self):
        return self.k_methodArray

    def countOfMethodArray(self):
        if self.k_methodArray is None:
            return 0
        return self.k_methodArray
    countOfMethodArray = objc.accessor(countOfMethodArray)

    def objectInMethodArrayAtIndex_(self, anIndex):
        return self.k_methodArray[anIndex]
    objectInMethodArrayAtIndex_ = objc.accessor(objectInMethodArrayAtIndex_)

    def insertObject_inMethodArrayAtIndex_(self, anObject, anIndex):
        self.k_methodArray.insert(anIndex, anObject)
    insertObject_inMethodArrayAtIndex_ = objc.accessor(insertObject_inMethodArrayAtIndex_)

    def removeObjectFromMethodArrayAtIndex_(self, anIndex):
        del self.k_methodArray[anIndex]
    removeObjectFromMethodArrayAtIndex_ = objc.accessor(removeObjectFromMethodArrayAtIndex_)

    def replaceObjectInMethodArrayAtIndex_withObject_(self, anIndex, anObject):
        self.k_methodArray[anIndex] = anObject
    replaceObjectInMethodArrayAtIndex_withObject_ = objc.accessor(replaceObjectInMethodArrayAtIndex_withObject_)

    def setMethodArray_(self, anArray):
        self.k_methodArray = anArray
    setMethodArray_ = objc.accessor(setMethodArray_)
