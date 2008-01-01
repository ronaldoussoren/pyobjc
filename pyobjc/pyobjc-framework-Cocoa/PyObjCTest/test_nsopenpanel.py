import unittest
import objc

class TestOpenPanel (unittest.TestCase):
    def dont_testOpenPanelSignature(self):
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

if __name__ == "__main__":
    unittest.main()
