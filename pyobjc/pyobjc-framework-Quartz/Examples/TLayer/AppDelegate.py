from Cocoa import *
import TLayerDemo
import objc

class AppDelegate (NSObject):
    shadowDemo = objc.ivar()

    def applicationDidFinishLaunching_(self, notification):
        self.showTLayerDemoWindow_(self)

    @objc.IBAction
    def showTLayerDemoWindow_(self, sender):
        if self.shadowDemo is None:
            self.shadowDemo = TLayerDemo.TLayerDemo.alloc().init()

        self.shadowDemo.window().orderFront_(self)

    def applicationShouldTerminateAfterLastWindowClosed_(self, app):
        return True
