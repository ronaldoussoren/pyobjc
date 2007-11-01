import unittest
import objc
import Message

class TestMessage (unittest.TestCase):
    def testClasses(self):
        self.assert_( hasattr(Message, 'NSMailDelivery') )
        self.assert_( isinstance(Message.NSMailDelivery, objc.objc_class) )

if __name__ == "__main__":
    unittest.main()
