from Cocoa import NSObject

class AppDelegate(NSObject):
    def applicationShouldOpenUntitledFile_(self, applicaton):
        return False
