#
#  ITunesCommunication.py
#  PyObjC2Test
#
#  Created by Jack Jansen on Tue Jun 17 2003.
#  Copyright (c) 2003 __MyCompanyName__. All rights reserved.
#

import objc
from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder

import iTunes

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
        # subclass specific initialization here
        # nib not loaded yet
        self.itunes = iTunes.iTunes()
        return self

    def getITunesInfo(self):
        curtrk = self.itunes.current_track
        try:
            current_track = self.itunes.get(curtrk)
        except iTunes.Error:
            NSRunAlertPanel(
                u'iTunes Communication Error',
                u'iTunes failed to return the current track',
                None,
                None,
                None)
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
        info = self.getITunesInfo()
        if info is None:
            return
        album, artist, genre = info
        document.setCDTitle_(album)
        document.setBandName_(artist)
        document.setMusicGenre_(genre)
