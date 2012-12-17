from Cocoa import *
import objc

class PathDemoController (NSObject):
    button      = objc.ivar()
    popup       = objc.ivar()
    window      = objc.ivar()
    demoView    = objc.ivar()

    def awakeFromNib(self):
        #  Add the title of your new demo to the END of this array.

        titles = [ 'Rectangles', 'Circles', 'Bezier Paths', 'Circle Clipping' ]

        self.popup.removeAllItems()

        for t in titles:
            self.popup.addItemWithTitle_(t)

    @objc.IBAction
    def runAgain_(self, sender):
        self.select_(self)

    @objc.IBAction
    def select_(self, sender):
        self.demoView.setDemoNumber_(self.popup.indexOfSelectedItem())
        self.demoView.setNeedsDisplay_(True)

    def applicationShouldTerminateAfterLastWindowClosed_(self, application):
        return True
