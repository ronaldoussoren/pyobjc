#
#  MyDocument.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#

from objc import YES, NO
from Foundation import *
from AppKit import *

from PyObjCTools import NibClassBuilder

NibClassBuilder.extractClasses("MyDocument")
class MyDocument(NibClassBuilder.AutoBaseClass):
    def init(self):
        self = super(MyDocument, self).init()
        if self:
            # subclass specific initialization here
            # nib not loaded yet
            pass
        return self

    def windowNibName(self):
        # the name of the NIB file containing the document UI
        return "MyDocument"

    def windowControllerDidLoadNib_(self, aController):
        super(MyDocument, self).windowControllerDidLoadNib_(aController)
        # initialize document UI after window controller loads NIB

    def dataRepresentationOfType_(self, aType):
        # return an NSData containing the document's data represented as
        # the type identified by aType.
        return nil

    def loadDataRepresentation_ofType_(self, data, aType):
        # load document from data (NSData instance) by interpreting
        # it as the type identified by aType.
        return YES
        
    def changeHueAction_(self, sender):
        """
        An example of a standard target action method implementation.
        """
        newHue = self.hueSlider.floatValue()
        self.hueView.setHue_(newHue)
    
    def awakeFromNib(self):
        """
        awakeFromNib() is invoked when the NIB that caused this object
        to be instantiated is loaded (MainMenu.nib).
        """
        self.changeHueAction_(None)
