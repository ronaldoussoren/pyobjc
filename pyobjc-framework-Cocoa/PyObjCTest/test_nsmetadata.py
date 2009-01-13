from PyObjCTools.TestSupport import *

from Foundation import *

class TestNSMetaData (TestCase):
    def testConstants(self):
        self.failUnless(isinstance(NSMetadataQueryDidStartGatheringNotification, unicode))
        self.failUnless(isinstance(NSMetadataQueryGatheringProgressNotification, unicode))
        self.failUnless(isinstance(NSMetadataQueryDidFinishGatheringNotification, unicode))
        self.failUnless(isinstance(NSMetadataQueryDidUpdateNotification, unicode))
        self.failUnless(isinstance(NSMetadataQueryResultContentRelevanceAttribute, unicode))
        self.failUnless(isinstance(NSMetadataQueryUserHomeScope, unicode))
        self.failUnless(isinstance(NSMetadataQueryLocalComputerScope, unicode))
        self.failUnless(isinstance(NSMetadataQueryNetworkScope, unicode))


if __name__ == "__main__":
    main()
