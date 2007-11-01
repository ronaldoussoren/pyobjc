from PyObjCTools import AppHelper, NibClassBuilder
from AppKit import *
from Foundation import NSZeroPoint

from math import floor
import sys

NibClassBuilder.extractClasses("MainMenu")

class Controller(NibClassBuilder.AutoBaseClass):
    """."""
    def changeTransparency_(self, sender):
        """."""
        self.itsWindow.setAlphaValue_(sender.floatValue())
        self.itsWindow.display()

class CustomView(NibClassBuilder.AutoBaseClass):
    """."""
    def awakeFromNib(self):
        """."""
        self.circleImage = NSImage.imageNamed_("circle")
        if self.circleImage is None:
            sys.stderr.write('failed to access circle image\n')
            raise RuntimeError
        self.pentaImage = NSImage.imageNamed_("pentagram")
        if self.pentaImage is None:
            sys.stderr.write('failed to access pentagram image\n')
            raise RuntimeError
        self.setNeedsDisplay_(True)
    
    def drawRect_(self, rect):
        """."""
        NSColor.clearColor().set()
        NSRectFill(self.frame())
        if self.window().alphaValue() > 0.7:
            self.circleImage.compositeToPoint_operation_(NSZeroPoint, NSCompositeSourceOver)
        else:
            self.pentaImage.compositeToPoint_operation_(NSZeroPoint, NSCompositeSourceOver)

        if floor(NSAppKitVersionNumber) <= NSAppKitVersionNumber10_1:
            self.window().setHasShadow_(False)
            self.window().setHasShadow_(True)
        else:
            self.window().invalidateShadow()

class CustomWindow(NibClassBuilder.AutoBaseClass):
    """."""
    def initWithContentRect_styleMask_backing_defer_(self, contentRect, aStyle,
                                                     bufferingType, flag):
        """."""
        result = \
            super(CustomWindow, self).initWithContentRect_styleMask_backing_defer_(
                contentRect, NSBorderlessWindowMask, NSBackingStoreBuffered, False)
        if result is None:
            sys.stderr.write('superclass call failed\n')
            raise RuntimeError
        result.setBackgroundColor_(NSColor.clearColor())
        result.setLevel_(NSStatusWindowLevel)
        result.setAlphaValue_(1.0)
        result.setOpaque_(False)
        result.setHasShadow_(True)
        return result
    
    def canBecomeKeyWindow(self):
        """."""
        return True
    
    def mouseDragged_(self, theEvent):
        """."""
        screenFrame = NSScreen.mainScreen().frame()
        if screenFrame is None:
            sys.stderr.write('failed to obtain screen\n')
            raise RuntimeError
        windowFrame = self.frame()
        if windowFrame is None:
            sys.stderr.write('failed to obtain frame\n')
            raise RuntimeError
        currentLocation = self.convertBaseToScreen_(self.mouseLocationOutsideOfEventStream())
        newOrigin = NSMakePoint((currentLocation.x - self.initialLocation.x),
                                (currentLocation.y - self.initialLocation.y))
        if (newOrigin.y + windowFrame.size.height) > \
            (screenFrame.origin.y + screenFrame.size.height):
            newOrigin.y = screenFrame.origin.y + \
                          (screenFrame.size.height + windowFrame.size.height)
        self.setFrameOrigin_(newOrigin)
    
    def mouseDown_(self, theEvent):
        """."""
        windowFrame = self.frame()
        if windowFrame is None:
            sys.stderr.write('failed to obtain frame\n')
            raise RuntimeError
        self.initialLocation = \
            self.convertBaseToScreen_(theEvent.locationInWindow())
        self.initialLocation.x -= windowFrame.origin.x
        self.initialLocation.y -= windowFrame.origin.y

if __name__ == "__main__":
    AppHelper.runEventLoop()
