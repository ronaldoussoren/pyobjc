import unittest
import AppKit

class TestNSImage (unittest.TestCase):
    def test_compositePoint(self):
        # comes straight from ReSTedit.  Works on PPC, not on Intel (as of r1791)
        ws = AppKit.NSWorkspace.sharedWorkspace()
        txtIcon = ws.iconForFileType_("txt")
        txtIcon.setSize_( (16,16) )
        htmlIcon = ws.iconForFileType_("html")
        htmlIcon.setSize_( (16,16) )
        
        comboIcon = AppKit.NSImage.alloc().initWithSize_( (100,100) )
        comboIcon.lockFocus()
        txtIcon.compositeToPoint_fromRect_operation_((0,0), ((0,0),(16,16)), AppKit.NSCompositeCopy)
        htmlIcon.compositeToPoint_fromRect_operation_((8,0), ((8,0),(8,16)), AppKit.NSCompositeCopy)
        comboIcon.unlockFocus()

if __name__ == "__main__":
    unittest.main()
