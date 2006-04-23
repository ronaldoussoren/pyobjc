from _CoreData import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "CoreData",
        globals(),
        bundle_identifier=u'com.apple.CoreData',
    )
import protocols

_objc.setSignatureForSelector("NSManagedObjectContext", "save:", "c@:o^@")
