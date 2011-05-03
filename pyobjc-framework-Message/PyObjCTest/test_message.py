import objc
import Message
from PyObjCTools.TestSupport import *

class TestMessage (TestCase):
    @onlyOn32Bit
    def testClasses(self):
        self.assert_( hasattr(Message, 'NSMailDelivery') )
        self.assert_( isinstance(Message.NSMailDelivery, objc.objc_class) )

if __name__ == "__main__":
    main()
