"""
WebKit doesn't add 'interesting' behaviour, just check that the 
module loaded correctly.
"""

import unittest

import os
import objc

if os.path.exists('/System/Library/Frameworks/WebKit.framework'):
    class WKTest (unittest.TestCase):

        def testConstants(self):
            # Test one string and one integer, to check if the 
            # constant-extraction script worked.
            import WebKit

            self.assert_(hasattr(WebKit, 'WebMenuItemTagOpenLinkInNewWindow'))
            self.assert_(hasattr(WebKit, 'WebHistoryItemsKey'))

            self.assertEquals(WebKit.WebMenuItemTagOpenLinkInNewWindow, 1)
            self.assertEquals(WebKit.WebHistoryItemsKey, 'WebHistoryItems')

        def testClasses(self):
            # Check that we loaded the WebKit framework by looking for a
            # class that should exist
            import WebKit

            self.assert_(hasattr(WebKit, 'WebFrame'))
            self.assert_(isinstance(WebKit.WebFrame, objc.objc_class))


        def testProtocols(self):
            import WebKit

            self.assert_(hasattr(WebKit.protocols, 'WebPolicyDelegate'))

if __name__ == "__main__":
    unittest.main()
