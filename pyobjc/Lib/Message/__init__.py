"""
Python mapping for the Message framework on MacOS X

This module does not contain docstrings for the wrapped code, check Apple's
documentation for details on how to use these functions and classes.
"""


import objc as _objc

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "Message",
        globals(),
        bundle_path=_objc.pathForFramework(
            "/System/Library/Frameworks/Message.framework")
    )
else:
    _objc.loadBundle(
        "Message",
        globals(),
        bundle_path=_objc.pathForFramework(
            "/System/Library/Frameworks/Message.framework")
    )

b =  _objc.runtime.NSBundle.bundleWithPath_(_objc.pathForFramework(
        '/System/Library/Frameworks/Message.framework'))
b.load()

# XXX: Need to generate this part
_objc.loadBundleVariables(b, globals(), [ 
        ('NSMIMEMailFormat', _objc._C_ID),
        ('NSASCIIMailFormat', _objc._C_ID),
        ('NSSMTPDeliveryProtocol', _objc._C_ID),
        ('NSSendmailDeliveryProtocol', _objc._C_ID),
])
del b

# Define useful utility methods here

