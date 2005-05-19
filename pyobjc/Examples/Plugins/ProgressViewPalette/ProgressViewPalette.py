import objc
from Foundation import *
from AppKit import *
from InterfaceBuilder import *
from ProgressView import ProgressView
from ProgressCell import ProgressCell
from ProgressViewInspector import ProgressViewInspector
#import pprint, os

#objc.setVerbose(1) ### DEBUG

#NSLog(u'ProgressViewPalette.py loaded')
#pprint.pprint(dict(os.environ))

class ProgressViewPalette (IBPalette):
    def finishInstantiate(self):
        # `finishInstantiate' can be used to associate non-view objects with
        # a view in the palette's nib.  For example:
        # self.associateObject_ofType_withView_(aNonUIObject,
        #       IBObjectPboardType , self.aView)
        pass

    def init(self):
        self = super(ProgressViewPalette, self).init()
        if self is None:
            return None

        NSView.registerViewResourceDraggingDelegate_(self)
        return self

    # Implementation functions for IBViewResourceDraggingDelegates protocol

    def viewResourcePasteboardTypes(self):
        return [NSColorPboardType]

    def acceptsViewResourceFromPasteboard_forObject_atPoint_(self,
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

class ProgressView(objc.Category(ProgressView)):
    def inspectorClassName(self):
        return u'ProgressViewInspector'

    def allowsAltDragging(self):
        return True

class ProgressCell(objc.Category(ProgressCell)):
    def inspectorClassName(self):
        return u'ProgressViewInspector'

    def ibMatchPrototype_(self, prototype):
        super(ProgressCell, self).ibMatchPrototype_(prototype)
        self.setPercentageIncrement_(prototype.percentageIncrement())
