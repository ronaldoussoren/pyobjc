'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import ScriptingBridge

class TestScriptingBridge (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(ScriptingBridge, 'SBApplication') )
        self.assert_( isinstance(ScriptingBridge.SBApplication, objc.objc_class) )
    def testProtocols(self):
        self.assert_( hasattr(ScriptingBridge, 'protocols') )

        self.assert_( hasattr(ScriptingBridge.protocols, 'SBApplicationDelegate') )
        self.assert_( isinstance(ScriptingBridge.protocols.SBApplicationDelegate, objc.informal_protocol) )



if __name__ == "__main__":
    unittest.main()

