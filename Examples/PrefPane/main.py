"""
Example showing of preference panes in Python
"""
print "loading python prefpane"

from AppKit import *
from PreferencePanes import *
import objc

class SimplePreferencePane (NSPreferencePane):
    value1Field = objc.IBOutlet('value1Field')
    value2Field = objc.IBOutlet('value2Field')
    resultField = objc.IBOutlet('resultField')
    button = objc.IBOutlet('button')

    def doIt_(self, sender):
        v1 = self.value1Field.floatValue()
        v2 = self.value2Field.floatValue()

        res = v1 + v2
        self.resultField.setFloatValue_(res)

    def initWithBundle_(self, bundle):
        self = super(SimplePreferencePane, self).initWithBundle_(bundle)
        if self is None: return None

        return self

    def mainViewDidLoad(self):
        print "mainViewDidLoad"
        self.value1Field.setFloatValue_(1.0)
        self.value2Field.setFloatValue_(2.0)

    def didSelect(self):
        print "selected"

    def didUnselect(self):
        print "Unselected"
