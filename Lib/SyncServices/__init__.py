from _SyncServices import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "SyncServices",
        globals(),
        bundle_identifier=u'com.apple.SyncServices',
    )
import protocols
