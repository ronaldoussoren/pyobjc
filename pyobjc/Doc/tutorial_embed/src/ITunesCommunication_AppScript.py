#######

#
#  ITunesCommunication.py
#  PyObjC2Test
#
#
# This is a variation on the ITunesCommuncation that uses a the 'appscript'
# module for the inter-application communication.

from objc import YES, NO
from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder

from appscript import *

# We tell NibClassBuilder to examine and remember all
# classes from the CDInfoDocument NIB file. This way,
# we can subclass our ITunesCommunication from AutoBaseClass
# later on, and its actual baseclass will be ITunesCommunication
# from the NIB file.
NibClassBuilder.extractClasses("CDInfoDocument")

class ITunesCommunication(NibClassBuilder.AutoBaseClass):
    def init(self):
        self = super(ITunesCommunication, self).init()
        return self

    def getItunesInfo(self):
        try:
            track = app('iTunes.app').current_track.get()
        except Exception:
            print "iTunes error: current track unavailable."
            return '', '', ''
        else:
            return track.album.get(), track.artist.get(), track.genre.get()
        def askITunes_(self, obj):
        # obj is the button the user pressed. We can go from here
        # to the document (an instance of CDInfoDocument)
        document = obj.window().windowController().document()
        # Try to get the iTunes info
        album, artist, genre = self.getItunesInfo()
        document.setCDTitle_(album)
        document.setBandName_(artist)
        document.setMusicGenre_(genre)
