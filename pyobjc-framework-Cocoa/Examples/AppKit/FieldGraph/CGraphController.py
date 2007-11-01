from Foundation import NSObject
from PyObjCTools import NibClassBuilder, AppHelper
from objc import *

from CGraphModel import *
from CGraphView import *
from fieldMath import *


NibClassBuilder.extractClasses("MainMenu")


#____________________________________________________________
class CGraphController(NibClassBuilder.AutoBaseClass):

#____________________________________________________________
# Update GUI display and control values

    def awakeFromNib(self):
        self.mapImage = NSImage.imageNamed_("Map")
        self.graphView.setMapImage(self.mapImage)
        self.drawGraph()

    def drawGraph(self):
        self.spacingDisplay.setFloatValue_(radToDeg(self.graphModel.getSpacing()))
        self.spacingSlider.setFloatValue_(radToDeg(self.graphModel.getSpacing()))
        self.fieldDisplay0.setFloatValue_(self.graphModel.getField(0))
        self.fieldDisplay1.setFloatValue_(self.graphModel.getField(1))
        self.fieldDisplay2.setFloatValue_(self.graphModel.getField(2))
        self.fieldSlider0.setFloatValue_(self.graphModel.getField(0))
        self.fieldSlider1.setFloatValue_(self.graphModel.getField(1))
        self.fieldSlider2.setFloatValue_(self.graphModel.getField(2))
        self.phaseDisplay0.setFloatValue_(radToDeg(self.graphModel.getPhase(0)))
        self.phaseDisplay1.setFloatValue_(radToDeg(self.graphModel.getPhase(1)))
        self.phaseDisplay2.setFloatValue_(radToDeg(self.graphModel.getPhase(2)))
        self.phaseSlider0.setFloatValue_(radToDeg(self.graphModel.getPhase(0)))
        self.phaseSlider1.setFloatValue_(radToDeg(self.graphModel.getPhase(1)))
        self.phaseSlider2.setFloatValue_(radToDeg(self.graphModel.getPhase(2)))

        totalField = self.graphModel.getField(0) + self.graphModel.getField(1) + self.graphModel.getField(2)

        RMSGain = self.graphModel.fieldGain()
        self.graphView.setGain(RMSGain, totalField)
        self.RMSGainDisplay.setFloatValue_(RMSGain*100.0)

        path, maxMag  = self.graphModel.getGraph()
        self.graphView.setPath(path, maxMag)


#____________________________________________________________
# Handle GUI values

    def fieldDisplay0_(self, sender):
        self.setNormalizedField(0, sender.floatValue())
        self.drawGraph()

    def fieldDisplay1_(self, sender):
        self.setNormalizedField(1, sender.floatValue())
        self.drawGraph()

    def fieldDisplay2_(self, sender):
        self.setNormalizedField(2, sender.floatValue())
        self.drawGraph()

    def fieldSlider0_(self, sender):
        self.setNormalizedField(0, sender.floatValue())
        self.drawGraph()

    def fieldSlider1_(self, sender):
        self.setNormalizedField(1, sender.floatValue())
        self.drawGraph()

    def fieldSlider2_(self, sender):
        self.setNormalizedField(2, sender.floatValue())
        self.drawGraph()

    def setNormalizedField(self, t, v):
        if self.fieldNormalizeCheck.intValue():
            f = [0, 0, 0]
            cft = 0
            for i in range(3):
                f[i] = self.graphModel.getField(i)
                cft += f[i]

            aft = cft - v
            if aft < 0.001:
                v = cft - 0.001
                aft = 0.001
            f[t] = v

            nft = 0
            for i in range(3):
                nft +=  f[i]
            r = aft / (nft - f[t])

            for i in range(3):
                self.graphModel.setField(i, f[i] * r)
            self.graphModel.setField(t, v)

        else:
            self.graphModel.setField(t, v)



    def phaseDisplay0_(self, sender):
        self.graphModel.setPhase(0, degToRad(sender.floatValue()))
        self.drawGraph()

    def phaseDisplay1_(self, sender):
        self.graphModel.setPhase(1, degToRad(sender.floatValue()))
        self.drawGraph()

    def phaseDisplay2_(self, sender):
        self.graphModel.setPhase(2, degToRad(sender.floatValue()))
        self.drawGraph()

    def phaseSlider0_(self, sender):
        self.graphModel.setPhase(0, degToRad(sender.floatValue()))
        self.drawGraph()

    def phaseSlider1_(self, sender):
        self.graphModel.setPhase(1, degToRad(sender.floatValue()))
        self.drawGraph()

    def phaseSlider2_(self, sender):
        self.graphModel.setPhase(2, degToRad(sender.floatValue()))
        self.drawGraph()

    def spacingDisplay_(self, sender):
        self.graphModel.setSpacing(degToRad(sender.floatValue()))
        self.drawGraph()

    def spacingSlider_(self, sender):
        self.graphModel.setSpacing(degToRad(sender.floatValue()))
        self.drawGraph()

    def settingDrawerButton_(self, sender):
        self.settingDrawer.toggle_(self)
