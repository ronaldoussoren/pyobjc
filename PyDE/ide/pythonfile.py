"""
Support for Python source files
"""
from AppKit import *

from PyObjCTools import NibClassBuilder
import re

NIBNAME="PythonDocument"

NibClassBuilder.extractClasses(NIBNAME)

UNKNOWN_ENCODING_WR="""\
The source code specifies a source code encoding that is unknown to the
runtime system. Please specify a different encoding (such as utf-8).

Your file is not saved.
"""


ENCODING_FAILED="""\
The source file does not specify an encoding, or specifies an encoding that
cannot represent all characters used in the file. Please specify a different
encoding (such as utf-8).

Your file is not saved.
"""


class PyDEPythonDocument (NibClassBuilder.AutoBaseClass):
    """
    Document class for a python source file
    """

    path = None

    def windowNibName(self):
        """ Return the name of our NIB file """
        return NIBNAME

    def readFromFile_ofType_(self, path, tp):
        """ Read document from a file """

        if self.textView is None:
            # We're not fully loaded yet, store the path
            self.path = path
        else:
            self.readPythonFile(path)
        return True

    def writeToFile_ofType_(self, path, tp):
        """ Save document to a file """

        text = self.textView.string()
        encoding = self.guessEncoding(text)

        try:
            text = text.encode(encoding)

        except LookupError:
            NSBeginAlertSheet(
                    "Cannot encode file",
                    "ok", None, None, self.textView.window(),
                    None, None, None, 0,  UNKNOWN_ENCODING_WR)
            return False

        except UnicodeDecodeError:
            NSBeginAlertSheet(
                    "Cannot encode file",
                    "ok", None, None, self.textView.window(),
                    None, None, None, 0,  ENCODING_FAILED)
            return False

        fp = open(path, 'w')
        fp.write(text)
        fp.close()
        return True

    def windowControllerDidLoadNib_(self, controller):
        """ Our NIB did load, finish initialization """
        if self.path:
            self.readPythonFile(self.path)

    def guessEncoding(self, text):
        """
        Return the encoding for a python source file

        The default is ASCII, but that can be changed using a PEP-263 cookie
        """

        encoding = 'ascii'
        lines = text.split('\n', 2)[:2]
        for ln in lines:
            m = re.search(r'coding[:=]\s*([A-Za-z0-9-_.]+)', ln)
            if m is not None:
                return m.group(1)

        return encoding

    def readPythonFile(self, path):
        """
        Read a python source file
        """
        fp = open(path)
        text = fp.read()
        fp.close()

        # XXX: Decoding might fail as wel (invalid encoding, or the decoder
        # failed). Show an alertsheet that allows to user to load the text
        # using some default encoding.
        encoding = self.guessEncoding(text)
        text = unicode(text, encoding)
        self.textView.setString_(text)
