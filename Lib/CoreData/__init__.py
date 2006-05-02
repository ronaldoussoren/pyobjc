from _CoreData import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "CoreData",
        globals(),
        bundle_identifier=u'com.apple.CoreData',
    )
import protocols
import _signatures
