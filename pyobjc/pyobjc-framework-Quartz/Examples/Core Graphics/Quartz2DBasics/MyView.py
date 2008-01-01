from Cocoa import *
from UIHandling import *
from PyObjCTools import NibClassBuilder
import AppDrawing
import math

_drawingCommand = kCommandStrokedAndFilledRects
_pdfDocument = None

class MyView (NibClassBuilder.AutoBaseClass):
    def drawRect_(self, rect):
        context = NSGraphicsContext.currentContext().graphicsPort()
        AppDrawing.myDispatchDrawing(context, _drawingCommand)

    def setDrawCommand_(self, sender):
        global _drawingCommand

        newCommand = sender.tag()

        if newCommand != _drawingCommand:
            _drawingCommand = newCommand
            self.setNeedsDisplay_(True)

            self.currentMenuItem.setState_(NSOffState)
	    self.currentMenuItem = sender;
	    self.currentMenuItem.setState_(NSOnState)

    def currentPrintableCommand(self):
        # The best representation for printing or exporting
        # when the current command caches using a bitmap context
        # or a layer is to not do any caching.
        if _drawingCommand == kCommandDoCGLayer:
            return kCommandDoUncachedDrawing
    
        return _drawingCommand

    def print_(self, sender):
        global _drawingCommand

        savedDrawingCommand = _drawingCommand
        _drawingCommand = self.currentPrintableCommand()
        NSPrintOperation.printOperationWithView_(self).runOperation()
        _drawingCommand = savedDrawingCommand

    def knowsPageRange_(self, range):
        return True, NSRange(1, 1)

    def rectForPage_(self, page):
        pi = NSPrintOperation.currentOperation().printInfo()
        paperSize = pi.paperSize()
        return NSMakeRect(0, 0, paperSize.width, paperSize.height)

    def validateMenuItem_(self, menuItem):
        if menuItem.tag() == _drawingCommand:
            self.currentMenuItem = menuItem
            menuItem.setState_(True)
        else:
            menuItem.setState_(False)

	return True
