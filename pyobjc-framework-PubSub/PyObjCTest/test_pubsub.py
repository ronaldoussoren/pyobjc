'''
Some simple tests to check that the framework is properly wrapped.
'''
import objc
from PyObjCTools.TestSupport import *
import PubSub

class TestPubSub (TestCase):
    def testClasses(self):
        self.assert_( hasattr(PubSub, 'PSAuthor') )
        self.assert_( isinstance(PubSub.PSAuthor, objc.objc_class) )


    def testProtocols(self):
        self.assert_( hasattr(PubSub, 'protocols') )
        self.assert_( hasattr(PubSub.protocols, 'PSClientDelegate') )
        self.assert_( isinstance(PubSub.protocols.PSClientDelegate, objc.informal_protocol) )


if __name__ == "__main__":
    main()
