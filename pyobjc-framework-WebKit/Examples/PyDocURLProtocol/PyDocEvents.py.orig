from Foundation import *
from Carbon.AppleEvents import kAEISGetURL, kAEInternetSuite
import struct

def fourCharToInt(code):
    return struct.unpack('l', code)[0]

class PyDocEventHandler (NSObject):
    def handleEvent_withReplyEvent_(self, event, replyEvent):
        print "handler called"


def setup():
    global handler

    handler = PyDocEventHandler.alloc().init()
    manager = NSAppleEventManager.sharedAppleEventManager()
    manager.setEventHandler_andSelector_forEventClass_andEventID_(
            handler, 'handleEvent:withReplyEvent:',
                fourCharToInt(kAEInternetSuite),
                fourCharToInt(kAEISGetURL))
