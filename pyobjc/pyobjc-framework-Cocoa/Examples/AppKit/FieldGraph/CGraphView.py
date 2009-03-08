import objc
from Foundation import *
from AppKit import *
from math import pi, sin, cos
from fieldMath import *

# Convience global variables
x, y = 0, 1
llc, sze = 0, 1 # Left Lower Corner, Size

#____________________________________________________________
class CGraphView(NSView):
    
    azmuthSlider = objc.IBOutlet()
    mapOffsetEWSlider = objc.IBOutlet()
    mapOffsetNSSlider = objc.IBOutlet()
    mapScaleSlider = objc.IBOutlet()
    mapVisibleSlider = objc.IBOutlet()
    azmuthDisplay = objc.IBOutlet()
    mapOffsetEWDisplay = objc.IBOutlet()
    mapOffsetNSDisplay = objc.IBOutlet()
    mapScaleDisplay = objc.IBOutlet()
    
    def initWithFrame_(self, frame):
        super(CGraphView, self).initWithFrame_(frame)
        self.setGridColor()
        self.setRmsColor()
        self.setGraphColor()
        self.graphMargin = 2
        self.mapImage = 0
        self.mapRect = 0
        self.mapVisible = 0.70
        self.mapScale = 3.0
        self.mapOffsetEW = 0.27
        self.mapOffsetNS = 0.40
        self.mapBaseRadius = 200

        self.lines = 2
        self.gain = 0.5
        return self

    def awakeFromNib(self):
        self.setCrossCursor()
        self.mapVisibleSlider.setFloatValue_(self.mapVisible)
        self.setAzmuth(125)
        self.setMapRect()

    def setCrossCursor(self):
        crosshairImage = NSImage.imageNamed_("CrossCursor")
        imageSize = crosshairImage.size()
        self.crossCursor = NSCursor.alloc().initWithImage_hotSpot_(crosshairImage, (8, 8))
        rect = self.bounds()
        self.trackingRect = self.addTrackingRect_owner_userData_assumeInside_(self.bounds(), self, 0, 0)

    def setGridColor(self, color=NSColor.greenColor()):
        self.gridColor = color

    def setRmsColor(self, color=NSColor.blueColor()):
        self.rmsColor = color

    def setGraphColor(self, color=NSColor.blackColor()):
        self.graphColor = color

    def setGain(self, gain, total):
        self.gain = gain
        self.totalField = total

    def setLines(self, lines):
        self.lines = lines

    def setMapImage(self, mapImage):
        self.mapImage = mapImage
        self.mapRect = ((0, 0), mapImage.size())

    def setPath(self, path, maxMag):
        self.path = path
        self.maxMag = maxMag
        self.setNeedsDisplay_(1)


    def drawRect_(self, rect):
        frame = self.frame()
        self.origin = frame[0]
        self.graphCenter = (frame[sze][x]/2, frame[sze][y]/2)
        self.graphRadius = (min(frame[sze][x], frame[sze][y]) / 2) - self.graphMargin

        NSColor.whiteColor().set()
        NSRectFill(self.bounds())

        self.drawMap()
        self.drawGrid()
        self.drawRMS()
        self.drawField()

    def drawMap(self):
        if self.mapImage == 0:
            return

        scale = self.mapScale * (self.graphRadius / self.mapBaseRadius) * self.gain / self.totalField
        xImageSize = scale * self.mapRect[sze][x]
        yImageSize = scale * self.mapRect[sze][y]
        xCenterMove = self.graphCenter[x] - self.graphRadius
        yCenterMove = self.graphCenter[y] - self.graphRadius

        xOffset = -((1 - self.mapOffsetEW) / 2) * xImageSize
        yOffset = -((1 + self.mapOffsetNS) / 2) * yImageSize
        xOffset += self.graphRadius + xCenterMove
        yOffset += self.graphRadius + yCenterMove

        drawInRect = ((xOffset, yOffset), (xImageSize, yImageSize))

        self.mapImage.drawInRect_fromRect_operation_fraction_(drawInRect, self.mapRect, NSCompositeSourceOver, self.mapVisible)

    def drawGrid(self):
        self.gridColor.set()
        self.drawCircle(1.0)
        self.drawAxisLines()

    def drawCircle(self, scale):
        center = self.graphCenter
        radius = self.graphRadius*scale
        x, y = 0, 1
        if radius >= 1:
            dotRect = ((center[x]-radius, center[y]-radius), (2*radius, 2*radius))
            path = NSBezierPath.bezierPathWithOvalInRect_(dotRect)
            path.stroke()

    def drawRMS(self):
        self.rmsColor.set()
        self.drawCircle(self.gain)

    def drawAxisLines(self):
        center = self.graphCenter
        radius = self.graphRadius
        x, y = 0, 1
        path = NSBezierPath.bezierPath()
        for i in range(1, self.lines+1):
            iR = pi / i
            cosR = cos(iR) * radius
            sinR = sin(iR) * radius

            path.moveToPoint_((center[x] - cosR, center[y] - sinR))
            path.lineToPoint_((center[x] + cosR, center[y] + sinR))
        path.closePath()
        path.stroke()

    def drawField(self):
        if self.maxMag:         # Don't want to divide by zero in the pathological case
            self.graphColor.set()
            path = self.path.copy()

            transform = NSAffineTransform.transform()
            transform.rotateByRadians_(-(pi / 2.0) - self.azmuth)
            path.transformUsingAffineTransform_(transform)

            transform = NSAffineTransform.transform()
            center = self.graphCenter
            transform.translateXBy_yBy_(center[0], center[1])
            transform.scaleBy_(self.graphRadius / self.maxMag)
            path.transformUsingAffineTransform_(transform)

            path.stroke()


