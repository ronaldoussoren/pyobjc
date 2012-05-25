from Foundation import *
import Foundation
from PyObjCTools.TestSupport import *

try:
    unicode
except NameError:
    unicode = str

class TestEAManager (TestCase):
    def testContants(self):
        self.assertIsInstance(NSAppleEventManagerWillProcessFirstEventNotification, unicode)
        self.assertIsInstance(NSAppleEventTimeOutDefault, float)
        self.assertIsInstance(NSAppleEventTimeOutNone, float)

    def testOpaque(self):
        self.assertHasAttr(Foundation, 'NSAppleEventManagerSuspensionID')
        self.assertHasAttr(NSAppleEventManagerSuspensionID, '__pointer__')

if __name__ == "__main__":
    main()
