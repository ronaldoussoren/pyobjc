#
#  GraphicsBindingsDocument.py
#  GraphicsBindings
#
#  Converted by u.fiedler on feb 2005
#  with great help from Bob Ippolito - Thank you Bob!
#
#  The original version was written in Objective-C by Malcolm Crawford
#  http://homepage.mac.com/mmalc/CocoaExamples/controllers.html

import objc
from PyObjCTools import NibClassBuilder, AppHelper

from RadiansToDegreesTransformer import RadiansToDegreesTransformer
from Foundation import * 

NibClassBuilder.extractClasses("GraphicsBindingsDocument")

class GraphicsBindingsDocument(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSDocument
    # The following outlets are added to the class:
    # graphicsView, shadowInspector, graphicsController

    graphics = objc.ivar('graphics')

    def init(self):
        self = super(GraphicsBindingsDocument, self).init()
        if self is None:
            return None
        self.graphics = [] # NSMutableArray.array()
        self.bindings = []
        return self

    def windowNibName(self):
        return "GraphicsBindingsDocument"

    def makeBinding_fromObject_toObject_withKeyPath_options_(self, key, fromObject, toObject, withKeyPath, options):
        self.bindings.append((fromObject, key))
        fromObject.bind_toObject_withKeyPath_options_(key, toObject, withKeyPath, options)

    def windowControllerDidLoadNib_(self, controller):
        super(GraphicsBindingsDocument, self).windowControllerDidLoadNib_(controller)
        
        # we can't do these in IB at the moment, as
        # we don't have palette items for them

        # allow the shadow inspector (joystick) to handle multiple selections
        offsetOptions = { u"NSAllowsEditingMultipleValuesSelection" : True }
        angleOptions = {
            u"NSValueTransformerName" :  u"RadiansToDegreesTransformer",
            u"NSAllowsEditingMultipleValuesSelection" : True,
        }

        BINDINGS = [
            (u'graphics',  self.graphicsView, self.graphicsController, u'arrangedObjects', None),
            (u'selectionIndexes', self.graphicsView, self.graphicsController, u'selectionIndexes', None),
            (u'offset', self.shadowInspector, self.graphicsController, u'selection.shadowOffset', offsetOptions),
            (u'angle', self.shadowInspector, self.graphicsController, u'selection.shadowAngle', angleOptions),
        ]
        for binding in BINDINGS:
            self.makeBinding_fromObject_toObject_withKeyPath_options_(*binding)

        # "fake" what should be set in IB if we had a palette...
        self.shadowInspector.maxOffset = 15
        
    def close(self):
        while self.bindings:
            obj, binding = self.bindings.pop()
            obj.unbind_(binding)
        super(GraphicsBindingsDocument, self).close()
            
    def dataRepresentationOfType_(self, aType):
        return NSKeyedArchiver.archivedDataWithRootObject_(self.graphics)
        
    def loadDataRepresentation_ofType_(self, data, aType):
        self.graphics = NSKeyedUnarchiver.unarchiveObjectWithData_(data)
        return True

vt = RadiansToDegreesTransformer.alloc().init()
NSValueTransformer.setValueTransformer_forName_(vt, u"RadiansToDegreesTransformer")