#____________________________________________________________
# Handle GUI values
    @objc.IBAction
    def mapVisibleSlider_(self, sender):
        self.mapVisible = (sender.floatValue())
        self.setNeedsDisplay_(1)

    @objc.IBAction
    def azmuthDisplay_(self, sender):
        self.setAzmuth(sender.floatValue())

    @objc.IBAction
    def azmuthSlider_(self, sender):
        self.setAzmuth(sender.floatValue())

    def setAzmuth(self, value):
        self.azmuth = degToRad(value)
        self.azmuthSlider.setFloatValue_(value)
        self.azmuthDisplay.setFloatValue_(value)
        self.setNeedsDisplay_(1)

    @objc.IBAction
    def mapScaleDisplay_(self, sender):
        self.mapScale = sender.floatValue()
        self.setMapRect()

    @objc.IBAction
    def mapScaleSlider_(self, sender):
        self.mapScale = sender.floatValue()
        self.setMapRect()

    @objc.IBAction
    def mapOffsetNSDisplay_(self, sender):
        self.mapOffsetNS = sender.floatValue()
        self.setMapRect()

    @objc.IBAction
    def mapOffsetNSSlider_(self, sender):
        self.mapOffsetNS = sender.floatValue()
        self.setMapRect()

    @objc.IBAction
    def mapOffsetEWDisplay_(self, sender):
        self.mapOffsetEW = sender.floatValue()
        self.setMapRect()

    @objc.IBAction
    def mapOffsetEWSlider_(self, sender):
        self.mapOffsetEW = sender.floatValue()
        self.setMapRect()

    def mouseUp_(self, event):
        loc = event.locationInWindow()
        xLoc = loc[x] - self.origin[x]
        yLoc = loc[y] - self.origin[y]
        xDelta = self.graphCenter[x] - xLoc
        yDelta = self.graphCenter[y] - yLoc


        scale = 0.5 * self.mapScale * (self.gain / self.totalField) * (self.graphRadius / self.mapBaseRadius)
        xOffset = xDelta / (scale * self.mapRect[sze][x])
        yOffset = yDelta / (scale * self.mapRect[sze][y])

        self.mapOffsetEW += xOffset
        self.mapOffsetNS -= yOffset
        self.setMapRect()

    def mouseDown_(self, event):
        self.crossCursor.set()


    def setMapRect(self):
        self.mapScaleDisplay.setFloatValue_(self.mapScale)
        self.mapScaleSlider.setFloatValue_(self.mapScale)
        self.mapOffsetEWDisplay.setFloatValue_(self.mapOffsetEW)
        self.mapOffsetEWSlider.setFloatValue_(self.mapOffsetEW)
        self.mapOffsetNSDisplay.setFloatValue_(self.mapOffsetNS)
        self.mapOffsetNSSlider.setFloatValue_(self.mapOffsetNS)
        self.setNeedsDisplay_(1)

    def mouseEntered_(self, event):
        print 'CGraphView: mouseEntered_'

    def mouseExited_(self, event):
        print 'CGraphView: mouseExited_'
