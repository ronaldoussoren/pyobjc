
from PyObjCTools.TestSupport import *
from AppKit import *

try:
    unicode
except NameError:
    unicode = str

class TestNSHelpManager (TestCase):
    def testConstants(self):
        self.assertIsInstance(NSContextHelpModeDidActivateNotification, unicode)
        self.assertIsInstance(NSContextHelpModeDidDeactivateNotification, unicode)

    def testMethods(self):
        self.assertResultIsBOOL(NSHelpManager.isContextHelpModeActive)
        self.assertArgIsBOOL(NSHelpManager.setContextHelpModeActive_, 0)
        self.assertResultIsBOOL(NSHelpManager.showContextHelpForObject_locationHint_)


if __name__ == "__main__":
    main()
