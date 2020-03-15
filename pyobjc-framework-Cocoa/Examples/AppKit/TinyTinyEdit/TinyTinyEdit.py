"""TinyTinyEdit -- A minimal Document-based Cocoa application."""

import Cocoa
import objc
import sys
from PyObjCTools import AppHelper


class TinyTinyDocument(Cocoa.NSDocument):
    textView = objc.IBOutlet()
    path = None

    def windowNibName(self):
        return "TinyTinyDocument"

    def readFromFile_ofType_(self, path, tp):
        if self.textView is None:
            # we're not yet fully loaded
            self.path = path
        else:
            # "revert"
            self.readFromUTF8_(path)
        return True

    def writeToFile_ofType_(self, path, tp):
        with open(path, "w") as f:
            text = self.textView.string()
            if sys.version_info[0] == 2:
                text = text.encode("utf-8")
            f.write(text)
        return True

    def windowControllerDidLoadNib_(self, controller):
        if self.path:
            self.readFromUTF8_(self.path)

    def readFromUTF8_(self, path):
        with open(path, "r") as f:
            text = f.read()

        if sys.version_info[0] == 2:
            text = text.decode("utf-8")
        self.textView.setString_(text)


if __name__ == "__main__":
    AppHelper.runEventLoop()
