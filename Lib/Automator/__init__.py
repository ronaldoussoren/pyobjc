from _Automator import *
import objc as _objc
if _objc.platform == 'MACOSX':
    _objc.loadBundle(
        "Automator",
        globals(),
        bundle_identifier=u'com.apple.AutomatorFramework',
    )
import protocols
