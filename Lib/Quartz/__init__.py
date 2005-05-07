from _Quartz import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "Quartz",
        globals(),
        bundle_identifier=u'com.apple.quartzframework',
    )
import protocols
