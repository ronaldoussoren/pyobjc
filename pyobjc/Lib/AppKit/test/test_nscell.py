import unittest
import objc

from AppKit import NSCell

class TestNSCell(unittest.TestCase):
    def testUnicode(self):
        u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
        cell = NSCell.alloc().initTextCell_(u)
        cell.setStringValue_(u)
        self.assertEquals(cell.stringValue(), u)

    def testInt(self):
        i = 17
        cell = NSCell.alloc().initTextCell_(u"")
        cell.setIntValue_(i)
        self.assertEquals(cell.intValue(), i)

    def testFloat(self):
        f = 3.125
        cell = NSCell.alloc().initTextCell_(u"")
        cell.setFloatValue_(f)
        self.assertEquals(cell.floatValue(), f)

if __name__ == '__main__':
    unittest.main( )
