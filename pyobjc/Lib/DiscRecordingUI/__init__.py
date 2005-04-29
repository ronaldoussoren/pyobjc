from _DiscRecordingUI import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "DiscRecordingUI",
        globals(),
        bundle_identifier=u'com.apple.DiscRecordingUI',
    )
import protocols
