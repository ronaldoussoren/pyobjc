from Foundation import NSObject
from WSTConnectionWindowControllerClass import WSTConnectionWindowController

class WSTApplicationDelegate (NSObject):
  def newConnectionAction_(self, sender):
    WSTConnectionWindowController.connectionWindowController().showWindow_(sender)

  def applicationDidFinishLaunching_(self, aNotification):
    print "foo"
    self.newConnectionAction_(None)
    print "bar"
