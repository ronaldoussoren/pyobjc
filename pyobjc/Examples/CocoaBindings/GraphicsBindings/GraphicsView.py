#
#  GraphicsView.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

PropertyObservationContext = 1091
GraphicsObservationContext = 1092
SelectionIndexesObservationContext = 1093


from Foundation import *
from AppKit import *
from objc import ivar
from Circle import Circle
from sets import Set

class GraphicsView(NSView):
    graphicsContainer = ivar(u'graphicsContainer')
    graphicsKeyPath   = ivar(u'graphicsKeyPath')

    selectionIndexesContainer = ivar(u'selectionIndexesContainer') # GraphicsArrayController
    selectionIndexesKeyPath   = ivar(u'selectionIndexesKeyPath')

    oldGraphics = ivar(u'oldGraphics')

    def exposedBindings(self):
        return [u"graphics", u"selectedObjects"]

    def initWithFrame_(self, frameRect):
        return super(GraphicsView, self).initWithFrame_(frameRect)
        
    def graphics(self):
        if not self.graphicsContainer: return None
        return self.graphicsContainer.valueForKeyPath_(self.graphicsKeyPath)
        
    def selectionIndexes(self):
        if not self.selectionIndexesContainer: return None
        return self.selectionIndexesContainer.valueForKeyPath_(self.selectionIndexesKeyPath)
        
    def startObservingGraphics_(self, graphics):
        if not graphics: return
        # Register to observe each of the new graphics, and
        # each of their observable properties -- we need old and new
        # values for drawingBounds to figure out what our dirty rect
        for newGraphic in graphics:
            # Register as observer for all the drawing-related properties
            newGraphic.addObserver_forKeyPath_options_context_(
                self, u"drawingBounds", (NSKeyValueObservingOptionNew | NSKeyValueObservingOptionOld), 
                PropertyObservationContext)
            keys = Circle.keysForNonBoundsProperties()
            for key in keys:
                newGraphic.addObserver_forKeyPath_options_context_(
                    self, key, 0, PropertyObservationContext)
                    
    def stopObservingGraphics_(self, graphics):
        if graphics is None: return
        for graphic in graphics:
            for key in graphic.class__().keysForNonBoundsProperties():
                graphic.removeObserver_forKeyPath_(self, key)
            graphic.removeObserver_forKeyPath_(self, u"drawingBounds")
        
    def bind_toObject_withKeyPath_options_(self, bindingName, observableObject, observableKeyPath, options):
        if bindingName == u"graphics":
            self.graphicsContainer = observableObject
            self.graphicsKeyPath = observableKeyPath
            self.graphicsContainer.addObserver_forKeyPath_options_context_(
                    self, self.graphicsKeyPath, (NSKeyValueObservingOptionNew |
                    NSKeyValueObservingOptionOld), GraphicsObservationContext)
            self.startObservingGraphics_(self.graphics())
            
        elif bindingName == u"selectionIndexes":
            self.selectionIndexesContainer = observableObject
            self.selectionIndexesKeyPath = observableKeyPath
            self.selectionIndexesContainer.addObserver_forKeyPath_options_context_(
                self, self.selectionIndexesKeyPath, 0, SelectionIndexesObservationContext)
        self.setNeedsDisplay_(True)
        
    def unbind_(self, bindingName):
        if bindingName == u"graphics":
            self.graphicsContainer.removeObserver_forKeyPath_(self, self.graphicsKeyPath)
            self.graphicsContainer = None
            self.graphicsKeyPath = None
        if bindingName == u"selectionIndexes":
            self.selectionIndexesContainer.removeObserver_forKeyPath_(self, self.selectionIndexesKeyPath)
            self.seletionIndexesContainer = None
            self.selectionIndexesKeyPath = None
        self.setNeedsDisplay_(True)

    def observeValueForKeyPath_ofObject_change_context_(self, keyPath, object, change, context):
        if context == GraphicsObservationContext:
            # Should be able to use
            # NSArray *oldGraphics = [change objectForKey:NSKeyValueChangeOldKey];
            # etc. but the dictionary doesn't contain old and new arrays...??
            newGraphics = Set(object.valueForKeyPath_(self.graphicsKeyPath))
            onlyNew = newGraphics - Set(self.oldGraphics)
            self.startObservingGraphics_(onlyNew)
            
            if self.oldGraphics:
                removed = Set(self.oldGraphics) - newGraphics
                self.stopObservingGraphics_(removed)
            
            self.oldGraphics = newGraphics
            
            # could check drawingBounds of old and new, but...
            self.setNeedsDisplay_(True)
            return
        
        if context == PropertyObservationContext:
            updateRect = (0,)
            # Note: for Circle, drawingBounds is a dependent key of all the other
            # property keys except color, so we'll get this anyway...
            if keyPath == u"drawingBounds":
                newBounds = change.objectForKey_(NSKeyValueChangeNewKey)
                oldBounds = change.objectForKey_(NSKeyValueChangeOldKey)
                updateRect = NSUnionRect(newBounds, oldBounds)
            else:
                updateRect = object.drawingBounds()
            updateRect = NSMakeRect(updateRect.origin.x-1.0,
                                updateRect.origin.y-1.0,
                                updateRect.size.width+2.0,
                                updateRect.size.height+2.0)
            self.setNeedsDisplay_(True)
            return
            
        if context == SelectionIndexesObservationContext:
            self.setNeedsDisplay_(True)
            return

    def drawRect_(self, rect):
        myBounds = self.bounds()
        NSDrawLightBezel(myBounds, myBounds) # AppKit Function
        clipRect = NSBezierPath.bezierPathWithRect_(NSInsetRect(myBounds, 2.0, 2.0))
        clipRect.addClip()
        
        # Draw graphics
        graphicsArray = self.graphics()
        if graphicsArray:
            for graphic in graphicsArray:
                graphicDrawingBounds = graphic.drawingBounds()
                if NSIntersectsRect(rect, graphicDrawingBounds):
                    graphic.drawInView_(self)
        
        # Draw a red box around items in the current selection.
        # Selection should be handled by the graphic, but this is a
        # shortcut simply for display.
        
        currentSelectionIndexes = self.selectionIndexes() # ist das wir ein Array im Indezes?
        if currentSelectionIndexes != None:
            path = NSBezierPath.bezierPath()
            index = currentSelectionIndexes.firstIndex()
            while index != NSNotFound:
                graphicDrawingBounds = graphicsArray[index].drawingBounds()
                if NSIntersectsRect(rect, graphicDrawingBounds):
                    path.appendBezierPathWithRect_(graphicDrawingBounds)
                index = currentSelectionIndexes.indexGreaterThanIndex_(index)
                    
            NSColor.redColor().set()
            path.setLineWidth_(1.5)
            path.stroke()

            
        # Fairly simple just to illustrate the point
    def mouseDown_(self, event):		
        # find out if we hit anything
        p = self.convertPoint_fromView_(event.locationInWindow(), None)
        for aGraphic in self.graphics():
            if aGraphic.hitTest_isSelected_(p, False):
                break; # aGraphic soll spaeter einen Wert haben, falls es getroffene gibt!
        else:
            aGraphic = None
                
        # if no graphic hit, then if extending selection do nothing
        # else set selection to nil
        if aGraphic == None:
            if not event.modifierFlags() & NSShiftKeyMask:
                self.selectionIndexesContainer.setValue_forKeyPath_(None, self.selectionIndexesKeyPath)
            return
            
        # graphic hit
        # if not extending selection (Shift key down) then set
        # selection to this graphic
        # if extending selection, then:
        # - if graphic in selection remove it
        # - if not in selection add it
        graphicIndex = self.graphics().index(aGraphic)
        if not event.modifierFlags() & NSShiftKeyMask:
            selection = NSIndexSet.indexSetWithIndex_(graphicIndex)
        else:
            if  self.selectionIndexes().containsIndex_(graphicIndex):
                selection = self.selectionIndexes().mutableCopy()
                selection.removeIndex_(graphicIndex)
            else:
                selection = self.selectionIndexes().mutableCopy()
                selection.addIndex_(graphicIndex)
        self.selectionIndexesContainer.setValue_forKeyPath_(selection, self.selectionIndexesKeyPath)


GraphicsView.exposeBinding_(u"graphics")
GraphicsView.exposeBinding_(u"selectionIndexes")
