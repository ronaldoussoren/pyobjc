import unittest

import objc

class TestRegressions(unittest.TestCase):
    def testQualifiersInSignature(self):
        import Foundation
        import AppKit
        AppKit.NSColor.redColor().getRed_green_blue_alpha_()

    def testOpenPanelSignature(self):
        """
        This test failed sometime after the 1.0b1 release (on Panther).
        """
        import AppKit

        o = AppKit.NSOpenPanel.openPanel()
        sig = o.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_.signature
        dclass= o.beginSheetForDirectory_file_types_modalForWindow_modalDelegate_didEndSelector_contextInfo_.definingClass
        sig = ''.join(objc.splitSignature(sig))
        self.assertEquals(
            sig,
            'v@:@@@@@:i')

    def testFSRepr(self):
        import Foundation
        fm = Foundation.NSFileManager.defaultManager()
        self.assertRaises(TypeError, fm.stringWithFileSystemRepresentation_length_, "/var")
        self.assertEquals(u"/var", fm.stringWithFileSystemRepresentation_length_("/var/boo", 4))

    def testUninitWarning(self):
        """
        Check that calling methods on unitialized objects raises an error
        """
        import warnings
        import Foundation

        o = Foundation.NSObject.alloc() # Not yet initialized
        warnings.filterwarnings('error', category=RuntimeWarning)
        try:
            self.assertRaises(RuntimeWarning, o.description)
        finally:
            del warnings.filters[0]

    def testMemoryInit(self):
        """
        Regression test for bug #814683, that didn't initialize the memory
        space for output parameters correctly.
        """
        import Foundation
        plist = 0
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0)
        self.assertEquals(r[1], None)
        r = Foundation.NSPropertyListSerialization.dataFromPropertyList_format_errorDescription_(plist, Foundation.NSPropertyListXMLFormat_v1_0)
        self.assertEquals(r[1], None)

if __name__ == '__main__':
    unittest.main()
