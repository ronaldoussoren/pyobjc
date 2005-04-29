from _AppleScriptKit import  *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "AppleScriptKit",
        globals(),
        bundle_identifier=u'com.apple.AppleScriptKit',
    )
import protocols
