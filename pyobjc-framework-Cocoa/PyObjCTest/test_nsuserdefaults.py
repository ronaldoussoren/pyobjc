import Foundation
import unittest

class PythonListAsValue (unittest.TestCase):

    def testSettingPythonList(self):
        defaults = Foundation.NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_([u'a', u'b', u'c'], u'randomKey')

        self.assertEquals(defaults.arrayForKey_(u'randomKey'), [u'a', u'b', u'c'])

if __name__ == "__main__":
    unittest.main()
