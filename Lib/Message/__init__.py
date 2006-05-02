"""
Python mapping for the Message framework on MacOS X

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


def _initialize():
    from Foundation import NSBundle
    import objc
    p = objc.pathForFramework(u"/System/Library/Frameworks/Message.framework")
    objc.loadBundle("Message", globals(), bundle_path=p)

    b = NSBundle.bundleWithPath_(p)
    # XXX: Need to generate this part
    objc.loadBundleVariables(b, globals(), [
            (u'NSMIMEMailFormat', objc._C_ID),
            (u'NSASCIIMailFormat', objc._C_ID),
            (u'NSSMTPDeliveryProtocol', objc._C_ID),
            (u'NSSendmailDeliveryProtocol', objc._C_ID),
    ])
_initialize()

import _signatures

# Define useful utility methods here

