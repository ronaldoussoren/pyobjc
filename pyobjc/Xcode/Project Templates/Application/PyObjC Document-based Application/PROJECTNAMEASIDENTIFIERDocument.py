#
#  ÇPROJECTNAMEASIDENTIFIERÈDocument.py
#  ÇPROJECTNAMEASIDENTIFIERÈ
#

from Foundation import *
from AppKit import *
import objc

from PyObjCTools import NibClassBuilder

class ÇPROJECTNAMEASIDENTIFIERÈDocument(NibClassBuilder.AutoBaseClass):

    # textView outlet is in the nib
    # path is an instance variable, initialized to None
    path = objc.ivar('path')
    
    def windowNibName(self):
        return u'ÇPROJECTNAMEASIDENTIFIERÈDocument'
    
    def readFromFile_ofType_(self, path, typ):
        if self.textView is None:
            # we're not yet fully loaded
            self.path = path
        else:
            # "revert"
            self.readFromUTF8File_(path)
        return True
    
    def writeToFile_ofType_(self, path, typ):
        f = file(path, 'w')
        text = self.textView.string()
        f.write(text.encode('utf8'))
        f.close()
        return True
    
    def windowControllerDidLoadNib_(self, controller):
        if self.path is not None:
            self.readFromUTF8File_(self.path)
    
    def readFromUTF8File_(self, path):
        f = file(path)
        text = unicode(f.read(), "utf8")
        f.close()
        self.textView.setString_(text)