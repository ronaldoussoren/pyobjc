from Foundation import NSObject
from WSTConnectionWindowControllerClass import WSTConnectionWindowController

from AppKit import NibLoader

NibLoader.loadClassesForNibFromBundle( "MainMenu" )

class WSTApplicationDelegate:
  __metaclass__ = NibLoader.NibClassBuilder

  def newConnectionAction_(self, sender):
    WSTConnectionWindowController.connectionWindowController().showWindow_(sender)

  def applicationDidFinishLaunching_(self, aNotification):
    self.newConnectionAction_(None)
