'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
import unittest
import PubSub

class TestPubSub (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(PubSub, 'PSAuthor') )
        self.assert_( isinstance(PubSub.PSAuthor, objc.objc_class) )

        self.assert_( hasattr(PubSub, 'PSPublishedFeed') )
        self.assert_( isinstance(PubSub.PSPublishedFeed, objc.objc_class) )

    def testProtocols(self):
        self.assert_( hasattr(PubSub, 'protocols') )
        self.assert_( hasattr(PubSub.protocols, 'PSClientDelegate') )
        self.assert_( isinstance(PubSub.protocols.PSClientDelegate, objc.informal_protocol) )

    def testValues(self):
        self.assert_( hasattr(PubSub, 'PSFeedSettingsIntervalDefault') )
        self.assert_( isinstance(PubSub.PSFeedSettingsIntervalDefault, float) )
        self.assertEquals(PubSub.PSFeedSettingsIntervalDefault, 0.0)

        self.assert_( hasattr(PubSub, 'PSFeedSettingsAllTypes') )
        self.assert_( PubSub.PSFeedSettingsAllTypes is None )

    def testVariables(self):
        
        self.assert_( hasattr(PubSub, 'PSFeedUpdatedEntriesKey') )
        self.assert_( isinstance(PubSub.PSFeedUpdatedEntriesKey, unicode) )

        # Bug!: the following definition is present in the header file but
        # not in the actual system (9A321)
        #self.assert_( hasattr(PubSub, 'PSEnclosureDownloadStateDidChange') )
        #self.assert_( isinstance(PubSub.PSEnclosureDownloadStateDidChange, unicode) )

    def testFunctions(self):
        # Use this to test for functions
        pass

        # self.assert_( hasattr(PubSub, 'FUNCTION') )

    def testOpaque(self):
        # Use this to test for opaque pointers
        pass

        # self.assert_( hasattr(PubSub, 'OPAQUE') )



if __name__ == "__main__":
    unittest.main()

