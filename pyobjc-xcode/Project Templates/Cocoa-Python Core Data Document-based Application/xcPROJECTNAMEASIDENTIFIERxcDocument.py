#
#  xcPROJECTNAMEASIDENTIFIERxcDocument.py
#  xcPROJECTNAMExc
#
#  Created by xcFULLUSERNAMExc on xcDATExc.
#  Copyright xcORGANIZATIONNAMExc xcYEARxc. All rights reserved.
#

from Foundation import *
from CoreData import *
from AppKit import *

class xcPROJECTNAMEASIDENTIFIERxcDocument(NSPersistentDocument):
    def init(self):
        self = super(xcPROJECTNAMEASIDENTIFIERxcDocument, self).init()
        # initialization code
        return self
        
    def windowNibName(self):
        return u"xcPROJECTNAMEASIDENTIFIERxcDocument"
    
    def windowControllerDidLoadNib_(self, aController):
        super(xcPROJECTNAMEASIDENTIFIERxcDocument, self).windowControllerDidLoadNib_(aController)
        # user interface preparation code
