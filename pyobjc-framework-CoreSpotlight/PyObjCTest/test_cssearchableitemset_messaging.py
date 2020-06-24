from PyObjCTools.TestSupport import TestCase


import CoreSpotlight


class TestCSSearchableItemAttributeSet_Messaging(TestCase):
    def testConstants(self):
        self.assertIsInstance(CoreSpotlight.CSMailboxInbox, str)
        self.assertIsInstance(CoreSpotlight.CSMailboxDrafts, str)
        self.assertIsInstance(CoreSpotlight.CSMailboxSent, str)
        self.assertIsInstance(CoreSpotlight.CSMailboxJunk, str)
        self.assertIsInstance(CoreSpotlight.CSMailboxTrash, str)
        self.assertIsInstance(CoreSpotlight.CSMailboxArchive, str)
