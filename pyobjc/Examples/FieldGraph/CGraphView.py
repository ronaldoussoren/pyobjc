from Foundation import NSObject
from PyObjCTools import NibClassBuilder
from objc import *

from AppKit import NSBezierPath, NSColor, NSRectFill, NSAffineTransform
from math import pi, sin, cos

#____________________________________________________________
class CGraphView(NibClassBuilder.AutoBaseClass):

	def awakeFromNib(self):
		self.lines = 2
		self.gain = 0.5
	
	def initWithFrame_(self, frame):
		super(CGraphView, self).initWithFrame_(frame)
		self.setGridColor()
		self.setRmsColor()
		self.setGraphColor()
		return self
		
	def setGridColor(self, color=NSColor.greenColor()):
		self.gridColor = color
		
	def setRmsColor(self, color=NSColor.blueColor()):
		self.rmsColor = color
		
	def setGraphColor(self, color=NSColor.blackColor()):
		self.graphColor = color
		
	def setGain(self, gain):
		self.gain = gain
		
	def setLInes(self, lines):
		self.lines = lines
		
	def setPath(self, path, maxMag):
		self.path = path
		if maxMag < 1e-5:
			# prevent divide by zero
			maxMag = 1e-5
		self.maxMag = maxMag
		
	def drawRect_(self, rect):
		frame = self.frame()
		self.graphCenter = (frame[1][0]/2, frame[1][1]/2)
		self.graphRadius = min(frame[1][0], frame[1][1]) / 2 - 4
		
		NSColor.whiteColor().set()
		NSRectFill(self.bounds())
		
		self.drawGrid()
		self.drawRMS()
		self.drawField()
		
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
		transform = NSAffineTransform.transform()
		center = self.graphCenter
		transform.translateXBy_yBy_(center[0], center[1])
		transform.scaleBy_(self.graphRadius / self.maxMag)
		path = self.path.copy()
		path.transformUsingAffineTransform_(transform)
		self.graphColor.set()
		path.stroke()
