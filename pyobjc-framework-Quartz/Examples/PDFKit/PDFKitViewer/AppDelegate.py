from Cocoa import NSObject


class AppDelegate(NSObject):
    def applicationShouldOpenUntitledFile_(self, application):
        return False
