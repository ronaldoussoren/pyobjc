import unittest
import objc
import os

from objc import YES, NO
from AppKit import NSWorkspace


class TestNSWorkspace(unittest.TestCase):
    def testInfoForFile(self):
        ws = NSWorkspace.sharedWorkspace()

        # A method with 2 output parameters, this means the result
        # is a tuple with 3 elements (return value, param1, param2)
        res = ws.getInfoForFile_application_type_(u'/', None, None)
        self.assert_(isinstance(res, tuple))
        self.assert_(len(res) == 3)
        self.assert_(res[0] == 1)
        self.assert_(res[1] == u'/System/Library/CoreServices/Finder.app')
        self.assert_(res[2] == u'')

if __name__ == '__main__':
    unittest.main( )
