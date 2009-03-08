import objc
import Message
from PyObjCTools.TestSupport import *

class TestMessage (TestCase):
    def testClasses(self):
        self.assert_( hasattr(Message, 'NSMailDelivery') )
        self.assert_( isinstance(Message.NSMailDelivery, objc.objc_class) )

if __name__ == "__main__":
    main()
