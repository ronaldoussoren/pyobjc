from PyObjCTools.TestSupport import *
from AppKit import *

class TestNSTableViewRowAction (TestCase):
    def testConstants(self):
        self.assertEqual(NSTableViewRowActionStyleRegular, 0)
        self.assertEqual(NSTableViewRowActionStyleDestructive, 1)

if __name__ == "__main__":
    main()
