#
#  JoystickView.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

from Foundation import *
from AppKit import *
from objc import ivar
from math import sin, cos, sqrt, atan2, pi

class JoystickView(NSView):
    AngleObservationContext = 2091
    OffsetObservationContext = 2092

    maxOffset = ivar(u"maxOffset", 'd')
    angle  = ivar(u"angle")#, 'd') # expect angle in degrees
    offset = ivar(u"offset")#, 'd')

    observedObjectForAngle    = ivar(u'observedObjectForAngle')
    observedKeyPathForAngle   = ivar(u'observedKeyPathForAngle')
    angleValueTransformerName = ivar(u'angleValueTransformerName')
    badSelectionForAngle      = ivar(u'badSelectionForAngle')
    multipleSelectionForAngle = ivar(u'multipleSelectionForAngle')
    allowsMultipleSelectionForAngle = ivar(u'allowsMultipleSelectionForAngle')

    observedObjectForOffset    = ivar(u'observedObjectForOffset')
    observedKeyPathForOffset   = ivar(u'observedKeyPathForOffset')
    offsetValueTransformerName = ivar(u'offsetValueTransformerName')
    badSelectionForOffset      = ivar(u'badSelectionForOffset')
    multipleSelectionForOffset = ivar(u'multipleSelectionForOffset')
    allowsMultipleSelectionForOffset = ivar(u'allowsMultipleSelectionForOffset')


    def valueClassForBinding_(cls, binding):
        # both require numbers
        return NSNumber
    valueClassForBinding_ = classmethod(valueClassForBinding_)


    def initWithFrame_(self, frameRect):
        self = super(JoystickView, self).initWithFrame_(frameRect)
        if self is None: return None
        self.maxOffset = 15.0
        self.offset = 0.0
        self.angle = 28.0
        self.multipleSelectionForAngle = False
        self.multipleSelectionForOffset = False
        return self


    def bind_toObject_withKeyPath_options_(
        self, bindingName, observableController, keyPath, options):

        if bindingName == u"angle":
            # observe the controller for changes -- note, pass binding identifier
            # as the context, so we get that back in observeValueForKeyPath:...
            # that way we can determine what needs to be updated.
            observableController.addObserver_forKeyPath_options_context_(
                self, keyPath, 0, self.AngleObservationContext)
            # register what controller and what keypath are
            # associated with this binding
            self.observedObjectForAngle = observableController
            self.observedKeyPathForAngle = keyPath
            # options
            self.angleValueTransformerName = options[u"NSValueTransformerName"]
            self.allowsMultipleSelectionForAngle = False
            if options[u"NSAllowsEditingMultipleValuesSelection"]:
                self.allowsMultipleSelectionForAngle = True

        if bindingName == u"offset":
            observableController.addObserver_forKeyPath_options_context_(
                self, keyPath, 0, self.OffsetObservationContext)
            self.observedObjectForOffset = observableController
            self.observedKeyPathForOffset = keyPath
            self.allowsMultipleSelectionForOffset = False
            if options[u"NSAllowsEditingMultipleValuesSelection"]:
                self.allowsMultipleSelectionForOffset = True


    def unbind_(self, bindingName):
        if bindingName == u"angle":
            if self.observedObjectForAngle is None:
                return
            self.observedObjectForAngle.removeObserver_forKeyPath_(
                self, self.observedKeyPathForAngle)
            self.observedObjectForAngle = None
            self.observedKeyPathForAngle = None
            self.angleValueTransformerName = None
        elif bindingName == u"offset":
            if self.observedObjectForOffset is None:
                return None
            self.observedObjectForOffset.removeObserver_forKeyPath_(
                self, self.observedKeyPathForOffset)
            self.observedObjectForOffset = None
            self.observedKeyPathForOffset = None


    def observeValueForKeyPath_ofObject_change_context_(self, keyPath, object, change, context):
        # we passed the binding as the context when we added ourselves
        # as an observer -- use that to decide what to update...
        # should ask the dictionary for the value...
        if context == self.AngleObservationContext:
            # angle changed
            # if we got a NSNoSelectionMarker or NSNotApplicableMarker, or
            # if we got a NSMultipleValuesMarker and we don't allow multiple selections
            # then note we have a bad angle
            newAngle = self.observedObjectForAngle.valueForKeyPath_(self.observedKeyPathForAngle)
            if (newAngle == NSNoSelectionMarker or newAngle == NSNotApplicableMarker
                or (newAngle == NSMultipleValuesMarker and not self.allowsMultipleSelectionForAngle)):
                self.badSelectionForAngle = True
            else:
                # note we have a good selection
                # if we got a NSMultipleValuesMarker, note it but don't update value
                self.badSelectionForAngle = False
                if newAngle == NSMultipleValuesMarker:
                    self.multipleSelectionForAngle = True
                else:
                    self.multipleSelectionForAngle = False
                    if self.angleValueTransformerName is not None:
                        vt = NSValueTransformer.valueTransformerForName_(self.angleValueTransformerName)
                        newAngle = vt.transformedValue_(newAngle)
                    self.setValue_forKey_(newAngle, u"angle")

        if context == self.OffsetObservationContext:
            # offset changed
            # if we got a NSNoSelectionMarker or NSNotApplicableMarker, or
            # if we got a NSMultipleValuesMarker and we don't allow multiple selections
            # then note we have a bad selection
            newOffset = self.observedObjectForOffset.valueForKeyPath_(self.observedKeyPathForOffset)
            if (newOffset == NSNoSelectionMarker or newOffset == NSNotApplicableMarker
                or (newOffset == NSMultipleValuesMarker and not self.allowsMultipleSelectionForOffset)):
                self.badSelectionForOffset = True
            else:
                # note we have a good selection
                # if we got a NSMultipleValuesMarker, note it but don't update value
                self.badSelectionForOffset = False
                if newOffset == NSMultipleValuesMarker:
                    self.multipleSelectionForOffset = True
                else:
                    self.setValue_forKey_(newOffset, u"offset")
                    self.multipleSelectionForOffset = False
        self.setNeedsDisplay_(True)


    def updateForMouseEvent_(self, event):
        """
        update based on event location and selection state
        behavior based on modifier key
        """
        if self.badSelectionForAngle or self.badSelectionForOffset:
            return # don't do anything

        # find out where the event is, offset from the view center
        p = self.convertPoint_fromView_(event.locationInWindow(), None)
        myBounds = self.bounds()
        xOffset = (p.x - (myBounds.size.width/2))
        yOffset = (p.y - (myBounds.size.height/2))

        newOffset = sqrt(xOffset*xOffset + yOffset*yOffset)
        if newOffset > self.maxOffset:
            newOffset = self.maxOffset
        elif newOffset < -self.maxOffset:
            newOffset = -self.maxOffset

        # if we have a multiple selection for offset and Shift key is pressed
        # then don't update the offset
        # this allows offsets to remain constant, but change angle
        if not ( self.multipleSelectionForOffset and (event.modifierFlags() & NSShiftKeyMask)):
            self.offset = newOffset
            # update observed controller if set
            if self.observedObjectForOffset is not None:
                self.observedObjectForOffset.setValue_forKeyPath_(newOffset, self.observedKeyPathForOffset)

        # if we have a multiple selection for angle and Shift key is pressed
        # then don't update the angle
        # this allows angles to remain constant, but change offset
        if not ( self.multipleSelectionForAngle and (event.modifierFlags() & NSShiftKeyMask)):
            newAngle = atan2(xOffset, yOffset)
            newAngleDegrees = newAngle / (pi/180.0)
            if newAngleDegrees < 0:
                newAngleDegrees += 360
            self.angle = newAngleDegrees
            # update observed controller if set
            if self.observedObjectForAngle is not None:
                if self.observedObjectForAngle is not None:
                    vt = NSValueTransformer.valueTransformerForName_(self.angleValueTransformerName)
                    newControllerAngle = vt.reverseTransformedValue_(newAngleDegrees)
                else:
                    newControllerAngle = angle
            self.observedObjectForAngle.setValue_forKeyPath_(newControllerAngle, self.observedKeyPathForAngle)
        self.setNeedsDisplay_(True)


    def mouseDown_(self, event):
        self.mouseDown = True
        self.updateForMouseEvent_(event)


    def mouseDragged_(self, event):
        self.updateForMouseEvent_(event)


    def mouseUp_(self, event):
        self.mouseDown = False
        self.updateForMouseEvent_(event)


    def acceptsFirstMouse_(self, event):
        return True

    def acceptsFirstResponder(self):
        return True


    def drawRect_(self, rect):
        """
        Basic goals here:
        If either the angle or the offset has a "bad selection":
        then draw a gray rectangle, and that's it.
        Note: bad selection is set if there's a multiple selection
        but the "allows multiple selection" binding is NO.

        If there's a multiple selection for either angle or offset:
        then what you draw depends on what's multiple.

        - First, draw a white background to show all's OK.

        - If both are multiple, then draw a special symbol.

        - If offset is multiple, draw a line from the center of the view
        - to the edge at the shared angle.

        - If angle is multiple, draw a circle of radius the shared offset
        - centered in the view.

        If neither is multiple, draw a cross at the center of the view
        and a cross at distance 'offset' from the center at angle 'angle'
        """
        myBounds = self.bounds()
        if self.badSelectionForAngle or self.badSelectionForOffset:
            # "disable" and exit
            NSDrawDarkBezel(myBounds,myBounds);
            return;
        # user can do something, so draw white background and
        # clip in anticipation of future drawing
        NSDrawLightBezel(myBounds,myBounds)
        clipRect = NSBezierPath.bezierPathWithRect_( NSInsetRect(myBounds,2.0,2.0) )
        clipRect.addClip()

        if self.multipleSelectionForAngle or self.multipleSelectionForOffset:
            originOffsetX = myBounds.size.width/2 + 0.5
            originOffsetY = myBounds.size.height/2 + 0.5
            if self.multipleSelectionForAngle and self.multipleSelectionForOffset:
                # draw a diagonal line and circle to denote
                # multiple selections for angle and offset
                NSBezierPath.strokeLineFromPoint_toPoint_(NSMakePoint(0,0), NSMakePoint(myBounds.size.width,myBounds.size.height))
                circleBounds = NSMakeRect(originOffsetX-5, originOffsetY-5, 10, 10)
                path = NSBezierPath.bezierPathWithOvalInRect_(circleBounds)
                path.stroke()
                return
            if self.multipleSelectionForOffset:
                # draw a line from center to a point outside
                # bounds in the direction specified by angle
                angleRadians = self.angle * (pi/180.0)
                x = sin(angleRadians) * myBounds.size.width + originOffsetX
                y = cos(angleRadians) * myBounds.size.height + originOffsetX
                NSBezierPath.strokeLineFromPoint_toPoint_(NSMakePoint(originOffsetX, originOffsetY),
                    NSMakePoint(x, y))
                return
            if self.multipleSelectionForAngle:
                # draw a circle with radius the shared offset
                # dont' draw radius < 1.0, else invisible
                drawRadius = self.offset
                if drawRadius < 1.0: drawRadius = 1.0
                offsetBounds = NSMakeRect(originOffsetX-drawRadius,
                         originOffsetY-drawRadius,
                         drawRadius*2, drawRadius*2)
                path = NSBezierPath.bezierPathWithOvalInRect_(offsetBounds)
                path.stroke()
                return
            # shouldn't get here
            return
        trans = NSAffineTransform.transform()
        trans.translateXBy_yBy_( myBounds.size.width/2 + 0.5, myBounds.size.height/2 + 0.5)
        trans.concat()
        path = NSBezierPath.bezierPath()

        # draw + where shadow extends
        angleRadians = self.angle * (pi/180.0)
        xOffset = sin(angleRadians) * self.offset
        yOffset = cos(angleRadians) * self.offset

        path.moveToPoint_( NSMakePoint(xOffset,yOffset-5) )
        path.lineToPoint_( NSMakePoint(xOffset,yOffset+5) )
        path.moveToPoint_( NSMakePoint(xOffset-5,yOffset) )
        path.lineToPoint_( NSMakePoint(xOffset+5,yOffset) )

        NSColor.lightGrayColor().set()
        path.setLineWidth_(1.5)
        path.stroke()

        # draw + in center of view
        path = NSBezierPath.bezierPath()

        path.moveToPoint_( NSMakePoint(0,-5) )
        path.lineToPoint_( NSMakePoint(0,+5) )
        path.moveToPoint_( NSMakePoint(-5,0) )
        path.lineToPoint_( NSMakePoint(+5,0) )

        NSColor.blackColor().set()
        path.setLineWidth_(1.0)
        path.stroke()


    def setNilValueForKey_(self, key):
        "We may get passed nil for angle or offset. Just use 0"
        self.setValue_forKey_(0, key)


    def validateMaxOffset_error(self,ioValue):
        if ioValue == None:
            # trap this in setNilValueForKey
            # alternative might be to create new NSNumber with value 0 here
            return True
        if ioValue <= 0.0:
            errorString = NSLocalizedStringFromTable(u"Maximum Offset must be greater than zero",
                   u"Joystick",
                   u"validation: zero maxOffset error")
            userInfoDict = { NSLocalizedDescriptionKey : errorString }
            error = NSError.alloc().initWithDomain_code_userInfo_(u"JoystickView", 1, userInfoDict)
            outError = error
            return False
        return True


JoystickView.exposeBinding_(u"offset")
JoystickView.exposeBinding_(u"angle")
