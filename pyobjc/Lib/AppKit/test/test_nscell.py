import unittest
import objc

from AppKit import NSCell

class TestNSCell(unittest.TestCase):
   def testString(self):
      cell = NSCell.alloc().init()
      s = 'string'
      cell.setStringValue_(s)
      self.assertEquals(cell.stringValue(), s)
      self.assertEquals(str(cell.stringValue()), s)

   def testUnicode(self):
      cell = NSCell.alloc().init()
      u = u'\xc3\xbc\xc3\xb1\xc3\xae\xc3\xa7\xc3\xb8d\xc3\xa8'
      cell.setStringValue_(u)
      self.assertEquals(cell.stringValue(), u)
      self.assertEquals(unicode(cell.stringValue()), u)

   def testInt(self):
      cell = NSCell.alloc().init()
      i = 17
      cell.setIntValue_(i)
      self.assertEquals(cell.intValue(), i)
      self.assertEquals(int(cell.intValue()), i)

   def testFloat(self):
      cell = NSCell.alloc().init()
      f = 3.14159
      cell.setFloatValue_(f)
      self.assertEquals(cell.floatValue(), f)
      self.assertEquals(float(cell.floatValue()), f)

def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestNSCell))
   return suite

if __name__ == '__main__':
   unittest.main( )
