#######

#
#  ITunesCommunication.py
#  PyObjC2Test
#
#
# This is a variation on the ITunesCommuncation that uses a the 'appscript'
# module for the inter-application communication.

import objc
from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder

from appscript import *

# We tell NibClassBuilder to examine and remember all
# classes from the CDInfoDocument NIB file. This way,
# we can subclass our ITunesCommunication from AutoBaseClass
# later on, and its actual baseclass will be ITunesCommunication
# from the NIB file.
# Since the NIB files are in the application, NOT the plugin, we
# need to specify this explicitly.  Typicaly, NIB files would be in the
# plugins.
NibClassBuilder.extractClasses("CDInfoDocument", bundle=NSBundle.mainBundle())

class ITunesCommunication(NibClassBuilder.AutoBaseClass):
    def init(self):
        self = super(ITunesCommunication, self).init()
        if self is None:
            return None
        return self

    def getITunesInfo(self):
        try:
            track = app('iTunes.app').current_track.get()
        except Exception:
            NSRunAlertPanel(
                u'iTunes Communication Error',
                u'iTunes failed to return the current track',
                None,
                None,
                None)
        else:
            return track.album.get(), track.artist.get(), track.genre.get()

    def askITunes_(self, obj):
        # obj is the button the user pressed. We can go from here
        # to the document (an instance of CDInfoDocument)
        document = obj.window().windowController().document()
        # Try to get the iTunes info
        info = self.getITunesInfo()
        if info is None:
            return
        album, artist, genre = info
        document.setCDTitle_(album)
        document.setBandName_(artist)
        document.setMusicGenre_(genre)
