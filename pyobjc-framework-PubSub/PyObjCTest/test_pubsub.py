"""
Some simple tests to check that the framework is properly wrapped.
"""
import objc
from PyObjCTools.TestSupport import *
import PubSub


class TestPubSub(TestCase):
    def testClasses(self):
        self.assertTrue(hasattr(PubSub, "PSAuthor"))
        self.assertTrue(isinstance(PubSub.PSAuthor, objc.objc_class))

    def testProtocols(self):
        self.assertFalse(hasattr(PubSub, "protocols"))
        # self.assertTrue( hasattr(PubSub.protocols, 'PSClientDelegate') )
        # self.assertTrue( isinstance(PubSub.protocols.PSClientDelegate, objc.informal_protocol) )


if __name__ == "__main__":
    main()
