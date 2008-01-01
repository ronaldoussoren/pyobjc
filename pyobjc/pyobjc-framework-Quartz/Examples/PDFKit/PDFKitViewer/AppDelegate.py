from Cocoa import *


class AppDelegate(NSObject):
    def applicationShouldOpenUntitledFile_(self, applicaton):
        return False
