import unittest
import AppKit


class TestNSDocument (unittest.TestCase):

    def testInitWithTypeAndError(self):
        # Mac OS X 10.4 and later
        if not hasattr(AppKit.NSDocument, 'initWithType_error_'):
            return

        self.assertEquals(AppKit.NSDocument.initWithType_error_.signature,
                '@@:@o^@')

if __name__ == "__main__":
    unittest.main()
