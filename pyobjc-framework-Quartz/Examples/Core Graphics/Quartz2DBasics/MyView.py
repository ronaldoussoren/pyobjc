import objc
import Cocoa
import UIHandling
import AppDrawing
import math

_drawingCommand = UIHandling.kCommandStrokedAndFilledRects
_pdfDocument = None

class MyView (Cocoa.NSView):
    currentMenuItem = objc.IBOutlet()

    def drawRect_(self, rect):
        context = Cocoa.NSGraphicsContext.currentContext().graphicsPort()
        AppDrawing.myDispatchDrawing(context, _drawingCommand)

    @objc.IBAction
    def setDrawCommand_(self, sender):
        global _drawingCommand

        newCommand = sender.tag()

        if newCommand != _drawingCommand:
            _drawingCommand = newCommand
            self.setNeedsDisplay_(True)

            self.currentMenuItem.setState_(Cocoa.NSOffState)
            self.currentMenuItem = sender;
            self.currentMenuItem.setState_(Cocoa.NSOnState)

    def currentPrintableCommand(self):
        # The best representation for printing or exporting
        # when the current command caches using a bitmap context
        # or a layer is to not do any caching.
        if _drawingCommand == UIHandling.kCommandDoCGLayer:
            return UIHandling.kCommandDoUncachedDrawing

        return _drawingCommand

    def print_(self, sender):
        global _drawingCommand

        savedDrawingCommand = _drawingCommand
        _drawingCommand = self.currentPrintableCommand()
        Cocoa.NSPrintOperation.printOperationWithView_(self).runOperation()
        _drawingCommand = savedDrawingCommand

    def knowsPageRange_(self, range):
        return True, Cocoa.NSRange(1, 1)

    def rectForPage_(self, page):
        pi = Cocoa.NSPrintOperation.currentOperation().printInfo()
        paperSize = pi.paperSize()
        return Cocoa.NSMakeRect(0, 0, paperSize.width, paperSize.height)

    def validateMenuItem_(self, menuItem):
        if menuItem.tag() == _drawingCommand:
            self.currentMenuItem = menuItem
            menuItem.setState_(True)
        else:
            menuItem.setState_(False)

        return True
