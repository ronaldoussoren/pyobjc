#
#  ITunesCommunication.py
#  PyObjC2Test
#
#  Created by Jack Jansen on Tue Jun 17 2003.
#  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
#

from objc import YES, NO
from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder

import iTunes

# We tell NibClassBuilder to examine and remember all
# classes from the CDInfoDocument NIB file. This way,
# we can subclass our ITunesCommunication from AutoBaseClass
# later on, and its actual baseclass will be ITunesCommunication
# from the NIB file.
NibClassBuilder.extractClasses("CDInfoDocument")

class ITunesCommunication(NibClassBuilder.AutoBaseClass):
    def init(self):
        self = super(ITunesCommunication, self).init()
        if self:
            # subclass specific initialization here
            # nib not loaded yet
            self.itunes = iTunes.iTunes()
        return self

    def getItunesInfo(self):
        curtrk = self.itunes.current_track
        try:
            current_track = self.itunes.get(curtrk)
        except iTunes.Error:
            print "iTunes failed to return current track"
            return None
        album = self.itunes.get(current_track.album)
        artist = self.itunes.get(current_track.artist)
        genre = self.itunes.get(current_track.genre)
        return album, artist, genre

    def askITunes_(self, obj):
        # obj is the button the user pressed. We can go from here
        # to the document (an instance of CDInfoDocument)
        document = obj.window().windowController().document()
        # Try to get the iTunes info
        info = self.getItunesInfo()
        if info:
            album, artist, genre = info
        else:
            album = ""
            artist = ""
            genre = ""
        document.setCDTitle_(album)
        document.setBandName_(artist)
        document.setMusicGenre_(genre)
