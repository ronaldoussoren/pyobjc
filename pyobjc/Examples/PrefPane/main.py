"""
Example showing of preference panes in Python
"""
print "loading python prefpane"

from AppKit import *
from Foundation import NSBundle
from PreferencePanes import *
import objc
from PyObjCTools import NibClassBuilder

# NibClassBuilder needs to read our Nib files to do its work,
# we need to specify the optional second argument to extractClasses
# because we're not in the main bundle.
NibClassBuilder.extractClasses("SimplePreferencePane", 
    objc.pluginBundle("SimplePreferencePane"))

class SimplePreferencePane (NibClassBuilder.AutoBaseClass):

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
