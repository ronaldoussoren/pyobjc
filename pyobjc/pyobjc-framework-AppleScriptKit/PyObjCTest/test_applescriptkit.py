'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import AppleScriptKit

class TestAppleScriptKit (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(AppleScriptKit, 'ASKPluginObject') )
        self.assert_( isinstance(AppleScriptKit.ASKPluginObject, objc.objc_class) )

if __name__ == "__main__":
    unittest.main()

