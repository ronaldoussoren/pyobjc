from ProgressView import ProgressView
from AppKit import *
from Foundation import *
from InterfaceBuilder import *
import objc

class ProgressViewInspector(IBInspector):
    slider = objc.IBOutlet('slider')
    textField = objc.IBOutlet('textField')
    colorWell = objc.IBOutlet('colorWell')

    def init(self):
        self = super(ProgressViewInspector, self).init()
        if self is None:
            return None

        if not NSBundle.loadNibNamed_owner_("ProgressViewInspector", self):
            NSLog("Couldn't load ProgressViewInspector.nib")
        return self

    def ok_(self, sender):
        """
        Modify object state
        """
        if sender is self.slider:
            self.object().setPercentageIncrement_(sender.intValue())
            self.textField.setIntValue_(sender.intValue())
        elif sender is self.textField:
            self.object().setPercentageIncrement_(sender.floatValue())
            self.slider.setFloatValue_(sender.floatValue())
        elif sender is self.colorWell:
            self.object().setColor_(self.colorWell.color())
        super(ProgressViewInspector, self).ok_(sender)

    def revert_(self, sender):
        """
        Revert to object state
        """
        percentageIncrement = self.object().percentageIncrement()
        self.slider.setFloatValue_(percentageIncrement)
        self.textField.setFloatValue_(percentageIncrement)
        self.colorWell.setColor_(self.object().color())
        super(ProgressViewInspector, self).revert_(sender)

    def wantsButtons(self):
        return False
