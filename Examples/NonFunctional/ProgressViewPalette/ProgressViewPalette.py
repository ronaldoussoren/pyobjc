import os, sys
sys.path.append(os.path.dirname(__file__))
from InterfaceBuilder import *
from ProgressView import ProgressView
from ProgressCell import ProgressCell
import objc
from AppKit import *

objc.setVerbose(1) ### DEBUG

class ProgressViewPalette (IBPalette):
    def finishInstantiate(self):
        # `finishInstantiate' can be used to associate non-view objects with
        # a view in the palette's nib.  For example:
        # self.associateObject_ofType_withView_(aNonUIObject,
        #       IBObjectPboardType , self.aView)
        pass

    def init(self):
        self = super(ProgressViewPalette, self).init()
        if self is None: return None

        NSView.registerViewResourceDraggingDelegate_(self)
        return self

    # Implementation functions for IBViewResourceDraggingDelegates protocol

    def viewResourcePasteboardTypes(self):
        return [NSColorPboardType]

    def acceptsViewResourceFromPasteboard_forObjeect_atPoint_(self,
            pasteboard, object, point):

        if NSColorPboardType in pasteboard.types():
            if isinstance(object, NSMatrix):
                b, row, column = object.getRow_column_forPoint_(point)
                if b:
                    cell = object.cellAtRow_column_(row, column)
                    if cell.respondsToSelector_('setColor:'):
                        return True
        if object.respondsToSelector_('setColor:'):
            return True
        return False

    def depositViewResourceFromPasteboard_onObject_atPoint_(
            self, pasteboard, object, point):

        color = NSColor.colorFromPasteboard_(pasteboard)

        if isinstance(object, NSMatrix):
            b, row, column = object.getRow_column_forPoint_(row, column, point)
            if b:
                cell = object.cellAtRow_column_(row, column)
                if cell.respondsToSelector_('setColor:'):
                    cell.setColor_(color)
        else:
            if object.respondsToSelector_('setColor:'):
                object.setColor_(color)

    def shouldDrawConnectionFrame(self):
        return True


#
# Poor mans categories...
#

ProgressView.inspectorClassName = lambda self: "ProgressViewInspector"
ProgressView.allowsAltDragging = lambda self: True

ProgressCell.inspectorClassName = lambda self: "ProgressViewInspector"

def ibMatchPrototype_(self, prototype):
    super(ProgressCell, self).ibMatchPrototype_(prototype)
    self.setPercentageIncrement_(prototype.percentageIncrement())

ProgressCell.ibMatchPrototype_ = ibMatchPrototype_
