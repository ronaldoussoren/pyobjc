from PyObjCTools import AppHelper, NibClassBuilder
from AppKit import *
from Foundation import *

NibClassBuilder.extractClasses("MainMenu")

class DraggableItemView(NibClassBuilder.AutoBaseClass):
    """."""
    _locationDefault = NSMakePoint(0.0, 0.0)
    _itemColorDefault = NSColor.redColor()
    _backgroundColorDefault = NSColor.whiteColor()
            
    def initWithFrame_(self, frame):
        """."""
        result = super(DraggableItemView, self).initWithFrame_(frame)
        if result is not None:
            result._location = self._locationDefault
            result._itemColor = self._itemColorDefault
            result._backgroundColor = self._backgroundColorDefault
        return result
    
    def drawRect_(self, rect):
        """."""
        NSColor.whiteColor().set()
        NSBezierPath.fillRect_(rect)
        self.itemColor().set()
        NSBezierPath.fillRect_(self.calculatedItemBounds())

    def isOpaque(self):
        """."""
        return (self.backgroundColor().alphaComponent() >= 1.0)

    def offsetLocationByX_andY_(self, x, y):
        """."""
        self.setNeedsDisplayInRect_(self.calculatedItemBounds())
        if self.isFlipped():
            invertDeltaY = -1
        else:
            invertDeltaY = 1
        self.location().x = self.location().x + x
        self.location().y = self.location().y + y * invertDeltaY
        self.setNeedsDisplayInRect_(self.calculatedItemBounds())

    def mouseDown_(self, event):
        """."""
        clickLocation = self.convertPoint_fromView_(event.locationInWindow(),
                                                    None)
        itemHit = self.isPointInItem_(clickLocation)
        if itemHit:
            self.dragging = True
            self.lastDragLocation = clickLocation
            NSCursor.closedHandCursor().push()

    def mouseDragged_(self, event):
        """."""
        if self.dragging:
            newDragLocation = \
                self.convertPoint_fromView_(event.locationInWindow(),
                                            None)
            self.offsetLocationByX_andY_(newDragLocation.x - \
                                         self.lastDragLocation.x,
                                         newDragLocation.y - \
                                         self.lastDragLocation.y)
            self.lastDragLocation = newDragLocation
            self.autoscroll_(event)

    def mouseUp_(self, event):
        """."""
        self.dragging = False
        # NSCursor has both an instance and a class method w/ the name 'pop'
        NSCursor.pyobjc_classMethods.pop()
        self.window().invalidateCursorRectsForView_(self)

    def acceptsFirstResponder(self):
        """."""
        return True

    def keyDown_(self, event):
        """."""
        handled = False
        characters = event.charactersIgnoringModifiers()
        if characters.isEqual_('r'):
            handled = True
            self.setItemPropertiesToDefault_(self)
        if handled is False:
            super(DraggableItemView, self).keyDown_(event)

    def changeColor_(self, sender):
        """."""
        self.setItemColor_(sender.color())

    def resetCursorRects(self):
        """."""
        self.discardCursorRects()
        self.addCursorRect_cursor_(self.calculatedItemBounds(),
                                   NSCursor.openHandCursor())

    def moveUp_(self, sender):
        """."""
        self.offsetLocationByX_andY_(0.0, 10.0)
        self.window().invalidateCursorRectsForView_(self)

    def moveDown_(self, sender):
        """."""
        self.offsetLocationByX_andY_(0.0, -10.0)
        self.window().invalidateCursorRectsForView_(self)

    def moveLeft_(self, sender):
        """."""
        self.offsetLocationByX_andY_(-10.0, 0.0)
        self.window().invalidateCursorRectsForView_(self)

    def moveRight_(self, sender):
        """."""
        self.offsetLocationByX_andY_(10.0, 0.0)
        self.window().invalidateCursorRectsForView_(self)

    def setItemPropertiesToDefault_(self, sender):
        """."""
        self.setLocation_(self._locationDefault)
        self.setItemColor_(self._itemColorDefault)
        self.setBackgroundColor_(self._backgroundColorDefault)

    def setLocation_(self, point):
        """."""
        if not NSEqualPoints(point, self.location()):
            self.setNeedsDisplayInRect_(self.calculatedItemBounds())
            self._location = point
            self.setNeedsDisplayInRect_(self.calculatedItemBounds())
            self.window().invalidateCursorRectsForView_(self)

    def location(self):
        """."""
        return self._location

    def setBackgroundColor_(self, aColor):
        """."""
        if not self.backgroundColor().isEqual_(aColor):
            self._backgroundColor = aColor
            self.setNeedsDisplayInRect_(self.calculatedItemBounds())

    def backgroundColor(self):
        """."""
        return self._backgroundColor

    def setItemColor_(self, aColor):
        """."""
        if not self.itemColor().isEqual_(aColor):
            self._itemColor = aColor
            self.setNeedsDisplayInRect_(self.calculatedItemBounds())

    def itemColor(self):
        """."""
        return self._itemColor

    def calculatedItemBounds(self):
        """."""
        return NSMakeRect(self.location().x, self.location().y,
                          60.0, 20.0)

    def isPointInItem_(self, testPoint):
        """."""
        itemHit = NSPointInRect(testPoint, self.calculatedItemBounds())
        if itemHit:
            pass
        return itemHit
    
if __name__ == "__main__":
    AppHelper.runEventLoop()
