"""
"""

import unittest
import objc

class MessageTest (unittest.TestCase):

    def testClasses(self):
        import Message

        self.assert_(hasattr(Message, 'NSMailDelivery'))
        self.assert_(isinstance(Message.NSMailDelivery, objc.objc_class))

    def testConstants(self):
        import Message

        self.assert_(hasattr(Message, 'NSSMTPDeliveryProtocol'))
        self.assert_(isinstance(Message.NSSMTPDeliveryProtocol, unicode))

if __name__ == "__main__":
    unittest.main()
