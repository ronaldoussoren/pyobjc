import Foundation
import unittest

class PythonListAsValue (unittest.TestCase):

    def testSettingPythonList(self):
        defaults = Foundation.NSUserDefaults.standardUserDefaults()
        defaults.setObject_forKey_(['a', 'b', 'c'], 'randomKey')

        self.assertEquals(defaults.arrayForKey_('randomKey'), ['a', 'b', 'c'])

if __name__ == "__main__":
    unittest.main()
