from _OSAKit import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "OSAKit",
        globals(),
        bundle_identifier=u'com.apple.OSAKit',
    )
import protocols
