"""
Some tests for the NSAttributedString extensions in AppKit
"""
import unittest
import AppKit
from Foundation import *
import objc

class TestAttributedString (unittest.TestCase):
    def testInitWithData(self):
        text = buffer("<B>hello world</B>")

        strval, attr, err = NSAttributedString.alloc(
                ).initWithData_options_documentAttributes_error_(
                    text, {})

        self.assert_(isinstance(strval, NSAttributedString))
        self.assertEquals(strval.string(), "<B>hello world</B>")
        self.assert_(isinstance(attr, NSDictionary))
        self.assert_(err is None)

    def testInitWithURL(self):
        filePath = __file__
        if filePath[-1] == 'c':
            # Make sure we're not reading the compiled file, which isn't text
            # and confuses this this.
            filePath = filePath[:-1]

        url = NSURL.fileURLWithPath_(filePath)

        strval, attr, err = NSAttributedString.alloc(
                ).initWithURL_options_documentAttributes_error_(
                    url, {})

        self.assert_(isinstance(strval, NSAttributedString))
        self.assertEquals(strval.string(), open(filePath, 'rb').read())
        self.assert_(isinstance(attr, NSDictionary))
        self.assert_(err is None)

    def testOthers(self):
        for attr in [
                'initWithData_options_documentAttributes_error_',
                'initWithURL_options_documentAttributes_error_',
                'initWithDocFormat_documentAttributes_',
                'initWithHTML_baseURL_documentAttributes_',
                'initWithHTML_documentAttributes_',
                'initWithHTML_options_documentAttributes_',
                'initWithPath_documentAttributes_',
                'initWithRTF_documentAttributes_',
                'initWithRTFD_documentAttributes_',
                'initWithURL_documentAttributes_',
            ]:

                m = getattr(NSAttributedString, attr)
                parts = objc.splitSignature(m.signature)
                for p in parts:
                    self.assertNotEquals(p[:1], '^')

if __name__ == "__main__":
    unittest.main()
