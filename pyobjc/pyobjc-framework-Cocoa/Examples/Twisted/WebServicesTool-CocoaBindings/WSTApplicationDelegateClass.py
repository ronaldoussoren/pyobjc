"""
WSTApplicationDelegateClass
"""

from AppKit import *

from PyObjCTools import AppHelper
from WSTConnectionWindowControllerClass import WSTConnectionWindowController

from twisted.internet import reactor

class WSTApplicationDelegate (NSObject):

    @objc.IBAction
    def newConnectionAction_(self, sender):
        """Action method fired when the user selects the 'new connection'
        menu item.  Note that the WSTConnectionWindowControllerClass is
        defined the first time this method is invoked.

        This kind of lazy evaluation is generally recommended;  it speeds
        app launch time and it ensures that cycles aren't wasted loading
        functionality that will never be used.

        (In this case, it is largely moot due to the implementation of
        applicationDidFinishLaunching_().
        """
        WSTConnectionWindowController.connectionWindowController().showWindow_(sender)

    def applicationShouldTerminate_(self, sender):
        if reactor.running:
            reactor.addSystemEventTrigger(
                'after', 'shutdown', AppHelper.stopEventLoop)
            reactor.stop()
            return False
        return True

    def applicationDidFinishLaunching_(self, aNotification):
        """Create and display a new connection window
        """
        reactor.interleave(AppHelper.callAfter)
        self.newConnectionAction_(None)
