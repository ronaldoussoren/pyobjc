import objc as _objc
from _Foundation import *

NSClassFromString = _objc.lookUpClass

# Do something smart to collect Foundation classes...

if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        'Foundation',
        globals(),
        bundle_identifier=u'com.apple.Foundation',
    )
else:
    _objc.loadBundle(
        'Foundation',
        globals(),
        bundle_path=_objc.pathForFramework(
            u'/System/Library/Frameworks/Foundation.framework',
        ),
    )

import protocols  # no need to export these, just register with PyObjC

#
# (informal) protocols eported for b/w compatibility
#
from protocols import NSConnectionDelegateMethods, \
                      NSDistantObjectRequestMethods, \
                      NSCopyLinkMoveHandler, NSKeyedArchiverDelegate, \
                      NSKeyedUnarchiverDelegate, NSNetServiceDelegateMethods, \
                      NSNetServiceBrowserDelegateMethods, NSPortDelegateMethods
