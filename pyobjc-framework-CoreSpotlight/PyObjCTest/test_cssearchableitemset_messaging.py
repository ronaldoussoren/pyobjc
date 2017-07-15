from PyObjCTools.TestSupport import *
import sys

if sys.maxsize > 2**32:

    import CoreSpotlight

    class TestCSSearchableItemAttributeSet_Messaging (TestCase):
        def testConstants(self):
            self.assertIsInstance(CoreSpotlight.CSMailboxInbox, unicode)
            self.assertIsInstance(CoreSpotlight.CSMailboxDrafts, unicode)
            self.assertIsInstance(CoreSpotlight.CSMailboxSent, unicode)
            self.assertIsInstance(CoreSpotlight.CSMailboxJunk, unicode)
            self.assertIsInstance(CoreSpotlight.CSMailboxTrash, unicode)
            self.assertIsInstance(CoreSpotlight.CSMailboxArchive, unicode)

if __name__ == "__main__":
    main()
