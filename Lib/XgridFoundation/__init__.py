from _XgridFoundation import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "XgridFoundation",
        globals(),
        bundle_identifier=u'com.apple.xgrid.foundation',
    )
import protocols
