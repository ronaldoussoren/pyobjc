from Foundation import NSObject
from WSTConnectionWindowControllerClass import WSTConnectionWindowController

from AppKit import NibClassBuilder
from AppKit.NibClassBuilder import AutoBaseClass

NibClassBuilder.extractClasses( "MainMenu" )
class WSTApplicationDelegate(AutoBaseClass):

  def newConnectionAction_(self, sender):
    WSTConnectionWindowController.connectionWindowController().showWindow_(sender)

  def applicationDidFinishLaunching_(self, aNotification):
    self.newConnectionAction_(None)
