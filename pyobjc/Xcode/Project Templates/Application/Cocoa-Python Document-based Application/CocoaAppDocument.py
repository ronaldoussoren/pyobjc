#
#  ÇPROJECTNAMEASIDENTIFIERÈDocument.py
#  ÇPROJECTNAMEÈ
#
#  Created by ÇFULLUSERNAMEÈ on ÇDATEÈ.
#  Copyright (c) ÇYEARÈ ÇORGANIZATIONNAMEÈ. All rights reserved.
#



from PyObjCTools import NibClassBuilder, AppHelper


NibClassBuilder.extractClasses("ÇPROJECTNAMEASIDENTIFIERÈDocument")


# class defined in TinyTinyDocument.nib
class ÇPROJECTNAMEASIDENTIFIERÈDocument(NibClassBuilder.AutoBaseClass):
    # the actual base class is NSDocument
    # The following outlets are added to the class:
    # textView

    path = None

    def windowNibName(self):
        return "ÇPROJECTNAMEASIDENTIFIERÈDocument"

    def readFromFile_ofType_(self, path, tp):
        if self.textView is None:
            # we're not yet fully loaded
            self.path = path
        else:
            # "revert"
            self.readFromUTF8(path)
        return True

    def writeToFile_ofType_(self, path, tp):
        f = file(path, "w")
        text = self.textView.string()
        f.write(text.encode("utf8"))
        f.close()
        return True

    def windowControllerDidLoadNib_(self, controller):
        if self.path:
            self.readFromUTF8(self.path)

    def readFromUTF8(self, path):
        f = file(path)
        text = unicode(f.read(), "utf8")
        f.close()
        self.textView.setString_(text)
