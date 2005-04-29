from _DiscRecording import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "DiscRecording",
        globals(),
        bundle_identifier=u'com.apple.DiscRecording',
    )
import protocols
