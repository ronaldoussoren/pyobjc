"""
Minimal applescript support.

The PyDocEventHandler handles just the event that is used to open URLs. Thanks
to this class you can use ``open pydoc:///os.open`` from a command-line, or
add ``pydoc:///`` to HTML files.
"""
from Foundation import *

from Carbon.AppleEvents import kAEISGetURL, kAEInternetSuite
import struct
import objc

def fourCharToInt(code):
    return struct.unpack('l', code)[0]

class PyDocEventHandler (NSObject):
    webview = objc.IBOutlet('webview')
    urlfield = objc.IBOutlet('urlfield')

    def handleEvent_withReplyEvent_(self, event, replyEvent):
        theURL = event.descriptorForKeyword_(fourCharToInt('----'))

        self.urlfield.setStringValue_(theURL.stringValue())
        self.webview.takeStringURLFrom_(theURL)


    def awakeFromNib(self):
        manager = NSAppleEventManager.sharedAppleEventManager()

        # Add a handler for the event GURL/GURL. One might think that
        # Carbon.AppleEvents.kEISInternetSuite/kAEISGetURL would work,
        # but the system headers (and hence the Python wrapper for those)
        # are wrong.
        manager.setEventHandler_andSelector_forEventClass_andEventID_(
            self, 'handleEvent:withReplyEvent:',
                fourCharToInt('GURL'),
                fourCharToInt('GURL'))
