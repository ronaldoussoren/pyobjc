from _AppKitScripting import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "AppKitScripting",
        globals(),
        bundle_identifier=u'com.apple.AppKitScripting',
    )
import protocols
