"""
Some simple tests to check that the framework is properly wrapped.
"""

import objc
import PubSub
from PyObjCTools.TestSupport import TestCase


class TestPubSub(TestCase):
    def testClasses(self):
        self.assertTrue(hasattr(PubSub, "PSAuthor"))
        self.assertTrue(isinstance(PubSub.PSAuthor, objc.objc_class))

    def testProtocols(self):
        self.assertFalse(hasattr(PubSub, "protocols"))
        # self.assertTrue( hasattr(PubSub.protocols, 'PSClientDelegate') )
        # self.assertTrue( isinstance(PubSub.protocols.PSClientDelegate, objc.informal_protocol) )


class TestCallableMetadata(TestCase):
    def test_callable_metadata_is_sane(self):
        self.assertCallableMetadataIsSane(PubSub)
