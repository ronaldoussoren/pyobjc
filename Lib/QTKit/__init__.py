from _QTKit import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "QTKit",
        globals(),
        bundle_identifier=u'com.apple.QTKit',
    )
import protocols
import _signatures
