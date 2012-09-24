from PyObjCTools.TestSupport import *

import OpenDirectory

try:
    unicode
except NameError:
    unicode = str

class TestODSession (TestCase):
    def testConstants(self):
        self.assertIsInstance(OpenDirectory.ODSessionProxyAddress, unicode)
        self.assertIsInstance(OpenDirectory.ODSessionProxyPort, unicode)
        self.assertIsInstance(OpenDirectory.ODSessionProxyUsername, unicode)
        self.assertIsInstance(OpenDirectory.ODSessionProxyPassword, unicode)

    def testMethods(self):
        self.assertArgIsOut(OpenDirectory.ODSession.sessionWithOptions_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODSession.initWithOptions_error_, 1)
        self.assertArgIsOut(OpenDirectory.ODSession.nodeNamesAndReturnError_, 0)

if __name__ == "__main__":
    main()
