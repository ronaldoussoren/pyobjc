from Foundation import NSObject
from PyObjCTools import NibClassBuilder, AppHelper
from objc import *

from CGraphModel import *

NibClassBuilder.extractClasses("MainMenu")


#____________________________________________________________
class CGraphController(NibClassBuilder.AutoBaseClass):

#____________________________________________________________
# Update GUI display and control values
	def awakeFromNib(self):
		self.RMSGainDisplayValue.setFloatValue_(self.graphModel.getRMSGain())
		self.towerSpacingDisplayValue.setFloatValue_(radToDeg(self.graphModel.getSpacing()))
		self.towerSpacingSliderValue.setFloatValue_(radToDeg(self.graphModel.getSpacing()))
		self.towerFieldDisplayValue0.setFloatValue_(self.graphModel.getField(0))
		self.towerFieldDisplayValue1.setFloatValue_(self.graphModel.getField(1))
		self.towerFieldDisplayValue2.setFloatValue_(self.graphModel.getField(2))
		self.towerFieldSliderValue0.setFloatValue_(self.graphModel.getField(0))
		self.towerFieldSliderValue1.setFloatValue_(self.graphModel.getField(1))
		self.towerFieldSliderValue2.setFloatValue_(self.graphModel.getField(2))
		self.towerPhaseDisplayValue0.setFloatValue_(radToDeg(self.graphModel.getPhase(0)))
		self.towerPhaseDisplayValue1.setFloatValue_(radToDeg(self.graphModel.getPhase(1)))
		self.towerPhaseDisplayValue2.setFloatValue_(radToDeg(self.graphModel.getPhase(2)))
		self.towerPhaseSliderValue0.setFloatValue_(radToDeg(self.graphModel.getPhase(0)))
		self.towerPhaseSliderValue1.setFloatValue_(radToDeg(self.graphModel.getPhase(1)))
		self.towerPhaseSliderValue2.setFloatValue_(radToDeg(self.graphModel.getPhase(2)))

		self.graphModel.drawGraph()


#____________________________________________________________
# Handle GUI values
	def towerFieldDisplayValueControl0_(self, sender):
		self.graphModel.setField(0, sender.floatValue())
		self.awakeFromNib()

	def towerFieldDisplayValueControl1_(self, sender):
		self.graphModel.setField(1, sender.floatValue())
		self.awakeFromNib()

	def towerFieldDisplayValueControl2_(self, sender):
		self.graphModel.setField(2, sender.floatValue())
		self.awakeFromNib()

	def towerFieldSliderValueControl0_(self, sender):
		self.graphModel.setField(0, sender.floatValue())
		self.awakeFromNib()

	def towerFieldSliderValueControl1_(self, sender):
		self.graphModel.setField(1, sender.floatValue())
		self.awakeFromNib()

	def towerFieldSliderValueControl2_(self, sender):
		self.graphModel.setField(2, sender.floatValue())
		self.awakeFromNib()

	def towerPhaseDisplayValueControl0_(self, sender):
		self.graphModel.setPhase(0, degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerPhaseDisplayValueControl1_(self, sender):
		self.graphModel.setPhase(1, degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerPhaseDisplayValueControl2_(self, sender):
		self.graphModel.setPhase(2, degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerPhaseSliderValueControl0_(self, sender):
		self.graphModel.setPhase(0, degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerPhaseSliderValueControl1_(self, sender):
		self.graphModel.setPhase(1, degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerPhaseSliderValueControl2_(self, sender):
		self.graphModel.setPhase(2, degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerSpacingDisplayValueControl_(self, sender):
		self.graphModel.setSpacing(degToRad(sender.floatValue()))
		self.awakeFromNib()

	def towerSpacingSliderValueControl_(self, sender):
		self.graphModel.setSpacing(degToRad(sender.floatValue()))
		self.awakeFromNib()
