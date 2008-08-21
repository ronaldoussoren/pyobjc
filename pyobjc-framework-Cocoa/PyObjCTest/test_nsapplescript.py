from Foundation import *
import unittest

class TestAE (unittest.TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSAppleScriptErrorMessage, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorNumber, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorAppName, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorBriefMessage, unicode))
        self.failUnless(isinstance(NSAppleScriptErrorRange, unicode))

    def testOutput(self):
        self.fail('- (BOOL)compileAndReturnError:(NSDictionary **)errorInfo;')
        self.fail('- (NSAppleEventDescriptor *)executeAndReturnError:(NSDictionary **)errorInfo;')
        self.fail('- (NSAppleEventDescriptor *)executeAppleEvent:(NSAppleEventDescriptor *)event error:(NSDictionary **)errorInfo;')
        self.fail('- (id)initWithContentsOfURL:(NSURL *)url error:(NSDictionary **)errorInfo;')


if __name__ == "__main__":
    unittest.main()
