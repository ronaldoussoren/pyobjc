"""
Dummy Foundation wrappers, just those parts needed for the unittests.
"""
import objc as _objc

__bundle__ = _objc.loadBundle(
        'Foundation',
        globals(),
        bundle_identifier=u'com.apple.Foundation',
)

_objc.loadBundleVariables(__bundle__, globals(), [
            ( 'NSPriorDayDesignations', _objc._C_ID ),
        ])

NSPropertyListXMLFormat_v1_0 = 100
NSKeyValueObservingOptionNew = 0x01
NSKeyValueObservingOptionOld = 0x02
